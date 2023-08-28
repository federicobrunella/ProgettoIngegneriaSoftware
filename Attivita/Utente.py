from Attivita.Persona import Persona

class Utente(Persona):

    def __init__(self, username, password, telefono, nome, email, dataNascita, cognome , codiceFiscale, codice):
        super().__init__(telefono, nome, email, dataNascita, cognome , codiceFiscale, codice)
        self.username = username
        self.password = password