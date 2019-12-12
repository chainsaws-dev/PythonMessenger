import sys
from PyQt5 import QtWidgets
from ClientForm import Ui_MainWindow


class ChatWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_handlers()

    def init_handlers(self):
        self.submit_button.clicked.connect(self.send_message)
        #Добавить событие по нажатию на Enter
        
    def send_message(self):
        message=self.text_to_send.text()
        self.chat_window_text.appendPlainText(message)
        self.text_to_send.clear()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()