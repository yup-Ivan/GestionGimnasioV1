from menus import *
from ejercicios import Cardio, Fuerza
from clientes import *
from datetime import date
from entrenadores import Entrenador

if __name__ == '__main__':

    lista_ejercicios = []
    lista_clientes = []
    lista_entrenadores = []
    cardio_simple = Cardio('Cardio simple', 1, 100, 20)
    lista_ejercicios.append(cardio_simple)
    lista_ejercicios.append(Cardio('Ejercicio aleatorio 1', 4, 111, 12))
    lista_ejercicios.append(Fuerza('Ejercicio aleatorio 2', 4, 111, 20, 50, 20, 5))
    
    jose = Crossfitero('Jose', '2004/11/28', 60, 2, 10, 10)
    lista_clientes.append(jose)
    jose.asignar_entrenamiento(cardio_simple)
    lista_clientes.append(Cliente('Ivan', '2005/11/28', 70, 2))
    lista_clientes.append(Culturista('Manuel', '2000/11/28', 50, 2))
    lista_clientes.append(Ciclista('Juan', '2001/11/28', 50, 2, 'Bici normal', 100))

    rocio = Entrenador('Rocio')
    lista_entrenadores.append(rocio)
    rocio.asignar_cliente(jose)
    lista_entrenadores.append(Entrenador('Josefa'))

    while True:

        match opcion_principal():

            case 1: # EJERCICIOS.

                match menu_ejercicios():

                    case 1: # Crear ejercicio.

                        nombre, nivel_de_dificultad, calorias = nuevo_ejercicio()
                        
                        match tipo_ejercicio():

                            case 1: # Crear ejercicio cardio.
                                
                                lista_ejercicios.append(Cardio(nombre, nivel_de_dificultad, calorias, duracion_cardio()))

                            case 2: # Crear ejercicio fuerza.

                                repeticiones, tiempo_tension, tiempo_descanso = ejercicio_fuerza()
                                lista_ejercicios.append(Fuerza(nombre, nivel_de_dificultad, calorias, repeticiones, tiempo_tension, tiempo_descanso))

                    case 2: # Imprimir ejercicios.

                        mostrar_ejercicios(lista_ejercicios)

                    case 3: # Borrar ejercicio.

                        eliminar_ejercicio(lista_ejercicios)

                        pass

            case 2: # CLIENTES.

                match menu_clientes():

                    case 1:

                        match tipo_cliente():

                            case 1: # Cliente normal

                                # condiciones_fisicas()
                                nombre, fecha_nacimiento, peso, condicion_fisica  = nuevo_cliente()
                                cli = Cliente(nombre, fecha_nacimiento, peso, condicion_fisica)
                                lista_clientes.append(cli)
                                asignar_entrenamiento(cli, lista_ejercicios)

                            case 2: # Cliente crossfitero

                                nombre, fecha_nacimiento, peso, condicion_fisica, intensidad, modalidad = nuevo_crossfitero()
                                cli = Crossfitero(nombre, fecha_nacimiento, peso, condicion_fisica, intensidad, modalidad)
                                lista_clientes.append(cli)
                                asignar_entrenamiento(cli, lista_ejercicios)

                            case 3: # Cliente culturista

                                nombre, fecha_nacimiento, peso, condicion_fisica  = nuevo_cliente()
                                cli = Culturista(nombre, fecha_nacimiento, peso, condicion_fisica)
                                lista_clientes.append(cli)
                                asignar_entrenamiento(cli, lista_ejercicios)

                            case 4: # Cliente ciclista

                                nombre, fecha_nacimiento, peso, condicion_fisica, tipo_de_bicicleta, kilometraje  = nuevo_ciclista()
                                cli = Culturista(nombre, fecha_nacimiento, peso, condicion_fisica, tipo_de_bicicleta, kilometraje)
                                lista_clientes.append(cli)
                                asignar_entrenamiento(cli, lista_ejercicios)
                    
                    case 2: # Mostrar los clientes.

                        cliente_seleccionado = seleccionar_cliente(lista_clientes)

                    case 3:

                        try:
                            calorias_consumidas = cliente_seleccionado.calcular_entrenamiento()
                            print(f'{cliente_seleccionado.nombre} ha consumido {round(calorias_consumidas, 2)} calorias.')
                        except:
                            print('Primero has de seleccionar "Consultar clientes" y seleccionar uno.')

                    case 4:

                        if isinstance(cliente_seleccionado, Cliente):
                            opcion = input('1. Eliminar entrenamiento\n2.Consultar entrenamientos\nSelecciona una opción: ')
                            
                            if opcion == 1:
                                eliminar_entrenamiento(cliente_seleccionado, lista_ejercicios)
                            elif opcion == 2:
                                entenamientos = cliente_seleccionado.consultar_entrenamientos()
                                for entenamiento in entenamientos:
                                    print(entenamiento)

                        elif isinstance(cliente_seleccionado, Crossfitero):
                            opcion = input('1. Eliminar entrenamiento\n2.Consultar entrenamientos\n3. Asignar WOD\nSelecciona una opción: ')
                            
                            if opcion == 1:
                                eliminar_entrenamiento(cliente_seleccionado, lista_ejercicios)
                            elif opcion == 2:
                                entenamientos = cliente_seleccionado.consultar_entrenamientos()
                                for entenamiento in entenamientos:
                                    print(entenamiento)   
                            elif opcion == 3:
                                pass # Asignar wod.
                        
                        elif isinstance(cliente_seleccionado, Culturista):
                            opcion = input('1. Eliminar entrenamiento\n2.Consultar entrenamientos\n3. Asignar rutina\nSelecciona una opción: ')
                            
                            if opcion == 1:
                                eliminar_entrenamiento(cliente_seleccionado, lista_ejercicios)
                            elif opcion == 2:
                                entenamientos = cliente_seleccionado.consultar_entrenamientos()
                                for entenamiento in entenamientos:
                                    print(entenamiento)   
                            elif opcion == 3:
                                pass # Asignar rutina.

                        elif isinstance(cliente_seleccionado, Ciclista):
                            opcion = input('1. Eliminar entrenamiento\n2.Consultar entrenamientos\n3. Kilometros Anuales\nSelecciona una opción: ')
                            
                            if opcion == 1:
                                eliminar_entrenamiento(cliente_seleccionado, lista_ejercicios)
                            elif opcion == 2:
                                entenamientos = cliente_seleccionado.consultar_entrenamientos()
                                for entenamiento in entenamientos:
                                    print(entenamiento)   
                            elif opcion == 3:
                                print(cliente_seleccionado.kilometros_anuales())

                    case 5:

                        print(eliminar_cliente(lista_clientes))

                    case 6:
                        
                        try:
                            print(f'Nombre del cliente seleccionado: {cliente_seleccionado.nombre}')
                        except:
                            print('No hay ningún cliente seleccionado, para seleccionar uno primero has de seleccionar "Consultar clientes".')

            case 3: # ENTRENADORES.

                match menu_entrenador():

                    case 1:

                        nuevo_entrenador = Entrenador(input('Introduce el nombre del nuevo entrenador: '))
                        lista_entrenadores.append(nuevo_entrenador)
                        print('Vamos a asignar un cliente al nuevo entrenador: ')
                        cliente_seleccionado = seleccionar_cliente(lista_clientes)
                        nuevo_entrenador.asignar_cliente(cliente_seleccionado)

                    case 2:

                        for entrenador in lista_entrenadores:
                            print(entrenador)

                    case 3:

                        entrenador_seleccionado = seleccionar_entrenador(lista_entrenadores)
                        clientes = entrenador_seleccionado.consultar_clientes()
                        print(f'Clientes de {entrenador.nombre}:')
                        for cliente in clientes:
                            print(cliente)

                    case 4:

                        
                        match modificar_entrenador():

                            case 1: # Asignar cliente.

                                print('Selecciona el entrenador que quieres editar: \n')
                                entrenador_seleccionado = seleccionar_entrenador(lista_entrenadores)
                                cliente_seleccionado = seleccionar_cliente(lista_clientes)
                                if cliente_seleccionado not in entrenador_seleccionado.consultar_clientes():
                                    entrenador_seleccionado.asignar_cliente(cliente_seleccionado)
                                else:
                                    print('Ese cliente ya está asignado a este entrenador.')

                            case 2: # Retirar cliente.

                                print('Selecciona el entrenador que quieres editar: \n')
                                entrenador_seleccionado = seleccionar_entrenador(lista_entrenadores)
                                print(f'\nClientes asignados a {entrenador_seleccionado.nombre}: ')
                                if entrenador_seleccionado.consultar_clientes():
                                    for index, cliente in enumerate(entrenador_seleccionado.consultar_clientes()):
                                        print(f'{index} - {cliente}')
                                    cliente_a_eliminar = int(input('Introduce el id del cliente a eliminar: '))
                                    for index, cliente in enumerate(entrenador_seleccionado.consultar_clientes()):
                                        if index == cliente_a_eliminar:
                                            entrenador_seleccionado.eliminar_cliente(cliente)
                                else:
                                    print('No hay clientes asignados a ese entrenador.')

                    case 5:

                        entrenador_seleccionado = seleccionar_entrenador(lista_entrenadores)
                        lista_entrenadores.remove(entrenador_seleccionado)

                    case 6:
                        
                        try:
                            print(f'Nombre del entrenador seleccionado: {entrenador_seleccionado.nombre}')
                        except:
                            print('No hay ningún entrenador seleccionado, para seleccionar uno primero has de seleccionar "Consultar entrenadores".')


            case 4: # SALIR.

                break