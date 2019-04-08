# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 06:32:52 2019

@author: Abd-Elrahman
"""
import math

class RailFence:
    def encryption( self, string, d):
        
        cipherText = ""
        
        for i in range(d):
            cipherText += string[i::d]      
        
        return cipherText
    def decryption( self, string, d):
        
        plainText = ""
        l = []
        n = math.ceil(len(string) / d)
        
        for i in range(d):
            if(len(string[i*n:]) >= n):
              l.append(string[i*n:i*n+n])
            else:
                l.append((string[i*n:] +  "_"*(n - len(string[i*n:]))))
                
                
        for i in range(len(l[0])):
            for j in range(len(l)):
                plainText += l[j][i] 
        
        
        return plainText.replace("_", "")


rail = RailFence()
d = rail.encryption("meetmeafterthetogaparty",3)
print(d)
e = rail.decryption(d,3)
print(e)