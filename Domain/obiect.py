def creeazaObiect (id, nume, descriere, pret, locatie):
    '''
    creeaza un obiect
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :return: un dictionar ce retine un obiect
    '''
    return {
        'id': id,
        'nume': nume,
        'descriere': descriere,
        'pret': pret,
        'locatie': locatie
    }

def getId (obiect):
    '''
    ia id-ul obiectului
    :param obiect: dictionar de tip obiect
    :return: id-ul obiectului
    '''
    return obiect['id']

def getNume (obiect):
    return obiect['nume']

def getDescriere (obiect):
    return obiect ['descriere']

def getPret (obiect):
    return obiect['pret']

def getLocatie (obiect):
    return obiect ['locatie']

def toString (obiect):
    return "id: {}, nume: {}, descriere: {}, pret: {}, locatie: {}". format(
        getId(obiect),
        getNume (obiect),
        getDescriere (obiect),
        getPret (obiect),
        getLocatie(obiect)
        )