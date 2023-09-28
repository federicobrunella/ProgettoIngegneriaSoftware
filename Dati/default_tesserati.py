import pickle
from datetime import datetime

from Attivita.Tesserato import Tesserato

#File per popolare con alcuni elementi di default il file pickle dei tesserati

tesserato1 = Tesserato(0,2,
                       datetime(year=2024, month=1, day=1),
                       "3663745504", "Paolo", "p.r@email.it",
                       datetime(year=2006, month=1, day=1), "Rossi",
                       "PSRNFCB23E288H", 1)

tesserato2 = Tesserato(0,2,
                       datetime(year=2024, month=1, day=1),
                       "3663745504", "Marco", "m.v@email.it",
                       datetime(year=2002, month=1, day=1), "Verdi",
                       "PSRNFCB23E288H", 2)

tesserato3 = Tesserato(0,2,
                       datetime(year=2024, month=1, day=1),
                       "3663745504", "Claudio", "c.b@email.it",
                       datetime(year=2004, month=1, day=1), "Bianchi",
                       "PSRNFCB23E288H", 3)

tesserati = [tesserato1, tesserato2, tesserato3]

with open('tesserati.pickle', 'wb') as f:
    pickle.dump(tesserati, f, pickle.HIGHEST_PROTOCOL)

with open('tesserati.pickle', 'rb') as f:
    try:
        tess = pickle.load(f)
        print(tess)
    except Exception as exc:
        print('Got pickling error: {0}'.format(exc))
