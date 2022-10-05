from random import *
import string

class Password:
    def __init__(self, how_long,how_many_specific_sing,how_many_letters,how_many_numbers):
        self.how_long=how_long
        self.how_many_specific_sing=how_many_specific_sing
        self.how_many_letters=how_many_letters
        self.how_many_numbers=how_many_numbers
        self.big_letters=0
        self.stringstring_of_characters='0'

    def __repr__(self):
        if self.how_many_specific_sing == 0 and self.how_many_letters == 0 and self.how_many_numbers > 0:
            return (f'Twoje hasło składa się z {self.how_long} znaków. Twoje hasło nie jest bezpieczne. '
                    f'Skład się z samych cyfr.'
                    f'Jeżeli chcesz, aby hasło było bezpieczne, '
                    f'stwórz hasło zawierjące wielkie i małe litery, cyfry oraz znaki specjalne ')

        elif self.how_many_specific_sing == 0 and self.how_many_numbers == 0 and self.how_many_letters > 0:
            if self.big_letters == 1:
                return(f'Twoje hasło składa się z {self.how_long} znaków. Twoje hasło nie jest bezpieczne. '
                       f'Skład się z samych liter.'
                    f'Jeżeli chcesz, aby hasło było bezpieczne, '
                       f'stwórz hasło zawierjące wielkie i małe litery, cyfry oraz znaki specjalne ')
            elif self.big_letters == 0:
                return(f'Twoje hasło składa się z {self.how_long} znaków. Twoje hasło nie jest bezpieczne. '
                       f'Skład się z samych liter.'
                    f'Jeżeli chcesz, aby hasło było bezpieczne, '
                       f'stwórz hasło zawierjące wielkie i małe litery, cyfry oraz znaki specjalne ')
        elif self.how_many_numbers == 0 and self.how_many_letters == 0 and self.how_many_specific_sing >0:
            return(f'Twoje hasło składa się z {self.how_long} znaków. Twoje hasło nie jest bezpieczne. '
                   f'Skład się z samych znaków specjalnych.'
                f'Jeżeli chcesz, aby hasło było bezpieczne, '
                   f'stwórz hasło zawierjące wielkie i małe litery, cyfry oraz znaki specjalne ')
        elif self.how_many_specific_sing > 0 and self.how_many_letters > 0 and self.how_many_numbers > 0:
            if self.big_letters == 0:
                return(f'Twoje hasło składa się z {self.how_long} znaków. Twoje hasło jest bezpieczne.'
                    f'Jeżeli chcesz zwiększyć jego siłę, dodaj do hasła wielkie litery ')
            elif self.big_letters == 1:
                return(f'Twoje hasło składa się z {self.how_long} znaków. Twoje hasło jest bezpieczne.')
        elif self.how_many_specific_sing > 0 and self.how_many_numbers > 0 and self.how_many_letters == 0:
            return (f'Twoje hasło składa się z {self.how_long} znaków. Twoje hasło nie jest bezpieczne.'
                    f'Składa się z samych cyfr i znaków specjalnych.'
                    f'Jeżeli chcesz zwiększyć jego siłę, dodaj do hasła małe i wielkie litery')
        elif self.how_many_specific_sing > 0 and self.how_many_numbers == 0 and self.how_many_letters > 0:
            if self.big_letters == 1:
                return (f'Twoje hasło składa się z {self.how_long} znaków. Twoje hasło nie jest bezpieczne.'
                     f'Składa się z samych liter znaków specjalnych.'
                     f'Jeżeli chcesz zwiększyć jego siłę, dodaj do hasła liczby')
            elif self.big_letters == 0:
                return (f'Twoje hasło składa się z {self.how_long} znaków. Twoje hasło nie jest bezpieczne.'
                 f'Składa się z samych  małych liter znaków specjalnych.'
                 f'Jeżeli chcesz zwiększyć jego siłę, dodaj do hasła liczby i wielkie litery')
        elif self.how_many_specific_sing == 0 and self.how_many_numbers > 0 and self.how_many_letters > 0:
            if self.big_letters == 1:
                return (f'Twoje hasło składa się z {self.how_long} znaków. Twoje hasło nie jest bezpieczne.'
                            f'Składa się z samych   liter i liczb.'
                            f'Jeżeli chcesz zwiększyć jego siłę, dodaj do hasła znaki specjalne')
            elif self.big_letters == 0:
                return (f'Twoje hasło składa się z {self.how_long} znaków. Twoje hasło nie jest bezpieczne.'
                            f'Składa się z małych   liter i liczb.'
                            f'Jeżeli chcesz zwiększyć jego siłę, dodaj do hasła znaki specjalne')


