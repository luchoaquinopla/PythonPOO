from Estudiante import Estudiante  # Asegúrate de ajustar la importación al nombre real de tu clase



def test_estudiante_inicializacion():
    estudiante = Estudiante("Juan", 18, "12th")
    
    assert estudiante.nombre == "Juan"
    assert estudiante.edad == 18
    assert estudiante.grado == "12th"
    


def test_estudiante_estudiar():
    estudiante = Estudiante("Lucho", 21, "3ero")
    assert estudiante.estudiar() == "el estudiante Lucho esta estudiando"
    

def test_probar_herencia():
    estudiante = Estudiante("Lucho", 21, "3ero")
    assert estudiante.nombre == "Lucho"
    assert estudiante.edad == 21
    assert estudiante.grado == "3ero"
    
def test_probar_herencia2():
    estudiante = Estudiante("Lucho", 21, "3ero")
    assert estudiante.imprimirEdadYNombre() == "La edad de Lucho es 21"
    assert estudiante.ImprimirGrado() == "el grado de Lucho es 3ero"

