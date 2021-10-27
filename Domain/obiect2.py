def creeazaObiect (id, nume, descriere, pret, locatie):
    '''
    creeaza un obiect
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :return: o lista ce retine un obiect
    '''
    lista = []
    lista.append(id)
    lista.append (nume)
    lista.append (descriere)
    lista.append (pret)
    lista.append (locatie)
    return lista

def getId (obiect):
    '''
    ia id-ul obiectului
    :param obiect: lista de tip obiect
    :return: id-ul obiectului
    '''
    return obiect[0]

def getNume (obiect):
    return obiect [1]

def getDescriere (obiect):
    return obiect [2]

def getPret (obiect):
    return obiect [3]

def getLocatie (obiect):
    return obiect [4]

def toString (obiect):
    return "id: {}, nume: {}, descriere: {}, pret: {}, locatie: {}". format(
        getId(obiect),
        getNume (obiect),
        getDescriere (obiect),
        getPret (obiect),
        getLocatie(obiect)
        )