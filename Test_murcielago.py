from Murcielago import Murcielago
# test_animal.py
def test_probar_MRO():
    murcielago = Murcielago()
    assert murcielago.comer() == "esta comiendo"
    assert murcielago.volar() == "esta volando"
    assert murcielago.amamantar() == "esta amamantando"
 