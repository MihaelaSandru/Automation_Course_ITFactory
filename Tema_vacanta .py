""" OBLIGATORII
1.1 Creeaza 3 liste care sa contina animale:
a. Mamifere
b. Reptile
c. Pasari
"""
mamifere = ['cal ', 'viezure ', 'nutrie ']
reptile = ['salamandra ', 'varan ', 'cameleon ']
pasari = ['pescarus ', 'vultur ', 'egreta ']

"""1.2. Sorteaza fiecare lista alphabetic"""
mamifere.sort()
reptile.sort()
pasari.sort()

"""1.3Creeaza alte 3 liste in care sa salvezi aceleasi elemente din primele 3 liste, 
dar cuvintele sa fie pe dos.
Exemplu insect_list = [“greiere”, “musca”] 🡪 insect_list_r = [“ereierg”, “acsum”]"""

def reverse_list(elem):
    return elem[::-1]


mamifere_invers = [reverse_list(elem) for elem in mamifere]
reptile_invers = [reverse_list(elem) for elem in reptile]
pasari_invers = [reverse_list(elem) for elem in pasari]
print(mamifere_invers)
print(reptile_invers)
print(pasari_invers)

"""1.4 Numara caracterele din fiecare element string din fiecare lista si
 afiseaza lista cu cele mai multe caractere."""
def longest(lista):
    long = 0
    for i in lista:
        long += len(i)
    return long


longest_lista_mamifere = longest(mamifere)
longest_lista_reptile = longest(reptile)
longest_lista_pasari = longest(pasari)

if longest_lista_mamifere > longest_lista_reptile and longest_lista_mamifere > longest_lista_pasari:
    print(mamifere, f'Lista cu cele mai multe caractere este: ', {longest_lista_mamifere}, ' caractere')
elif longest_lista_reptile > longest_lista_pasari:
    print(reptile, f'Lista cu cele mai multe caractere este: ', {longest_lista_reptile},  ' caractere')
else:
    print(pasari, f'Lista cu cele mai multe caractere este: ',{longest_lista_pasari},  ' caractere')


"""1.5 Inlocuieste fiecare al doilea element din fiecare lista cu “I am an intruder”"""

mamifere = ['cal ', 'viezure ', 'nutrie ']
reptile = ['salamandra ', 'varan ', 'cameleon ']
pasari = ['pescarus ', 'vultur ', 'egreta ']


mamifere[1] = 'I am an intruder'
reptile[1] = 'I am an intruder'
pasari[1] = 'I am an intruder'

#or  mamifere[1] = reptile[1] = pasari[1] = "I am an intruder"

"""1.6 Sa se amestece toate elementele random din prima lista. Poti folosi .shuffle()"""


random.shuffle(mamifere)
random.shuffle(reptile)
random.shuffle(pasari)

"""Sa se parcurga lista si daca se gaseste elemental “I am an intruder”, 
sa se returneze pozitia lui, sa se stearga din lista si sa se returneze mesajul:
 “The intruder was kicked out”"""

for x in range(len(mamifere)-1):
    if mamifere[x] == 'I am an intruder':
        print(f'{x} este indexul cautat')
        mamifere.remove(mamifere[x])
        print('The intruder was kicked out')
    else:
        pass

for x in range(len(reptile)-1):
    if reptile[x] == 'I am an intruder':
        print(f'{x} este indexul cautat')
        reptile.remove(reptile[x])
        print('The intruder was kicked out')
    else:
        pass

for x in range(len(pasari)-1):
    if pasari[x] == 'I am an intruder':
        print(f'{x} este indexul cautat')
        pasari.remove(pasari[x])
        print('The intruder was kicked out')
    else:
        pass


"""
2.1 Creeaza clasa animal cu 4 atribute si 2 metode
2.2 Creeaza alte 3 clase care sa mosteneasca clasa animal si adauga inca o metoda
"""

	Creeaza clasa animal cu 4 atribute si 2 metode
  A variable stored in an instance or class is called an attribute.
  A function stored in an instance or class is called a method.
class Animal:
    def __init__(self, varsta, greutate ):
        self.varsta = varsta
        self.greutate = greutate


    def get_varsta(self):
        return self.varsta
    def get_greutate(self):
        return self.greutate
#
"""
2.2 Creeaza alte 3 clase care sa mosteneasca clasa animal si adauga inca o metoda
"""
# Creeaza alte 3 clase care sa mosteneasca clasa animal si adauga inca o metoda

class Feline(Animal):
    def __init__(self, varsta, greutate, sex):
        super().__init__(varsta, greutate)
        self.sex = 'Female'
        print('Alo?')

