
import re
import datetime


def define_user_name():

    while True:
        try:
            name_check = re.compile(r"[^A-Za-zs-]")
            name = input("Podaj imie: ")

            if name_check.search(name):
                print("Wprowadz poprawne imie (tylko litery).")
                continue

        except ValueError:
            print("Wprowadz poprawne imie (tylko litery).")
            continue

        if len(name) > 30:
            print('Za dlugie imie (max. 30 znakow.')
        else:
            break

    else:
        print('Fatal error')

    return name


def define_user_surname():

    while True:
        try:
            surname_check = re.compile(r"[^A-Za-zs-]")
            surname = input("Podaj nazwisko: ")

            if surname_check.search(surname):
                print("Wprowadz poprawne nazwisko (tylko litery + ewentualnie '-').")
                continue

        except ValueError:
            print("Wprowadz poprawne nazwisko (tylko litery + ewentualnie '-').")
            continue

        if len(surname) > 60:
                print('Za dlugie nazwisko (max. 60 znakow.')
        else:
            break

    else:
        print('Fatal error')

    return surname


def define_user_age():

    while True:
        try:
            age = int(input("Podaj wiek: "))

        except ValueError:
            print("Wpisales niepoprawny wiek, dozwolone tylko liczby naturalne.")
            continue

        if age > 100:
            print("Nie przesadzasz z tym wiekiem ?")
        else:
            break

    else:
        print("Fatal error.")

    return age


def define_user_birth_date():

    while True:
        try:
            date_entry = input('Wprowadź datę urodzenia w formacie YYYY-MM-DD: ')
            year, month, day = map(int, date_entry.split('-'))
            birth_date = datetime.date(year, month, day)

        except ValueError:
            print("Wpisales niepoprawna datę, dozwolone tylko liczby naturalne.")
            continue

        now = datetime.datetime.now()
        today = datetime.date(now.year, now.month, now.day)

        if birth_date >today:
            print('Wprowadzona data jest w przyszłości, wprowadź poprawną datę.')
        else:
            break

    else:
        print("Fatal error")

    return birth_date


def define_user_occupation():

    occupation_decision = input('Czy chcesz podać zawód? T/N: ')

    while True:
        if occupation_decision == 'N':
            return print('Uzytkownik nie chce podac zawodu.')
            break

        elif occupation_decision == 'T':
            occupation = input("Wprowadź nazwę zawodu: ")
            break

        else:
            return print('Uzytkownik nie dokonal wyboru.')
            break

    else:
        print("Fatal error")

    return occupation
