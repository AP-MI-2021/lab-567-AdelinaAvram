from Domain.obiect2 import creeazaObiect, getId, getNume, getDescriere, getPret, getLocatie

def mutareLocatie (lista, locatie, id):
    '''
    muta obiectul cu id-ul id de la locatia curenta la locatia data ca parametru
    :param lista: lista de obiecte
    :param locatie: string ce reprezinta noua locatie a obiectului
    :param id: id-ul obiectului
    :return: o lista noua in care s-a modificat locatia obiectului cu id-ul id
    '''
    listaNoua = []
    for obiect in lista:
        if getId(obiect)==id:
            id = getId (obiect)
            nume = getNume (obiect)
            descriere = getDescriere (obiect)
            pret = getPret (obiect)
            obiectNou = creeazaObiect (id, nume, descriere, pret, locatie)
            listaNoua.append(obiectNou)
        else:
            listaNoua.append (obiect)
    return listaNoua