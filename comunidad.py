#Imports
import numpy as np
import random

class Comunidad:
    def __init__(self, num_ciudadanos, promedio_conexion_fisica, enfermedad, num_infectados, probabilidad_conexion_fisica):
        self.num_ciudadanos = num_ciudadanos
        self.promedio_conexion_fisica = promedio_conexion_fisica
        self.enfermedad = enfermedad
        self.probabilidad_conexion_fisica = probabilidad_conexion_fisica
        
        self.susceptibles = num_ciudadanos - num_infectados
        self.infectados = num_infectados
        self.recuperados = 0
        self.muertos = 0
    
    def step(self):
        new_infectados = self.calcular_nuevos_infectados()
        new_recuperados = self.calcular_nuevos_recuperados()
        new_muertos = self.calcular_nuevos_muertos()
        
        self.susceptibles -= new_infectados
        self.infectados += new_infectados - new_recuperados - new_muertos
        self.recuperados += new_recuperados
        self.muertos += new_muertos
        
        if self.infectados < 0:
            self.infectados = 0
        if self.susceptibles < 0:
            self.susceptibles = 0
    
    def calcular_nuevos_infectados(self):
        posibles_infectados = self.infectados * self.promedio_conexion_fisica
        nuevas_infecciones = np.sum(np.random.rand(int(posibles_infectados)) < self.probabilidad_conexion_fisica)
        return min(nuevas_infecciones, self.susceptibles)
    
    def calcular_nuevos_recuperados(self):
        nuevos_recuperados = int(round(self.enfermedad.tasa_recuperacion * self.infectados))
        return min(nuevos_recuperados, self.infectados)
    
    def calcular_nuevos_muertos(self):
        tasa_mortalidad = 0.02
        nuevos_muertos = int(round(tasa_mortalidad * self.infectados))
        return min(nuevos_muertos, self.infectados)