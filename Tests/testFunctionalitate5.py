from Logic.CRUD import adaugaObiect
from Logic.functionalitate5 import sumPriceLocation

def testSumPriceLocation():
    lista = []
    lista = adaugaObiect("1", "sticle", "transparente", 20, "GIGA", lista)
    lista = adaugaObiect("2", "portofolii", "roz", 5.6, "ABCD", lista)
    lista = adaugaObiect("3", "jucarii", "plastelina", 15, "GIGA", lista)

    assert sumPriceLocation("ABCD", lista) == 5.6
    assert sumPriceLocation ("GIGA", lista) == 35
    assert sumPriceLocation ("raft", lista) is None