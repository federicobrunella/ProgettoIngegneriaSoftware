import os
import pickle

from Attivita.Utente import Utente

utente1 = Utente("utente1", "password", "", "", "", "", "", "", 1)
utente2 = Utente("utente2", "password", "", "", "", "", "", "", 2)

utenti = [utente1, utente2]

with open('utenti.pickle', 'wb') as f:
    pickle.dump(utenti, f, pickle.HIGHEST_PROTOCOL)

with open('utenti.pickle', 'rb') as f:
    try:
        utenti = pickle.load(f)
        print(utenti)
    except Exception as exc:
        print('Got pickling error: {0}'.format(exc))

with open('utenti.pickle', 'rb') as f:
    current = pickle.load(f)
    print(current)