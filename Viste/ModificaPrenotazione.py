from datetime import datetime

from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy
from PyQt5 import QtCore, QtGui, QtWidgets

from Attivita.GestionePrenotazioni import GestionePrenotazioni
from Attivita.Prenotazione import Prenotazione

class VistaModificaPrenotazione(QWidget):
    def __init__(self, id, callback=None, parent=None):
        super(VistaModificaPrenotazione, self).__init__(parent)
        self.callback = callback
        self.id = id
        self.gridLayout = QGridLayout()

        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonSalva = QtWidgets.QPushButton()
        self.pushButtonSalva.setObjectName("pushButtonSalva")
        self.gridLayout.addWidget(self.pushButtonSalva, 11, 1, 1, 1)
        self.checkBoxCorso = QtWidgets.QCheckBox()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxCorso.sizePolicy().hasHeightForWidth())
        self.checkBoxCorso.setSizePolicy(sizePolicy)
        self.checkBoxCorso.setObjectName("checkBoxCorso")
        self.gridLayout.addWidget(self.checkBoxCorso, 8, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 10, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEditIDPrenotante = QtWidgets.QLineEdit()
        self.lineEditIDPrenotante.setObjectName("lineEditIDPrenotante")
        self.gridLayout.addWidget(self.lineEditIDPrenotante, 1, 1, 1, 1)
        self.timeEditInizio = QtWidgets.QTimeEdit()
        self.timeEditInizio.setObjectName("timeEditInizio")
        self.gridLayout.addWidget(self.timeEditInizio, 2, 1, 1, 1)
        self.dateEditData = QtWidgets.QDateEdit()
        self.dateEditData.setObjectName("dateEditData")
        self.gridLayout.addWidget(self.dateEditData, 5, 1, 1, 1)
        self.timeEditFine = QtWidgets.QTimeEdit()
        self.timeEditFine.setObjectName("timeEditFine")
        self.gridLayout.addWidget(self.timeEditFine, 3, 1, 1, 1)
        self.spinBoxPedana = QtWidgets.QSpinBox()
        self.spinBoxPedana.setObjectName("spinBoxPedana")
        self.gridLayout.addWidget(self.spinBoxPedana, 4, 1, 1, 1)

        self.pushButtonSalva.setText("Salva")
        self.checkBoxCorso.setText("Corso")
        self.label_2.setText("ID Prenotante")
        self.label.setText("Nuova Prenotazione:")
        self.label_4.setText("Ora Fine:")
        self.label_6.setText("Data")
        self.label_3.setText("Ora Inizio:")
        self.label_5.setText("Numero Pedana")

        controller = GestionePrenotazioni()
        prenotazione = controller.ricercaPerId(self.id)

        self.lineEditIDPrenotante.setText(str(prenotazione.idPrenotante))
        self.timeEditInizio.setTime(QTime(prenotazione.oraInizio.hour, prenotazione.oraInizio.minute, 0))
        self.timeEditFine.setTime(QTime(prenotazione.oraFine.hour, prenotazione.oraFine.minute, 0))
        if prenotazione.corso == 2:
            self.checkBoxCorso.setChecked(True)
        else:
            self.checkBoxCorso.setChecked(False)
        self.spinBoxPedana.setValue(int(prenotazione.numPedana))

        self.pushButtonSalva.clicked.connect(self.salva)


        self.setLayout(self.gridLayout)
        self.resize(350, 500)
        self.setWindowTitle("Gestionale Palestra Scherma")


    def salva(self):
        idPrenotante = int(self.lineEditIDPrenotante.text())

        oraInizio = datetime(year=self.dateEditData.date().year(),
                                  month=self.dateEditData.date().month(),
                                  day=self.dateEditData.date().day(),
                                  hour=self.timeEditInizio.time().hour(),
                                  minute=self.timeEditInizio.time().minute())

        oraFine = datetime(year=self.dateEditData.date().year(),
                                month=self.dateEditData.date().month(),
                                day=self.dateEditData.date().day(),
                                hour=self.timeEditFine.time().hour(),
                                minute=self.timeEditFine.time().minute())

        numPedana = self.spinBoxPedana.value()
        corso = self.checkBoxCorso.checkState()


        prenotazione = Prenotazione(self.id, idPrenotante,
                                     oraInizio,
                                     oraFine,
                                     numPedana, corso)

        controller = GestionePrenotazioni()
        controller.modificaPrenotazione(self.id, prenotazione)

        self.callback()
        self.close()

