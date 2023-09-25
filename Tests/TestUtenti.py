import unittest

from Attivita.Utente import Utente
from Attivita.GestioneUtenti import GestioneUtenti

class UtentiModuleTest(unittest.TestCase):

    def testInserimentoUtente(self):
        controller = GestioneUtenti()

        codice = controller.getLastCodice() + 1

        utente = Utente("testUser", "testUser",
                        "2334435454", "testUser",
                        "tesstUser@email.it", "",
                        "testUser", "BRNDEO2324", codice)

        controller.aggiungiUtente(utente)

        verifica = controller.ricercaPerCodice(codice)

        assert(verifica.username == utente.username)

if __name__ == '__main__':
    unittest.main()
