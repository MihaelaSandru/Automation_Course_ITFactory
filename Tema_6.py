## Exerciții obligatorii - grad de dificultate: Usor spre Mediu ##

'''
1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
- descrie_cerc() - va PRINTA culoarea și raza
- aria() - va RETURNA aria
- diametru()
- circumferinta()
'''

class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare


    def descrie_cerc(self):
        return self.culoare and self.raza


    def aria(self):
        return self.raza**2


    def diametru(self):
        return self.raza*2


    def circumferinta(self):
        return self.raza**2*3.14


'''
2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
- descrie()
- aria()
- perimetrul()
- schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().
'''
class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare


    def descrie(self):
        print('Datele sunt: ', self.lungime, self. latime, self.culoare)


    def aria(self):
        return self.latime + self.latime


    def perimetru(self):
        return 2*self.lungime + 2*self.latime


    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


obj1 = Dreptunghi(10, 20, 'rosu')
obj1.descrie()


'''
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
- descrie()
- nume_complet()
- salariu_lunar()
- salariu_anual()
- marire_salariu(procent)
'''

class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Detalii anagajat: Nume: {self.nume} Prenume: {self.prenume} Salariu: {self.salariu}')

    def nume_complet(self):
        nume_complet = self.nume + ' ' + self.prenume
        return nume_complet

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        marire = procent * self.salariu / 100
        return marire


angajat1 = Angajat('Birlic', 'Gheorghe', 12000)
angajat1.descrie()
print(f'Numele complet al angajatului este: {angajat1.nume_complet()}')
print(f'Salariul lunar al angajaturlui este: {angajat1.salariu_lunar()} RON')
print(f'Salariul anual al angajaturlui este: {angajat1.salariu_anual()} RON')
print(f'Angajatul a primit o marire de {angajat1.marire_salariu(10)} RON')

angajat2 = Angajat('Sandru', 'Sabin', 8000)
angajat2.descrie()
print(f'Numele complet al angajatului este: {angajat2.nume_complet()}')
print(f'Salariul lunar al angajaturlui este: {angajat2.salariu_lunar()} RON')
print(f'Salariul anual al angajaturlui este: {angajat2.salariu_anual()} RON')
print(f'Angajatul a primit o marire de {angajat2.marire_salariu(12)} RON')


'''
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
- afisare_sold() - Titularul x are în contul y suma de n lei
- debitare_cont(suma)
- creditare_cont(suma)
'''

class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular} are in contul: {self.iban} suma de {self.sold} lei')

    def debitare_cont(self, suma):
        debitare = self.sold - suma
        print(f'Contul {self.iban} a fost debitat cu suma de {suma} lei')
        self.sold = debitare
        return debitare

    def creditare_cont(self, suma):
        creditare = self.sold + suma
        print(f'Contul {self.iban} a fost creditat cu suma de {suma} lei')
        self.sold = creditare
        return creditare


cont1 = Cont('ABC1234', 'Raed Arafat', 150.00)
cont1.afisare_sold()
cont1.debitare_cont(12)
cont1.afisare_sold()
cont1.creditare_cont(312)
cont1.afisare_sold()


cont2 = Cont('ABC1235', 'Larisa Dragna', 900.00)
cont2.afisare_sold()
cont2.debitare_cont(100)
cont2.afisare_sold()
cont2.creditare_cont(4925654.84)
cont2.afisare_sold()



## Exerciții Opționale - grad de dificultate: Mediu spre greu.##

'''
1. Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
- schimbă_cantitatea(cantitate)
- schimbă_prețul(pret)
- schimbă_nume_produs(nume)
- generează_factura() - va printa tabelar dacă reușiți
Factura seria x numar y
Data: generați automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7 | 700 | 49000
'''
from datetime import datetime

class Invoice:
    series = 'ABC'

    def __init__(self, number, product_name, quantity, unit_price):
        self.number = number
        self.product_name = product_name
        self.quantity = quantity
        self.unit_price = unit_price


    def change_quantity(self, quantity):
        self.quantity = quantity
        return self.quantity


    def change_price(self, price):
        self.unit_price = price
        return self.unit_price


    def change_product_name(self, name):
        self.product_name = name
        return self.product_name


    def generate_invoice(self):
        date = datetime.today().strftime('%m.%d.%Y')
        total = self.quantity * self.unit_price
        print(f'The Invoice with series{self.series} and number: {self.number}')
        print(f'Date: ', date)
        print('{:<20}{:<12}{:<18}'.format('|PRODUCT', '| QUANTITY', '| PRICE PER UNIT', '|GRAND TOTTAL'))
        print('{:<20}{:<12}{:<18}'.format('-------------------', '|---------', '|------------', '|---------'))
        print('{:<20}{:<12}{:<20}'.format(''+str(self.product_name), '| ' + str(self.quantity), '| ' + str(self.unit_price), '| '+ str(total)))
        print('{:<20}{:<12}{:<12}'.format('-------------------', '|---------', '|------------', '|---------'))


