import pickle

class GestioneUtenti:

    def getAllUtenti(self):
        with open('Dati/utenti.pickle', 'rb') as f:
            try:
                utenti = pickle.load(f)
            except Exception as exc:
                print('Got pickling error: {0}'.format(exc))
            return utenti
