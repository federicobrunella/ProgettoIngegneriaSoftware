from datetime import datetime

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy
from PyQt5 import QtCore, QtGui, QtWidgets

from Attivita.GestionePrenotazioni import GestionePrenotazioni
from Attivita.Prenotazione import Prenotazione

class VistaDettaglioPrenotazione(QWidget):
    def __init__(self, id, callback=None, parent=None):
        super(VistaDettaglioPrenotazione, self).__init__(parent)
        self.callback = callback
        self.id = id
        self.gridLayout = QGridLayout()

        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelNumPedana = QtWidgets.QLabel()
        self.labelNumPedana.setObjectName("labelNumPedana")
        self.gridLayout.addWidget(self.labelNumPedana, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel()
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel()
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 10, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 9, 0, 1, 2)
        self.labelIDPrenotazione = QtWidgets.QLabel()
        self.labelIDPrenotazione.setObjectName("labelIDPrenotazione")
        self.gridLayout.addWidget(self.labelIDPrenotazione, 3, 1, 1, 1)
        self.labelData = QtWidgets.QLabel()
        self.labelData.setObjectName("labelData")
        self.gridLayout.addWidget(self.labelData, 7, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel()
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.labelOraFine = QtWidgets.QLabel()
        self.labelOraFine.setObjectName("labelOraFine")
        self.gridLayout.addWidget(self.labelOraFine, 5, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel()
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel()
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.labelIDPrenotante = QtWidgets.QLabel()
        self.labelIDPrenotante.setObjectName("labelIDPrenotante")
        self.gridLayout.addWidget(self.labelIDPrenotante, 2, 1, 1, 1)
        self.labelOraInizio = QtWidgets.QLabel()
        self.labelOraInizio.setObjectName("labelOraInizio")
        self.gridLayout.addWidget(self.labelOraInizio, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel()
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.labelCorso = QtWidgets.QLabel()
        self.labelCorso.setObjectName("labelCorso")
        self.gridLayout.addWidget(self.labelCorso, 8, 1, 1, 1)

        controller = GestionePrenotazioni()
        prenotazione = controller.ricercaPerId(self.id)

        self.labelNumPedana.setText(str(prenotazione.numPedana))
        self.label_3.setText("Ora Fine:")
        self.label_11.setText("ID Prenotante:")
        self.pushButton.setText("Ok")
        self.labelIDPrenotazione.setText(str(self.id))
        self.labelData.setText(str(prenotazione.oraInizio.date()))
        self.label_4.setText("Ora Inizio:")
        self.label_2.setText("ID Prenotazione:")
        self.labelOraFine.setText(str(prenotazione.oraFine))
        self.label_10.setText("Corso")
        self.label.setText("Dettaglio Prenotazione:")
        self.label_8.setText("Data")
        self.labelIDPrenotante.setText(str(prenotazione.idPrenotante))
        self.labelOraInizio.setText(str(prenotazione.oraInizio))
        self.label_6.setText("Numero Pedana")
        if prenotazione.corso == 0:
            self.labelCorso.setText("NO")
        else:
            self.labelCorso.setText("SI")

        self.pushButton.clicked.connect(self.indietro)

        self.setLayout(self.gridLayout)
        self.resize(350, 500)
        self.setWindowTitle("Gestionale Palestra Scherma")

    def indietro(self):
        self.close()
