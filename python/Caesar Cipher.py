# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 19:48:28 2019

@author: Abd-Elrahman
"""
#file handeling class
class FileIO:
    
    def readFile( self, fileName):
        f = open( fileName,'r')
        content = f.read()
        f.close()
        return content
    
    def writeFile( self, fileName, content):
        f = open( fileName,'w')
        f.write(content)
        f.close()



class CaesarCipher:
    
    
    def incrypt( self, string, step):
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
istring = cipher.incrypt(string , 5)

#writing output to a file
file.writeFile("outputFile.txt", istring)

#checking the decrypt function
dstring = cipher.decrypt(istring, 5)
file.writeFile('checkDecrypt.txt', dstring)

                
        