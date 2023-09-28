
class Prenotazione:

    #Costruttore
    def __init__(self, id, idPrenotante, oraInizio, oraFine, numPedana, corso):
        self.id = id
        self.idPrenotante = idPrenotante
        self.oraInizio = oraInizio
        self.oraFine = oraFine
        self.numPedana = numPedana
        self.corso = corso