class Porcine(Animal):
    def __init__(self, varsta, greutate, sociabil):
        super().__init__(varsta, greutate)
        self.sociabil = True
        print('Alo?')


class Cabaline(Animal):
    def __init__(self, varsta, greutate, culoare):
        super().__init__(varsta, greutate)
        self.culoare = 'Maro'
        print(f'Ati vazut un cal {culoare}?')




cat = Feline(2, 3, 'Female')
porc = Porcine(5, 150, 'Da')
cal = Cabaline(3, 150, 'maro')


"""Ex3. Sa se introduca un cuvant de la tastatura si sa se afiseze ce lungime are, 
cate consoane, cate vocale are si daca are vreun numar in compozitie."""

x = input("Type a word: ")
vowels = 0
consonants = 0
numbers = 0
vowels_list = ['a', 'e', 'i', 'o', 'u']
for i in range(len(x)):
    if x[i].isdigit():
        numbers += 1
    elif x[i] in vowels_list:
        vowels += 1
    else:
        consonants += 1
print(f'The typed word has {numbers} numbers, {vowels} vowels and {consonants} consonants')



"""
Ex4.
1.   Sa se creeze un dictionar cu 5 carti care sa contina
numele cartii, autorul, nr_pag, mesaj (daca este available sau nu)
2.   Sa se creeze o functie care sa ii permita bibliotecarului sa poate adauga carti noi in biblioteca (dictionar).
3.   Sa se creeze o functie care sa ii permita bibliotecarului sa poata sterge carti din biblioteca
4.   Sa se creeze o functie care sa ii permita bibliotecarului
sa introduca un nume de carte si sa verifice daca este available sau nu
"""
class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, pages, availability):
        self.books[title] = {'author': author, 'pages': pages, 'availability': availability}

    def delete_book(self, title):
        if title in self.books:
            del self.books[title]
            print(f'The book {title} has been deleted.')
        else:
            print(f'The book {title} was not found in the library.')

    def check_availability(self, title):
        if title in self.books:
            if self.books[title]['availability']:
                print(f'The book {title} is available.')
            else:
                print(f'The book {title} is not available.')
        else:
            print(f'The book {title} was not found in the library.')

    def check_by_name(self, name):
        for title, book in self.books.items():
            if book['author'] == name:
                print(f'The book {title} is written by {name}')
            else:
                print(f'The book was not written by {name}')


library = Library()
library.add_book('Title 1', 'Author 1', 250, True)
library.add_book('Title 2', 'Author 2', 300, False)
library.add_book('Title 3', 'Author 1', 150, True)

library.check_availability('Title 1')
library.check_by_name('Author 1')
library.delete_book('Title 2')

"""Ex5. – Medium
Un user poate sa creeze o rezervare la restaurant care sa contina nume, data, ora, numar persoane, numar mese. 
Numarul de mese se va calcula automat in functie de numarul de persone introdus de utilizator. 
O masa stim ca poate sa aiba 6 locuri.
Cand veti rula programul va aparea prima data un mesaj de genul:
==== “Welcome to our restaurant restaurant_name” ====. 
Puteti alege voi numele restaurantului si mesajul de welcome.
Clientul va fi intrebat daca vrea sa faca o rezervare
Daca raspunde nu, atunci va primi mesajul, “Maybe next time! Have a nice day!”
Daca raspunde da, atunci va fi intrebat numele, data, ora si numarul de persoane.
Dupa ce utilizatorul a introdus datele va fi anuntat ca rezervarea a fost creata:
Reservation was created on the name X, on date Y, at Z hour for N persons.
Sa se foloseasca functii.
Sa se creeze si o functie care apelata va returna lista de rezervari.
"""


restaurant_name = "Nobu"
print("==========Welcome to ", {restaurant_name}, " Restaurant!==========")
want_reservation = input("Would you like to make a reservation (Y/N)? ")
if want_reservation == "N":
        print("Maybe next time! Have a nice day! ")
else:


        def make_reservation(client_name, date, time,  num_people):
            num_tables = num_people // 6
            if num_people % 6 != 0:
                num_tables += 1
            print("Reservation for", client_name, "on", date, "at", time, "for", num_people, "people.")
            print("Number of tables needed:", num_tables)

        client_name = input("Enter the client name: ")
        date = input("Enter the date of reservation (MM/DD/YYYY): ")
        time = input('Enter the time (HH:MM): ')
        num_people = int(input("Enter the number of people: "))
        make_reservation(client_name, date, time, num_people)



