from datetime import datetime

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy
from PyQt5 import QtCore, QtGui, QtWidgets

from Attivita.Tesserato import Tesserato
from Attivita.GestioneTesserati import GestioneTesserati

class VistaModificaTesserato(QWidget):
    def __init__(self, codice, callback=None, parent=None):
        super(VistaModificaTesserato, self).__init__(parent)
        self.callback = callback
        self.codice = codice
        self.gridLayout = QGridLayout()

        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditTelefono = QtWidgets.QLineEdit()
        self.lineEditTelefono.setObjectName("lineEditTelefono")
        self.gridLayout.addWidget(self.lineEditTelefono, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel()
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEditCognome = QtWidgets.QLineEdit()
        self.lineEditCognome.setObjectName("lineEditCognome")
        self.gridLayout.addWidget(self.lineEditCognome, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel()
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.dateEditDataNascita = QtWidgets.QDateEdit()
        self.dateEditDataNascita.setObjectName("dateEditDataNascita")
        self.gridLayout.addWidget(self.dateEditDataNascita, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel()
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEditCodFiscale = QtWidgets.QLineEdit()
        self.lineEditCodFiscale.setObjectName("lineEditCodFiscale")
        self.gridLayout.addWidget(self.lineEditCodFiscale, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel()
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEditEmail = QtWidgets.QLineEdit()
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.gridLayout.addWidget(self.lineEditEmail, 6, 1, 1, 1)
        self.checkBoxIstruttore = QtWidgets.QCheckBox()
        self.checkBoxIstruttore.setObjectName("checkBoxIstruttore")
        self.gridLayout.addWidget(self.checkBoxIstruttore, 9, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 12, 0, 1, 2)
        self.pushButtonSalva = QtWidgets.QPushButton()
        self.pushButtonSalva.setObjectName("pushButtonSalva")
        self.gridLayout.addWidget(self.pushButtonSalva, 13, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel()
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.lineEditNome = QtWidgets.QLineEdit()
        self.lineEditNome.setObjectName("lineEditNome")
        self.gridLayout.addWidget(self.lineEditNome, 1, 1, 1, 1)
        self.checkBoxCertificato = QtWidgets.QCheckBox()
        self.checkBoxCertificato.setObjectName("checkBoxCertificato")
        self.gridLayout.addWidget(self.checkBoxCertificato, 11, 1, 1, 1)

        self.label_4.setText("Data di nascita")
        self.label_6.setText("Telefono:")
        self.label.setText("Nuovo tesserato:")
        self.label_5.setText("Codice Fiscale:")
        self.label_3.setText("Cognome:")
        self.checkBoxIstruttore.setText("Istruttore")
        self.pushButtonSalva.setText("Salva")
        self.label_2.setText("Nome:")
        self.label_7.setText("e-mail:")
        self.checkBoxCertificato.setText("Certificato Medico")

        controller = GestioneTesserati()
        tesserato = controller.getTesseratoPerCodice(self.codice)

        self.lineEditNome.setText(tesserato.nome)
        self.lineEditCognome.setText(tesserato.cognome)
        self.lineEditEmail.setText(tesserato.email)
        self.lineEditTelefono.setText(tesserato.telefono)
        self.lineEditCodFiscale.setText(tesserato.codiceFiscale)

        if tesserato.certificato==2:
            self.checkBoxCertificato.setChecked(True)
        else:
            self.checkBoxCertificato.setChecked(False)

        if tesserato.istruttore==2:
            self.checkBoxIstruttore.setChecked(True)
        else:
            self.checkBoxIstruttore.setChecked(False)

        self.pushButtonSalva.clicked.connect(self.salva)

        self.setLayout(self.gridLayout)
        self.resize(350, 500)
        self.setWindowTitle("Gestionale Palestra Scherma - Home")


    def salva(self):
        self.istruttore = self.checkBoxIstruttore.checkState()
        self.certificato = self.checkBoxCertificato.checkState()
        print(self.certificato)
        print(self.istruttore)
        self.nome = self.lineEditNome.text()
        self.cognome = self.lineEditCognome.text()
        self.codFiscale = self.lineEditCodFiscale.text()
        self.email = self.lineEditEmail.text()
        self.telefono = self.lineEditTelefono.text()

        self.dataNascita = datetime(year=self.dateEditDataNascita.date().year(),
                                    month=self.dateEditDataNascita.date().month(),
                                    day=self.dateEditDataNascita.date().day())

        # aggiungere campo a interfaccia
        self.dataScadenza = datetime(year=2000,
                                     month=1,
                                     day=1)

        tesserato = Tesserato(self.istruttore, self.certificato,
                              self.dataScadenza,
                              self.telefono, self.nome, self.email,
                              self.dataNascita, self.cognome,
                              self.codFiscale, self.codice)

        controller = GestioneTesserati()
        controller.modificaTesserato(self.codice, tesserato)

        self.callback()
        self.close()
