from Logic.CRUD import adaugaObiect, stergeObiect, modificaObiect
from Logic.functionalitate1 import mutareLocatie
from Domain.obiect2 import toString
from Logic.functionalitate2 import concatenare
from Logic.functionalitate3 import CelMaiMarePretLocatie
from Logic.functionalitate4 import SortAscByPrice

def uiAdaugaObiect(lista):
    try:
        id = input ("Dati id-ul: ")
        nume = input ("Dati numele: ")
        descriere = input ("Dati descrierea: ")
        pret = float(input ("Dati pretul: "))
        locatie = input ("Dati locatia: ")
        return adaugaObiect (id, nume, descriere, pret, locatie, lista)
    except ValueError as ve:
        print ("Eroare: {}".format(ve))
        return lista


def uiStergeObiect(lista):
    id = input("Dati id-ul obiectului pe care doriti sa il eliminati din lista: ")
    return stergeObiect (id, lista)

def uiModificaObiect (lista):
    try:
        id = input("Dati id-ul obiectului de modificat: ")
        nume = input("Dati noul nume: ")
        descriere = input("Dati noua descriere: ")
        pret = float(input("Dati noul pret: "))
        locatie = input("Dati noua locatie: ")
        return modificaObiect (id, nume, descriere, pret, locatie, lista)
    except ValueError as ve:
        print ("Eroare: {}".format(ve))
        return lista

def uiMutaLocatie (lista):
    try:
        id = input ("Dati id-ul obiectului a carui locatie doriti sa o modificati: ")
        locatie = input ("Dati noua locatie: ")
        return mutareLocatie (lista, locatie, id)
    except ValueError as ve:
        print ("Eroare: {}".format(ve))
        return lista

def uiConcatenare (lista):
    try:
        s = input ("Dati string-ul pe care doriti sa-l adaugati la descrieri: ")
        price = float(input("Dati pretul: "))
        return concatenare (s, price, lista)
    except ValueError as ve:
        print ("Eroare: {}".format(ve))
        return lista

def uiCelMaiMarePretLocatie (lista):
    locatie = input ("Dati locatia pentru care vreti sa aflati cel mai mare pret: ")
    return CelMaiMarePretLocatie (locatie, lista)

def uiSortAscByPrice(lista):
    ListaSortata = SortAscByPrice (lista)
    return ListaSortata

def printMenu():
    print ("1. Adaugare obiect")
    print ("2. Stergere obiect")
    print ("3. Modificare obiect")
    print ("4. Muta obiecte dintr-o locatie in alta")
    print ("5. Concatenarea unui sir dat la descrierile obiectelor care au pretul mai mare decat un pret dat")
    print ("6. Determina cel mai mare pret de la o anumita locatie")
    print ("7. Sorteaza lista crescator dupa pretul achizitiei")
    print ("a. Afisare obiecte")
    print ("x. Iesire")

def ShowAll (lista):
    for obiect in lista:
        print (toString(obiect))

def runMenu(lista):
    while True:
        printMenu()
        optiune = input ("Dati optiunea: ")
        if optiune == "1":
            lista = uiAdaugaObiect (lista)
        elif optiune == "2":
            lista = uiStergeObiect (lista)
        elif optiune == "3":
            lista = uiModificaObiect (lista)
        elif optiune == "4":
            lista = uiMutaLocatie (lista)
        elif optiune == "5":
            lista = uiConcatenare (lista)
        elif optiune == "6":
            max = uiCelMaiMarePretLocatie (lista)
            print (max)
        elif optiune == "7":
            lista = uiSortAscByPrice(lista)
        elif optiune == "a":
            ShowAll (lista)
        elif optiune == "x":
            break
        else:
            print ("Optiunea gresita. Reincercati!")