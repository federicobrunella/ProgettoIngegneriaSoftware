from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5 import QtGui, QtWidgets

from Attivita.GestioneTesserati import GestioneTesserati

class VistaDettaglioTesserato(QWidget):
    def __init__(self, codice, callback=None, parent=None):
        super(VistaDettaglioTesserato, self).__init__(parent)
        self.callback = callback
        self.codice = codice
        self.gridLayout = QGridLayout()

        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 2)
        self.labelNome = QtWidgets.QLabel()
        self.labelNome.setObjectName("labelNome")
        self.gridLayout.addWidget(self.labelNome, 3, 1, 1, 1)
        self.labelTelefono = QtWidgets.QLabel()
        self.labelTelefono.setObjectName("labelTelefono")
        self.gridLayout.addWidget(self.labelTelefono, 8, 1, 1, 1)
        self.labelScadenza = QtWidgets.QLabel()
        self.labelScadenza.setObjectName("labelScadenza")
        self.gridLayout.addWidget(self.labelScadenza, 11, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel()
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 10, 0, 1, 1)
        self.labelDataNascita = QtWidgets.QLabel()
        self.labelDataNascita.setObjectName("labelDataNascita")
        self.gridLayout.addWidget(self.labelDataNascita, 5, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 13, 0, 1, 2)
        self.labelCognome = QtWidgets.QLabel()
        self.labelCognome.setObjectName("labelCognome")
        self.gridLayout.addWidget(self.labelCognome, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel()
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel()
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)
        self.labelCertificato = QtWidgets.QLabel()
        self.labelCertificato.setObjectName("labelCertificato")
        self.gridLayout.addWidget(self.labelCertificato, 10, 1, 1, 1)
        self.labelcodFiscale = QtWidgets.QLabel()
        self.labelcodFiscale.setObjectName("labelcodFiscale")
        self.gridLayout.addWidget(self.labelcodFiscale, 6, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 12, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel()
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.labelIstruttore = QtWidgets.QLabel()
        self.labelIstruttore.setObjectName("labelIstruttore")
        self.gridLayout.addWidget(self.labelIstruttore, 9, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel()
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel()
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 9, 0, 1, 1)
        self.labelEmail = QtWidgets.QLabel()
        self.labelEmail.setObjectName("labelEmail")
        self.gridLayout.addWidget(self.labelEmail, 7, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel()
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 11, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel()
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_11 = QtWidgets.QLabel()
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)
        self.labelCodice = QtWidgets.QLabel()
        self.labelCodice.setObjectName("labelCodice")
        self.gridLayout.addWidget(self.labelCodice, 2, 1, 1, 1)

        controller = GestioneTesserati()
        tesserato = controller.getTesseratoPerCodice(self.codice)

        self.labelNome.setText(tesserato.nome)
        self.labelTelefono.setText(tesserato.telefono)
        self.labelScadenza.setText(str(tesserato.scadenza))
        self.label_9.setText("Certificato Medico:")
        self.labelDataNascita.setText(str(tesserato.dataNascita))
        self.pushButton.setText("Ok")
        self.labelCognome.setText(tesserato.cognome)
        self.label_3.setText("Data di Nascita:")
        self.label_10.setText("Telefono:")
        if tesserato.certificato == 0:
            self.labelCertificato.setText("NO")
        else:
            self.labelCertificato.setText("SI")
        self.labelcodFiscale.setText(tesserato.codiceFiscale)
        self.label_4.setText("Cognome")
        if tesserato.istruttore == 0:
            self.labelIstruttore.setText("NO")
        else:
            self.labelIstruttore.setText("SI")
        self.label_8.setText("Email")
        self.label_5.setText("Istruttore:")
        self.labelEmail.setText(tesserato.email)
        self.label_7.setText("Data Scadenza")
        self.label_2.setText("Nome:")
        self.label_6.setText("Codice Fiscale:")
        self.label.setText("Dettaglio Tesserato:")
        self.label_11.setText("Codice:")
        self.labelCodice.setText(str(self.codice))

        self.pushButton.clicked.connect(self.indietro)

        self.setLayout(self.gridLayout)
        self.resize(350, 500)
        self.setWindowTitle("Gestionale Palestra Scherma")

    def indietro(self):
        self.close()
