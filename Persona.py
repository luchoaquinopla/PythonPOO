class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def imprimirEdadYNombre(self):
        return (f'La edad de {self.nombre} es {self.edad}')