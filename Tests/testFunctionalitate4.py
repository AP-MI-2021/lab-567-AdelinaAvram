from Logic.CRUD import adaugaObiect
from Logic.functionalitate4 import SortAscByPrice
from Domain.obiect2 import getId

def testSortAscByPrice():
    lista = []
    lista = adaugaObiect("1", "sticle", "transparente", 20, "GIGA", lista)
    lista = adaugaObiect("2", "portofolii", "roz", 5.6, "ABCD", lista)
    lista = adaugaObiect("3", "jucarii", "plastelina", 15, "GIGA", lista)

    ListaSortata = SortAscByPrice (lista)

    assert getId(ListaSortata[0]) == "2"
    assert getId(ListaSortata[1]) == "3"
    assert getId(ListaSortata[2]) == "1"
