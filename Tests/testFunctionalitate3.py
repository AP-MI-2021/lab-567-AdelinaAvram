from Logic.CRUD import adaugaObiect
from Logic.functionalitate3 import CelMaiMarePretLocatie


def testCelMaiMarePretLocatie ():
    lista = []
    lista = adaugaObiect("1", "portofolii", "roz", 5.6, "ABCD", lista)
    lista = adaugaObiect("2", "sticle", "transparente", 20, "GIGA", lista)
    lista = adaugaObiect("3", "jucarii", "plastelina", 15, "GIGA", lista)

    assert CelMaiMarePretLocatie ("ABCD", lista) == 5.6
    assert CelMaiMarePretLocatie ("GIGA", lista) == 20
    assert CelMaiMarePretLocatie ("TETH", lista) is None
