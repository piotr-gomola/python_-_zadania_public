
from formularz_klasy_funkcje import define_user_name, define_user_surname, define_user_age, define_user_birth_date, define_user_occupation

class User:

    def __init__(self):

        self.name = define_user_name()
        self.surname = define_user_surname()
        self.age = define_user_age()
        self.birth_date = define_user_birth_date()
        self.occupation = define_user_occupation()

    def as_txt_entry(self):
        return f"{self.name}, {self.surname}, {self.age}, {self.birth_date}, {self.occupation}"


entry = User().as_txt_entry()
# print(entry)

save_in_file = input('Czy chcesz zapisać dane w pliku? T/N: ')
while True:
    if save_in_file == 'N':
        break
    elif save_in_file == 'T':
        file_name = input("Wprowadź nazwę pliku: ")
        with open(file_name + ".txt", 'a') as file:
            file.write(entry)
        break
    else:
        print('Uzytkownik nie dokonal wyboru.')
        break
