import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("MYGUI")
        self.resize(320,430)
        
        #label num1
        self.lbl_num1 = QLabel("NUM1:",self)
        self.lbl_num1.move(10,100)
        self.lbl_num1.resize(100,100)
        self.lbl_num1.setStyleSheet("color: red")
        
        #textfield num1
        self.edt_num1 = QLineEdit ("",self)
        self.edt_num1.move(50,145)
        
        #button num1
        self.btn_num1 = QPushButton("GET INPUT",self)
        self.btn_num1.move(200,145)
        self.btn_num1.resize(70,20)
        self.btn_num1.clicked.connect(self.num_1)
        self.btn_num1.setStyleSheet("background-color:wheat")
        
        #num 2
        self.lbl_num2 = QLabel("NUM2:",self)
        self.lbl_num2.move(10,150)
        self.lbl_num2.resize(100,100)
        self.lbl_num2.setStyleSheet("color: blue")
        
        #textfield num2
        self.edt_num2 = QLineEdit ("",self)
        self.edt_num2.move(50,195)
        
        #button num2
        self.btn_num2 = QPushButton("GET INPUT",self)
        self.btn_num2.move(200,195)
        self.btn_num2.resize(70,20)
        self.btn_num2.clicked.connect(self.num_2)
        self.btn_num2.setStyleSheet("background-color:wheat")
        
        #label result
        self.lbl_res = QLabel("RESULT:",self)
        self.lbl_res.move(10,200)
        self.lbl_res.resize(100,100)
        self.lbl_res.setStyleSheet("color: brown")
        #textfield res
        self.edt_res = QLineEdit ("",self)
        self.edt_res.move(50,245)
        
        #operation buttons.........................
        
        #button +
        self.btn_plus = QPushButton("+",self)
        self.btn_plus.move(10,300)
        self.btn_plus.resize(60,50)
        self.btn_plus.setStyleSheet("background-color:yellow")
        self.btn_plus.clicked.connect(self.btn_clickedplus)
        
        #button -
        self.btn_sub = QPushButton("-",self)
        self.btn_sub.move(70,300)
        self.btn_sub.resize(60,50)
        self.btn_sub.setStyleSheet("background-color:lightsalmon")
        self.btn_sub.clicked.connect(self.btn_clickedsub)
        
        #button *
        self.btn_mul = QPushButton("x",self)
        self.btn_mul.move(130,300)
        self.btn_mul.resize(60,50)
        self.btn_mul.setStyleSheet("background-color:crimson")
        self.btn_mul.clicked.connect(self.btn_clickedmul)
        
        #button /
        self.btn_div = QPushButton("/",self)
        self.btn_div.move(190,300)
        self.btn_div.resize(60,50)
        self.btn_div.setStyleSheet("background-color:Tomato")
        self.btn_div.clicked.connect(self.btn_clickeddiv)
        
        #button clr
        self.btn_clr = QPushButton("clear",self)
        self.btn_clr.move(250,300)
        self.btn_clr.resize(60,50)
        self.btn_clr.setStyleSheet("background-color:Orangered")
        self.btn_clr.clicked.connect(self.btn_clickedclr)
        
   #functions..............................................     
        
    def num_1(self):
        
        #function of num1
        num1,a = QInputDialog.getInt(self,"Input","enter num1",0,0,100,1)
        self.edt_num1.setText(str(num1))
        
    def num_2(self):
        
        #function of num1
        num2,b = QInputDialog.getInt(self,"Input","enter num1",0,0,100,1)
        self.edt_num2.setText(str(num2))
        
    def btn_clickedplus(self):
        
        #function of plus
        f = self.edt_num1.text()
        g = self.edt_num2.text()
        k = int(f)+int(g)
        self.edt_res.setText(str(k))
        
    def btn_clickedsub(self):
        
        #function of sub
        f = self.edt_num1.text()
        g = self.edt_num2.text()
        k = int(f)-int(g)
        self.edt_res.setText(str(k))
        
    def btn_clickedmul(self):
        
        #function of mul
        f = self.edt_num1.text()
        g = self.edt_num2.text()
        k = int(f)*int(g)
        self.edt_res.setText(str(k))
        
    def btn_clickeddiv(self):
        
        #function of div
        f = self.edt_num1.text()
        g = self.edt_num2.text()
        k = int(f)/int(g)
        self.edt_res.setText(str(k))
        
    def btn_clickedclr(self):
        
        #function of clear
        self.edt_num1.clear()
        self.edt_num2.clear()
        self.edt_res.clear()
        


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    dlg = Window()
    dlg.show()
    app.exec_()