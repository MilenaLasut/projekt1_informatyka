# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:33:33 2019

@author: Admin
"""
from projekt1_inf import pkt_przeciecia, roznica
import sys
from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel, QWidget, QApplication, QGridLayout, QColorDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.figure import Figure3
import matplotlib.pyplot as plt

class AppWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title='Licz punkt przecięcia dwóch odcinków' #definicja tytułu okna aplikacji
        self.initInterface()
        self.initWidgets()
        
        
    def initInterface(self):
        self.setWindowTitle(self.title) #wpisanie tytułu okna
        self.setGeometry(300,200,1000,800) #położenie i rozmair okna aplikacji
        self.show() #wyswietlenie okna 
        
    def initWidgets(self): #deklaracja wszystkich wudgetów aplikacji
        button = QPushButton('Punkt przecięcia',self)
        buttonColAB= QPushButton('Kolor odcinka AB',self)
        buttonColCD= QPushButton('Kolor odcinka CD',self)
        buttonColP= QPushButton('Kolor punktu P ',self)
        buttonClear =  QPushButton('Wyczysc',self)
        buttonRoz = QPushButton('Różnica długosci',self)
        xaLabel = QLabel('XA:',self)
        yaLabel = QLabel('YA:',self)
        self.xaEdit = QLineEdit()
        self.yaEdit = QLineEdit()
        
        xbLabel = QLabel('XB:',self)
        ybLabel = QLabel('YB:',self)
        self.xbEdit = QLineEdit()
        self.ybEdit = QLineEdit()
        
        xcLabel = QLabel('XC:',self)
        ycLabel = QLabel('YC:',self)
        self.xcEdit = QLineEdit()
        self.ycEdit = QLineEdit()
        
        xdLabel = QLabel('XD:',self)
        ydLabel = QLabel('YD:',self)
        self.xdEdit = QLineEdit()
        self.ydEdit = QLineEdit()
        
        xpLabel = QLabel('XP:',self)
        ypLabel = QLabel('YP:',self)
        self.xpEdit = QLineEdit()
        self.ypEdit = QLineEdit()
        
        txtLabel = QLabel('Położenie punktu:',self)
        self.txtEdit = QLineEdit()
        
        rozLabel = QLabel('Różnica:',self)
        self.rozEdit = QLineEdit()
        opisLabel = QLabel('Komentarz:',self)
        self.opisEdit = QLineEdit()
        
        
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        
        #wyswietlanie
        grid = QGridLayout() #użycie układu siatki do rozmieszczenia obiektów
        
        grid.addWidget(xaLabel, 0, 0) #ułożenie kolejnych elementów interfejsu
        grid.addWidget(self.xaEdit, 0, 1)
        grid.addWidget(yaLabel, 1, 0)
        grid.addWidget(self.yaEdit, 1, 1)
        
        grid.addWidget(xbLabel, 0, 2)
        grid.addWidget(self.xbEdit, 0, 3)
        grid.addWidget(ybLabel, 1, 2)
        grid.addWidget(self.ybEdit, 1, 3)
        
        grid.addWidget(xcLabel, 0, 4)
        grid.addWidget(self.xcEdit, 0, 5)
        grid.addWidget(ycLabel, 1, 4)
        grid.addWidget(self.ycEdit, 1, 5)
        
        grid.addWidget(xdLabel, 0, 6)
        grid.addWidget(self.xdEdit, 0, 7)
        grid.addWidget(ydLabel, 1, 6)
        grid.addWidget(self.ydEdit, 1, 7)
        
        grid.addWidget(xpLabel, 4, 0)
        grid.addWidget(self.xpEdit, 4, 1)
        grid.addWidget(ypLabel, 5, 0)
        grid.addWidget(self.ypEdit, 5, 1)
        
        grid.addWidget(button, 3, 1)
        grid.addWidget(buttonColAB, 2, 1)
        grid.addWidget(buttonColCD, 2, 3)
        grid.addWidget(buttonColP, 2, 5)
        grid.addWidget(buttonClear, 5, 7)
        grid.addWidget(buttonRoz, 9, 0)
        
        grid.addWidget(self.canvas, 6, 2, 20, -1) #położenie i rozmiar okna na wykres 
        self.setLayout(grid)
        
        grid.addWidget(txtLabel, 4, 3)
        grid.addWidget(self.txtEdit, 5, 3, 1 ,3)
        
        grid.addWidget(rozLabel, 10, 0, 1, 2)
        grid.addWidget(self.rozEdit, 11, 0, 1 ,2)
        grid.addWidget(opisLabel, 12, 0, 1, 2)
        grid.addWidget(self.opisEdit, 13, 0, 1 ,2)
        
        # podpięcie funkcji do wszystkich przycisków
        button.clicked.connect(self.oblicz)
        buttonColAB.clicked.connect(self.zmienkolorAB)
        buttonColCD.clicked.connect(self.zmienkolorCD)
        buttonColP.clicked.connect(self.zmienkolorP)
        buttonClear.clicked.connect(self.clear)
        buttonRoz.clicked.connect(self.roznica)
        
    def clear(self): #funkcja do czyszczenia pól tekstowych
        self.xaEdit.clear()
        self.yaEdit.clear()
        self.xbEdit.clear()
        self.ybEdit.clear()
        self.xcEdit.clear()
        self.ycEdit.clear()
        self.xdEdit.clear()
        self.ydEdit.clear()
        self.xpEdit.clear()
        self.ypEdit.clear()
        self.txtEdit.clear()
    
    def zmienkolorAB(self): #funkcje do zmiany koloru linii i punktu na wykresie 
        kolor=QColorDialog.getColor()
        if kolor.isValid():
            self.pktprz(kolAB=kolor.name())
    def zmienkolorCD(self):
        kolor1=QColorDialog.getColor()
        if kolor1.isValid():
            self.pktprz(kolCD=kolor1.name())
    def zmienkolorP(self):
        kolor2=QColorDialog.getColor()
        if kolor2.isValid():
            self.pktprz(kolP=kolor2.name())
            
            
    def sprawdzliczbe(self,element): #funkcja ktora sprawdza czy wpisane współrzedne są prawidłowe
        if element.text().lstrip('-').replace('.','',1).isdigit():
            return float(element.text())
        else:
            element.setFocus()
            return(None)
            
    def oblicz(self):
        self.pktprz()

        
    def pktprz(self,kolAB='y',kolCD='b',kolP='g'): #definicja funkcji głównej i 
        xa=self.sprawdzliczbe(self.xaEdit)
        ya=self.sprawdzliczbe(self.yaEdit)
        xb=self.sprawdzliczbe(self.xbEdit)
        yb=self.sprawdzliczbe(self.ybEdit)
        xc=self.sprawdzliczbe(self.xcEdit)
        yc=self.sprawdzliczbe(self.ycEdit)
        xd=self.sprawdzliczbe(self.xdEdit)
        yd=self.sprawdzliczbe(self.ydEdit)
        
        if None not in [xa,ya,xb,yb,xc,yc,xd,yd]: #jesli funkcja sprawdzająca nie poda błędu to kontunuujemy 
            xa = float(self.xaEdit.text())
            ya = float(self.yaEdit.text())
            xb = float(self.xbEdit.text())
            yb = float(self.ybEdit.text())
            xc = float(self.xcEdit.text())
            yc = float(self.ycEdit.text())
            xd = float(self.xdEdit.text())
            yd = float(self.ydEdit.text())
            
            t1,t2,XP,YP,txt=pkt_przeciecia(xa,ya,xb,yb,xc,yc,xd,yd) #użycie funkcji obliczającej, wraz z zapisem do pliku tekstowego
            
            self.xpEdit.setText(str(XP)) #wpisanie współrzędnych punktu przecięcia w odpowiednie miejsca
            self.ypEdit.setText(str(YP))
            self.txtEdit.setText(str(txt)) #wpisanie opisu położenia punktu
            
            self.figure.clear() #wyczyszczenie pola na wykres 
            ax = self.figure.add_subplot(111)
            
            if t1>=0 and t1<=1: #zależnosci warunkujące położenie punktu względem odcinków
                if t2>=0 and t2<=1:
                    pass
                else:
                    ax.plot([YP,yc],[XP,xc],':')
            else:
                if t2>=0 and t2<=1:
                    ax.plot([YP,ya],[XP,xa],':')
                else:
                    ax.plot([YP,yc],[XP,xc],':')
                    ax.plot([YP,ya],[XP,xa],':')
    
            #wykresy zawiracjące odcinki, punkt przecięcia i przedłużenia
            ax.plot([ya,yb],[xa,xb],color=kolAB,label='AB')
            ax.plot([yc,yd],[xc,xd],color=kolCD,label='CD')
            ax.scatter(YP,XP,color=kolP,marker='^',label='punkt przecięcia P')
            ax.scatter(ya,xa,color=kolAB,marker='o',label='punkt A')
            ax.scatter(yb,xb,color=kolAB,marker='o',label='punkt B')
            ax.scatter(yc,xc,color=kolCD,marker='o',label='punkt C')
            ax.scatter(yd,xd,color=kolCD,marker='o',label='punkt D')
            
            ax.legend() #legenda z opisem punktów i odnicków
            self.canvas.draw()
            
    def roznica(self):
        
        xa=self.sprawdzliczbe(self.xaEdit)
        ya=self.sprawdzliczbe(self.yaEdit)
        xb=self.sprawdzliczbe(self.xbEdit)
        yb=self.sprawdzliczbe(self.ybEdit)
        xc=self.sprawdzliczbe(self.xcEdit)
        yc=self.sprawdzliczbe(self.ycEdit)
        xd=self.sprawdzliczbe(self.xdEdit)
        yd=self.sprawdzliczbe(self.ydEdit)
        
        if None not in [xa,ya,xb,yb,xc,yc,xd,yd]: #jesli funkcja sprawdzająca nie poda błędu to kontunuujemy 
            xa = float(self.xaEdit.text())
            ya = float(self.yaEdit.text())
            xb = float(self.xbEdit.text())
            yb = float(self.ybEdit.text())
            xc = float(self.xcEdit.text())
            yc = float(self.ycEdit.text())
            xd = float(self.xdEdit.text())
            yd = float(self.ydEdit.text())
        
            wynik, opis = roznica(xa,ya,xb,yb,xc,yc,xd,yd)
            print(wynik,opis)
            self.rozEdit.setText(str(wynik))
            self.opisEdit.setText(opis)
        
    
def main():
    app = QApplication(sys.argv)
    window = AppWindow()
    app.exec_()
    
if __name__ == '__main__':
    main()