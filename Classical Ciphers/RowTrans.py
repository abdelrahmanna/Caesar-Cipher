# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 07:52:45 2019

@author: Abd-Elrahman
"""
import numpy as np

class RowTrans:
    def encryption( self, string, key):
        cipherText = ""
        
        #checking the validity of the key
        if(len(list(set(key))) < len(key)):
            raise Exception("the key is not valide")
            
        #adding xs to the text in case it does not divisible by the length of the key to be able to turn it into matrix later
        while(len(string)%len(key) != 0):
            string += "x"
            
        #turn the text into numpy array
        string = np.asarray(list(string))
        
        #reshping the array into matrinx
        string = np.reshape(string,(-1, len(key)))
        
        #creating the cipher text
        for i in range(len(key)):
            cipherText += ''.join(string[:,key.find(str(i+1))])    
        return cipherText.replace(" ", "")
    
    def decryption( self, string, key):
        plainText = ""
        
        #checking the validity of the key
        if(len(list(set(key))) < len(key)):
            raise Exception("the key is not valide")
            
        #adding xs to the text in case it does not divisible by the length of the key to be able to turn it into matrix later        
        while(len(string)%len(key) != 0):
            string += " "

        #turn the text into numpy array
        string = np.asarray(list(string))
        
        #reshping the array into matrinx
        string = np.reshape(string,(-1, len(key)))
        
        l = []
        
        #rearrenging the rows of the string matrix
        for i in key:
            l.append(string[int(i)-1,:])
        
        
        l = np.array([np.array(x) for x in l]).transpose()
        
        #creating the plain text
        for i in l:
            plainText += ''.join(i)
        return plainText.replace(" " , "")

row = RowTrans()
d = row.encryption("attackpostponed","4312567")
print(d)
print(row.decryption(d,"4312567"))
