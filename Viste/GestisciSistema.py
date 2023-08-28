from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy
from PyQt5 import QtCore, QtGui, QtWidgets

from Viste.ImpostazioneOrari import VistaOrari
from Viste.ImpostazionePrezzi import VistaPrezzi
from Viste.ImpostazioniPedane import VistaPedane

class VistaSistema(QWidget):

    def __init__(self, parent=None):
        super(VistaSistema, self).__init__(parent)
        self.gridLayout = QGridLayout()

        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 4)
        self.pushButtonBackup = QtWidgets.QPushButton()
        self.pushButtonBackup.setObjectName("pushButtonBackup")
        self.gridLayout.addWidget(self.pushButtonBackup, 4, 0, 1, 1)
        self.pushButtonPedane = QtWidgets.QPushButton()
        self.pushButtonPedane.setObjectName("pushButtonPedane")
        self.gridLayout.addWidget(self.pushButtonPedane, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 6, 0, 1, 3)
        self.listView = QtWidgets.QListView()
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 7, 0, 1, 4)
        self.pushButtonNuovoOperatore = QtWidgets.QPushButton()
        self.pushButtonNuovoOperatore.setObjectName("pushButtonNuovoOperatore")
        self.gridLayout.addWidget(self.pushButtonNuovoOperatore, 8, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 9, 0, 1, 4)
        self.pushButtonOrari = QtWidgets.QPushButton()
        self.pushButtonOrari.setObjectName("pushButtonOrari")
        self.gridLayout.addWidget(self.pushButtonOrari, 4, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 4)
        self.pushButtonPrezzi = QtWidgets.QPushButton()
        self.pushButtonPrezzi.setObjectName("pushButtonPrezzi")
        self.gridLayout.addWidget(self.pushButtonPrezzi, 4, 3, 1, 1)
        self.pushButtonIndietro = QtWidgets.QPushButton()
        self.pushButtonIndietro.setObjectName("pushButtonIndietro")
        self.gridLayout.addWidget(self.pushButtonIndietro, 10, 0, 1, 1)

        self.label_2.setText("Operazioni Amministratore:")
        self.pushButtonBackup.setText("Backup")
        self.pushButtonPedane.setText("Gestisci Pedane")
        self.label.setText("Lista Operatori:")
        self.pushButtonNuovoOperatore.setText("Nuovo Operatore")
        self.pushButtonOrari.setText("Gestisci Orari")
        self.pushButtonPrezzi.setText("Gestisci Prezzi")
        self.pushButtonIndietro.setText("Indietro")

        self.pushButtonIndietro.clicked.connect(self.indietro)
        self.pushButtonOrari.clicked.connect(self.gestisciOrari)
        self.pushButtonPrezzi.clicked.connect(self.gestisciPrezzi)
        self.pushButtonPedane.clicked.connect(self.gestisciPedane)

        self.setLayout(self.gridLayout)
        self.resize(1000, 800)
        self.setWindowTitle("Gestionale Palestra Scherma - Sistema")

    def indietro(self):
        self.close()

    def gestisciOrari(self):
        self.vista_orari = VistaOrari()
        self.vista_orari.show()

    def gestisciPrezzi(self):
        self.vista_prezzi = VistaPrezzi()
        self.vista_prezzi.show()

    def gestisciPedane(self):
        self.vista_pedande = VistaPedane()
        self.vista_pedande.show()
