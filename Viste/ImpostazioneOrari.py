from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy
from PyQt5 import QtCore, QtGui, QtWidgets

class VistaOrari(QWidget):

    def __init__(self, parent=None):
        super(VistaOrari, self).__init__(parent)
        self.gridLayout = QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel()
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.pushButtonIndietro = QtWidgets.QPushButton()
        self.pushButtonIndietro.setObjectName("pushButtonIndietro")
        self.gridLayout.addWidget(self.pushButtonIndietro, 6, 0, 1, 1)
        self.timeEditFine = QtWidgets.QTimeEdit()
        self.timeEditFine.setObjectName("timeEditFine")
        self.gridLayout.addWidget(self.timeEditFine, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.pushButtonSalva = QtWidgets.QPushButton()
        self.pushButtonSalva.setObjectName("pushButtonSalva")
        self.gridLayout.addWidget(self.pushButtonSalva, 6, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.timeEditInizio = QtWidgets.QTimeEdit()
        self.timeEditInizio.setObjectName("timeEditInizio")
        self.gridLayout.addWidget(self.timeEditInizio, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel()
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 5, 2, 1, 1)
        self.lineEditDurataSlot = QtWidgets.QLineEdit()
        self.lineEditDurataSlot.setObjectName("lineEditDurataSlot")
        self.gridLayout.addWidget(self.lineEditDurataSlot, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 3)

        self.label_3.setText("Inizio Giornata")
        self.pushButtonIndietro.setText("Indietro")
        self.pushButtonSalva.setText("Salva")
        self.label_2.setText("Durata Slot Prenotazione (minuti)")
        self.label.setText("Orari Prenotazioni:")
        self.label_4.setText("Fine Giornata")

        self.pushButtonIndietro.clicked.connect(self.indietro)
        self.pushButtonSalva.clicked.connect(self.salva)

        self.setLayout(self.gridLayout)
        self.resize(400, 300)
        self.setWindowTitle("Gestionale Palestra Scherma - Prezzi")

    def indietro(self):
        self.close()

    def salva(self):
        self.close()