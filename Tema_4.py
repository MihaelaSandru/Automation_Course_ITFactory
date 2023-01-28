# Exerciții obligatorii - grad de dificultate: Usor spre Mediu ##

'''
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']

for masina in masini:
    print(f'Mașina mea preferată este {masina}')

for masina in range(len(masini)):
    print(f'FOR: Masina mea preferata este {masini[masina]}')

a = 0
while a <= len(masini):
    print(f'Mașina mea preferată este {masini[a]}')
    a += 1



'''
2. Aceeași listă:
Folosește un for else
În for
- Modifică elementele din listă astfel încât să fie scrie cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista.
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']

for masina in range(1, len(masini[:-1])):
    masini[masina] = masini[masina].upper()
else:
    print(masini)


'''
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']
car_wanted = input('Introdu marca de masina dorita: ').capitalize()

for car in masini:
    if car == car_wanted:
        print(f'Am găsit mașina dorită de dvs: {car_wanted}')
        break
    else:
        print(f'Am găsit mașina {car}. Mai căutam')
else:
    print('Nu avem la vanzare modelul de masina introdus')

'''
4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == 'Lăstun'or masina == 'Trabant':

        continue
    print(f'S-ar putea să vă placă mașina {masina}')

'''
5. Modernizează parcul de mașini:
- Crează o listă goală, masini_vechi.
- Itereaza prin mașini.
- Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
- Printează Modele vechi: x.
- Modele noi: x.
'''

masini_vechi = []

for masina in masini:
    if masina == 'Lăstun' or masina == 'Trabant':
        masini_vechi.append(masina)
        index = masini.index(masina)

print('Modele vechi:',  masini_vechi)
print('Modele noi: ',  masini)

'''
6. Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
- Prezintă doar mașinile care se încadrează în acest buget.
- Itereaza prin dict.items() și accesează mașina și prețul.
- Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
- Iterează prin listă.
'''

pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
for masina in pret_masini:
    if pret_masini[masina] <= 15000:
        print(f"{masina} si costa {pret_masini[masina]}")

a = pret_masini.items()

for masina in a:
    print(masina)
for masina1 in a:
    if masina1[1] <= 15000:
        print(f"Pentru un buget de sub 15000 euro puteți alege mașină ", masina1[0])


'''
7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
- Iterează prin ea.
- Afișează de câte ori apare 3 (nu ai voie să folosești count).
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

for numar in numere:
    print(numar)

trei_apare = 0

for numar in numere:
    if numar == 3:
        trei_apare += 1
print (f"3 apare de {trei_apare} ori in lista.")

'''
8. Aceeași listă:
- Iterează prin ea
- Calculează și afișează suma numerelor (nu ai voie să folosești sum).
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

suma = 0

for numar in range(len(numere)):
    suma += numere[numar]
    print(suma)

'''
9. Aceeași listă:
- Iterează prin ea.
- Afișază cel mai mare număr (nu ai voie să folosești max).
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

for i in numere:
    if numere[i] < i:
        print(i)

'''
10. Aceeași listă:
- Iterează prin ea.
- Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
- Afișază noua listă.
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for n in numere:
    print(-n)

# Exerciții Opționale - grad de dificultate: Mediu spre greu..##

'''
1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final
'''

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for nr in alte_numere:
    if nr % 2 == 0:
        numere_pare.append(nr)
    else:
        numere_impare.append(nr)
    if nr > 0:
        numere_pozitive.append(nr)
    else:
        numere_negative.append(nr)

print('Numerele pare sunt: ', numere_pare)
print('Numerele impare sunt: ', numere_impare)
print('NUmerele pozitive sunt: ', numere_pozitive)
print('Numerele negative sunt: ', numere_negative)


'''
2. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
'''

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

for i in range (len(alte_numere)):
    for j in range (i + 1, len((alte_numere))):
        if alte_numere[i] > alte_numere [j]:
            alte_numere[i], alte_numere[j], = alte_numere[j], alte_numere[i]
print(alte_numere)

'''
3. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr
Programul îi spune:
● Nr secret e mai mare
● Nr secret e mai mic
● Felicitări! Ai ghicit!
'''


import random
number = random.randint(1, 30)
input = int(input('Guess the number: '))
if number < input:
    print(f'You lose, you got {input} that is higher than {number}')
elif number > input:
    print(f' You lose, you got {input} that is lower than {number}')
else:
    print(f'Gz!, you got {input} and the number was {number}')

'''
4. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777
Ex:3
1
22
333
'''

nr = int(input("Scrie un numar: "))
i = 1
while i <= nr:
    print(' ')
    for j in range(i):
        j = i
        print(j, end='')
        j = j + 1
    i = i + 1

'''
5.
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
'''

tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'Cifra curenta este {tastatura_telefon[i][j]}')

# sau cu for each
for row in tastatura_telefon:
    for column in row:
        print(f'FOR EACH: Cifra curenta este {column}')

