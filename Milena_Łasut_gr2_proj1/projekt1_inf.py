# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 12:27:58 2019

@author: Admin


"""
import matplotlib.pyplot as plt
from math import sqrt


def wczyt(x):
    if x.lstrip('-').replace('.','',1).isdigit()==True:
        x1=float(x)
    else:
        print("niepoprawna forma wprowadzonych danych")    
    return x1

#XA=wczyt(input("Podaj współrzędną X punktu A:"))
#YA=wczyt(input("Podaj współrzędną Y punktu A:"))
#XB=wczyt(input("Podaj współrzędną X punktu B:"))
#YB=wczyt(input("Podaj współrzędną Y punktu B:"))
#
#XC=wczyt(input("Podaj współrzędną X punktu C:"))
#YC=wczyt(input("Podaj współrzędną Y punktu C:"))
#XD=wczyt(input("Podaj współrzędną X punktu D:"))
#YD=wczyt(input("Podaj współrzędną Y punktu D:"))

def pkt_przeciecia(XA,YA,XB,YB,XC,YC,XD,YD):
    
    if ((XB-XA)*(YD-YC)-(YB-YA)*(XD-XC))!=0:
           
        t1=((XC-XA)*(YD-YC)-(YC-YA)*(XD-XC))/((XB-XA)*(YD-YC)-(YB-YA)*(XD-XC))
        t2=((XC-XA)*(YB-YA)-(YC-YA)*(XB-XA))/((XB-XA)*(YD-YC)-(YB-YA)*(XD-XC))
        XP1=XA+t1*(XB-XA)
        YP1=YA+t1*(YB-YA)
        XP1=round(XP1,3)
        YP1=round(YP1,3)
        if t1>=0 and t1<=1:
            if t2>=0 and t2<=1:
                txt='Punkt przecięcia należy do obu odcników'
            else:
                txt='Punkt przecięcia należy tylko do odcinka AB'
        
        else:
            if t2>=0 and t2<=1:
                txt='Punkt przecięcia należy tylko do odcinka CD'
            else:
                txt='Punkt leży na przedłużeniu obu odcinków'
        
        with open('zapis.txt','w') as zapis:
            zapis.write('|{:^10s}|{:^10s}|\n'.format('X [m]','Y [m]'))
            zapis.write('|{:^10.3f}|{:^10.3f}|'.format(XP1,YP1))
            
#        plt.plot([YA,YB],[XA,XB])
#        plt.plot([YC,YD],[XC,XD])
#        plt.scatter(YP1,XP1)
        
    else:
        txt='Odcinki są równoległe. Brak punktu przecięcia'
        XP1='brak'
        YP1='brak'
    
    
    return t1, t2, XP1,YP1,txt

#wynik=pkt_przeciecia(XA,YA,XB,YB,XC,YC,XD,YD)

def roznica(xa,ya,xb,yb,xc,yc,xd,yd):
    dxAB = xb-xa #obliczanie przyrostu współrzędnych 
    dyAB = yb-ya
    dxCD = xd-xc
    dyCD = yd-yc
    
    lenAB=sqrt(dxAB**2+dyAB**2)
    lenCD=sqrt(dxCD**2+dyCD**2)
    
    roz=lenAB-lenCD
    if roz<0:
        opis='Odcinek AB jest dłuższy niż CD'
    elif roz>0:
        opis='Odcinek AB jest dłuższy niż CD'
    else:
        opis='Oba odcinki są równej długosci'
        
    wynik=abs(roz)
    wynik = round(wynik, 3)
    
    return wynik, opis
    