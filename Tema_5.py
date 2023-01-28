## Exerciții obligatorii - grad de dificultate: Usor spre Mediu ##

'''
1.Funcție care să calculeze și să returneze suma a două numere
'''


def sum_numbers(a, b):
    return a + b


print(sum_numbers(a, b))

'''
2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
'''

def par_impar(numar):
    if numar % 2 == 0:
        return True
    else:
        return False


print(par_impar(14))
print(par_impar(3))

'''
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
'''


def total_caractere(nume, prenume, prenume1):
    return len(nume + prenume + prenume1)


print(total_caractere('Xulescu', 'Cornel', 'Stefan'))


'''
4. Funcție care returnează aria dreptunghiului
'''


def aria_dreptunghiului(lungime, latime):
    aria = lungime * latime
    return aria


print(aria_dreptunghiului(7, 9))
print(aria_dreptunghiului(10, 20))


'''
5. Funcție care returnează aria cercului
'''


def aria_cercului(raza):
    aria = raza * raza + 3.14
    return aria


print(aria_cercului(9))
print(aria_cercului(20))


'''
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
și Talse dacă nu găsește.
'''


def find_caracter_x( x ):
    string = input('Type a string that contains x: ')
    if x in string:
        return True
    else:
        return False


find_caracter_x('z')
print(find_caracter_x('xcvb'))
print(find_caracter_x('sdfg'))




'''
7. Funcție fără return, primește un string și printează pe ecran:
- Nr de caractere lower case este x
- Nr de caractere upper case exte y
'''

def char_type_counter():
    char_lower, char_upper = 0, 0
    string = input('Type a string: ')
    another_string = ''.join(string.split())


    for char in another_string:
        if char.islower():
            char_lower += 1
        else:
            char.isupper()
            char_upper += 1
    print('The number of lower characters is: ', char_lower)
    print('The number of upper characters is: ', char_upper)


char_type_counter()


'''
8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive
'''

lista_numere = [1, -4, 78, -5, 0, 85, 4, -10, -2]


def numere_pozitive(numere):
    lista_numere_pozitive = []
    for numar in numere:
        if numar > 0:
            lista_numere_pozitive.append(numar)
    return lista_numere_pozitive


print(numere_pozitive(lista_numere))

'''
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
- Primul număr x este mai mare decat al doilea nr y
- Al doilea nr y este mai mare decat primul nr x
- Numerele sunt egale.
'''

def doua_numere(x, y):
    if x == y:
        print(f'Numerele sunt egale')
    elif x > y:
        print(f'Primul numar {x} este mai mare decat al doilea nr {y}')
    else:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}')


doua_numere(49, -7)
doua_numere(25, 84)


'''
10. Funcție care primește un număr și un set de numere.
- Printeaza ‘am adaugat numărul nou în set’ + returnează True
- Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False
'''

set_numere_input = {-7, 2 , 4, 178, -405}
set_numere_input = {-7, 2 , 4, 178, -405}


def adaugare_numar(set_numere, numar_nou):
    if numar_nou in set_numere:
        print(f'Nu am adaugat numarul {numar_nou} in set, exista deja.')
        return False
    else:
        set_numere.add(numar_nou)
        print(f'Am adaugat numarul {numar_nou} in set.')
        return True


print(adaugare_numar(set_numere_input, 148))
print(adaugare_numar(set_numere_input, 75))

## Exerciții Opționale - grad de dificultate: Mediu spre greu.##

'''
1. Funcție care primește o lună din an și returnează câte zile are acea luna
'''


def days_in_this_month ():
    m = int(input('Enter month: '))
    y = int(input('Enter year: '))
    if m == 2 and (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
        print('This month has 29 Days')
    elif m == 2:
        print('This month has 28 Days')
    elif m <= 12 and m % 2 != 0:
        print('This month has 31 Days')
    else:
        print('This month has 30 Days')


days_in_this_month()

'''
2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
împărțirea a două numere.
În final vei putea face:
a, b, c, d = calculator(10, 2)
- print("Suma: ", a)
- print("Diferenta: ", b)
- print("Inmultirea: ", c)
- print("Impartirea: ", d)
'''


def calculator(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a, b, c, d


a, b, c, d = calculator(3, 2)

print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)


'''
3. Funcție care primește o lista de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
'''


def count_cifre(list):
    count_dict = {}
    for cifre in list:
        if cifre in count_dict:
            count_dict[cifre] += 1
        else:
            count_dict[cifre] = 1
    print(count_dict)


count_cifre([1, 5, 5, 5, 2, 3, 1])


'''
4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
'''


def max_number(num1, num2, num3):
    # return max(num1, num2, num3)
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


max_number(5, 3, 7)


'''
5. Funcție care să primească un număr și să returneze suma tuturor numerelor
de la 0 la acel număr
Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
'''

def suma_num(a):
    suma = 0
    for i in range(0, a + 1):
        suma = suma + i
    return suma


print(suma_num(75))

## Exerciții Opționale - Bonus ##

'''
1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
numerele comune
Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
'''

def numbers_same_same(list1, list2):
    list3 = []
    for x in list1:
        if x in list2:
            list3.append(x)
    print(f'Numerele same same sunt: {list3}')


numbers_same_same([1,2,1,2,3], [9,8,7,6,3,2,1])

'''
2.. Funcție care să aplice o reducere de preț
Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
invalidă.
'''

def discount(pret, reducere):
    pret_redus = pret - reducere/100*pret
    if pret_redus > 0:
        print('Pretul dupa reducere este:', {pret_redus},  'RON')
    elif pret_redus == 0:
        print('Produs gratuit')
    else:
        print('Reducerea e invalida')


discount(100, 75)

'''
3. Funcție care să afișeze data și ora curentă din ro
(bonus: afișați și data și ora curentă din China)
'''

from datetime import datetime
import pytz


def data_ora():
    data_ora_ro = datetime.now()
    print('Data si ora in Romania:', data_ora_ro.date(), data_ora_ro.hour)
    china_tz = pytz.timezone('Asia/Singapore')
    data_ora_china = datetime.now(china_tz)
    print('Data si ora in China:', data_ora_china.date(), data_ora_china.hour)


data_ora()


'''
4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
Crăciun dacă nu vrei să ne zici cand e ziua ta :)
'''

from datetime import date


def countdown_date(year):
    b_day = date(year=year, month=2, day=2)
    days_til_b_day = (b_day - date.today()).days
    return days_til_b_day


print(countdown_date(2023))






