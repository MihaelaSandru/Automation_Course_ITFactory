## Exerciții obligatorii - grad de dificultate: Ușor spre Mediu: ##

'''
1. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
'''
''' in cadrul unui if else, se pot pune conditii care sa duca programul intr-o directie sau alta,
 in f() de rezultatul conditiei '''

'''
2. Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural
daca este numar intreg mai mare ca 0)
'''

x = int(input('Write a natural number: '))
if x > 0 and x <= 9:
   print('Well done!')
else:
   print('This is not a natural number!')

'''
3. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
'''

x = float(input('Write a number: '))
if x > 0:
   print('This is a negative number')
elif x == 0:
   print('This is a neutral number')
else:
   print('This is a positive number')

'''
4. Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).
'''

x = float(input('Write a number: '))
if x > -2 and x < 13:
   print('X is in between -2 and 13')
else:
   print('X is NOT in between -2 and 13')

'''
5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna
cate numere sunt intre x si y, nu rezultatul diferentei intre x si y). Hint: Se va folosi functia
abs
'''

x = int(input('Write a number: '))
y = int(input('Write another number: '))
z = x - y
if z < 5:
   print('The value is lower than 5')
elif z == 5:
   print('The value is 5')
else:
   print('The value is higher than 5')

'''
6. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)
'''

x = int(input('Input number lower than 5 and higher than 27:  '))
if not (x < 5) and (x > 27):
  print('Corect')
else:
  print('Incorect')


'''
7. Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale,
daca nu, afiseaza care din ele este mai mare
'''

x = input('Input a number: ')
y = input('Input a number: ')
z = max(x,y)
if x == y:
   print('They are the same value')
else:
   print(z)

'''
8. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca
triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau
oarecare (nicio latura nu e egala).
'''

x = int(input('Latura 1: '))
y = int(input('Latura 2: '))
z = int(input('Latura 3: '))

if x == y == z:
   print('This is an echilateral triangle')
elif x == y or y == z or x == z:
  print('This is a isoscel triangle')
else:
  print('This is a oarecare triangle')

'''
9. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie!
Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.
'''

x = (input('Type e letter: '))
if x.lower() in ('a', 'e', 'i','o','u'):
   print('This is a Vowel')
elif x.upper() in ('A', 'E', 'I', 'O', 'U'):
   print('This is a Vowel')
else:
   print('This is not a Vowel')

'''
10. Transforma si printeaza notele din sistem românesc in sistem american dupa cum
urmeaza:
a. Peste 9 => A
b. Peste 8 => B
c. Peste 7 => C
d. Peste 6 => D
e. Peste 4 => E
f. 4 sau sub => F
'''

Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F

nota = int(input('Ce nota ai? '))

if nota >= 9 :
  print('Echivalentul este A')
elif nota >= 8:
  print('Echivalentul este B')
elif nota >= 7:
  print('Echivalentul este C')
elif nota >= 6 :
  print('Echivalentul este D')
elif nota > 4:
  print('Echivalentul este E')
else:
  print('Echivatentul este F')




## Exerciții Opționale - grad de dificultate: Mediu spre greu. ##

'''
1. Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
'''

x = int(input('Enter at least 4 digits: '))
if x >= 4:
   print(f'{x} are cel putin 4 cifre')
else:
   print(f'{x} nu are cel putin 4 cifre')


'''
2. Verifica daca x are exact 6 cifre
'''

x = len(input('Enter exactly 6 digits number: '))
if x == 6:
   print(f'{x} has exactly 6 digits')
else:
   print(f'{x} does not have exactly 6 digits')

'''
3. Verifica daca x este numar par sau impar
'''

x = int(input('Enter a number: '))
if (x % 2) != 0:
   print(f'{x} is  odd')
else:
   print(f'{x} is even')


'''
4. Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre
ele
'''

x = int(input('Enter First number: '))
y = int(input('Enter Second number: '))
z = int(input('Enter Third number: '))
if (x > y) and (x > z):
    print(f'{x} is the highest')
elif (y > x) and (y > z):
    print(f'{y} is the highest')
elif x == y == z:
    print('The values are the same')
else:
    print(f'{z} is the highest')

'''
5. Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca
triunghiul este valid sau nu (un triunghi este valid daca suma tuturor unghiurilor este de
180 de grade sau daca suma lungimilor a oricare doua laturi este mai mare decat
lungimea celei de-a treia laturi)
'''

