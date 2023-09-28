from datetime import datetime

from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5 import QtGui, QtWidgets

from Attivita.GestioneUtenti import GestioneUtenti
from Attivita.Utente import Utente

class VistaNuovoUtente(QWidget):
    def __init__(self, codice, callback=None, parent=None):
        super(VistaNuovoUtente, self).__init__(parent)
        self.callback = callback
        self.codice = codice
        self.gridLayout = QGridLayout()

        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditTelefono = QtWidgets.QLineEdit()
        self.lineEditTelefono.setObjectName("lineEditTelefono")
        self.gridLayout.addWidget(self.lineEditTelefono, 9, 1, 1, 1)
        self.label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 12, 0, 1, 2)
        self.lineEditNome = QtWidgets.QLineEdit()
        self.lineEditNome.setObjectName("lineEditNome")
        self.gridLayout.addWidget(self.lineEditNome, 1, 1, 1, 1)
        self.pushButtonSalva = QtWidgets.QPushButton()
        self.pushButtonSalva.setObjectName("pushButtonSalva")
        self.gridLayout.addWidget(self.pushButtonSalva, 13, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel()
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.lineEditCognome = QtWidgets.QLineEdit()
        self.lineEditCognome.setObjectName("lineEditCognome")
        self.gridLayout.addWidget(self.lineEditCognome, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel()
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 9, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel()
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 10, 0, 1, 1)
        self.lineEditUsername = QtWidgets.QLineEdit()
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.gridLayout.addWidget(self.lineEditUsername, 10, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.dateEditDataNascita = QtWidgets.QDateEdit()
        self.dateEditDataNascita.setObjectName("dateEditDataNascita")
        self.gridLayout.addWidget(self.dateEditDataNascita, 4, 1, 1, 1)
        self.lineEditCodFiscale = QtWidgets.QLineEdit()
        self.lineEditCodFiscale.setObjectName("lineEditCodFiscale")
        self.gridLayout.addWidget(self.lineEditCodFiscale, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditEmail = QtWidgets.QLineEdit()
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.gridLayout.addWidget(self.lineEditEmail, 7, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel()
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 11, 0, 1, 1)
        self.lineEditPassword = QtWidgets.QLineEdit()
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.gridLayout.addWidget(self.lineEditPassword, 11, 1, 1, 1)

        self.label.setText("Nuovo Operatore:")
        self.pushButtonSalva.setText("Salva")
        self.label_7.setText("Email:")
        self.label_5.setText("Telefono:")
        self.label_8.setText("Username:")
        self.label_3.setText("Cognome:")
        self.label_2.setText("Nome:")
        self.label_6.setText("Data Nascita")
        self.label_4.setText("Codice Fiscale:")
        self.label_9.setText("Password:")

        self.pushButtonSalva.clicked.connect(self.salva)

        self.setLayout(self.gridLayout)
        self.resize(350, 500)
        self.setWindowTitle("Gestionale Palestra Scherma")


    def salva(self):
        self.nome = self.lineEditNome.text()
        self.cognome = self.lineEditCognome.text()
        self.codFiscale = self.lineEditCodFiscale.text()
        self.email = self.lineEditEmail.text()
        self.telefono = self.lineEditTelefono.text()

        self.dataNascita = datetime(year=self.dateEditDataNascita.date().year(),
                                    month=self.dateEditDataNascita.date().month(),
                                    day=self.dateEditDataNascita.date().day())


        self.username = self.lineEditUsername.text()
        self.password = self.lineEditPassword.text()

        utente = Utente(self.username, self.password,
                        self.telefono, self.nome, self.email,
                        self.dataNascita, self.cognome, self.codFiscale, self.codice)

        controller = GestioneUtenti()
        controller.aggiungiUtente(utente)

        self.callback()
        self.close()

