import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("MYGUI")
        self.resize(320,430)
        
        #label Color selected
        self.lbl_color_selected = QLabel("Color selected",self)
        self.lbl_color_selected.move(50,25)
        
        #To group buttons
        self.btncolor = QButtonGroup()
        
        #Radio button green
        self.rbt_green = QRadioButton("Green",self)
        self.rbt_green.move(50,50)
        self.btncolor.addButton(self.rbt_green)
        self.rbt_green.clicked.connect(self.evt_green)
        
        #Radio button red
        self.rbt_red = QRadioButton("Red",self)
        self.rbt_red.move(50,70)
        self.btncolor.addButton(self.rbt_red)
        self.rbt_red.clicked.connect(self.evt_red)
        
        #Radio button pink
        self.rbt_pink = QRadioButton("Pink",self)
        self.rbt_pink.move(50,90)
        self.btncolor.addButton(self.rbt_pink)
        self.rbt_pink.clicked.connect(self.evt_pink)
        
        #Radio button blue
        self.rbt_blue = QRadioButton("Blue",self)
        self.rbt_blue.move(50,110)
        self.btncolor.addButton(self.rbt_blue)
        self.rbt_blue.clicked.connect(self.evt_blue)
        
        #Radio button ornge
        self.rbt_orange = QRadioButton("orange",self)
        self.rbt_orange.move(50,130)
        self.btncolor.addButton(self.rbt_orange)
        self.rbt_orange.clicked.connect(self.evt_orange)
        
    #functions.............................................. 
        
    def evt_green(self):
        
        #function of green radio button
        ss = self.rbt_green.text()
        QMessageBox.information(self,"Color Clicked",ss)
        self.lbl_color_selected.setStyleSheet("Color:"+ss)
        
    def evt_red(self):
        
        #function of red radio button
        ss = self.rbt_red.text()
        QMessageBox.information(self,"Color Clicked",ss)
        self.lbl_color_selected.setStyleSheet("Color:"+ss)
        
    def evt_pink(self):
        
        #function of pink radio button
        ss = self.rbt_pink.text()
        QMessageBox.information(self,"Color Clicked",ss)
        self.lbl_color_selected.setStyleSheet("Color:"+ss)
        
    def evt_blue(self):
        
        #function of blue radio button
        ss = self.rbt_blue.text()
        QMessageBox.information(self,"Color Clicked",ss)
        self.lbl_color_selected.setStyleSheet("Color:"+ss)
        
    def evt_orange(self):
        
        #function of orange radio button
        ss = self.rbt_orange.text()
        QMessageBox.information(self,"Color Clicked",ss)
        self.lbl_color_selected.setStyleSheet("Color:"+ss)
        
        
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    dlg = Window()
    dlg.show()
    app.exec_()