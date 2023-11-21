from Persona import Persona
class Estudiante(Persona):
    def __init__(self,nombre, edad, grado):
        super(). __init__(nombre, edad)
        self.grado = grado 
        
    
    def estudiar(self):
        return (f'el estudiante {self.nombre} esta estudiando')
    
    def ImprimirGrado(self):
        return (f'el grado de {self.nombre} es {self.grado}')
        