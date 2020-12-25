class People:
    def __init__ (self, name, age, hight):
       self.name = name
       self.age = age
       self.hight = hight
    
    def set_name(self, new):
        self.__name = new
    
    def set_age(self, new):
        self.__age = new

    def set_hight(self, new):
        self.__hight = new
    
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    
    def get_hight(self):
        return self.__hight

    def imprimir(self):
        print(f'Name: {self.__name}\nAge: {self.__age}\nHight: {self.__hight}')

class agenda(People):
    lista = [10]
    def __init__(self,name, age, hight):
        super().__init__(name, age, hight)
    
    def armazenaPessoa(self, People):
        lista.append(People)
    
    def imprimir(self):
        print(lista)

pablo = People('pablo', 24, 1.76)
Agenda = agenda(pablo)
Agenda.imprimir()