from Domain.obiect2 import getPret

def SortAscByPrice (lista):
    '''
    sorteaza crescator lista dupa valoarea pretului de achizitie al obiectelor
    :param lista: lista de obiecte
    :return: lista sortata crescator dupa pretul de achizitie
    '''

    ListaSortata = sorted (lista, key=lambda obiect:getPret(obiect))
    return ListaSortata