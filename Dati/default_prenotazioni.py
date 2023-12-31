import pickle
from datetime import datetime

from Attivita.Prenotazione import Prenotazione

#File per popolare con alcuni elementi di default il file pickle delle prenotazioni

prenotazione1 = Prenotazione(1, 1,
                             datetime(year=2023, month=12, day=12, hour=14, minute=0),
                             datetime(year=2023, month=12, day=12, hour=15, minute=0),
                             1,0)

prenotazione2 = Prenotazione(2, 1,
                             datetime(year=2023, month=12, day=12, hour=15, minute=0),
                             datetime(year=2023, month=12, day=12, hour=16, minute=0),
                             1,0)

prenotazione3 = Prenotazione(3, 1,
                             datetime(year=2023, month=12, day=12, hour=16, minute=0),
                             datetime(year=2023, month=12, day=12, hour=17, minute=0),
                             1,2)



prenotazioni = [prenotazione1, prenotazione2, prenotazione3]

with open('prenotazioni.pickle', 'wb') as f:
    pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)

with open('prenotazioni.pickle', 'rb') as f:
    try:
        tess = pickle.load(f)
        print(tess)
    except Exception as exc:
        print('Got pickling error: {0}'.format(exc))


