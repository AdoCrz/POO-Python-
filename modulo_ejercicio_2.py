
import numpy as np
import math    

#### Definiendo clase 2 ####

class Elipse:

    def __init__(self, radio_menor = 0, radio_mayor = 0):

        if isinstance(radio_menor, (float, int)) and isinstance(radio_mayor, (float, int)) :
            self.__radio_menor = radio_menor
            self.radio_mayor = radio_mayor

        else:
            print("Alguno de los valores no es númerico, por favor introduce un valor numérico")

    @property

    def radio_menor(self):
        return self.__radio_menor
    
    @property

    def radio_mayor(self):
        return self.__radio_mayor

    @radio_menor.setter
    
    def radio_menor(self, radio_menor):

        if isinstance(radio_menor, (float, int)):
            self.__radio_menor = radio_menor
        else:
            print("El valor no es númerico, por favor introduce un valor numérico")

    @radio_mayor.setter

    def radio_mayor (self, radio_mayor):

        if isinstance(radio_mayor, (float, int)):
            self.__radio_mayor = radio_mayor

        else:
            print("El valor no es númerico, por favor introduce un valor numérico")


    def perimetro(self):

        return 2 * math.pi * np.sqrt((np.square(self.__radio_menor) + np.square(self.__radio_mayor)) / 2)
    
    def area(self):
        return  math.pi * self.radio_mayor * self.radio_menor
    
    def __str__(self):
        return "Elipse: (%.2f, %.2f )" % (self.__radio_menor, self.__radio_mayor)
