
import numpy as np
import math   
import pandas as pd 

#### Definiendo clase 4 ####

class TablaDatos:

    def __init__(self, df = pd.DataFrame()):
        self.__df = df

    @property

    def df(self):
        return self.__df
        
    
    def __variables_categoricas(self):

        posiciones_cat = []
        indice = 0  
        
        for columna in self.__df.columns:
            if self.df[columna].dtype == 'object': 
                posiciones_cat.append(indice)  
                indice += 1  
        return posiciones_cat
            
    def __variables_numericas(self):

        posiciones_num = []
        indice = 0  
        
        for columna in self.__df.columns:
            if self.df[columna].dtype in ['float64', 'int64']: 
                posiciones_num.append(indice)  
                indice += 1  
        return posiciones_num    
            
    def resumen_columnas (self):
        res_dicc = {}

        for index in self.__variables_numericas():
            nombre_columna = self.__df.columns[index]
            res_dicc[nombre_columna] = self.__df[nombre_columna].mean()

        for index in self.__variables_categoricas():
            nombre_columna = self.__df.columns[index]
            res_dicc[nombre_columna] = self.__df[nombre_columna].mode()[0]

        return res_dicc
    
    def producto_punto (self, x1, x2):

        if x1 not in self.__variables_numericas() or x2 not in self.__variables_numericas():
            return print("Alguno de los números de columna no es númerico")
            
        resultado = (self.__df.iloc[:, x1] * self.__df.iloc[:, x2]).sum()

        return {"Columna 1" : self.__df.columns[x1] ,
                "Columna 2" : self.__df.columns[x2],
                "Producto Punto: " : resultado }
    
    def renombrar_columnas(self, nombre, index): 

        columnas = list(self.__df.columns)
        columnas[index] = nombre
        self.__df.columns = columnas
        
    def eliminar_columna(self, columna):
        
        if columna not in self.__df.columns:
            return f"La columna '{columna}' no existe en el DataFrame"
        
        self.__df.drop(columns=[columna], inplace=True)
        
    def __str__(self):
        
        return f"Data Frame: {self.__df}"



    



        