from Logic.CRUD import adaugaObiect, getById
from Logic.functionalitate2 import concatenare
from Domain.obiect2 import getDescriere

def testConcatenare():
    lista = []
    lista = adaugaObiect("1", "portofolii", "roz", 5.6, "ABCD", lista)
    lista = adaugaObiect ("2", "sticle", "transparente", 20, "5GT4", lista)
    lista = adaugaObiect ("3", "jucarii", "plastelina", 15, "GIGA", lista)

    lista = concatenare ("flori", 10, lista)
    obiectNeupdatat = getById ("1", lista)
    obiectUpdatat1 = getById ("2", lista)
    obiectUpdatat2 = getById ("3", lista)

    assert len(lista) == 3
    assert getDescriere(obiectNeupdatat) == "roz"
    assert getDescriere (obiectUpdatat1) == "transparenteflori"
    assert getDescriere (obiectUpdatat2) == "plastelinaflori"

