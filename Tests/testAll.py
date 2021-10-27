from Tests.testDomeniu  import testObiect
from Tests.testCRUD import testAdaugaObiect, testStergeObiect, testModificaObiect
from Tests.testFunctionalitate1 import testMutareLocatie

def runAllTests():
    testObiect()
    testAdaugaObiect()
    testStergeObiect()
    testModificaObiect()
    testMutareLocatie()