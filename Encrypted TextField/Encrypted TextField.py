import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui  import *
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MYGUI")
        self.resize(200,200)
        self.edt_name = QLineEdit ("",self)
        self.edt_name.setPlaceholderText ("HELLO!!")
        self.edt_name.setEchoMode(QLineEdit.Password)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Window()
    dlg.show()
    app.exec_()