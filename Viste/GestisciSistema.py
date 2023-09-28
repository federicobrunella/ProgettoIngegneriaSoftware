from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QListView
from PyQt5 import QtCore, QtGui, QtWidgets

from Viste.ImpostazioneOrari import VistaOrari
from Viste.ImpostazionePrezzi import VistaPrezzi
from Viste.ImpostazioniPedane import VistaPedane
from Viste.DettaglioUtente import VistaDettaglioUtente
from Viste.NuovoUtente import VistaNuovoUtente
from Viste.ModificaUtente import VistaModificaUtente

from Attivita.GestioneUtenti import GestioneUtenti

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
        self.listView = QListView()
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
        self.pushButtonElimina = QtWidgets.QPushButton()
        self.pushButtonElimina.setObjectName("pushButtonElimina")
        self.gridLayout.addWidget(self.pushButtonElimina, 8, 2, 1, 1)
        self.pushButtonModifica = QtWidgets.QPushButton()
        self.pushButtonModifica.setObjectName("pushButtonModifica")
        self.gridLayout.addWidget(self.pushButtonModifica, 8, 1, 1, 1)
        self.pushButtonDettagli = QtWidgets.QPushButton()
        self.pushButtonDettagli.setObjectName("pushButtonDettagli")
        self.gridLayout.addWidget(self.pushButtonDettagli, 8, 0, 1, 1)

        self.label_2.setText("Operazioni Amministratore:")
        self.pushButtonBackup.setText("Backup")
        self.pushButtonPedane.setText("Gestisci Pedane")
        self.label.setText("Lista Operatori:")
        self.pushButtonNuovoOperatore.setText("Nuovo Operatore")
        self.pushButtonOrari.setText("Gestisci Orari")
        self.pushButtonPrezzi.setText("Gestisci Prezzi")
        self.pushButtonIndietro.setText("Indietro")
        self.pushButtonElimina.setText("Elimina Operatore")
        self.pushButtonModifica.setText("Modifica Operatore")
        self.pushButtonDettagli.setText("Dettagli")

        self.updateList()

        self.pushButtonIndietro.clicked.connect(self.indietro)
        self.pushButtonOrari.clicked.connect(self.gestisciOrari)
        self.pushButtonPrezzi.clicked.connect(self.gestisciPrezzi)
        self.pushButtonPedane.clicked.connect(self.gestisciPedane)

        self.pushButtonElimina.clicked.connect(self.eliminaUtente)
        self.pushButtonDettagli.clicked.connect(self.dettagliUtente)
        self.pushButtonModifica.clicked.connect(self.modificaUtente)
        self.pushButtonNuovoOperatore.clicked.connect(self.nuovoUtente)

        self.pushButtonBackup.setDisabled(True)

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

    def nuovoUtente(self):
        controller = GestioneUtenti()
        codice = controller.getLastCodice()

        self.vista_nuovo_utente = VistaNuovoUtente(codice=codice+1, callback=self.updateList)
        self.vista_nuovo_utente.show()

    def eliminaUtente(self):
        try:
            selected = self.listView.selectedIndexes()[0].data()
            codice = int(selected.split("-")[1].strip().split(" ")[1])
            print(codice)
            controller = GestioneUtenti()
            controller.eliminaUtente(codice=codice, callback=self.updateList)
        except IndexError:
            print("INDEX ERROR")
            return

    def modificaUtente(self):
        try:
            selected = self.listView.selectedIndexes()[0].data()
            codice = int(selected.split("-")[1].strip().split(" ")[1])
            print(codice)
            self.vista_modifica_utente = VistaModificaUtente(codice=codice, callback=self.updateList)
            self.vista_modifica_utente.show()
        except IndexError:
            print("INDEX ERROR")
            return

    def dettagliUtente(self):
        try:
            selected = self.listView.selectedIndexes()[0].data()
            codice = int(selected.split("-")[1].strip().split(" ")[1])
            self.vista_dettaglio_utente = VistaDettaglioUtente(codice=codice)
            self.vista_dettaglio_utente.show()
        except IndexError:
            print("INDEX ERROR")
            return

    def loadUtenti(self):
        controller = GestioneUtenti()
        self.utenti = controller.getAllUtenti()

    def updateList(self):
        self.utenti = []
        self.loadUtenti()

        try:
            listview_model = QStandardItemModel(self.listView)
            for utente in self.utenti:
                item = QStandardItem()
                nome = f"{utente.username} {utente.nome} {utente.cognome} - Codice: {utente.codice}"
                item.setText(nome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                listview_model.appendRow(item)
            self.listView.setModel(listview_model)
        except Exception as exc:
            print('error: {0}'.format(exc))
