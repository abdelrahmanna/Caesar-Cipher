# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:56:45 2019

@author: Abd-Elrahman
"""


import numpy as np
import itertools as itr
class PlayFair:
    
    
    def encrypt( self, string, Matrix):
        
        incryptedString = ""
        string = string.replace(" ", "")
        
        string = self.removeRepeatedChr(string)
        
        #making sure the string is of even length
        if(len(string) % 2 != 0): 
            string = string + "x"
            
        #dividing the string into 
        string = np.reshape(np.array(list(string)), (-1,2))
        for i in string:
            
            a = i[0]
            b = i[1]
            indexa =  list(zip(*np.where(a == Matrix)))[0]
            indexb =  list(zip(*np.where(b == Matrix)))[0]
                       
            if(indexa[0] == indexb[0]):
                if(indexa[0] == len(Matrix[0])):
                    indexa[0] = -1
                    indexb[1] = 0
                incryptedString += Matrix[ indexa[0] + 1, indexa[1]] 
                incryptedString += Matrix[ indexb[0] + 1, indexb[1]]
            elif(indexa[1] == indexb[1]):
                if(indexa[0] == len(Matrix[0])):
                    indexb[0] = -1
                    indexa[1] = 0
                incryptedString += Matrix[ indexa[0], indexa[1] + 1] 
                incryptedString += Matrix[ indexb[0],indexb[1] + 1]
            else:
                incryptedString += Matrix[ indexa[0], indexb[1]] 
                incryptedString += Matrix[ indexb[0], indexa[1]]
                
        return incryptedString
    
    def decrypt( self, string,  Matrix):
        
        decryptedString = ""
        string = string.replace(" ", "")
        
        string = self.removeRepeatedChr(string)
        
        if(len(string) % 2 != 0): 
            string = string + "x"
            
        string = np.reshape(np.array(list(string)), (-1,2))
        
        for i in string:
            
            a = i[0]
            b = i[1]
            indexa =  list(zip(*np.where(a == Matrix)))[0]
            indexb =  list(zip(*np.where(b == Matrix)))[0]
           # print(indexa[0],a,indexb[0],b
            
            if(indexa[0] == indexb[0]):
                decryptedString += Matrix[ indexa[0] - 1, indexa[1]] 
                incryptedString += Matrix[ indexb[0] - 1, indexb[1]]
            elif(indexa[1] == indexb[1]):
                decryptedString += Matrix[ indexa[0], indexa[1] - 1] 
                decryptedString += Matrix[ indexb[0],indexb[1] - 1]
            else:
                decryptedString += Matrix[ indexa[0], indexb[1]] 
                decryptedString += Matrix[ indexb[0], indexa[1]]
        return decryptedString

    def generateMatrix( self, string = ''):
        alphabet = 'abcdefghiklmnopqrstuvwxyz'
        if (string != ''):
            string = string.replace('j','i').strip(' ')
            string = ''.join(ch for ch, _ in itr.groupby(string))
            
            for i in string:
                alphabet = alphabet.replace(str(i),'')
            alphabet = string + alphabet
            
            alphabet = np.reshape(np.array(list(alphabet)), (5,5))
            return alphabet
        return alphabet
    
    def removeRepeatedChr( self, string):
        
        for i in range(1,len(string)):
            if(string[i-1] == string[i]):
               string = string[:i]+'x'+string[i+1:]
            
        return string

cipher = PlayFair()
m = cipher.generateMatrix('monarchy')

print(cipher.encrypt("hammer", m))
print(cipher.decrypt(cipher.encrypt("hammer", m),m))