from Domain.obiect2 import creeazaObiect, getId, getNume, getDescriere, getPret, getLocatie


def testObiect():
     obiect = creeazaObiect ("1", "portofolii", "roz", 5.6, "1A52" )
     assert getId (obiect) == "1"
     assert getNume (obiect) == "portofolii"
     assert getDescriere (obiect) == "roz"
     assert getPret (obiect) == 5.6
     assert getLocatie (obiect) == "1A52"
