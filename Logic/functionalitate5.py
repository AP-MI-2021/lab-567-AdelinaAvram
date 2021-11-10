from Domain.obiect2 import getLocatie, getPret

def sumPriceLocation(locatie, lista):
    '''
    determina suma preturilor obiect depozitate intr-o locatie data
    :param locatie: string
    :param lista: lista de obiecte
    :return: suma preturilor depozitate in locatia data locatie
    '''
    if len(locatie)!=4:
        raise ValueError ("Locatia introdusa nu are 4 caractere! ")
    sum = None
    for obiect in lista:
        if getLocatie(obiect) == locatie:
            if sum == None:
                sum = getPret(obiect)
            else:
                sum = sum + getPret(obiect)
    return sum
