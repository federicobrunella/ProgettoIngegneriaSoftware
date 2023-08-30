import pickle

class GestioneUtenti:
    def getAllUtenti(self):
        with open('Dati/utenti.pickle', 'rb') as f:
            try:
                utenti = pickle.load(f)
            except Exception as exc:
                print('Got pickling error: {0}'.format(exc))
            return utenti

    def getLastCodice(self):
        self.utenti = []
        self.utenti = self.getAllUtenti()

        codice = self.utenti[len(self.utenti)-1].codice

        return codice

    def salvaAllUtenti(self, utenti):
        with open('Dati/utenti.pickle', 'wb') as f:
            pickle.dump(utenti, f, pickle.HIGHEST_PROTOCOL)

    def aggiungiTeserato(self, utente):
        self.utenti = []
        self.utenti = self.getAllUtenti()

        self.utenti.append(utente)
        self.salvaAllUtenti(self.utenti)

    def eliminaTesserato(self, codice, callback=None):
        self.callback = callback
        self.utenti = []
        self.utenti = self.getAllUtenti()

        for utente in self.utenti:
            if(utente.codice == codice):
                self.utenti.remove(utente)

        self.salvaAllUtenti(self.utenti)
        self.callback()

    def ricercaPerCodice(self, codice):
        self.utenti = []
        self.utenti = self.getAllUtenti()

        for utente in self.utenti:
            if utente.codice == codice:
                return utente
