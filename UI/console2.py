from Logic.CRUD import adaugaObiect, stergeObiect, modificaObiect
from Logic.functionalitate1 import mutareLocatie
from Logic.functionalitate2 import concatenare
from Logic.functionalitate3 import CelMaiMarePretLocatie
from Logic.functionalitate4 import SortAscByPrice
from Domain.obiect2 import toString

def HelpMenu():
    print ("1. Pentru comanda add, introduceti id, nume, descriere, pret si locatie")
    print ("2. Pentru commanda delete, introduceti indicele obiectului pe care doriti sa il stergeti")
    print ("3. Pentru comanda update, introduceti indicele obiectului pe care doriti sa il modificati si noul nume, noua descriere, noul pret si noua locatie")
    print ("4. Pentru comanda move location, introduceti noua locatie pe care vreti sa o atribuiti obiectului si indicele acestuia in lista")
    print ("5. Pentru comanda concatenate, introduceti string-ul pe care doriti sa il concatenati si pretul de la care incepe concatenarea")
    print ("6.. Pentru comanda highest price per location, introduceti locatia pentru care doriti sa aflati cel mai mare pret")
    print ("7. Pentru commanda sort asc by price, nu mai introduceti niciun parametru")
    print ("a. Pentru comanda show All, nu mai introduceti niciun parametru")
    print ("x. Pentru comanda quit, nu mai introduceti niciun parametru")

def runMenu2():
    HelpMenu()
    while True:
        comenzi = input ("Dati comenzile, separate cu punct si virgula, cu parametrii separati prin virgula: ")
        ComandaCuParametri = comenzi.split(";")
        lista = []
        for command in ComandaCuParametri:
            tokens = command.split (",")
            if tokens[0] == "add":
                try:
                    lista = adaugaObiect (tokens[1], tokens[2], tokens[3], float(tokens[4]), tokens[5], lista)
                except ValueError as ve:
                    print("Eroare: {}".format(ve))
            elif tokens [0] == "delete":
                lista = stergeObiect (tokens[1], lista)
            elif tokens [0] == "update":
                try:
                    lista = modificaObiect (tokens[1], tokens[2], tokens[3], float(tokens[4]), tokens[5], lista)
                except ValueError as ve:
                    print("Eroare: {}".format(ve))
            elif tokens[0] == "move location":
                try:
                    lista = mutareLocatie (lista, tokens[1], tokens[2])
                except ValueError as ve:
                    print("Eroare: {}".format(ve))
            elif tokens [0] == "concatenate":
                try:
                    lista = concatenare (tokens[1], float(tokens[2]), lista)
                except ValueError as ve:
                    print("Eroare: {}".format(ve))
            elif tokens [0] == "highest price per location":
                print (CelMaiMarePretLocatie(tokens[1], lista))
            elif tokens [0] == "sort asc by price":
                lista = SortAscByPrice (lista)
            elif tokens [0] == "show All":
                for obiect in lista:
                    print (toString(obiect))
                print()
            elif tokens [0] == "quit":
                break
            else:
                print ("Optiune gresita. Reincercati!")

