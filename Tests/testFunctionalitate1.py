from Logic.functionalitate1 import mutareLocatie
from Logic.CRUD import adaugaObiect, getById
from Domain.obiect import getId, getNume, getDescriere, getPret, getLocatie

def testMutareLocatie():
    lista = []
    lista = adaugaObiect("1", "portofolii", "roz", 5.6, "ABCD", lista)

    lista = mutareLocatie (lista, "GIGA", "1")

    obiectUpdatat = getById ("1", lista)
    assert getId(obiectUpdatat) == "1"
    assert getNume(obiectUpdatat) == "portofolii"
    assert getDescriere (obiectUpdatat) == "roz"
    assert getPret (obiectUpdatat) == 5.6
    assert getLocatie(obiectUpdatat) == "GIGA"

