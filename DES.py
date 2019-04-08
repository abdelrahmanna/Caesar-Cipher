# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 19:24:06 2019

@author: Abd-Elrahman
"""
#choose test
test = 2

if (test == 1):
     theKey = "133457799BBCDFF1"#the encryption  and decryption key
     theMsg = "0123456789ABCDEF"#massege to be encryption
     theExp = "85E813540F0AB405"#expected cipher text
elif (test == 2):
     theKey = "38627974656B6579"#the encryption  and decryption key
     theMsg = "6D6573736167652E"#massege to be encryption
     theExp = "7CF45E129445D451"#expected cipher text
     
     
def generateSubKeys(key):  

    """Generates the 16 subkeys from the key

    Parameters
    ----------
    the 64-bit key used for encryption and decryption


    Returns
    -------
    list of 16 56-bit keys 
    """
    
    
    key = bin(int(key, 16))[2:].zfill(8)
    while(len(key) < 64):
        key = '0'+key
        
    #the first permutation matrix
    PC1 = [[57, 49, 41, 33, 25, 17, 9],
          [1, 58, 50, 42, 34, 26, 18],
          [10, 2, 59, 51, 43, 35, 27],
          [19, 11, 3, 60, 52, 44, 36],
          [63, 55, 47, 39, 31, 23, 15],
          [7, 62, 54, 46, 38, 30, 22],
          [14, 6, 61, 53, 45, 37, 29],
          [21, 13, 5, 28, 20, 12, 4]]
    
    #applyng the permutation matrix
    key56 = ''
    for i in range(8):
        for j in range(7):
            key56 += key[PC1[i][j]-1]
            
    #deviding the 56-bit key into two parts left and right        
    l0 = key56[:28]
    r0 = key56[28:]

    #creating the 16 keys
    leftShiftArray = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    lkeys = [l0[leftShiftArray[0]:]+ l0[:leftShiftArray[0]]] 
    rkeys = [r0[leftShiftArray[0]:] + r0[:leftShiftArray[0]]]
    for i in range(1,16):
        lkeys.append(lkeys[i-1][leftShiftArray[i]:] + lkeys[i-1][:leftShiftArray[i]])
        rkeys.append(rkeys[i-1][leftShiftArray[i]:] + rkeys[i-1][:leftShiftArray[i]])
    
    keys = []
    for i in range(16):
        keys.append(lkeys[i]+rkeys[i])
    
    #applyring Second permutation matrix
    PC2 = [[14, 17, 11, 24, 1, 5],
           [3, 28, 15, 6, 21, 10],
           [23, 19, 12, 4, 26, 8],
           [16, 7, 27, 20, 13, 2],
           [41, 52, 31, 37, 47, 55],
           [30, 40, 51, 45, 33, 48],
           [44, 49, 39, 56, 34, 53],
           [46, 42, 50, 36, 29, 32]]
    
    
    permkeys = []
    for k in range(16):
        bitString= ""
        for i in range(8):
            for j in range(6):
                bitString += keys[k][PC2[i][j]-1]
        permkeys.append(bitString)
    
    return permkeys

def encrypt(msg, keys):
    """Generates cipher text
    Parameters
    ----------
    the massege to be encrypted and the 16 subkeys


    Returns
    -------
    cipher text
    """
    return des(msg, keys, True)

def decrypt(msg, keys):
    
    """Generates cipher text
    Parameters
    ----------
    the massege to be decrypted and the 16 subkeys


    Returns
    -------
    plain text
    """
    return des(msg, keys, False)

def des(message, keys,flag):
    
    """applies the des algorthm to generate the ciphre or plain text 
    Parameters
    ----------
    the massege to be decrypted or encrypted, the 16 subkeys and boolean flag to determen the process (encryption or decryption)


    Returns
    -------
    a string containing either plain text or cipher text
    """
    #convert message into bit string
    message = bin(int(message, 16))[2:].zfill(8)
    while(len(message) < 64):
        message = '0'+message
    
    #switch to decryption if choosed
    if(not flag):
        keys = keys[::-1]

    
    #initial permutation matrix
    IP = [[58, 50, 42, 34, 26, 18, 10, 2],
         [60, 52, 44, 36, 28, 20, 12, 4],
         [62, 54, 46, 38, 30, 22, 14, 6],
         [64, 56, 48, 40, 32, 24, 16, 8],
         [57, 49, 41, 33, 25, 17, 9, 1],
         [59, 51, 43, 35, 27, 19, 11, 3],
         [61, 53, 45, 37, 29, 21, 13, 5],
         [63, 55, 47, 39, 31, 23, 15, 7]]
    
    #inverse permution matrix
    IPinv = [[40, 8, 48, 16, 56, 24, 64, 32],
            [39, 7, 47, 15, 55, 23, 63, 31],
            [38, 6, 46, 14, 54, 22, 62, 30],
            [37, 5, 45, 13, 53, 21, 61, 29],
            [36, 4, 44, 12, 52, 20, 60, 28],
            [35, 3, 43, 11, 51, 19, 59, 27],
            [34, 2, 42, 10, 50, 18, 58, 26],
            [33, 1, 41, 9, 49, 17, 57, 25]]
    
    #appling IP to message
    permMess = ""
    for i in range(8):
        for j in range(8):
            permMess += message[IP[i][j]-1]
    # message to lift and right
    l0 = permMess[:32]
    r0 = permMess[32:]
    l = [l0]
    r = [r0]
    
    for i in range(1,17):
        l.append(r[i-1])
        r.append(xor(l[i-1],fun(r[i-1], keys[i-1])))
    
    #creating the final text
    rl = r[-1]+l[-1]
    result =''
    for i in range(8):
        for j in range(8):
            result += rl[IPinv[i][j]-1]  
    
    result = hex(int(result,2))[2:]
    return result.upper()

def fun( right, key):
    """applies the function f(R_n, K_n)
    Parameters
    ----------
    the value of L_n-1 + f(R_n-1, k_n-1) where R_0 is the right half of the plain text, and the nth key


    Returns
    -------
    32 bit string
    """
    #expanding the message
    expantion = [[32, 1, 2, 3, 4, 5],
                [4, 5, 6, 7, 8, 9],
                [8, 9, 10, 11, 12, 13],
                [12, 13, 14, 15, 16, 17],
                [16, 17, 18, 19, 20, 21],
                [20, 21, 22, 23, 24, 25],
                [24, 25, 26, 27, 28, 29],
                [28, 29, 30, 31, 32, 1]]
    
    exRight = ""
    for i in range(8):
        for j in range(6):
            exRight += right[expantion[i][j] - 1]
        
        
    #applynig xor between the message and the key
    exRight = xor(exRight, key)
    
    #applyin the x-boxes on the message
    exRight = applySboxes(exRight)
    p = [[16, 7, 20, 21],
        [29, 12, 28, 17],
        [1, 15, 23, 26],
        [5, 18, 31, 10],
        [2, 8, 24, 14],
        [32, 27, 3, 9],
        [19, 13, 30, 6],
        [22, 11, 4, 25]]
    

    result = "";
    for i in range(8):
        for j in range(4):
            result += exRight[p[i][j] - 1]

    return result

def applySboxes(string):
    """applies the sboxes to a key 
    Parameters
    ----------
    48 bit key


    Returns
    -------
    a 32 bit string
    """
    parts =[]
    rows = []
    col = []
    for i in range(8):
        parts.append(string[i*6:(i+1)*6])
        rows.append(parts[i][0]+parts[i][-1])
        col.append(parts[i][1:-1])
        
    sBoxes = [
            #sbox 1
            [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
             [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
             [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
             [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
             
             #sbox 2
             [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
              [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
              [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
              [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
              
             #sbox 3
             [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
              [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
              [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
              [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
              
             #sbox 4
             [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
              [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
              [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
              [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
              
             #sbox 5
             [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
              [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
              [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
              [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
              
            #sbox 6  
            [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
             [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
             [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
             [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
            #sbox 7
            [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
             [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
             [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
             [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
             
            #sbox 8
            [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
             [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
             [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
             [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
            ]
    holder = ""
    s = ""
    for i in range(8):
        s += bin(sBoxes[i][int(rows[i],2)][int(col[i],2)])[2:].zfill(4)
           
        while(len(s) % 4 != 0 and len(s) < 4 or s== ""):
             s = '0'+s
        holder += s
        s = ''

    return holder
    

    
def xor( s1, s2):
    """xor over two bit strings
    Parameters
    ----------
    two bit strings s1,s2


    Returns
    -------
    a string contains the xor of s1,s2
    """
    if(len(s1) != len(s2)):
        raise Exception("can't apply xor function on non-equal strings")
    s0 = ""
    for i in range(len(s1)):
        if(s1[i] == s2[i]):
            s0 += '0'
        else:
            s0 += '1'
    return s0

#calling the functions
subKeys = generateSubKeys(theKey)
theCph = encrypt(theMsg, subKeys)
thePlain = decrypt(theCph, subKeys)

#print the output 
print("Key     : " + theKey)
print("Message : " + theMsg)
print("Cipher  : " + theCph)
print("Expected: " + theExp)
print("Plain   : " + thePlain)