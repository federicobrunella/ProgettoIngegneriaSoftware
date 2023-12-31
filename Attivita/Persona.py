import datetime

class Persona:

    #Costruttore
    def __init__(self, telefono = "", nome = "", email = "", dataNascita = "", cognome = "", codiceFiscale = "", codice = -1):
        self.codice = codice
        self.codiceFiscale = codiceFiscale
        self.cognome = cognome
        self.dataNascita = dataNascita
        self.email = email
        self.nome = nome
        self.telefono = telefono


    #Restituisce tutti gli attributi della persona
    def getInfoPersona(self):
        return {
            "codice": self.codice,
            "codiceFiscale": self.codiceFiscale,
            "cognome": self.cognome,
            "dataNascita": self.dataNascita,
            "email": self.email,
            "nome": self.nome,
            "telefono": self.telefono
        }

    #Elimina tutti gli attributi della persona
    def resetPersona(self):
        self.codice = -1
        self.codiceFiscale = ""
        self.cognome = ""
        self.dataNascita = ""
        self.email = ""
        self.nome = ""
        self.telefono = ""