def make_password():


        password = Password(how_long=int(input('Z ilu znaków ma składać się Twoje hasło? '
                                               '(Twoje hało powinno składać się od 8-15 znaków)')), how_many_specific_sing=
        int(input('Ile znaków specjalnych powinno posiadać?')),
                                how_many_letters=int(input('Z ilu liter powinno się składać?')),
                                how_many_numbers=int(input('Z ilu liczb powinno się składać')))
        if password.how_many_letters>0:
            password.big_letters = int(input('Wpisz 1 jeżeli hasło powinno posiadać wielkie litery, w innym przypadku wpisz 0'))
        elif password.how_many_letters<0:
            password.big_letters = int(input('Wpisz 1 jeżeli hasło powinno posiadać wielkie litery, w innym przypadku wpisz 0'))
        return password


def key(password):

    if password.how_many_specific_sing==0 and password.how_many_letters==0 and password.how_many_numbers>0:
            key=1
    elif password.how_many_specific_sing==0 and password.how_many_numbers==0 and  password.how_many_letters>0:
        if password.big_letters==1:
            key=2
        elif password.big_letters==0:
            key=3
    elif password.how_many_numbers==0 and password.how_many_letters==0 and password.how_many_specific_sing>0:
        key=4
    elif password.how_many_specific_sing>0 and password.how_many_letters>0 and password.how_many_numbers>0:
        if password.big_letters==1:
            key = 5
        elif password.big_letters==0:
            key = 6
    elif password.how_many_specific_sing>0 and password.how_many_numbers>0 and password.how_many_letters==0:
        key=7
    elif password.how_many_specific_sing>0 and password.how_many_numbers==0 and password.how_many_letters>0:
        if password.big_letters==1:
            key=8
        elif password.big_letters==0:
            key=9
    elif password.how_many_specific_sing==0 and password.how_many_numbers>0 and password.how_many_letters>0:
        if password.big_letters==1:
            key=10
        elif password.big_letters==0:
            key=11
    return key



