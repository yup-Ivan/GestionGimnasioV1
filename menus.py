
def condiciones_fisicas():
    condiciones = [
        {"id" : "1", "cond" : "Sedentario"},
        {"id" : "2", "cond" : "Actividad ligera (1 a 2 días por semana, actividad ligera)"},
        {"id" : "3", "cond" : "Actividad media (3 días por semana, combina actividad enérgica y ligera)"},
        {"id" : "4", "cond" : "Actividad intensa (4 a 5 días por semana, principalmente actividad enérgica)"},
        {"id" : "5", "cond" : "Deportista (6 días por semana, actividad muy enérgica o profesional)"}
    ]
    print()
    for condicion in condiciones:
        print(f'{condicion["id"]} - {condicion["cond"]}')

def opcion_principal():
    return int(input("""
1 - Ejercicios 
2 - Clientes 
3 - Entrenadores 
4 - Salir
Selecciona una opción: """))

def menu_ejercicios():
    return int(input("""
1 - Crear ejercicio 
2 - Consultar ejercicios (se mostrarán los ejercicios y se dará la opción de modificar un ejercicio existente) 
3 - Borrar ejercicio 
Selecciona una opción: """))

def menu_clientes():
    return int(input("""
1 - Crear cliente 
2 - Consultar clientes (se mostrarán los clientes y se dará la opción de seleccionar un cliente existente) 
3 - Calcular ejercicio (del cliente seleccionado, si hay alguno) 
4 - Modificar cliente o *VER OPCIONES* (del cliente seleccionado, si hay alguno) 
5 - Borrar cliente  (del cliente seleccionado, si hay alguno) 
6 - Cliente seleccionado: (indicará “ninguno” o el nombre del cliente si sí hay alguno seleccionado) 
Selecciona una opción: """))

def tipo_ejercicio():
    return int(input("""
1. Cardio.
2. Fuerza.        
Selecciona una opción: """))

def tipo_cliente():
    return int(input("""
1. Cliente normal.
2. Cliente crossfitero.
3. Cliente culturista.
4. Cliente ciclista.
Selecciona una opción: """))

def menu_entrenador():
    return int(input("""
1 - Crear entrenador 
2 - Consultar entrenadores (se mostrarán los entrenadores y se dará la opción de seleccionar un entrenador) 
3 - Ver lista de clientes (del entrenador seleccionado, si hay alguno) 
4 - Modificar entrenador (del entrenador seleccionado, si hay alguno) 
5 - Borrar entrenador (del entrenador seleccionado, si hay alguno) 
6 - Entrenador seleccionado: (indicará “ninguno” o el nombre del entrenador si sí hay alguno seleccionado) 
Selecciona una opción: """))

def nuevo_ejercicio():
    nombre = input('Introduce el nombre del ejercicio: ')
    nivel_de_dificultad = input('Introduce el nivel de dificultad: ') 
    calorias = input('Introduce las calorias que consume por horas el ejercicio: ')
    return nombre, nivel_de_dificultad, calorias

def duracion_cardio():
    return input("Duración del ejercicio: ")

def ejercicio_fuerza():
    repeticiones = input('Introduce las repeticiones: ')
    tiempo_tension = input('Introduce el tiempo en tensión: ')
    tiempo_descanso = input('Introduce el tiempo de descanso: ')
    return repeticiones, tiempo_tension, tiempo_descanso

def mostrar_ejercicios(lista_ejercicios):
    print("\nEJERCICIOS DISPONIBLES: ")
    for i, ejercicio in enumerate(lista_ejercicios):
        print(f'{i} - {ejercicio}')

def eliminar_ejercicio(lista_ejercicios):
    mostrar_ejercicios(lista_ejercicios)
    lista_ejercicios.pop(int(input('Indica el número del ejercicio que deses borrar: ')))

def nuevo_cliente():
    nombre = input('Introduce tu nombre: ')
    fecha_nacimiento = input('Introduce la fecha de nacimiento: ')
    peso = input('Introduce tu peso: ')
    condicion_fisica = input('Introduce tu condición física: ')
    return nombre, fecha_nacimiento, peso, condicion_fisica

def nuevo_crossfitero():
    nombre, fecha_nacimiento, peso, condicion_fisica  = nuevo_cliente()
    intensidad = input('Introduce tu intensidad: ')
    modalidad = input('Introduce tu modalidad: ')
    return nombre, fecha_nacimiento, peso, condicion_fisica, intensidad, modalidad

def nuevo_ciclista():
    nombre, fecha_nacimiento, peso, condicion_fisica  = nuevo_cliente()
    tipo_de_bicicleta = input('Introduce el tipo de bici: ')
    kilometraje = float(input('Introduce el kiometraje: '))
    return nombre, fecha_nacimiento, peso, condicion_fisica, tipo_de_bicicleta, kilometraje

def buscar_entrenamiento(lista_ejercicios):
    mostrar_ejercicios(lista_ejercicios)
    entrenamiento = int(input('Selecciona un entrenamiento: '))
    for index, ejercicio in enumerate(lista_ejercicios):
        if entrenamiento == index:
            return ejercicio

def asignar_entrenamiento(cliente, lista_ejercicios):
    ejercicio = buscar_entrenamiento(lista_ejercicios)
    cliente.asignar_entrenamiento(ejercicio)

def eliminar_entrenamiento(cliente, lista_ejercicios):
    ejercicio = buscar_entrenamiento(lista_ejercicios)
    cliente.eliminar_entrenamiento(ejercicio)

def mostrar_clientes(lista_clientes):
    for index, cliente in enumerate(lista_clientes):
        print(f"{index} - {cliente}")

def seleccionar_cliente(lista_clientes):
    mostrar_clientes(lista_clientes)
    cli = int(input('Introduce el id del cliente que deseas seleccionar: '))
    for index, cliente in enumerate(lista_clientes):
        if index == cli:
            print(f'Has seleccionado al cliente: {cliente.nombre}')
            return cliente

def mostrar_entrenadores(lista_entrenadores):
    for index, entrenador in enumerate(lista_entrenadores):
        print(f"{index} - {entrenador}")

def seleccionar_entrenador(lista_entrenadores):
    mostrar_entrenadores(lista_entrenadores)
    entr = int(input('Introduce el id del entrenador que deseas seleccionar: '))
    for index, entrenador in enumerate(lista_entrenadores):
        if index == entr:
            print(f'Has seleccionado al cliente: {entrenador.nombre}')
            return entrenador
        
def eliminar_cliente(lista_clientes):
    cliente_a_borrar = seleccionar_cliente(lista_clientes)
    nombre_cliente_a_borrar = cliente_a_borrar.nombre
    lista_clientes.remove(cliente_a_borrar)
    return f'Se ha eliminado a {nombre_cliente_a_borrar}'

def modificar_entrenador():
    return int(input("""
1. Asignar cliente.
2. Eliminar cliente.
Selecciona una opción: """))