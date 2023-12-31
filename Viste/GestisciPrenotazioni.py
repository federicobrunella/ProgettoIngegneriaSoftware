from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QWidget, QGridLayout, QListView
from PyQt5 import QtWidgets

from Attivita.GestionePrenotazioni import GestionePrenotazioni
from Viste.NuovaPrenotazione import VistaNuovaPrenotazione
from Viste.ModificaPrenotazione import VistaModificaPrenotazione
from Viste.DettaglioPrenotazione import VistaDettaglioPrenotazione


class VistaPrenotazioni(QWidget):

    def __init__(self, parent=None):
        super(VistaPrenotazioni, self).__init__(parent)
        self.gridLayout = QGridLayout()

        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.listView = QListView()
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 2, 0, 1, 5)
        self.pushButtonCercaNome = QtWidgets.QPushButton()
        self.pushButtonCercaNome.setObjectName("pushButtonCercaNome")
        self.gridLayout.addWidget(self.pushButtonCercaNome, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 2)
        self.pushButtonIndietro = QtWidgets.QPushButton()
        self.pushButtonIndietro.setObjectName("pushButtonIndietro")
        self.gridLayout.addWidget(self.pushButtonIndietro, 5, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 4, 1, 1)
        self.label = QtWidgets.QLabel()
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.pushButtonCercaData = QtWidgets.QPushButton()
        self.pushButtonCercaData.setObjectName("pushButtonCercaData")
        self.gridLayout.addWidget(self.pushButtonCercaData, 1, 3, 1, 1)
        self.ricercaNome = QtWidgets.QLineEdit()
        self.ricercaNome.setObjectName("ricercaNome")
        self.gridLayout.addWidget(self.ricercaNome, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonDettaglio = QtWidgets.QPushButton()
        self.pushButtonDettaglio.setObjectName("pushButtonDettaglio")
        self.verticalLayout.addWidget(self.pushButtonDettaglio)
        self.pushButtonModifica = QtWidgets.QPushButton()
        self.pushButtonModifica.setObjectName("pushButtonModifica")
        self.verticalLayout.addWidget(self.pushButtonModifica)
        self.pushButtonElimina = QtWidgets.QPushButton()
        self.pushButtonElimina.setObjectName("pushButtonElimina")
        self.verticalLayout.addWidget(self.pushButtonElimina)
        self.pushButtonNuovaPrenotazione = QtWidgets.QPushButton()
        self.pushButtonNuovaPrenotazione.setObjectName("pushButtonNuovaPrenotazione")
        self.verticalLayout.addWidget(self.pushButtonNuovaPrenotazione)
        self.gridLayout.addLayout(self.verticalLayout, 2, 5, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit()
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 1, 2, 1, 1)

        self.pushButtonCercaNome.setText("Cerca")
        self.label_2.setText("Cerca per Data:")
        self.pushButtonIndietro.setText("Indietro")
        self.pushButton.setText("Mostra Tutti")
        self.label.setText("Cerca per ID:")
        self.pushButtonCercaData.setText("Cerca")
        self.pushButtonDettaglio.setText("Dettagli")
        self.pushButtonModifica.setText("Modifica")
        self.pushButtonElimina.setText("Elimina")
        self.pushButtonNuovaPrenotazione.setText("Nuova Prenotazione")

        self.updateList()

        self.pushButtonIndietro.clicked.connect(self.indietro)
        self.pushButtonNuovaPrenotazione.clicked.connect(self.nuovaPrenotazione)
        self.pushButtonCercaNome.clicked.connect(self.cercaPerPrenotante)
        self.pushButtonCercaData.clicked.connect(self.cercaPerData)
        self.pushButton.clicked.connect(self.mostraTutti)
        self.pushButtonElimina.clicked.connect(self.eliminaPrenotazione)
        self.pushButtonModifica.clicked.connect(self.modificaPrenotazione)
        self.pushButtonDettaglio.clicked.connect(self.dettaglioPrenotazione)

        self.setLayout(self.gridLayout)
        self.resize(1000, 800)
        self.setWindowTitle("Gestionale Palestra Scherma - Prenotazioni")

    def indietro(self):
        self.close()

    def mostraTutti(self):
        self.updateList()

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
            listview_model = QStandardItemModel(self.listView)
            for prenotazione in self.prenotazioni:
                item = QStandardItem()
                nome = f"Tesserato: {prenotazione.idPrenotante} - Prenotazione: {prenotazione.id} - Inizio: {prenotazione.oraInizio} Fine: {prenotazione.oraFine}"
                item.setText(nome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                listview_model.appendRow(item)
            self.listView.setModel(listview_model)
        except Exception as exc:
            print('error: {0}'.format(exc))


    def cercaPerPrenotante(self):
        campoRicerca = self.ricercaNome.text()
        controller = GestionePrenotazioni()
        self.result =[]
        self.result = controller.ricercaPerPrenotante(campoRicerca)
        print(self.result)

        try:
            listview_model = QStandardItemModel(self.listView)
            for prenotazione in self.result:
                item = QStandardItem()
                nome = f"Tesserato: {prenotazione.idPrenotante} - Prenotazione: {prenotazione.id} - Inizio: {prenotazione.oraInizio} Fine: {prenotazione.oraFine}"
                item.setText(nome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                listview_model.appendRow(item)
            self.listView.setModel(listview_model)
        except Exception as exc:
            print('error cercaPerPrenotante'.format(exc))

    def cercaPerData(self):
            campoRicerca = self.dateEdit.date()
            controller = GestionePrenotazioni()
            self.result = []
            self.result = controller.ricercaPerData(campoRicerca)
            print(self.result)

            try:
                listview_model = QStandardItemModel(self.listView)
                for prenotazione in self.result:
                    item = QStandardItem()
                    nome = f"Tesserato: {prenotazione.idPrenotante} - Prenotazione: {prenotazione.id} - Inizio: {prenotazione.oraInizio} Fine: {prenotazione.oraFine}"
                    item.setText(nome)
                    item.setEditable(False)
                    font = item.font()
                    font.setPointSize(18)
                    item.setFont(font)
                    listview_model.appendRow(item)
                self.listView.setModel(listview_model)
            except Exception as exc:
                print('error cercaPerData'.format(exc))


    def eliminaPrenotazione(self):
        try:
            selected = self.listView.selectedIndexes()[0].data()
            id = int(selected.split("-")[1].strip().split(" ")[1])
            controller = GestionePrenotazioni()
            controller.eliminaPrenotazione(id=id, callback=self.updateList)
        except Exception as exc:
            print("INDEX ERROR")
            return

    def modificaPrenotazione(self):
        try:
            selected = self.listView.selectedIndexes()[0].data()
            id = int(selected.split("-")[1].strip().split(" ")[1])
            print(id)
            self.vista_modifica_prenotazione = VistaModificaPrenotazione(id=id, callback=self.updateList)
            self.vista_modifica_prenotazione.show()
        except IndexError:
            print("INDEX ERROR")
            return

    def dettaglioPrenotazione(self):
        try:
            selected = self.listView.selectedIndexes()[0].data()
            id = int(selected.split("-")[1].strip().split(" ")[1])
            print(id)

            self.vista_dettaglio_prenotazione = VistaDettaglioPrenotazione(id=id)
            self.vista_dettaglio_prenotazione.show()
        except Exception as exc:
            print("INDEX ERROR")
            return

