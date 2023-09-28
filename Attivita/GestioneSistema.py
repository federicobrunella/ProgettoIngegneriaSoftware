import pickle


class GestioneSistema:

    #Restituisce il file pickle del sistema
    def getCurrentSistema(self):
        with open('Dati/sistema.pickle', 'rb') as f:
            try:
                sistema = pickle.load(f)
            except Exception as exc:
                print('Got pickling error: {0}'.format(exc))
            return sistema

    #Salva il file pickle del sistema
    def salvaSistema(self, sistema):
        with open('Dati/sistema.pickle', 'wb') as f:
            pickle.dump(sistema, f, pickle.HIGHEST_PROTOCOL)

    #Salva all'interno del file pickle gli orari(durata slot, inizio giornata, fine giornata)
    def salvaOrari(self, durataSlotPrenotazione, orarioInizioGiornata, orarioFineGiornata):
        self.sistema = self.getCurrentSistema()

        self.sistema.durataSlotPrenotazione = durataSlotPrenotazione
        self.sistema.orarioInizioGiornata = orarioInizioGiornata
        self.sistema.orarioFineGiornata = orarioFineGiornata

        self.salvaSistema(self.sistema)

    #Salva il numero delle pedane all'interno del file pickle
    def salvaPedane(self, numPedane):
        self.sistema = self.getCurrentSistema()

        self.sistema.numPedane = numPedane

        self.salvaSistema(self.sistema)

    #Salva il prezzo di tesseramento all'interno del file pickle
    def salvaPrezzo(self, prezzo):
        self.sistema = self.getCurrentSistema()

        self.sistema.prezzoTess = prezzo

        self.salvaSistema(self.sistema)





