from Logic.CRUD import adaugaObiect, stergeObiect, modificaObiect, getById
from Domain.obiect import getId, getNume, getDescriere, getPret, getLocatie


def testAdaugaObiect ():
    lista = []
    lista = adaugaObiect ("1", "portofolii", "roz", 5.6, "ABCD", lista)

    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getNume(getById("1", lista)) == "portofolii"
    assert getDescriere(getById("1", lista)) == "roz"
    assert getPret(getById("1", lista)) == 5.6
    assert getLocatie(getById("1", lista)) == "ABCD"

def testStergeObiect ():
    lista = []
    lista = adaugaObiect("1", "portofolii", "roz", 5.6, "ABCD", lista)
    lista = adaugaObiect ("2", "caiete", "subtiri", 10, "1ERT", lista)

    lista = stergeObiect("1", lista)

    assert len(lista) == 1
    assert getById ("1", lista) is None
    assert getById ("2", lista) is not None

    lista = stergeObiect ("3", lista)

    assert len(lista) == 1
    assert getById ("2", lista) is not None

def testModificaObiect():
    lista = []
    lista = adaugaObiect("1", "portofolii", "roz", 5.6, "ABCD", lista)
    lista = adaugaObiect("2", "caiete", "subtiri", 10, "1ERT", lista)

    lista = modificaObiect ("1", "mouses", "black", 30, "AERT", lista)

    obiectUpdatat = getById ("1", lista)
    assert getId (obiectUpdatat) == "1"
    assert getNume (obiectUpdatat) == "mouses"
    assert getDescriere (obiectUpdatat) == "black"
    assert getPret (obiectUpdatat) == 30
    assert getLocatie (obiectUpdatat) == "AERT"

    obiectNeupdatat = getById ("2", lista)
    assert getId(obiectNeupdatat) == "2"
    assert getNume(obiectNeupdatat) == "caiete"
    assert getDescriere(obiectNeupdatat) == "subtiri"
    assert getPret(obiectNeupdatat) == 10
    assert getLocatie(obiectNeupdatat) == "1ERT"



