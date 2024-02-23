from datetime import date

class Cliente(object):
    valor_valido = lambda x: x in [1,2,3,4,5]

    def __init__(self, nombre : str, fecha_nacimiento : date, peso : float, condicion_fisica : int):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.peso = peso
        self._condicion_fisica = condicion_fisica # ver si falla
        self.entrenamientos = []

    @property
    def condicion_fisica(self):
        return self._condicion_fisica
    
    @condicion_fisica.setter
    def condicion_fisica(self, valor):
        if Cliente.valor_valido(valor):
            self._condicion_fisica == valor
        else: 
            print('Valor invalido.')

    def asignar_entrenamiento(self, ejercicio):
        if ejercicio.nivel_de_dificultad <= int(self.condicion_fisica):
            self.entrenamientos.append(ejercicio)
        else:
            print('No puede hacer ese ejercicio.')

    def eliminar_entrenamiento(self, ejercicio):
        if ejercicio in self.entrenamientos:
            self.entrenamientos.remove(ejercicio)
        else:
            print('Ese ejercicio no está en la lista de ejercicios de este cliente.')

    def consultar_entrenamientos(self):
        return self.entrenamientos

    def calcular_entrenamiento(self):
        return sum(ejercicio.calorias_quemadas() for ejercicio in self.entrenamientos)

    def __str__(self):
        return f'Nombre: {self.nombre}, Fecha Nacimiento: {self.fecha_nacimiento}, Peso: {self.peso}, Condicion Física: {self.condicion_fisica}'

class Crossfitero(Cliente):

    def __init__(self, nombre, fecha_nacimiento, peso, condicion_fisica: int, intensidad, modalidad):
        super().__init__(nombre, fecha_nacimiento, peso, condicion_fisica)
        self.intensidad = intensidad
        self.modalidad = modalidad

    def asignar_entrenamiento(self, ejercicio):
        super().asignar_entrenamiento(ejercicio)
        ejercicios_fuerza = 0
        ejercicios_cardio = 0
        funt = lambda x, y: x - y in [-1,0,1]
        if not self.entrenamientos:
            self.entrenamientos.append(ejercicio)
        else:
            if funt(ejercicios_fuerza, ejercicios_cardio):
                self.entrenamientos.append(ejercicio)
            else:
                print('No puedes agregar ese ejercicio.')

    def eliminar_entrenamiento(self, ejercicio):
        return super().eliminar_entrenamiento(ejercicio)

    def asignar_wod(self, wod):
        self.entrenamientos = wod
    
    def __str__(self):
        return f'Nombre: {self.nombre}, Fecha Nacimiento: {self.fecha_nacimiento}, Peso: {self.peso}, Condicion Física: {self.condicion_fisica}, Intensidad: {self.intensidad}, Modalidad: {self.modalidad}'

class Culturista(Cliente):

    def __init__(self, nombre, fecha_nacimiento, peso, condicion_fisica: int):
        super().__init__(nombre, fecha_nacimiento, peso, condicion_fisica)

    def asignar_entrenamiento(self, ejercicio):
        super().asignar_entrenamiento(ejercicio)

    def eliminar_entrenamiento(self, ejercicio):
        return super().eliminar_entrenamiento(ejercicio)

    def asignar_rutina(self, rutina):
        if self.condicion_fisica >= 4:
            self.entrenamientos = rutina
        else:
            print('Su condición física es insuficiente.')

    def __str__(self):
        return f'Nombre: {self.nombre}, Fecha Nacimiento: {self.fecha_nacimiento}, Peso: {self.peso}, Condicion Física: {self.condicion_fisica}'

class Ciclista(Cliente):

    def __init__(self, nombre, fecha_nacimiento, peso, condicion_fisica: int, tipo_de_bicicleta, kilometraje):
        super().__init__(nombre, fecha_nacimiento, peso, condicion_fisica)
        self.tipo_de_bicicleta = tipo_de_bicicleta
        self.kilometraje = kilometraje

    def asignar_entrenamiento(self, ejercicio):
        super().asignar_entrenamiento(ejercicio)

    def eliminar_entrenamiento(self, ejercicio):
        return super().eliminar_entrenamiento(ejercicio)

    def kilometros_anuales(self):
        if self.condicion_fisica >= 3:
            return self.kilometraje * 12
        else:
            print('Su condición física es insuficiente.')

    def __str__(self):
        return f'Nombre: {self.nombre}, Fecha Nacimiento: {self.fecha_nacimiento}, Peso: {self.peso}, Condicion Física: {self.condicion_fisica}, Tipo Bicicleta: {self.tipo_de_bicicleta}, Kilometraje: {self.kilometraje}'