from Domain.obiect import creeazaObiect, getId

def adaugaObiect(id, nume, descriere, pret, locatie, lista):
    '''
    adauga un obiect intr-o lista
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :param lista: lista de obiecte
    :return: lista continand vechile elemente si noul obiect
    '''
    obiect = creeazaObiect(id, nume, descriere, pret, locatie)
    return lista + [obiect]

def getById (id, lista):
    '''
    gaseste un obiect cu id-ul dat intr-o lista
    :param id: string
    :param lista: lista de obiecte
    :return: obiectul cu id-ul dat din lista sau None, in caz contrar
    '''
    for obiect in lista:
        if getId(obiect) == id:
            return obiect
    else:
        return None

def stergeObiect (id, lista):
    '''
    sterge un obiect dintr-o lista
    :param id: id-ul obiectului care va fi sters din lista
    :param lista: lista de obiecte
    :return: lista continand toate elementele initiale fara obiectul cu id-ul dat
    '''
    return [obiect for obiect in lista if id!= getId(obiect)]

def modificaObiect (id, nume, descriere, pret, locatie, lista):
    '''
    modifica un obiect dupa id
    :param id: id-ul obiectului
    :param nume: numele obiectului
    :param descriere: descrierea obiectului
    :param pret: pretul obiectului
    :param locatie: locatia obiectului
    :param lista: lista de obiecte
    :return: lista modificata
    '''
    listaNoua = []
    for obiect in lista:
        if getId (obiect) == id:
            obiectNou = creeazaObiect(id, nume, descriere, pret, locatie)
            listaNoua.append(obiectNou)
        else:
            listaNoua.append(obiect)
    return listaNoua



