import os
import pickle

class GestioneUtenti:

    #Restituisce tutti gli utenti del file pickle
    def getAllUtenti(self):
        with open("Dati/utenti.pickle", 'rb') as f:
            try:
                utenti = pickle.load(f)
            except Exception as exc:
                print('Got pickling error: {0}'.format(exc))
            return utenti

    #Restituisce il codice dell'ultimo utente
    def getLastCodice(self):
        self.utenti = []
        self.utenti = self.getAllUtenti()

        codice = self.utenti[len(self.utenti)-1].codice

        return codice

    #Salva tutti gli utenti all'interno del file pickle
    def salvaAllUtenti(self, utenti):
        with open('Dati/utenti.pickle', 'wb') as f:
            pickle.dump(utenti, f, pickle.HIGHEST_PROTOCOL)

    #Aggiunge un utente all'interno del file pickle
    def aggiungiUtente(self, utente):
        self.utenti = []
        self.utenti = self.getAllUtenti()

        self.utenti.append(utente)
        self.salvaAllUtenti(self.utenti)

    #Elimina un utente
    def eliminaUtente(self, codice, callback=None):
        self.callback = callback
        self.utenti = []
        self.utenti = self.getAllUtenti()

        for utente in self.utenti:
            if(utente.codice == codice):
                self.utenti.remove(utente)

        self.salvaAllUtenti(self.utenti)
        self.callback()

    #Ricerca un utente all'interno del file pickle tramite il codice
    def ricercaPerCodice(self, codice):
        self.utenti = []
        self.utenti = self.getAllUtenti()

        for utente in self.utenti:
            if utente.codice == codice:
                return utente

    #Modifica un utente all'interno del file pickle
    def modificaUtente(self, codice, utenteMod):
        self.utenti = []
        self.utenti = self.getAllUtenti()

        for utente in self.utenti:
            if utente.codice == codice:
                utente.nome = utenteMod.nome
                utente.cognome = utenteMod.cognome
                utente.codiceFiscale = utenteMod.codiceFiscale
                utente.dataNascita = utenteMod.dataNascita
                utente.username = utenteMod.username
                utente.password = utenteMod.password
                utente.telefono = utenteMod.telefono
                utente.email = utenteMod.email

        self.salvaAllUtenti(self.utenti)

