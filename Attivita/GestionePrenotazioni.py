import pickle


class GestionePrenotazioni:

    #Prende tutte le prenotazioni nel file pickle
    def getAllPrenotazioni(self):
        with open('Dati/prenotazioni.pickle', 'rb') as f:
            try:
                prenotazioni = pickle.load(f)
            except Exception as exc:
                print('Got pickling error: {0}'.format(exc))
            return prenotazioni

    #Salva all'interno del file pickle tutte le prenotazioni
    def salvaAllPrenotazioni(self, prenotazioni):
        with open('Dati/prenotazioni.pickle', 'wb') as f:
            pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)

    #Aggiunge una singola prenotazione all'interno del file pickle
    def aggiungiPrenotazione(self, prenotazione):
        self.prenotazioni = []
        self.prenotazioni = self.getAllPrenotazioni()

        self.prenotazioni.append(prenotazione)
        self.salvaAllPrenotazioni(self.prenotazioni)

    #Prende l'id dell'ultima prenotazione sul file pickle
    def getLastCodice(self):
        self.prenotazioni = []
        self.prenotazioni = self.getAllPrenotazioni()

        codice = self.prenotazioni[len(self.prenotazioni)-1].id

        return codice

    #Ricerca una prenotazione all'interno del file pickle tramite l'id di un prenotante
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

    #Ricerca una prenotazione all'interno del file pickle tramite la data di prenotazione
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


    #Elimina una prenotazione all'interno del file pickle
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

    #Ricerca una prenotazione con un id
    def ricercaPerId(self, id):
        self.prenotazioni = []
        self.prenotazioni = self.getAllPrenotazioni()

        for prenotazione in self.prenotazioni:
            if prenotazione.id == id:
                return prenotazione

    #Modifica una prenotazione
    def modificaPrenotazione(self, id, prenotazione):
        self.prenotazioni = []
        self.prenotazioni = self.getAllPrenotazioni()

        for pren in self.prenotazioni:
            if pren.id == id:
                print('ok')
                pren.idPrenotante = prenotazione.idPrenotante
                pren.numPedana = prenotazione.numPedana
                pren.oraInizio = prenotazione.oraInizio
                pren.oraFine = prenotazione.oraFine
                pren.corso = prenotazione.corso

        self.salvaAllPrenotazioni(self.prenotazioni)


