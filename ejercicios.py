from abc import ABC, abstractmethod, abstractclassmethod

class Ejercicio(ABC):

    @abstractmethod
    def __init__(self, nombre, nivel_de_dificultad : int, calorias):
        pass

    @abstractmethod
    def calorias_quemadas(self):
        pass

class Cardio(Ejercicio):

    def __init__(self, nombre, nivel_de_dificultad : int, calorias, duracion):
        self.nombre = nombre
        self.nivel_de_dificultad = nivel_de_dificultad
        self.calorias = calorias
        self.duracion = duracion

    def calorias_quemadas(self):
        return self.duracion / 60 * self.calorias
    
    def __str__(self):
        return f'Nombre: {self.nombre}, Dificultad: {self.nivel_de_dificultad}, Calorias: {self.calorias}, Duración: {self.duracion}'

class Fuerza(Ejercicio):

    def __init__(self, nombre, nivel_de_dificultad : int, calorias, series, repeticiones, tiempo_tension, tiempo_descanso):
        self.nombre = nombre
        self.nivel_de_dificultad = nivel_de_dificultad
        self.calorias = calorias
        self.series = series
        self.repeticiones = repeticiones
        self.tiempo_tension = tiempo_tension
        self.tiempo_descanso = tiempo_descanso

    def calorias_quemadas(self):
        return (self.series * self.repeticiones * self.tiempo_tension + (self.series - 1) * self.tiempo_descanso) * self.calorias
    
    def __str__(self):
        return f'Nombre: {self.nombre}, Dificultad: {self.nivel_de_dificultad}, Calorias: {self.calorias}, Series: {self.series}, Repeticiones : {self.repeticiones}, Tiempo Tension: {self.tiempo_tension}, Tiempo Descanso: {self.tiempo_descanso}'
