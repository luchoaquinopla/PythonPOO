from Personaje import Personaje

def test_fusion():
    goku = Personaje("Goku", 10)
    vegeta = Personaje("Vegeta", 10)
    
    
    assert goku.mostrarNombre() == "Mi nombre es Goku"
    assert vegeta.mostrarNombre() == "Mi nombre es Vegeta"
    
    assert goku.mostrarHabilidad() == "Mi poder de habilidad es 10"
    assert vegeta.mostrarHabilidad() == "Mi poder de habilidad es 10"
    
    fusion = goku + vegeta
    
    assert fusion.mostrarNombre() == "Mi nombre es GokuVegeta"
    assert fusion.mostrarHabilidad() == "Mi poder de habilidad es 100"
    