x = int(input('Prima latura este: '))
y = int(input('A 2-a latura este: '))
z = int(input('A 3-a latura este: '))
# Check if the angles sum is 180 or not
if (x + y + z == 180) and X != 0 and y != 0 and z != 0:
    print('The Triangle is valid')
else:
    print('The triangle is invalid')

'''
6. Avand stringul: 'Coral is either the stupidest animal or the smartest rock' citește de
la tastatura un număr x de tip int și afișează stringul fără ultimele x caractere. ex: dacă
ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the
smarte'
'''

string = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('How many characters do you want to chop from the end? '))
print(f'{string[: - x]}')

'''
7. Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format
din primele 5 caractere + ultimele 5
'''


string2 = string[:5] + string[-5:]
print(string2)

'''
8. Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza
indexul de start al cuvântului rock - adică poziția in string la care începe cuvântul rock
(hint: este o funcție care te ajuta sa faci asta). Folosind aceasta variabila + slicing,
afișează tot stringul pana la acest cuvant. Output asteptat: 'Coral is either the stupidest
animal or the smartest '
'''

string3 = string.index('rock')
print(string3)
sliced_string = slice(string3)
print(string[sliced_string])

'''
9. Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel. Se
va folosi un assert. Atentie: se dorește ca programul sa fie case insensitive, adica 'apA'
e acceptat ca un string in care primul si ultimul caracter este la fel (hint, te poti folosi de o
functie pentru a face string-ul case insensitive)
'''

x = input('Give string: ')
first_char = x[0].lower()
last_char = x[-1].lower()
assert first_char == last_char, 'Primul si ultimul caracter nu sunt la fel'
print('Primul si ultimul caracter sunt la fel')


'''
10.  Avand stringul '0123456789'
● Afișați doar numerele pare
● Afișați doar numerele impare
(hint: folositi slicing, controlați din pas)
'''

numbers_string = '0123456789'
print(f' The even numbers are:', numbers_string[0::2])
print(f'The odd numbers are:', numbers_string[1::2])

'''
2. Joc de noroc
- Cauta pe net si vezi cum se genereaza un numar random
- Imagineaza-ti ca dai cu zarul si salvezi acest numar intr-o variabila numita dice_roll.
Numarul salvat va fi generat random cu metoda gasita in online
- Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator
- Verifica si afiseaza daca utilizatorul a ghicit numarul
- Vor exista 3 optiuni care vor trebui tratate:
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
● Ai ghicit. Felicitari? Ai ales x si zarul a fost y
'''



import random
number = random.randint(1,6)
input = int(input('Guess the number: '))
if number < input:
   print(f'You lose, you got {input} that is higher than {number}')
elif number > input:
   print(f' You lose, you got {input} that is lower than {number}')
else:
   print(f'Gz!, you got {input} and the number was {number}')



## Exerciții Bonus ##

'''
1. Vrem sa cream o aplicatie pentru achizitionare bilete de avion care sa primeasca drept
inputuri urmatoarele informatii:
a. Varsta
b. Insotit de mama
c. Insotit de tata
d. Pasaport
e. Act permisiune mama
f. Act permisiune tata
Conditii de imbarcare:
1. Daca pers are varsta peste 18 ani si are pasaport
2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte
si are permisiune in scris de la celalat parinte
Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu toate
variantele care crezi ca ar trebui testate. Genereaza scenarii de testare cu expected results si
apoi ruleaza codul pentru a verifica daca expected results sunt egale cu actual results.
Exemple:
1. Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
2. Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
'''


varsta = int(input("Va rugam sa introduceti varsta pasagerului "))
pasaport_valid = input("E pasaportul valid? Da/Nu ")
if varsta>=18 and pasaport_valid == "Da":
    print("Va puteti imbarca")
elif varsta<18 and pasaport_valid == "Da":
    ambii_parinti = input("E copilul insotit de ambii parinti? ")
    if ambii_parinti == "Da":
        print("Va puteti imbarca")
    else:
        permisiune = input("Permisiune parinte lipsa: ")
        if permisiune == "Da":
            print("Va puteti imbarca")
        else:
            print("Nu va puteti imbarca")
else:
    print("Nu va puteti imbarca")