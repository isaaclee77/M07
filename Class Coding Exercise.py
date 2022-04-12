
class Animal:
    def __init__(self, name, species):
        self.__name = name
        self.__species = species

    @property
    def name(self):
        print('getting name')
    
    @property
    def species(self):
        print('getting species')
    
    def move(self):
        print('moving')
    def eat(self):
        print('eating')


class books:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
    
    def read(self):
        print('reading')


class vehicle:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
    
    def drive(self):
        print('driving')

