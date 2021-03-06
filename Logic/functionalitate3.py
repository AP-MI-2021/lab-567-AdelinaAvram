from Domain.obiect2 import getPret, getLocatie

def CelMaiMarePretLocatie(locatie, lista):
    '''
    determina cel mai mare pret de achizitie al unui obiect aflat la o locatie data
    :param locatie: string
    :param lista: lista de obiecte
    :return: cel mai mare pret de achizitie al unui obiect aflat la o locatie data
    '''
    if len(locatie)!=4:
        raise ValueError ("Locatia introdusa nu are 4 caractere! ")
    max = None
    for obiect in lista:
        if getLocatie(obiect) == locatie:
            pret = getPret (obiect)
            if max == None or pret > max:
                max = pret

    return max