import pickle

class GestioneTesserati:

    def getAllTesserati(self):
        with open('Dati/tesserati.pickle', 'rb') as f:
            try:
                tesserati = pickle.load(f)
            except Exception as exc:
                print('Got pickling error: {0}'.format(exc))
            return tesserati

    def getLastCodice(self):
        self.tesserati = []
        self.tesserati = self.getAllTesserati()

        codice = self.tesserati[len(self.tesserati)-1].codice

        return codice

    def salvaAllTesserati(self, tesserati):
        with open('Dati/tesserati.pickle', 'wb') as f:
            pickle.dump(tesserati, f, pickle.HIGHEST_PROTOCOL)

    def aggiungiTeserato(self, tesserato):
        self.tesserati = []
        self.tesserati = self.getAllTesserati()

        self.tesserati.append(tesserato)
        self.salvaAllTesserati(self.tesserati)

    def eliminaTesserato(self, codice, callback=None):
        self.callback = callback
        self.tesserati = []
        self.tesserati = self.getAllTesserati()

        for tesserato in self.tesserati:
            if(tesserato.codice == codice):
                self.tesserati.remove(tesserato)

        self.salvaAllTesserati(self.tesserati)
        self.callback()

    def modificaTesserato(self, codice, tesseratoModificato, callback=None):
        self.callback = callback
        self.tesserati = []
        self.tesserati = self.getAllTesserati()

        for tesserato in self.tesserati:
            if (tesserato.codice == codice):
                tesserato.nome = tesseratoModificato.nome
                tesserato.cognome = tesseratoModificato.cognome
                tesserato.istruttore = tesseratoModificato.istruttore
                tesserato.certificato = tesseratoModificato.certificato
                tesserato.dataNascita = tesseratoModificato.dataNascita
                tesserato.email = tesseratoModificato.email
                tesserato.telefono = tesseratoModificato.telefono

        self.salvaAllTesserati(self.tesserati)

    def cercaTesseratoPerNome(self, nome, cognome):
        pass

    def getTesseratoPerCodice(self, codice):
        self.tesserati = []
        self.tesserati = self.getAllTesserati()

        for tesserato in self.tesserati:
            if(tesserato.codice == codice):
                return tesserato

