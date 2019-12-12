import sys
from PyQt5 import QtWidgets
from ClientForm import Ui_MainWindow

from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineOnlyReceiver

class ConnectorProtocol(LineOnlyReceiver):
    factory: 'Connector'

    def connectionMade(self):
        self.factory.window.protocol = self        

    def LineRecieved(self, line: bytes):
        message = line.decode()
        self.factory.window.chat_window_text.appendPlainText(message)
  

class Connector(ClientFactory):
    window: 'ChatWindow'
    protocol=ConnectorProtocol

    def __init__(self, app_window):
        self.window = app_window


class ChatWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    protocol: ConnectorProtocol
    reactor = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_handlers()

    def init_handlers(self):
        self.submit_button.clicked.connect(self.send_message)
        #Добавить событие по нажатию на Enter

    def closeEvent(self, event):
        self.reactor.callFromThread(self.reactor.stop)

    def send_message(self):
        message=self.text_to_send.text()
        #self.chat_window_text.appendPlainText(message)
        self.protocol.sendLine(message.encode())
        self.text_to_send.setText('')



app = QtWidgets.QApplication(sys.argv)

import qt5reactor

window = ChatWindow()
window.show()

qt5reactor.install()

from twisted.internet import reactor

reactor.connectTCP(
    "localhost",
    1234,
    Connector(window)
)

window.reactor = reactor
reactor.run()