def generaiting_password(password,key):
    try:

        key1 = [1,2, 3, 4, 5, 6, 7, 8, 0]
        key3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u',
                       'w', 'y', 'z', 'x']
        key4=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '}', '[', ']', '?', '<', '>', ',', '.', '/',
                     '\',', '+', '=']
        key2=[]
        for i in key3:
            y=i.upper()
            key2.append(y)
        all=password.how_many_specific_sing+ password.how_many_numbers+password.how_many_letters
        if password.how_long != all:
            print('Ups! Coś poszło nie tak. Ustal hasło jeszcze raz. Pamiętaj by, '
                      'zadeklarowana ilość znaków była odpowiednia z ilością znaków specjalnych, liczb i liter')
        elif password.how_long > 15:
            print('Nie można utworzyć hasła. Ilość znaków nie zgodna z wymaganiami.'
          'Twoje hasło powinno zawierać od 8 do 15 znaków')
        elif password.how_long<8:
            print('Nie można utworzyć hasła. Ilość znaków nie zgodna z wymaganiami.'
          'Twoje hasło powinno zawierać od 8 do 15 znaków')

        else:
            if key==1:
                finish_key=sample(key1,password.how_many_numbers)
            elif key ==2:
                finish_key=[]
                little_letter_key=sample(key3, password.how_many_letters-3)
                bigger_letter_key=sample(key2,3)
                for i in little_letter_key:
                    finish_key.append(i)
                for i in bigger_letter_key:
                    finish_key.append(i)
            elif key ==3:
                finish_key=sample(key3,password.how_many_letters)
            elif key ==4:
                finish_key=sample(key4,password.how_many_specific_sing)

            elif key ==5:
                finish_key = []
                numbers_key = sample(key1, password.how_many_numbers)
                sings_key = sample(key4, password.how_many_specific_sing)
                little_letter_key = sample(key3, password.how_many_letters-1)
                bigger_letter_key=sample(key2,1)
                for i in numbers_key:
                    finish_key.append(i)
                for i in sings_key:
                    finish_key.append(i)
                for i in little_letter_key:
                    finish_key.append(i)
                for i in bigger_letter_key:
                    finish_key.append(i)
            elif key ==6:
                finish_key=[]
                numbers_key=sample(key1,password.how_many_numbers)
                sings_key=sample(key4,password.how_many_specific_sing)
                letter_key=sample(key3,password.how_many_letters)
                for i in numbers_key:
                    finish_key.append(i)
                for i in sings_key:
                    finish_key.append(i)
                for i in letter_key:
                    finish_key.append(i)
            elif key==7:
                finish_key = []
                numbers_key = sample(key1, password.how_many_numbers)
                sings_key = sample(key4, password.how_many_specific_sing)
                for i in numbers_key:
                    finish_key.append(i)
                for i in sings_key:
                    finish_key.append(i)
            elif key==8:
                finish_key = []
                sings_key=sample(key4, password.how_many_specific_sing)
                little_letter_key = sample(key3, password.how_many_letters - 1)
                bigger_letter_key = sample(key2, 1)
                for i in sings_key:
                    finish_key.append(i)
                for i in little_letter_key:
                    finish_key.append(i)
                for i in bigger_letter_key:
                    finish_key.append(i)
            elif key==9:
                finish_key = []
                sings_key = sample(key4, password.how_many_specific_sing)
                little_letter_key = sample(key3, password.how_many_letters)
                for i in sings_key:
                    finish_key.append(i)
                for i in little_letter_key:
                    finish_key.append(i)
            elif key==10:
                finish_key = []
                numbers_key=sample(key1,password.how_many_numbers)
                little_letter_key = sample(key3, password.how_many_letters - 1)
                bigger_letter_key = sample(key2, 1)
                for i in numbers_key:
                    finish_key.append(i)
                for i in little_letter_key:
                    finish_key.append(i)
                for i in bigger_letter_key:
                    finish_key.append(i)
            elif key==11:
                finish_key = []
                numbers_key=sample(key1,password.how_many_numbers)
                little_letter_key = sample(key3, password.how_many_letters)
                for i in numbers_key:
                    finish_key.append(i)
                for i in little_letter_key:
                    finish_key.append(i)

            password.stringstring_of_characters=' '.join(str(i)for i in finish_key)
            print(f'Twoje hasło to {password.stringstring_of_characters}')



    except: print('Ups! Coś poszło nie tak. Ustal hasło jeszcze raz. Pamiętaj by, '
                      'zadeklarowana ilość znaków była odpowiednia z ilością znaków specjalnych, liczb i liter')

def save(password):
    try:
        print('Czy chcesz zapisać hasło? T/N')
        choose=input()
        choose=choose.upper()
        if choose=='T':
            file=open('hasło.txt', 'w')
            file.write(password.stringstring_of_characters)
            file.close()
            print('Twoje hasło zostało zapisane. Do widzenia.')
        elif choose=='N':
            print('Do widzenia')
        else:
            print('Wybrano zły znak')
    except: print('Wybrano zły znak.')



def menu():
    try:
        while True:
            password = make_password()
            k = key(password)
            z = generaiting_password(password, k)
            if password.stringstring_of_characters=='0':
                print ('Czy chcesz stworzyć nowe hasło? T/N')
                choose=input()
                choose=choose.upper()
                if choose=='N':
                    print('Do widzenia')
                    break
                elif choose=='T':
                    pass

            else:
                print(password)
                save(password)
                break
    except: print('Wybrano zły znak!')


class Password_generator:
    def __init__(self, password):
        self.password = password

    def __repr__(self):
        return ('Twój osobisty generator haseł. Służy do generowania ciągu znaków z możliwością zapisania go do pliku.')

menu() #wywołanie generatora





