from Attivita.Persona import Persona

class Tesserato(Persona):

    #Costruttore
    def __init__(self, istruttore, certificato, scadenza, telefono, nome, email, dataNascita, cognome , codiceFiscale, codice):
        super().__init__(telefono, nome, email, dataNascita, cognome , codiceFiscale, codice)
        self.certificato = certificato
        self.istruttore = istruttore
        self.scadenza = scadenza