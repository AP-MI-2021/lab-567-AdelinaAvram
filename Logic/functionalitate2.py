from Domain.obiect2 import creeazaObiect, getId, getNume, getDescriere, getPret, getLocatie

def concatenare (s, price, lista):
    '''
    concateneaza sirul s la descrierile elementelor din lista l al caror pret > price
    :param s: string
    :param pret: float
    :param lista: lista de obiecte
    :return: lista initiala in care s-a concatenat sirul s la descrierile obiectelor din lista al caror pret > price
    '''
    listaNoua = []
    for obiect in lista:
        if getPret(obiect) > price:
            id = getId (obiect)
            nume = getNume (obiect)
            descriere = getDescriere(obiect) + s
            pret = getPret (obiect)
            locatie = getLocatie (obiect)
            obiectNou = creeazaObiect (id, nume, descriere, pret, locatie)
            listaNoua.append(obiectNou)
        else:
            listaNoua.append(obiect)
    return listaNoua
