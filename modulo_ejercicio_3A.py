
import numpy as np
import math   
import pandas as pd 

#### Definiendo clase 3 ####

class Operacion:

    def __init__(self, X = [], Y = []):
        
        if len(X) != len(Y):
            print("Las listas deben tener la misma cantidad de registros")
        
        else:
            
            self.__X = X
            self.__Y = Y
    
    @property

    def X (self):
        return self.__X
    
    @property

    def Y (self):
        return self.__Y
    
    @X.setter

    def X (self, X):

        if len(X) != len(self.__Y):
            print("Las listas deben tener la misma cantidad de registros")
        else:
            self.__X = X


    @Y.setter

    def Y (self, Y):
        
        if len(Y) != len(self.__X):
            print("Las listas deben tener la misma cantidad de registros")
        
        else:
            self.__Y = Y



    def Sumatoria (self):
        
        resultado = []      

        for valores in range(len(self.__X)):
            resultado.append(self.__X[valores] + self.__Y[valores])

        return resultado
    
    def Sumatoria_2(self):

        return sum(self.__X) + sum(self.__Y)
    
    def Matriz (self):
        return pd.DataFrame({"Lista X" : self.__X, "Lista Y": self.__Y})
    

    def Matriz_2(self):
        return [[self.X[i], self.Y[i]] for i in range(len(self.X))]

    def Producto_Punto (self):

        resultado = []
        for valores in range(len(self.__X)):
            resultado.append((self.__X[valores] * self.__Y[valores]))

        return sum(resultado)
    
    def Menor (self):

        contador_x = 0
        contador_y = 0

        for valor in range(len(self.__X)):
            if self.__X[valor] < self.__Y[valor]:
                contador_x += 1
            elif self.__Y[valor] < self.__X[valor]:
                contador_y += 1

        if contador_x > contador_y:
            return self.__X
        
        elif contador_y > contador_x:
            return self.__Y

        else:
            return self.__X    

    
    def Interseccion(self):
        resultado = []
        
        for valor in self.__X:
            if valor in self.__Y and valor not in resultado:
                resultado.append(valor)

        return resultado

    def __str__(self):
        return f"Las listas X y Y son: {self.__X, self.__Y} "
