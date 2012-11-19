# Program ma za zadanie wyswietlanie zagadnienia z poprzednio wprowadzonej puli i pytania czy ma ono byc dalej w puli zagadnien. W zaleznosci od powiedzi albo wywala zagadnienie z puli, albo zachowuje i losuje kolejne 

#-*- coding: iso-8859-2 -*-
# tu wstawiamy utf-8, iso-8859-2 lub windows-1250

import random
import xlrd     #dzialanie na arkuszach
import sys
import Image    #dzialanie na obrazkach
import os   #dzialanie na systemie plikow
import subprocess

class quiz:
    def __init__(self,nazwa="Quiz 1"):
        self.nazwa_quizu=nazwa
        self.Lq=[]

    def view(self):
        random.shuffle(self.Lq)
        print "\n"
        print self.Lq[0]
        self.evalq()

    def inputq(self,pyt=0):
        if pyt == 0:
            book = xlrd.open_workbook("data.xls", encoding_override="iso-8859-2")
            sheet = book.sheets()[0]
            #data = []
            for i in xrange(sheet.nrows):
                self.Lq.append(sheet.row_values(i)[0])
        else:
            self.Lq.append(pyt)            

    def removeq(self, idq):
        del self.Lq[idq]

    def evalq(self):
        print "\n"
        odp=raw_input("Umiesz odpowiedziec (t/n):  ")
        if odp == "t":
            del self.Lq[0]
        elif odp =="n":
            print ";("
        else:
            print "mialo byc n albo t! Powtarzamy pytanie w przyszlosci."

    def show_im(self):
        diri=os.getcwd()
        nextdir=diri + "/images"
        os.chdir(nextdir)
        listi=os.listdir(os.getcwd())
      
        while(len(listi) != 0):
            #fili=random.choice(listi)
            random.shuffle(listi)
            fili=listi[0]
            im=Image.open(fili)
            im.show() 
            odp2=raw_input("Umiesz odpowiedziec (t/n): ")
            if odp2 == "t":
                print "miodzio \n"
                print fili
                del listi[0]
            elif odp2 == "n":
                print ";("
                print fili
            else:
                print "mialo byc n albo t! BRZYDKO"
        os.chdir(diri)
        
   
pyt=["jak sie masz?", "czy jest zwiazana z pozycja", "ona wted miala meza", "kto tam jest"]

chir = quiz()
chir.show_im()
#chir.inputq()
#try:
#    while(1):
#        chir.view()
#except:
#    print " \n *********KONIEC********* \n "
#    sys.exit()




