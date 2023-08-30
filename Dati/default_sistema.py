import pickle
from datetime import datetime

from Attivita.Sistema import Sistema

sistema = Sistema(60, datetime(year=2000, month=1, day=1, hour=8, minute=0),
                  datetime(year=2000, month=1, day=1, hour=19, minute=0), 20, 109.92)

with open('sistema.pickle', 'wb') as f:
    pickle.dump(sistema, f, pickle.HIGHEST_PROTOCOL)

with open('sistema.pickle', 'rb') as f:
    try:
        sis = pickle.load(f)
        print(sis)
    except Exception as exc:
        print('Got pickling error: {0}'.format(exc))
