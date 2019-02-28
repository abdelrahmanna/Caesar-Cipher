# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 19:48:28 2019

@author: Abd-Elrahman
"""
#file handeling class

from fileIO import FileIO



class CaesarCipher:
    
    
    def encrypt( self, string, step):
        incryptedString = ""
        for i in string:
            if(i.isalpha()):
                incryptedString += chr(ord('a')+((ord(i) + step - ord('a'))% 26))
            else:
                incryptedString += i
        return incryptedString
    
    def decrypt( self, string,  step):
        decryptedString = ""
        for i in string:
            if(i.isalpha()):
                decryptedString += chr(ord('a')+((ord(i) - step - ord('a'))% 26))
            else:
                decryptedString += i
        return decryptedString

#creating opjects
file  = FileIO()
cipher = CaesarCipher()

#read input
string = file.readFile("inputFile.txt")

#incrypting input with caesar cipher
istring = cipher.encrypt(string , 5)

#writing output to a file
file.writeFile("outputFile.txt", istring)

#checking the decrypt function
dstring = cipher.decrypt(istring, 5)
file.writeFile('checkDecrypt.txt', dstring)

                
        