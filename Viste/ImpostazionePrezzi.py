from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy
from PyQt5 import QtCore, QtGui, QtWidgets

class VistaPrezzi(QWidget):

    def __init__(self, parent=None):
        super(VistaPrezzi, self).__init__(parent)
        self.gridLayout = QGridLayout()

        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButtonIndietro = QtWidgets.QPushButton()
        self.pushButtonIndietro.setObjectName("pushButtonIndietro")
        self.gridLayout.addWidget(self.pushButtonIndietro, 2, 0, 1, 1)
        self.pushButtonSalva = QtWidgets.QPushButton()
        self.pushButtonSalva.setObjectName("pushButtonSalva")
        self.gridLayout.addWidget(self.pushButtonSalva, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.lineEditPrezzo = QtWidgets.QLineEdit()
        self.lineEditPrezzo.setObjectName("lineEditPrezzo")
        self.gridLayout.addWidget(self.lineEditPrezzo, 1, 1, 1, 1)

        self.label_2.setText("Prezzo Tesseramento (EURO):")
        self.pushButtonIndietro.setText("Indietro")
        self.pushButtonSalva.setText("Salva")
        self.label.setText("Prezzi")

        self.pushButtonIndietro.clicked.connect(self.indietro)
        self.pushButtonSalva.clicked.connect(self.salva)

        self.setLayout(self.gridLayout)
        self.resize(400, 100)
        self.setWindowTitle("Gestionale Palestra Scherma - Prezzi")

    def indietro(self):
        self.close()

    def salva(self):
        self.close()