import click


class Matura():

    def __init__(self):
        self.row = []
        self.procent = []
        self.row_dict = []
        self.year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
        self.voivodeship = ["Dolnośląskie", "Kujawsko-pomorskie", "Lubelskie",  "Lubuskie","Łódzkie",
                       "Małopolskie", "Mazowieckie", "Opolskie", "Podkarpackie","Podlaskie", "Pomorskie", "Śląskie", "Świętokrzyskie",
                       "Warmińsko-Mazurskie", "Wielkopolskie", "Zachodniopomorskie"]

        self.list_gender = [["kobiety", 0], ["mężczyźni", 0], ["kobiety", "mężczyźni"]]
        self.keys = ['Terytorium', 'Przystąpiło/zdało', 'Płeć ', 'Rok', 'Liczba osób']

    def open_file(self, file):
        lines = []
        self.f = open(file, "r", encoding="latin2")
        for line in self.f:
            lines.append(line)
        for i in range(len(lines)):
            self.row.append(lines[i].split(";"))
        self.f.close()
        return self.row

    def replace_char(self, row):
        swietokrzyskie = row[469][0]
        slaskie = row[433][0]
        dolnoslaskie = row[37][0]

        for i in range(len(row)):
            for j in range(len(row[i])):
                if row[i][j][:6] == 'przyst':
                    row[i][j] = "przystapiło"
                if row[i][j][:6] == 'Przyst':
                    row[i][j] = "Przystąpiło/zdało"
                elif row[i][j] == swietokrzyskie:
                    row[i][j] = "Świętokrzyskie"
                elif row[i][j] == slaskie:
                    row[i][j] = "Śląskie"
                elif row[i][j] == dolnoslaskie:
                    row[i][j] = "Dolnośląskie"
                elif row[i][j][:6] == "mężczy":
                    row[i][j] = "mężczyźni"
                elif row[i][j] == "przystapiło":
                    row[i][j] = "przystąpiło"
                else:
                    row[i][j]
        return row

    def dictionary(self, row):
        dictionary = {}
        row_dict = []
        for i in range(1, len(row)):
            dictionary = dict([(self.keys[j], row[i][j]) for j in range(len(self.keys))])
            row_dict.append(dictionary)
        return row_dict

    def one(self, row_dict, year, voi, gender=2):
        suma = 0
        licznik = 1
        for i in range(len(row_dict)):
            if row_dict[i].get(self.keys[0]) == self.voivodeship[voi]:
                if row_dict[i].get(self.keys[1]) == "przystąpiło":
                    if int(row_dict[i].get(self.keys[3])) in range(2010, year + 1):
                        if row_dict[i].get(self.keys[2]) in self.list_gender[gender]:
                            suma += int(row_dict[i].get(self.keys[4]))
                        licznik += 1


        srednia = int(suma / licznik)
        print(f"{year} - {srednia}")

    def create_list_proc(self, row_dict, gender=2):
        przystapilo = []
        zdalo = []
        procent = []
        for i in range(len(row_dict)):
            if row_dict[i].get(self.keys[0]) != "Polska":
                if self.list_gender[gender][1] == 0:
                    if int(row_dict[i].get(self.keys[3])) in self.year:
                        if row_dict[i].get(self.keys[2]) == self.list_gender[gender][0]:
                            if row_dict[i].get(self.keys[1]) == "przystąpiło":
                                przystapilo.append(int(row_dict[i].get(self.keys[4])))
                            elif row_dict[i].get(self.keys[1]) == "zdało":
                                zdalo.append(int(row_dict[i].get(self.keys[4])))
                else:
                    if int(row_dict[i].get(self.keys[3])) in self.year:
                        if row_dict[i].get(self.keys[1]) == "przystąpiło":
                            if row_dict[i].get(self.keys[3]) == row_dict[i - 1].get(self.keys[3]):
                                przystapilo.append(int(row_dict[i].get(self.keys[4])) + int(row_dict[i - 1].get(self.keys[4])))
                        elif row_dict[i].get(self.keys[1]) == "zdało":
                            if row_dict[i].get(self.keys[3]) == row_dict[i -1].get(self.keys[3]):
                                zdalo.append(int(row_dict[i].get(self.keys[4])) + int(row_dict[i -1 ].get(self.keys[4])))
        if len(przystapilo) == len(zdalo):
            for i in range(len(zdalo)):
                procent.append(int((zdalo[i] / przystapilo[i]) * 100))
        return procent

    def two(self, procent, voi):
        procent_dict = {}
        for i in range(len(self.year)):
            procent_dict[self.year[i]] = procent[voi*len(self.year)+i]

        print(self.voivodeship[voi])
        for key, element in procent_dict.items():
            print(f"{key} - {element}%")

    def three(self, procent, year):
        procent_dict = {}
        procent_app =[]
        tupler = ()
        for i in range(int(len(procent) / len(self.voivodeship))):
            for j in range(0, int(len(procent)), len(self.year)):
                procent_app.append(procent[i + j])
            tupler = tuple(procent_app)
            procent_app.clear()
            procent_dict.update([(self.year[i], tupler)])

        for key, element in procent_dict.items():
            if key == year:
                print(f"{key} - {self.voivodeship[element.index(max(element))]}")


    def four(self, procent):
        procent_app = []
        procent_dict = {}
        tupler = ()
        for i in range(int(len(procent) / len(self.year))):
            for j in range(len(self.year)):
                procent_app.append(procent[i + j])
            tupler = tuple(procent_app)
            procent_app.clear()
            procent_dict.update([(self.voivodeship[i], tupler)])

        for i in range(len(self.voivodeship)):
            for j in range(len(procent_dict.get(self.voivodeship[1])) - 1):
                if procent_dict.get(self.voivodeship[i])[j] > procent_dict.get(self.voivodeship[i])[j + 1]:
                    print(f"{self.voivodeship[i]}: {self.year[j]} --> {self.year[j + 1]}")

    def five(self, procent, voi1, voi2):
        procent_app = []
        procent_dict = {}
        tupler = ()
        for i in range(int(len(procent) / 9)):
            for j in range(len(self.year)):
                procent_app.append(procent[i + j])
            tupler = tuple(procent_app)
            procent_app.clear()
            procent_dict.update([(self.voivodeship[i], tupler)])

        for i in range(len(procent_dict.get(self.voivodeship[voi1]))):
            if procent_dict.get(self.voivodeship[voi1])[i] > procent_dict.get(self.voivodeship[voi2])[i]:
                print(f" {self.year[i]} - {self.voivodeship[voi1]}")
            elif procent_dict.get(self.voivodeship[voi1])[i] < procent_dict.get(self.voivodeship[voi2])[i]:
                print(f" {self.year[i]} - {self.voivodeship[voi2]}")
            else:
                print(f"{self.year[i]} - Takie same")



