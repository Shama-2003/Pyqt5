import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui  import *
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MYGUI")
        self.resize(1000,1000)
        #Adding Qlabel
        self.lbl_text = QLabel("Hello",self)
        self.lbl_text.move(200,100)
        self.lbl_text.resize(200,100)
        self.btn_en = QPushButton("Enable_text",self)
        self.enable()
        
    def enable(self):
        #Adding an button
        self.btn_en.setText("Enable_text")
        self.btn_en.move(200,100)
        self.btn_en.clicked.connect(self.btn_clicked)
        self.lbl_text.setEnabled(False)
        
    def btn_clicked(self):
        self.btn_en.setText("Disable_text")
        self.lbl_text.setEnabled(True)
        self.btn_en.clicked.connect(self.enable)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Window()
    dlg.show()
    app.exec_()
