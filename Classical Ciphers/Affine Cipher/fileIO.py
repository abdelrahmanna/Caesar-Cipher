# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 17:57:31 2019

@author: Abd-Elrahman
"""

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