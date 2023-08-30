import pickle
from datetime import date, datetime


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

    def ricercaPerPrenotante(self, campoRicerca):
        self.result = []

        self.prenotazioni = []
        self.prenotazioni = self.getAllPrenotazioni()

        try:
            for prenotazione in self.prenotazioni:
                if int(campoRicerca) == prenotazione.idPrenotante:
                    self.result.append(prenotazione)

        except Exception as exc:
            print('error ricercaPrenotante'.format(exc))

        return self.result

    def ricercaPerData(self, campoRicerca):
        self.result = []


        self.prenotazioni = []
        self.prenotazioni = self.getAllPrenotazioni()



        try:
            for prenotazione in self.prenotazioni:
                try:
                    if campoRicerca == prenotazione.oraInizio.date():
                        self.result.append(prenotazione)
                except Exception as ex:
                    print('error ricercaData'.format(ex))
                    print(prenotazione.oraInizio.date())
                    print(campoRicerca)

        except Exception as exc:
            print('error ricercaData'.format(exc))

        return self.result


    def eliminaPrenotazione(self, id, callback=None):
        self.callback = callback
        self.prenotazioni = []
        self.prenotazioni = self.getAllPrenotazioni()
        try:
            for prenotazione in self.prenotazioni:
                if(prenotazione.id == id):
                    self.prenotazioni.remove(prenotazione)
        except Exception as ex:
            print('Error: eliminaPrenotazione'.format(ex))
            print(id)
        self.salvaAllPrenotazioni(self.prenotazioni)
        self.callback()


