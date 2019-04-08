# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 01:28:39 2019

@author: Abd-Elrahman
"""
from itertools import permutations
import numpy as np
class Vigenere:
    
    
    def encrypt( self, string, key):
        """
        the encription is done using 
        ['abcdefghijklmnopqrstuvwxyz',
         'bcdefghijklmnopqrstuvwxyza',
         'cdefghijklmnopqrstuvwxyzab',
         'defghijklmnopqrstuvwxyzabc',
         'efghijklmnopqrstuvwxyzabcd',
         'fghijklmnopqrstuvwxyzabcde',
         'ghijklmnopqrstuvwxyzabcdef',
         'hijklmnopqrstuvwxyzabcdefg',
         'ijklmnopqrstuvwxyzabcdefgh',
         'jklmnopqrstuvwxyzabcdefghi', 
         'klmnopqrstuvwxyzabcdefghij',
         'lmnopqrstuvwxyzabcdefghijk',
         'mnopqrstuvwxyzabcdefghijkl',
         'nopqrstuvwxyzabcdefghijklm',
         'opqrstuvwxyzabcdefghijklmn',
         'pqrstuvwxyzabcdefghijklmno',
         'qrstuvwxyzabcdefghijklmnop', 
         'rstuvwxyzabcdefghijklmnopq', 
         'stuvwxyzabcdefghijklmnopqr',
         'tuvwxyzabcdefghijklmnopqrs', 
         'uvwxyzabcdefghijklmnopqrst',
         'vwxyzabcdefghijklmnopqrstu',
         'wxyzabcdefghijklmnopqrstuv',
         'xyzabcdefghijklmnopqrstuvw',
         'yzabcdefghijklmnopqrstuvwx',
         'zabcdefghijklmnopqrstuvwxy']
        as a shifting reference where a leter of the key referes to the position of the the string and the corresponding leter of 
        the plain text referes to the posiotion of a character in that string 
        """
        encryptedString = ""
        
        #creating the table
        table = self.getTablue()
        
        #creatiing a dictionary with the alphabet characters as keys and indices as values
        dic = self.alphaDict()
        
        
        string = string.replace(" ","")
        
        #elongating the key incase it's shorter than the plain text
        if(len(key) != len(string)):
            key = self.createKey(string, key)
        
        #creating the cipher text
        for i in range(len(string)):
            encryptedString += table[dic[key[i]]][dic[string[i]]]
            
        return encryptedString
    
    def decrypt( self, string,  key):
        """
        the decryption follows simpller way of emplementation but they both are the same concept 
        we simply subtract the charcter and get thier remainder
        """
        decryptedString = ""
        string = string.replace(" ","")
        
        #elongating the key incase it's shorter than the plain text
        if(len(key) != len(string)):
            key = self.createKey(string, key)
            
        #creating the plain text
        for i in range(len(string)):
            decryptedString += chr(ord('a') + (ord(string[i]) - ord(key[i])) % 26)
        return decryptedString

    
    def getTablue(self):
        """
        creating the alphabet table that we use in encrypt function
        """
        
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        table= [] 
        
        for i in range(26):
            alpha =alpha[-1:] + alpha[:-1]
            table.insert( 0, alpha)
            
        return table
    
    def alphaDict(self):
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        n = range(26)
        return dict(zip(alpha,n))
    
    def elongateKey( self, string, key):
        """
        this function make the key longer by repeating it to match the length of the plain and cipher texts
        """
        key2 = [key[i % len(key)] for i in range(len(string))]
        return key2
        

Vigenere = Vigenere()
t = Vigenere.encrypt('wearediscoveredsaveyourself', 'deceptive')
d = Vigenere.decrypt(t,'deceptivedeceptivedeceptive')
print(t)
print(d)