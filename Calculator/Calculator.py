import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("MYGUI")
        self.resize(320,430)
        
        #textfield
        self.edt_name = QLineEdit ("",self)
        self.edt_name.resize(350,45)
        self.edt_name.move(0,150)
        
        #btn 7
        self.btn_seven = QPushButton("7",self)
        self.btn_seven.move(10,200)
        self.btn_seven.resize(60,50)
        self.btn_seven.clicked.connect(self.btn_clicked7)
        
        #btn 8
        self.btn_eight = QPushButton("8",self)
        self.btn_eight.move(70,200)
        self.btn_eight.resize(60,50)
        self.btn_eight.clicked.connect(self.btn_clicked8)
        
        #btn 9 
        self.btn_nine = QPushButton("9",self)
        self.btn_nine.move(130,200)
        self.btn_nine.resize(60,50)
        self.btn_nine.clicked.connect(self.btn_clicked9)
        
        #btn /
        self.btn_div = QPushButton("/",self)
        self.btn_div.move(190,200)
        self.btn_div.resize(60,50)
        self.btn_div.clicked.connect(self.btn_clickeddiv)
        
        #btn 4
        self.btn_four = QPushButton("4",self)
        self.btn_four.move(10,250)
        self.btn_four.resize(60,50)
        self.btn_four.clicked.connect(self.btn_clicked4)
        
        #btn 5
        self.btn_five = QPushButton("5",self)
        self.btn_five.move(70,250)
        self.btn_five.resize(60,50)
        self.btn_five.clicked.connect(self.btn_clicked5)
        
        #btn 6
        self.btn_six = QPushButton("6",self)
        self.btn_six.move(130,250)
        self.btn_six.resize(60,50)
        self.btn_six.clicked.connect(self.btn_clicked6)
        
        #btn *
        self.btn_mul = QPushButton("x",self)
        self.btn_mul.move(190,250)
        self.btn_mul.resize(60,50)
        self.btn_mul.clicked.connect(self.btn_clickedmul)
        
        #btn 1
        self.btn_one = QPushButton("1",self)
        self.btn_one.move(10,300)
        self.btn_one.resize(60,50)
        self.btn_one.clicked.connect(self.btn_clicked1)
        
        #btn 2
        self.btn_two = QPushButton("2",self)
        self.btn_two.move(70,300)
        self.btn_two.resize(60,50)
        self.btn_two.clicked.connect(self.btn_clicked2)
        
        #btn 3
        self.btn_three = QPushButton("3",self)
        self.btn_three.move(130,300)
        self.btn_three.resize(60,50)
        self.btn_three.clicked.connect(self.btn_clicked3)
        
        #btn -
        self.btn_sub = QPushButton("-",self)
        self.btn_sub.move(190,300)
        self.btn_sub.resize(60,50)
        self.btn_sub.clicked.connect(self.btn_clickedsub)
        
        #btn 0
        self.btn_zero = QPushButton("0",self)
        self.btn_zero.move(10,350)
        self.btn_zero.resize(60,50)
        self.btn_zero.clicked.connect(self.btn_clicked0)
        
        #btn .
        self.btn_dot = QPushButton(".",self)
        self.btn_dot.move(70,350)
        self.btn_dot.resize(60,50)
        self.btn_dot.clicked.connect(self.btn_clickeddot)
        
        #btn =
        self.btn_equal = QPushButton("=",self)
        self.btn_equal.move(130,350)
        self.btn_equal.resize(60,50)
        self.btn_equal.clicked.connect(self.btn_clickedequal)
        
        #btn +
        self.btn_plus = QPushButton("+",self)
        self.btn_plus.move(190,350)
        self.btn_plus.resize(60,50)
        self.btn_plus.clicked.connect(self.btn_clickedplus)
        
        #btn %
        self.btn_mod = QPushButton("%",self)
        self.btn_mod.move(250,200)
        self.btn_mod.resize(60,50)
        self.btn_mod.clicked.connect(self.btn_clickedmod)
        
        #btn floor
        self.btn_floor = QPushButton("//",self)
        self.btn_floor.move(250,250)
        self.btn_floor.resize(60,50)
        self.btn_floor.clicked.connect(self.btn_clickedfloor)
        
        #btn **
        self.btn_exponential = QPushButton("**",self)
        self.btn_exponential.move(250,300)
        self.btn_exponential.resize(60,50)
        self.btn_exponential.clicked.connect(self.btn_clickedexponential)
        
        #btn clr
        self.btn_clr = QPushButton("C",self)
        self.btn_clr.move(250,350)
        self.btn_clr.resize(60,50)
        self.btn_clr.clicked.connect(self.btn_clickedclr)
    
    #btn operations...................
        
    def btn_clicked7(self):
        
        #function for button 7
        a = self.edt_name.text()
        self.edt_name.setText(a+"7")
        
    def btn_clicked8(self):
        
        #function for button 8
        a = self.edt_name.text()
        self.edt_name.setText(a+"8")
        
    def btn_clicked9(self):
        
        #function for button 9
        a = self.edt_name.text()
        self.edt_name.setText(a+"9")
        
    def btn_clicked4(self):
        
        #function for button 4
        a = self.edt_name.text()
        self.edt_name.setText(a+"4")
        
    def btn_clicked5(self):
        
        #function for button 5
        a = self.edt_name.text()
        self.edt_name.setText(a+"5")
        
    def btn_clicked6(self):
        
        #function for button 6
        a = self.edt_name.text()
        self.edt_name.setText(a+"6")
        
    def btn_clicked3(self):
        
        #function for button 3
        a = self.edt_name.text()
        self.edt_name.setText(a+"3")
        
    def btn_clicked2(self):
        
        #function for button 2
        a = self.edt_name.text()
        self.edt_name.setText(a+"2")
        
    def btn_clicked1(self):
        
        #function for button 1
        a = self.edt_name.text()
        self.edt_name.setText(a+"1")
        
    def btn_clicked0(self):
        #function for button 0
        a = self.edt_name.text()
        self.edt_name.setText(a+"0")
        
    def btn_clickeddot(self):
        
        #function for dot
        a = self.edt_name.text()
        self.edt_name.setText(a+".")
        
    def btn_clickedplus(self):
        
        #function to add
        a = self.edt_name.text()
        self.edt_name.setText(a+"+")
        
    def btn_clickedmul(self):
        
        #function to multiply
        a = self.edt_name.text()
        self.edt_name.setText(a+"*")
        
    def btn_clickeddiv(self):
        
        #function to divide
        a = self.edt_name.text()
        self.edt_name.setText(a+"/")
        
    def btn_clickedsub(self):
        
        #function to subtract
        a = self.edt_name.text()
        self.edt_name.setText(a+"-")
        
        
    def btn_clickedexponential(self):
        
        #function to perform exponential
        a = self.edt_name.text()
        self.edt_name.setText(a+"**")
        
    def btn_clickedfloor(self):
        
        #function to perform floor division
        a = self.edt_name.text()
        self.edt_name.setText(a+"//")
        
    def btn_clickedmod(self):
        
        #function to perform modulo
        a = self.edt_name.text()
        self.edt_name.setText(a+"%")
        
    def btn_clickedclr(self):
        
        #function to clear
        self.edt_name.clear()
        
    
    def btn_clickedequal(self):
        
        #function for equal
        a = eval(self.edt_name.text())
        self.edt_name.setText(str(a))
        
        
        
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    dlg = Window()
    dlg.show()
    app.exec_()