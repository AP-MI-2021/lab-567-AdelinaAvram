from Logic.CRUD import adaugaObiect, stergeObiect, modificaObiect
from Logic.functionalitate1 import mutareLocatie
from Domain.obiect2 import toString
from Logic.functionalitate2 import concatenare
from Logic.functionalitate3 import CelMaiMarePretLocatie
from Logic.functionalitate4 import SortAscByPrice
from Logic.functionalitate5 import sumPriceLocation


def uiAdaugaObiect(lista, undoOperations):
    try:
        id = input ("Dati id-ul: ")
        nume = input ("Dati numele: ")
        descriere = input ("Dati descrierea: ")
        pret = float(input ("Dati pretul: "))
        locatie = input ("Dati locatia: ")
        rezultat = adaugaObiect (id, nume, descriere, pret, locatie, lista)
        undoOperations.append (lista)
        return rezultat
    except ValueError as ve:
        print ("Eroare: {}".format(ve))
        return lista


def uiStergeObiect(lista, undoOperations):
    id = input("Dati id-ul obiectului pe care doriti sa il eliminati din lista: ")
    rezultat = stergeObiect(id, lista)
    undoOperations.append (lista)
    return rezultat

def uiModificaObiect (lista, undoOperations):
    try:
        id = input("Dati id-ul obiectului de modificat: ")
        nume = input("Dati noul nume: ")
        descriere = input("Dati noua descriere: ")
        pret = float(input("Dati noul pret: "))
        locatie = input("Dati noua locatie: ")
        rezultat = modificaObiect (id, nume, descriere, pret, locatie, lista)
        undoOperations.append(lista)
        return rezultat
    except ValueError as ve:
        print ("Eroare: {}".format(ve))
        return lista

def uiMutaLocatie (lista, undoOperations):
    try:
        id = input ("Dati id-ul obiectului a carui locatie doriti sa o modificati: ")
        locatie = input ("Dati noua locatie: ")
        rezultat = mutareLocatie (lista, locatie, id)
        undoOperations.append(lista)
        return rezultat
    except ValueError as ve:
        print ("Eroare: {}".format(ve))
        return lista

def uiConcatenare (lista, undoOperations):
    try:
        s = input ("Dati string-ul pe care doriti sa-l adaugati la descrieri: ")
        price = float(input("Dati pretul: "))
        rezultat = concatenare (s, price, lista)
        undoOperations.append(lista)
        return rezultat
    except ValueError as ve:
        print ("Eroare: {}".format(ve))
        return lista

def uiCelMaiMarePretLocatie (lista):
    try:
        locatie = input ("Dati locatia pentru care vreti sa aflati cel mai mare pret: ")
        return CelMaiMarePretLocatie (locatie, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))

def uiSortAscByPrice(lista, undoOperations):
    ListaSortata = SortAscByPrice (lista)
    undoOperations.append(lista)
    return ListaSortata

def uiSumPriceLocation(lista):
    try:
        locatie = input ("Dati locatia pentru care vreti sa aflati suma preturilor obiectelor depozitate acolo: ")
        return sumPriceLocation(locatie, lista)
    except ValueError as ve:
        print ("Eroare: {}".format(ve))


def printMenu():
    print ("1. Adaugare obiect")
    print ("2. Stergere obiect")
    print ("3. Modificare obiect")
    print ("4. Muta obiecte dintr-o locatie in alta")
    print ("5. Concatenarea unui sir dat la descrierile obiectelor care au pretul mai mare decat un pret dat")
    print ("6. Determina cel mai mare pret de la o anumita locatie")
    print ("7. Sorteaza lista crescator dupa pretul achizitiei")
    print ("8. Afiseaza suma preturilor pentru fiecare locatie")
    print ("u. Undo list")
    print ("a. Afisare obiecte")
    print ("x. Iesire")

def ShowAll (lista):
    for obiect in lista:
        print (toString(obiect))

def runMenu(lista):
    undoOperations = []
    while True:
        printMenu()
        optiune = input ("Dati optiunea: ")
        if optiune == "1":
            lista = uiAdaugaObiect (lista, undoOperations)
        elif optiune == "2":
            lista = uiStergeObiect (lista, undoOperations)
        elif optiune == "3":
            lista = uiModificaObiect (lista, undoOperations)
        elif optiune == "4":
            lista = uiMutaLocatie (lista, undoOperations)
        elif optiune == "5":
            lista = uiConcatenare (lista, undoOperations)
        elif optiune == "6":
            max = uiCelMaiMarePretLocatie (lista)
            print (max)
        elif optiune == "7":
            lista = uiSortAscByPrice(lista, undoOperations)
        elif optiune == "8":
            sum = uiSumPriceLocation (lista)
            if sum == None:
                print ("Nu exista niciun obiect in locatia data.")
            else:
                print (sum)
        elif optiune == "u":
            if len(undoOperations) > 0:
                operations = undoOperations.pop()
                lista = operations
        elif optiune == "a":
            ShowAll (lista)
        elif optiune == "x":
            break
        else:
            print ("Optiunea gresita. Reincercati!")