from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy
from PyQt5 import QtCore, QtGui, QtWidgets

from Viste.GestisciPrenotazioni import VistaPrenotazioni
from Viste.GestisciSistema import VistaSistema
from Viste.GestisciTesserati import VistaTesserati

class VistaHome(QWidget):

    def __init__(self, utente ,parent=None):
        super(VistaHome, self).__init__(parent)
        self.utenteLoggato = utente
        self.gridLayout = QGridLayout()

        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.sistemaPushButton = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sistemaPushButton.sizePolicy().hasHeightForWidth())
        self.sistemaPushButton.setSizePolicy(sizePolicy)
        self.sistemaPushButton.setObjectName("sistemaPushButton")
        self.gridLayout.addWidget(self.sistemaPushButton, 1, 2, 1, 1)
        self.prenotazioniPushButton = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prenotazioniPushButton.sizePolicy().hasHeightForWidth())
        self.prenotazioniPushButton.setSizePolicy(sizePolicy)
        self.prenotazioniPushButton.setObjectName("prenotazioniPushButton")
        self.gridLayout.addWidget(self.prenotazioniPushButton, 1, 1, 1, 1)
        self.tesseratiPushButton = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tesseratiPushButton.sizePolicy().hasHeightForWidth())
        self.tesseratiPushButton.setSizePolicy(sizePolicy)
        self.tesseratiPushButton.setObjectName("tesseratiPushButton")
        self.gridLayout.addWidget(self.tesseratiPushButton, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel()
        self.label.setEnabled(True)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.sistemaPushButton.setText("GESTIONE SISTEMA")
        self.prenotazioniPushButton.setText("GESTIONE PRENOTAZIONI")
        self.tesseratiPushButton.setText("GESTIONE TESSERATI")
        self.label.setText("Current User:")
        self.label_2.setText(self.utenteLoggato.username)

        if(self.utenteLoggato.username != "admin"):
            self.sistemaPushButton.setDisabled(True)

        self.prenotazioniPushButton.clicked.connect(self.gestisciPrenotazioni)
        self.sistemaPushButton.clicked.connect(self.gestisciSistema)
        self.tesseratiPushButton.clicked.connect(self.gestisciTesserati)



        self.setLayout(self.gridLayout)
        self.resize(400, 300)
        self.setWindowTitle("Gestionale Palestra Scherma - Home")

    def gestisciPrenotazioni(self):
        self.vista_gestisci_prenotazioni = VistaPrenotazioni()
        self.vista_gestisci_prenotazioni.show()

    def gestisciSistema(self):
        self.vista_gestisci_sistema = VistaSistema()
        self.vista_gestisci_sistema.show()

    def gestisciTesserati(self):
        self.vista_gestisci_tesserati = VistaTesserati()
        self.vista_gestisci_tesserati.show()