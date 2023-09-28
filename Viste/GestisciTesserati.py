import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QListView
from PyQt5 import QtCore, QtGui, QtWidgets

from Viste.NuovoTesserato import VistaNuovoTesserato
from Attivita.GestioneTesserati import GestioneTesserati
from Viste.ModificaTesserato import VistaModificaTesserato
from Viste.DettaglioTesserato import VistaDettaglioTesserato

class VistaTesserati(QWidget):

    def __init__(self, parent=None):
        super(VistaTesserati, self).__init__(parent)
        self.gridLayout = QGridLayout()

        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButtonCerca = QtWidgets.QPushButton()
        self.pushButtonCerca.setObjectName("pushButtonCerca")
        self.gridLayout.addWidget(self.pushButtonCerca, 1, 2, 1, 1)
        self.pushButtonTutti = QtWidgets.QPushButton()
        self.pushButtonTutti.setObjectName("pushButtonTutti")
        self.gridLayout.addWidget(self.pushButtonTutti, 1, 3, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonDettagli = QtWidgets.QPushButton()
        self.pushButtonDettagli.setObjectName("pushButtonDettagli")
        self.verticalLayout.addWidget(self.pushButtonDettagli)
        self.pushButtonModifica = QtWidgets.QPushButton()
        self.pushButtonModifica.setObjectName("pushButtonModifica")
        self.verticalLayout.addWidget(self.pushButtonModifica)
        self.pushButtonRinnova = QtWidgets.QPushButton()
        self.pushButtonRinnova.setObjectName("pushButtonRinnova")
        self.verticalLayout.addWidget(self.pushButtonRinnova)
        self.pushButtonElimina = QtWidgets.QPushButton()
        self.pushButtonElimina.setObjectName("pushButtonElimina")
        self.verticalLayout.addWidget(self.pushButtonElimina)
        self.pushButtonNuovo = QtWidgets.QPushButton()
        self.pushButtonNuovo.setObjectName("pushButtonNuovo")
        self.verticalLayout.addWidget(self.pushButtonNuovo)
        self.gridLayout.addLayout(self.verticalLayout, 2, 3, 1, 1)
        self.lineEditCerca = QtWidgets.QLineEdit()
        self.lineEditCerca.setObjectName("lineEditCerca")
        self.gridLayout.addWidget(self.lineEditCerca, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.listWidget = QListView()
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 3)
        self.pushButtonIndietro = QtWidgets.QPushButton()
        self.pushButtonIndietro.setObjectName("pushButtonIndietro")
        self.gridLayout.addWidget(self.pushButtonIndietro, 5, 0, 1, 1)

        self.label_2.setText("Cerca per Nome")
        self.pushButtonCerca.setText("Cerca")
        self.pushButtonDettagli.setText("Dettagli")
        self.pushButtonModifica.setText("Modifica")
        self.pushButtonRinnova.setText("Rinnova")
        self.pushButtonElimina.setText("Elimina")
        self.pushButtonNuovo.setText("Nuovo Tesserato")
        self.label.setText("Tesserati:")
        self.pushButtonIndietro.setText("Indietro")
        self.pushButtonTutti.setText("Mostra Tutti")

        self.updateList()

        self.pushButtonIndietro.clicked.connect(self.indietro)
        self.pushButtonNuovo.clicked.connect(self.nuovoTesserato)
        self.pushButtonElimina.clicked.connect(self.eliminaTesserato)
        self.pushButtonModifica.clicked.connect(self.modificaTesserato)
        self.pushButtonDettagli.clicked.connect(self.dettaglioTesserato)
        self.pushButtonCerca.clicked.connect(self.cerca)
        self.pushButtonTutti.clicked.connect(self.mostraTutti)
        self.pushButtonRinnova.setDisabled(True)

        self.setLayout(self.gridLayout)
        self.resize(1000, 800)
        self.setWindowTitle("Gestionale Palestra Scherma - Tesserati")

    def indietro(self):
        self.close()

    def mostraTutti(self):
        self.updateList()

    def cerca(self):
        campoRicerca = self.lineEditCerca.text()
        controller = GestioneTesserati()
        self.result =[]
        self.result = controller.ricercaPerNominativo(campoRicerca)
        print(self.result)

        try:
            listview_model = QStandardItemModel(self.listWidget)
            for tesserato in self.result:
                item = QStandardItem()
                nome = f"{tesserato.nome} {tesserato.cognome} - Codice: {tesserato.codice}"
                item.setText(nome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                listview_model.appendRow(item)
            self.listWidget.setModel(listview_model)
        except Exception as exc:
            print('error: {0}'.format(exc))


    def eliminaTesserato(self):
        try:
            selected = self.listWidget.selectedIndexes()[0].data()
            codice = int(selected.split("-")[1].strip().split(" ")[1])
            print(codice)
            controller = GestioneTesserati()
            controller.eliminaTesserato(codice=codice, callback=self.updateList)
        except IndexError:
            print("INDEX ERROR")
            return

    def modificaTesserato(self):
        try:
            selected = self.listWidget.selectedIndexes()[0].data()
            codice = int(selected.split("-")[1].strip().split(" ")[1])

            self.vista_modifica_tesserato = VistaModificaTesserato(codice=codice, callback=self.updateList)
            self.vista_modifica_tesserato.show()
        except IndexError:
            print("INDEX ERROR")
            return

    def dettaglioTesserato(self):
        try:
            selected = self.listWidget.selectedIndexes()[0].data()
            codice = int(selected.split("-")[1].strip().split(" ")[1])
            print(codice)

            self.vista_dettaglio_tesserato = VistaDettaglioTesserato(codice=codice)
            self.vista_dettaglio_tesserato.show()
        except IndexError:
            print("INDEX ERROR")
            return

    def nuovoTesserato(self):
        #devo identificare l'ultimo codice salvato e usare in ordine il successivo
        controller = GestioneTesserati()
        codice = controller.getLastCodice()
        self.vista_inserimento_nuovo_tesserato = VistaNuovoTesserato(codice+1, callback=self.updateList)
        self.vista_inserimento_nuovo_tesserato.show()

    def loadTesserati(self):
        controller = GestioneTesserati()
        self.tesserati = controller.getAllTesserati()
        print(self.tesserati)

    def updateList(self):
        self.tesserati = []
        self.loadTesserati()

        try:
            listview_model = QStandardItemModel(self.listWidget)
            for tesserato in self.tesserati:
                item = QStandardItem()
                nome = f"{tesserato.nome} {tesserato.cognome} - Codice: {tesserato.codice}"
                item.setText(nome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                listview_model.appendRow(item)
            self.listWidget.setModel(listview_model)
        except Exception as exc:
            print('error: {0}'.format(exc))
