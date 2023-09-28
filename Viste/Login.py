from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


from Viste.Home import VistaHome
from Attivita.GestioneUtenti import GestioneUtenti

class VistaLogin(QWidget):

    def __init__(self, parent=None):
        super(VistaLogin, self).__init__(parent)
        self.gridLayout = QGridLayout()


        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit()
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit().Password)
        self.gridLayout.addWidget(self.lineEdit_2, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel()
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 2)
        self.label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)

        self.label_3.setText("Password:")
        self.label_2.setText("Username:")
        self.pushButton.setText("LOGIN")
        self.label.setText("Login")

        self.pushButton.clicked.connect(self.login)

        self.setLayout(self.gridLayout)

        self.resize(400, 300)
        self.setWindowTitle("Gestionale Palestra Scherma")

    def loadUtenti(self):
        controller = GestioneUtenti()
        self.utenti = controller.getAllUtenti()

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        self.utenti = []
        self.loadUtenti()

        logged = False

        for utente in self.utenti:
            if(utente.username == username and utente.password == password):
                logged = True
                self.vista_home = VistaHome(utente)
                self.vista_home.show()
                self.close()

        if not logged:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Errore di Autenticazione!")
            msg.setInformativeText('Username o Password ERRATI, riprovare!')
            msg.setWindowTitle("Errore")
            msg.exec_()

