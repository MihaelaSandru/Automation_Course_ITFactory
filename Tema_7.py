'''
1. Creează-ți cont de github și încarcă într-un repo nou tot ce am facut până
acum la ore.
Curs git/github https://bit.ly/3yfFvqL
VIDEOS 1, 2 si 3
2. Rezolvă exercițiul după ce ai urcat proiectul (tot ce am facut până acum
împreună).

ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’
INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură

ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
implementezi metoda abstractă aria)
Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)

POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Patrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui
3. Actualizează proiectul pe github facand un push la noul cod
În Foldereul de teme ajunge să pui doar linkul cu proiectul tău public
Curs git/github
https://bit.ly/3yfFvqL - VIDEO 4
'''


#-----2 ABSTRACTION

from abc import abstractmethod, ABC

class GeometicalForm(ABC):
    pi = 3.14

    @abstractmethod
    def area(self):
        pass


    def describe(self):
        print('Most likely I have corners!')


#-----2.1 INHERITANCE


class Square(GeometicalForm):
    def __init__(self, side):
     self.__side = side


#-----2.2 ENCAPSULATION


    @property
    def get_side(self):
        return self.__side


    def set_side(self, new_side):
        self.__side = new_side


    def del_side(self):
        del self.__side


    def area(self):
        return self.__side ** 2




class Circle(GeometicalForm):
    def __init__(self, ray):
        self.__ray = ray


    @property
    def get_ray(self):
        return self.__ray


    def set_ray(self, new_ray):
        self.__ray = new_ray


    def del_ray(self):
        del self.__ray


    def area(self):
        return self.pi  *  self.__ray ** 2


#-----2.3 POLYMORPHISM


    def describe(self):
        print("I don't have corners")


def calculate_area(shape):
    return shape.area()



sqare1 = Square(2)
sqare1.describe()
print('The side of the square1 is: ', sqare1.get_side)
print('The area of the square1 is: ', sqare1.area())
sqare1.set_side(16)
print('The new value of the side on square1 is: ', sqare1.get_side)
print('The area is now: ', sqare1.area())
#sqare1.del_side()  # had to be commentd out so calculate area can work

circle1 = Circle(22)
circle1.describe()
print('The area of the circle1 is: ', circle1.area())
circle1.set_ray(127)
print('the new value of the ray in circle1 is: ', circle1.get_ray)
print('The area of the circle1 is now: ', circle1.area())
#circle1.del_ray()  # had to be commentd out so calculate area can work

print('The polymorphed functon returned the value for the square1: ', calculate_area(sqare1))
print('The polymorphed functon returned the value for the circle1: ', calculate_area(circle1))


