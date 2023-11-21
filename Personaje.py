class Personaje:
    def __init__(self, nombre, habilidad):
        self.nombre = nombre
        self.habilidad = habilidad
        
    def mostrarNombre(self):
        return (f'Mi nombre es {self.nombre}')
    
    def mostrarHabilidad(self):
        return (f'Mi poder de habilidad es {self.habilidad}')
    
    def __add__(self, otro):
        nuevo_nombre = f"{self.nombre}{otro.nombre}"
        nueva_habilidad = self.habilidad * otro.habilidad
        return Personaje(nuevo_nombre, nueva_habilidad)
        