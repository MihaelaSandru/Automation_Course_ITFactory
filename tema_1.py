'''
1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
'''

# Variabila = locatie de memorie in care se stochează valori.

'''
2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă :
- string
- int
- float
- bool
Observație: Valorile vor fi alese de tine după preferințe.
'''

a = 'Miha are mere' #string
b = 9 #int
c = round(9.9) #era float, am vrut sa ma joc si sa pun toate tipurile pe o singura linie la exercitiul 5 si atunci cred ca am pus round 😀
d = (c>b) #bool
e = ['Miha' , 'are', (c),''  'pere'] #list

'''
3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
'''
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

'''
4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere):
- Verifică tipul acesteia.
'''

c = round(9.9)
print(type(c))

'''
5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
Rezolvă nepotrivirile de tip prin ce modalitate dorești.
'''

print(a[0:9], b, a[9:13], 'si se lauda la Pycharm:', e,  c<b)
print("Miha are 9 mere si se lauda la Python\n")
print('\n'.join(map(str, e)))

msg = f'{a} {e} "Miha nu are ce face cu ele"'
print(msg)


'''
6. Citește de la tastatură:
- numele;
- prenumele.
Afișează: 'Numele complet are x caractere'.
'''

nume = input('Care este numele tau? ')
prenume = input('Care este prenumele tau? ')
# print(nume + ' ' + prenume)


'''
7. Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.
'''

lungime_dreptunghi = int(input('Care este lungimea dreptunghiului? '))
latime_dreptunghi = int(input('Care este latimea dreptunghiului'))
print('Aria dreptunghiului este: ',lungime_dreptunghi * latime_dreptunghi)

'''
8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
- afișează de câte ori apare cuvântul 'the';
'''

str  = "Coral is either the stupidest animal or the smartest rock"
print(str.count(' the '))

'''
9. Același string.
● Afișează de câte ori apare cuvântul 'the';
● Printează rezultatul.
'''

prop ='Coral is either the stupidest animal or the smartest rock'
print(f'{prop.replace("the", "THE")}')


'''
10. Același string.
● Folosiți un assert ca să verificați dacă acest string conține doar numere.
'''

assert "Coral is either the stupidest animal or the smartest rock".isnumeric() == True, 'This text DOES NOT have only numbers'
print('The text has only numbers')

## Exerciții Opționale - grad de dificultate: Mediu spre greu (s-ar putea să ai nevoie de Google). ##

'''
1. Exercițiu:
- citește de la tastatură un string de dimensiune impară;
- afișează caracterul din mijloc.
'''


culoare_preferata = input('Care este culoarea ta preferata? ')
lenght = len(culoare_preferata)%2

if (lenght == 0):
   print('Propozitia are numar par de caractere')
else:
   print('Propozitia are numar IMPAR de caractere')



optiune_impara = input('Alege una dintre optiuni: patru, sapte, opt ')
caracterul_din_mijloc = optiune_impara[len(optiune_impara)//2]
print(caracterul_din_mijloc)


'''
2. Folosind assert, verifică dacă un string este palindrom.
'''

x = input('Insert a word: ')
assert  x == x[::-1] == True, 'This is not a palindrome'
print('This is a palindrome')


'''
3. Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.
'''

intrebare = input('Scrie un string: ')
x, y = text.split(‘’)
print(f’Primul cuvant este: {x}’)

print (f' Ultimul cuvant: {y}’)


'''
4. Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.
'''

string = input('Scrie Alabala portocala: ')
first_char = string[0]
last_char = string[-1]
print(first_char + string[1:-1].replace(first_char,first_char.upper()) + last_char)

'''
5.Exercițiu:
- citește un user de la tastatură;
- citește o parolă;
- afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
afișeze corect.
eg: parola abc => ***
parola abcd => ****
'''


user = input('Enter User: ')
password = input('Enter Password: ')
char_count = len(password)
star = '*' * char_count
print(f'Parola pt user {user} este {star} si are {char_count} caractere')
