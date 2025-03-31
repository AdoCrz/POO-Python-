
#### Definiendo clase 1 ####
import numpy as np
import math

class Circulo:
    def __init__(self, radio = 0):
        if isinstance(radio, (float, int)):
            self.__radio = radio
        else:
            print("El valor no es númerico, por favor introduce un valor numérico")

    @property

    def radio(self):
        return self.__radio
    
    @radio.setter
    
    def radio(self, radio):

        if isinstance(radio, (float, int)):
            self.__radio = radio
        else:
            print("El valor no es númerico, por favor introduce un valor numérico")


    def perimetro(self):

        return 2 * math.pi * self.__radio
    
    def area(self):
        return  math.pi * (np.square(self.__radio))
    
    def __str__(self):
        return "Radio circulo: (%.2f)" % (self.__radio)
    

