import pickle

class GestionePrenotazioni:
    def getAllPrenotazioni(self):
        with open('Dati/prenotazioni.pickle', 'rb') as f:
            try:
                prenotazioni = pickle.load(f)
            except Exception as exc:
                print('Got pickling error: {0}'.format(exc))
            return prenotazioni

    def salvaAllPrenotazioni(self, prenotazioni):
        with open('Dati/prenotazioni.pickle', 'wb') as f:
            pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)

    def aggiungiPrenotazione(self, prenotazione):
        self.prenotazioni = []
        self.prenotazioni = self.getAllPrenotazioni()

        self.prenotazioni.append(prenotazione)
        self.salvaAllPrenotazioni(self.prenotazioni)

    def getLastCodice(self):
        self.prenotazioni = []
        self.prenotazioni = self.getAllPrenotazioni()

        codice = self.prenotazioni[len(self.prenotazioni)-1].id

        return codice

