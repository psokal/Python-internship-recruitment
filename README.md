# Python-rekrutacja
This project analyzes data of people who joined and passed the final exams between 2010 and 2018.
Script matura.py solves [these five](https://github.com/psokal/Python-rekrutacja/backend_zadanie-python.txt) problems.


## Documentation

You can run this project in the terminal. 
(Remember to put the file "Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv" in folder with script matura.py)
```
$ python matura.py --help
Usage: matura.py [OPTIONS] COMMAND [ARGS]...

  Program analizuje dane dotyczące liczby osób, które przystąpiły oraz zdały
  maturę w latach 2010-2018.

  Źródło danych: https://dane.gov.pl/dataset/1567/resource/17363

Options:
  --help  Show this message and exit.

Commands:
  1  obliczenie średniej liczby osób, które przystąpiły do egzaminu dla...
  2  obliczenie procentowej zdawalności dla danego województwa na...
  3  podanie województwa o najlepszej zdawalności w konkretnym roku
  4  wykrycie województw, które zanotowały regresję
  5  porównanie dwóch województw
```

```
$ python matura.py 1 --help
Usage: matura.py 1 [OPTIONS] WOJEWODZTWO ROK [PLEC]

  obliczenie średniej liczby osób, które przystąpiły do egzaminu dla danego
  województwa na przestrzeni lat, do podanego roku włącznie

Options:
  --help  Show this message and exit.
 ```
 ```
 $ python matura.py 2 --help
 Usage: matura.py 2 [OPTIONS] WOJEWODZTWO [PLEC]

  obliczenie procentowej zdawalności dla danego województwa na przestrzeni
  lat

Options:
  --help  Show this message and exit.
```

```
$ python matura.py 3 --help
Usage: matura.py 3 [OPTIONS] ROK [PLEC]

  podanie województwa o najlepszej zdawalności w konkretnym roku

Options:
  --help  Show this message and exit.
```

```
$ python matura.py 4 --help
Usage: matura.py 4 [OPTIONS] [PLEC]

  wykrycie województw, które zanotowały regresję

Options:
  --help  Show this message and exit.
```

```
$ python matura.py 5 --help
Usage: matura.py 5 [OPTIONS] WOJEWODZTWO_1 WOJEWODZTWO_2 [PLEC]

  porównanie dwóch województw

Options:
  --help  Show this message and exit.
```

#### Gender
* 0 - women
* 1 - men
* 2 - women and men (default)

#### Dictionary of voivodeships:
| Number | Voivodeship |
| ------ | ------ |
| 0 | Dolnośląskie |
| 1 | Kujawsko-pomorskie
| 2 | Lubelskie |
| 3 | Lubuskie |
| 4 | Łódzkie |
| 5 | Małopolskie |
| 6 | Mazowieckie |
| 7 | Opolskie |
| 8 | Podkarpackie |
| 9 | Podlaskie |
| 10 | Pomorskie |
| 11 | Śląskie |
| 12 | Świętokrzyskie |
| 13 | Warmińsko-Mazurskie |
| 14 | Wielkopolskie |
| 15 | Zachodniopomorskie |



## Features
* Using numpy and pandas packages to answer questions  
* Implementation unit tests
* Downloading data from the API
* One-time uploading of data to the database (sqlite) and downloading from the database by commands


## Author
Paulina Sokal




