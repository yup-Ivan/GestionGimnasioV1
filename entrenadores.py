class Entrenador(object):

    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_de_clientes = []
    
    def asignar_cliente(self, cliente):
        if cliente not in self.lista_de_clientes:
            self.lista_de_clientes.append(cliente)
        else:
            print('Ya se ha asignado previamente el cliente a este entrenador.')

    def eliminar_cliente(self, cliente):
        if cliente in self.lista_de_clientes:
            self.lista_de_clientes.remove(cliente)

    def consultar_clientes(self):
        return self.lista_de_clientes
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre}'