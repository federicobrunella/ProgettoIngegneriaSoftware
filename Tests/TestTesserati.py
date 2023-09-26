import unittest
from datetime import datetime

from Attivita.Tesserato import Tesserato
from Attivita.GestioneTesserati import GestioneTesserati

class TesseratiModuleTest(unittest.TestCase):

    def testInserimentoTesserato(self):
        controller = GestioneTesserati()

        codice = controller.getLastCodice() + 1

        tesserato = Tesserato(0, 2,
                               datetime(year=2024, month=1, day=1),
                               "3663745504", "testTesserato", "email@email.it",
                               datetime(year=2006, month=1, day=1), "testTesserato",
                               "PSRNFCB23E288H", codice)

        controller.aggiungiTeserato(tesserato)

        verifica = controller.getTesseratoPerCodice(codice)

        assert(tesserato.nome == verifica.nome)


if __name__ == '__main__':
    unittest.main()