@click.group()


def mat():
    """Program analizuje dane dotyczące liczby osób, które przystąpiły oraz zdały maturę w latach 2010-2018. \n
        Źródło danych: https://dane.gov.pl/dataset/1567/resource/17363 """


@mat.command('1', help="obliczenie średniej liczby osób, które przystąpiły do egzaminu dla danego województwa na przestrzeni lat, do podanego roku włącznie")
@click.argument('wojewodztwo', type=click.INT)
@click.argument('rok', type=click.INT)
@click.argument('plec', type=click.INT, default=2)

def one(**kwargs):
    matura.one(matura.dictionary(matura.replace_char(matura.row)), (kwargs['rok']), (kwargs['wojewodztwo']), (kwargs['plec']))


@mat.command('2', help="obliczenie procentowej zdawalności dla danego województwa na przestrzeni lat")
@click.argument('wojewodztwo', type=click.INT)
@click.argument('plec', type=click.INT, default=2)


def two(**kwargs):
    matura.two(matura.create_list_proc(matura.dictionary(matura.replace_char(matura.row)), (kwargs['plec'])), (kwargs['wojewodztwo']))


@mat.command('3', help="podanie województwa o najlepszej zdawalności w konkretnym roku")
@click.argument('rok', type=click.INT)
@click.argument('plec', type=click.INT, default=2)

def three(**kwargs):
    matura.three(matura.create_list_proc(matura.dictionary(matura.replace_char(matura.row)), (kwargs['plec'])), (kwargs['rok']))


@mat.command('4', help="wykrycie województw, które zanotowały regresję")
@click.argument('plec', type=click.INT, default=2)


def four(**kwargs):
    matura.four(matura.create_list_proc(matura.dictionary(matura.replace_char(matura.row)), (kwargs['plec'])))


@mat.command('5', help="porównanie dwóch województw")
@click.argument('wojewodztwo_1', type=click.INT)
@click.argument('wojewodztwo_2', type=click.INT)
@click.argument('plec', type=click.INT, default=2)


def five(**kwargs):
    matura.five(matura.create_list_proc(matura.dictionary(matura.replace_char(matura.row)), (kwargs['plec'])), (kwargs['wojewodztwo_1']), (kwargs['wojewodztwo_2']))



if __name__ == '__main__':
    matura = Matura()
    matura.open_file("Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv")
    mat()


