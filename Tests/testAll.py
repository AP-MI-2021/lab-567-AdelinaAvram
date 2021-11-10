from Tests.testDomeniu  import testObiect
from Tests.testCRUD import testAdaugaObiect, testStergeObiect, testModificaObiect
from Tests.testFunctionalitate1 import testMutareLocatie
from Tests.testFunctionalitate2 import testConcatenare
from Tests.testFunctionalitate3 import testCelMaiMarePretLocatie
from Tests.testFunctionalitate4 import testSortAscByPrice
from Tests.testFunctionalitate5 import testSumPriceLocation

def runAllTests():
    testObiect()
    testAdaugaObiect()
    testStergeObiect()
    testModificaObiect()
    testMutareLocatie()
    testConcatenare()
    testCelMaiMarePretLocatie()
    testSortAscByPrice()
    testSumPriceLocation()