invoice1 = Invoice(1, 'Electricity', 12, 9)
invoice1.generate_invoice()
invoice1.change_quantity(200)
invoice1.change_price(800)
invoice1.change_product_name('Therapy')
invoice1.generate_invoice()


'''
2.Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
- descrie() - se vor printa toate atributele, în afară de culori_disponibile
- înmatriculare() - va schimba atributul înmatriculată în True
- vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
- accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
- franeaza() - mașina se va opri și va avea viteza 0
'''


class Masina:
    marca = 'Racheta'
    viteza_actuala = 0
    culoare = 'gri'
    culori_disponibile = {'albastru', 'verde', 'roz', 'mov', 'negru'}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def description(self):
        print()
        print(f'Marca: {self.marca}')
        print(f'Model: {self.model}')
        print(f'Viteza Maxima: {self.viteza_maxima}')
        print(f'Viteza Actuala: {self.viteza_actuala}')
        print(f'Culoare: {self.culoare}')
        print(f'Inmatriculata: {self.inmatriculata}')

    def inmatriculare(self):
        response = (input(f'Doriti sa schimbati statusul masinii: (y/n)')).lower()
        if response == 'y':
            self.inmatriculata = True
        else:
            return

    def vopseste(self, culoare):
        if culoare in self.culori_disponibile:
            print(f'Am vopsit masina in culoarea {culoare}')
            self.culoare = culoare
        else:
            print(f'Errore: Culoarea nu exista, alegeti alta culoare')
            return

    def accelereaza(self, viteza):
        if viteza <= 0:
            print('Erroare')
        elif viteza > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
            print(f'Masina a accelerat la {self.viteza_actuala} km/h')
        else:
            self.viteza_actuala = viteza
            print(f'masina a accelerat la {self.viteza_actuala} km/h')

    def franeaza(self):
        self.viteza_actuala = 0
        print(f'Masina s-a oprit si are viteza de {self.viteza_actuala} km/h')


masina1 = Masina('model1', 210)
culoare = input('Introdu culoarea: ')
masina1.vopseste(culoare)
masina1.description()
masina1.accelereaza(1000)
masina1.franeaza()
masina1.inmatriculare()
masina1.description()

'''
3. Clasa TodoList
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
Metode:
- adauga_task(nume, descriere) - se va adauga in dict
- finalizează_task(nume) - se va sterge din dict
- afișează_todo_list() - doar cheile
- afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
printăm detalii suplimentare.
- Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
adauge.
- Dacă acesta răspunde nu - la revedere
- Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
dict
'''


class Todo:
    dict = {}

    def add_task(self, name, description):
        self.dict[name] = description

    def task_done(self, name):
        self.dict.pop(name)
        print(f'Task {name} has been completed. GZ!')

    def show_todo(self):
        print('Lista de taskuri: ')
        for key in self.dict:
            print(key)

    def show_details(self, name):
        if name not in self.dict.keys():
            add_new_task = input(f"Task-ul cautat \"{name}\" nu este in todo list. Vrei sa-l adaugam? (y/n)").lower()
            if add_new_task == "y":
                description = input("Adauga o descriere task-ului: ")
                self.add_task(name, description)
            else:
                print("Ok, Goodbye!")
        else:
            print(f"Task-ul \"{name}\" este deja in todo list cu descrierea: \"{self.dict[name]}\"")


todo1 = Todo()
todo1.add_task('obiectul1', 'cu descrierea aceasta frumoasa')

todo2 = Todo()
todo2.add_task('obiectul2', 'cu descrierea aceasta si mai frumoasa')

todo3 = Todo()
todo3.add_task('obiectul3', 'cu descrierea cea mai frumoasa')
todo3.show_todo()
todo3.show_details('obiectul')
todo3.task_done('obiectul3')
todo3.show_todo()
todo3.show_details('obiectul')



