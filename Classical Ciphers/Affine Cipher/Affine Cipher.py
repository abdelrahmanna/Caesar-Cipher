# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 17:52:05 2019

@author: Abd-Elrahman
"""

from fileIO import FileIO

class AffineCipher:
    
    
    def encrypt( self, string, k, p):
        incryptedString = ""
        for i in string:
            if(i.isalpha()):
                incryptedString += chr(ord('a')+((p*(ord(i)  - ord('a')) + k)% 26))
            else:
                incryptedString += i
        return incryptedString
    
    
    def decrypt( self, string, k, p):
        decryptedString = ""
        for i in string:
            if(i.isalpha()):
                decryptedString += chr(ord('a')+(int((ord(i)  - ord('a') - k)/p)% 26))
            else:
                decryptedString += i
        return decryptedString

file  = FileIO()
cipher = AffineCipher()

file.writeFile( "inputFile.txt", "hello, world!!")
#read input
string = file.readFile("inputFile.txt")

#incrypting input with caesar cipher
istring = cipher.encrypt(string , 1, 3)

#writing output to a file
file.writeFile("outputFile.txt", istring)

#checking the decrypt function
dstring = cipher.decrypt(istring, 1, 3)
file.writeFile('checkDecrypt.txt', dstring)