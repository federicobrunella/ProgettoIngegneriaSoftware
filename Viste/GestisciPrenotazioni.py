from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QListView
from PyQt5 import QtCore, QtGui, QtWidgets

from Attivita.GestionePrenotazioni import GestionePrenotazioni
from Viste.NuovaPrenotazione import VistaNuovaPrenotazione


class VistaPrenotazioni(QWidget):

    def __init__(self, parent=None):
        super(VistaPrenotazioni, self).__init__(parent)
        self.gridLayout = QGridLayout()

        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ricercaData = QtWidgets.QLineEdit()
        self.ricercaData.setObjectName("ricercaData")
        self.gridLayout.addWidget(self.ricercaData, 1, 2, 1, 1)
        self.ricercaNome = QtWidgets.QLineEdit()
        self.ricercaNome.setObjectName("ricercaNome")
        self.gridLayout.addWidget(self.ricercaNome, 1, 0, 1, 1)
        self.listWidget = QListView()
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 5)
        self.pushButtonCercaNome = QtWidgets.QPushButton()
        self.pushButtonCercaNome.setObjectName("pushButtonCercaNome")
        self.gridLayout.addWidget(self.pushButtonCercaNome, 1, 1, 1, 1)
        self.pushButtonCercaData = QtWidgets.QPushButton()
        self.pushButtonCercaData.setObjectName("pushButtonCercaData")
        self.gridLayout.addWidget(self.pushButtonCercaData, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel()
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(104, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 4, 1, 1)
        self.pushButtonIndietro = QtWidgets.QPushButton()
        self.pushButtonIndietro.setObjectName("pushButtonIndietro")
        self.gridLayout.addWidget(self.pushButtonIndietro, 3, 0, 1, 1)
        self.pushButtonNuovaPrenotazione = QtWidgets.QPushButton()
        self.pushButtonNuovaPrenotazione.setObjectName("pushButtonNuovaPrenotazione")
        self.gridLayout.addWidget(self.pushButtonNuovaPrenotazione, 3, 3, 1, 2)

        self.pushButtonCercaNome.setText("Cerca")
        self.pushButtonCercaData.setText("Cerca")
        self.label.setText("Cerca per id Prenotante:")
        self.label_2.setText("Cerca per Data:")
        self.pushButtonNuovaPrenotazione.setText("Nuova Prenotazione")
        self.pushButtonIndietro.setText("Indietro")

        self.updateList()

        self.pushButtonIndietro.clicked.connect(self.indietro)
        self.pushButtonNuovaPrenotazione.clicked.connect(self.nuovaPrenotazione)
        self.pushButtonCercaNome.clicked.connect(self.cercaPerPrenotante)
        self.pushButtonCercaData.clicked.connect(self.cercaPerData)

        self.setLayout(self.gridLayout)
        self.resize(1000, 800)
        self.setWindowTitle("Gestionale Palestra Scherma - Prenotazioni")

    def indietro(self):
        self.close()

    def loadPrenotazioni(self):
        controller = GestionePrenotazioni()
        self.prenotazioni = controller.getAllPrenotazioni()

    def nuovaPrenotazione(self):
        #devo identificare l'ultimo codice salvato e usare in ordine il successivo
        controller = GestionePrenotazioni()
        codice = controller.getLastCodice()
        self.vista_inserimento_nuova_prenotazione = VistaNuovaPrenotazione(codice+1, callback=self.updateList)
        self.vista_inserimento_nuova_prenotazione.show()

    def updateList(self):
        self.prenotazioni = []
        self.loadPrenotazioni()

        try:
            listview_model = QStandardItemModel(self.listWidget)
            for prenotazione in self.prenotazioni:
                item = QStandardItem()
                nome = f"Id: {prenotazione.idPrenotante} - Inizio: {prenotazione.oraInizio} Fine: {prenotazione.oraFine}"
                item.setText(nome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                listview_model.appendRow(item)
            self.listWidget.setModel(listview_model)
        except Exception as exc:
            print('error: {0}'.format(exc))


    def cercaPerPrenotante(self):
        campoRicerca = self.ricercaNome.text()
        controller = GestionePrenotazioni()
        self.result =[]
        self.result = controller.ricercaPerPrenotante(campoRicerca)
        print(self.result)

        try:
            listview_model = QStandardItemModel(self.listWidget)
            for prenotazione in self.result:
                item = QStandardItem()
                nome = f"Id: {prenotazione.idPrenotante} - Inizio: {prenotazione.oraInizio} Fine: {prenotazione.oraFine}"
                item.setText(nome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                listview_model.appendRow(item)
            self.listWidget.setModel(listview_model)
        except Exception as exc:
            print('error cercaPerPrenotante'.format(exc))

    def cercaPerData(self):
            campoRicerca = self.ricercaData.text()
            controller = GestionePrenotazioni()
            self.result = []
            self.result = controller.ricercaPerData(campoRicerca)
            print(self.result)

            try:
                listview_model = QStandardItemModel(self.listWidget)
                for prenotazione in self.result:
                    item = QStandardItem()
                    nome = f"Id: {prenotazione.idPrenotante} - Inizio: {prenotazione.oraInizio} Fine: {prenotazione.oraFine}"
                    item.setText(nome)
                    item.setEditable(False)
                    font = item.font()
                    font.setPointSize(18)
                    item.setFont(font)
                    listview_model.appendRow(item)
                self.listWidget.setModel(listview_model)
            except Exception as exc:
                print('error cercaPerPrenotante'.format(exc))
