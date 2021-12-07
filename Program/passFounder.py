#-------------------------------------------------------------------------------
# Name:        passFounder
# Purpose:
#
# Author:      MegaByte
#
# Created:     07/12/2021
# Copyright:   (c) MegaByte 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

def Founder():
    passW = ""
    for i in range(0, 16):
        tmp = random.randint(0, 4)
        if tmp == 1:
            txt = random.randint(0, len(txt_Lower))
            passW = passW + (txt_Lower[txt])
            print(passW)
        if tmp == 2:
            txt = random.randint(0, len(txt_Upper))
            passW = passW + (txt_Upper[txt])
            print(passW)
        if tmp == 3:
            txt = random.randint(0, len(txt_Int))
            passW = passW + (txt_Int[txt])
            print(passW)
        if tmp == 4:
            txt = random.randint(0, len(txt_Symbol))
            passW = passW + (txt_Symbol[txt])
            print(passW)
    print("Your password is",passW)


txt_Lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
txt_Upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
txt_Int = ["0","1","2","3","4","5","6","7","8","9"]
txt_Symbol = ["£","$","%","^","&","*","(",")","_","-","+","=","[","]","{","}","'","@",":",";","#","~","?","|",".",","]
tmp = 0
txt = 0


Founder()




