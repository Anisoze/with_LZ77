import symbol
import sys
import os
from tkinter import W
import turtle



def ask(num1,num2):
    while(True):
        f=(input())
        if(len(f)==0 or ord(f)<ord(str(num1)) or ord(f)>ord(str(num2))):
            print("\nwrong input\n")
        else:
            return int(f)


def ask_block():
    while(True):
        f=input()
        try:
            f=int(f)
        except:
            print("\nwrong input\n")
        else:
            if(f<1):
                print("\nwrong input\n")
            else:
                return f






def probability_Huffman(data, rd, b):          #probability_Huffman
    
    if(rd==False):  #count
        dictionary=[]
        if(b):              #bytes
            
            sr=bytearray()
            i=0
            for i in data:
                if(sr.count(i) == 0):
                    k=data.count(i)
                    dictionary.append((i, k))
                    sr.append(i)
                    
       
        dictionary.sort(key=lambda x: (x[1], x[0]))
  



    print(dictionary)
    return dictionary








def Huffman():
    
    name="out_LZ77.txt"
    name2="out_Huffman.txt"
    

    b=True
    file=open(name, "rb")

    file2=open(name2, "wb")
    
    data=file.read()
    data2=bytearray()
    dictionary=probability_Huffman(data, False, b)

    
    A=list(list(zip(*dictionary))[1])
    
    #формирование внутренних узлов

    s=0
    r=0
    n=len(A)
    for t in range(n-1):
        #выбираем первый узел потомок
        if((s>n-1) or (r<t and A[r]<A[s])):
            #выбираем внутренний узел
            A[t]=A[r]
            A[r]=t+1
            r+=1
        else:
            #выбираем лист
            A[t]=A[s]
            s+=1
            
        #выбираем втором потомок
        if((s>n-1) or (r<t and A[r]<A[s])):
            #внутренний
            A[t]=A[t]+A[r]
            A[r]=t+1
            r+=1
        else:
            #лист
            A[t]=A[t]+A[s]
            s+=1


    #преобразование индексов родительских узлов в значения глубин каждого узла
    A[n-1]=-1
    A[n-2]=0
    t=n-2
    while(t>-1):
        A[t]=A[A[t]-1]+1
        t-=1
        
    #преобразование значения глубины внутренних узлов в значения глубины листьев (длин кодов)
    a=0
    u=0
    d=0
    t=n-2
    x=n-1
    while(True):
        #определяем количество узлов с глубиной d
        while(t>=0 and A[t]==d):
            u+=1
            t-=1
        #назначаем листьями узлы, которые не являются внутренними
        while(a>u):
            A[x]=d
            x-=1
            a-=1
        #переходми к следующему значению глубины
        a=2*u
        d+=1
        u=0
        if(a<=0):
            break
        
    print(A)
    
    Dt={}

       
    m=[0 for i in range(n)]          #подсчитываем число символов с одинаковой длиной кода
    Base=[0 for i in range(A[0]+1)]
    
    for i in range(n):
        m[A[i]]=m[A[i]]+1

        #вычисляем значение base для каждой длины кода
    s=0
    for k in range(A[0],0,-1):
        Base[k]=s>>(A[0]-k)
        s=s+(m[k]<<(A[0]-k))

        #вычисляем коды для каждого символа входного алфавита
    p=0
    B=[0 for i in range(n)]
    for i in range(n):
        if(p!=A[i]):
            j=0
            p=A[i]
        B[i]=j+Base[A[i]]
        j+=1

        
    print('')
    sr=""

    
    if(b):
        for i in range(n):
            b_=bin(B[i])[2:]
            sr+=str(dictionary[i][0])+' '+(A[i]-len(b_))*'0'+b_+'\n'
            Dt[dictionary[i][0]]=(A[i]-len(b_))*'0'+b_
   

    print(sr)
    file3=open("dictionary_Haffman.txt", "w", encoding="utf=8")
    file3.write(sr)



    sr=""
    for i in data:
        sr+=Dt[i]
    i=0
    s=""
    k=0
    for i in sr:
        s+=i
        k+=1
        if(k==8):
            data2.append(int('0b'+s,2))
            s=""   
            k=0
    if(len(s)>0):       
        data2.append(int('0b'+s,2))
    data2.append(len(s))
      
    file2.write(data2)
    file.close()
    file2.close()
    file3.close()
    
    








def decode_Huffman():

    name="back_Huffman.txt"
    
    bt=True
    file2=open(name,"wb")
    data2=bytearray()
    file=open("out_Huffman.txt","rb")
    file3=open("dictionary_Haffman.txt","r", encoding="utf-8")
    data=file.read()
    data3=file3.read()

    if(bt):         #bytes
        sym=""
        sr=""
        Dt={}
        i=0
        while(i<len(data3)):
            while(data3[i]!=' '):
                sym+=data3[i]
                i+=1
            i+=1            
            while(i<len(data3) and data3[i]!='\n'):
                sr+=data3[i]
                i+=1
            Dt[sr]=int(sym)
            sym=""
            i+=1
            sr=""
    
        sr=""
        i=0
        q=data[-1]
        while(i<len(data)-1):
            b=bin(data[i])[2:]
            if(len(b)<8 and i!=len(data)-2):
                b=(8-len(b))*'0'+b  
            if(i!=len(data)-2):
                for j in b:
                    sr+=j
                    if(sr in Dt):
                        data2.append(Dt[sr])
                        sr=""
            else:
                if(len(b)<q):
                    b=(q-len(b))*'0'+b
                for j in b:
                    sr+=j
                    if(sr in Dt):
                        data2.append(Dt[sr])
                        sr=""
            i+=1        



    file2.write(data2)
    file.close()
    file2.close()
    file3.close()
                
    
    




def LZ77():                                         #LZ77
    print("\nchoose open:\n1 - in_LZ77.txt\n2 - enwik8\n3 - other\n")
    f2=ask(1,3)
    if(f2==1):
        name="in_LZ77.txt"
    elif(f2==2):
        name="enwik8"
    elif(f2==3):
        print("\nenter name\n")
        name=input()
    

    name2="out_LZ77.txt"       
    file=open(name, "rb")
    file2=open(name2, "wb")
        

    mode=1
    data=file.read()
    if(mode==1):
        data2=bytearray()
        data3=bytearray()

        
    print("\nenter buffer size\n")
    while(True):
        buff_size=ask_block()
        if(buff_size>32767):
            print("\nchoose a smaller buffer (max 32767)\n")
        else:
            break
    buff=""
    list_of_turples=[]
    i=0
    k=0
    q=0
    dt=bytearray()

    while(i<len(data)):
        buff=data[max(i-buff_size,0):i]
        L=0
        start=len(buff)
        while(True):
            s=data[i:i+L+1]
            if(buff.find(s)>=0 and i+L < len(data)):
                start=buff.find(s)
                L+=1
            else:
                break
            
        if(mode==1):    #use bytes
            if(L>0):        #turple
                if(q>0):        #single not empty
                    data2.append(int('0b'+bin(q|128)[2:],2))
                    q=0
                    for j in data3:
                        data2.append(j)
                    data3=bytearray()
                elif(k==127):                               #out of range
                    data2.append(int('0b'+bin(k)[2:],2))
                    for j in list_of_turples:
                        if(j[0]>127):                            #takes 2 bytes  
                            y=j[0].to_bytes(2, "big")
                            data2.append(int.from_bytes(y[0:1], byteorder="big"))
                            data2.append(int.from_bytes(y[1:2], byteorder="big"))
                        else:                                       #takes 1 byte
                            data2.append(int('0b'+bin(j[0]|128)[2:],2))
                        if(j[1]>127):                              
                            y=j[1].to_bytes(2, "big")
                            data2.append(int.from_bytes(y[0:1], byteorder="big"))
                            data2.append(int.from_bytes(y[1:2], byteorder="big"))
                        else:
                            data2.append(int('0b'+bin(j[1]|128)[2:],2))
                    k=0
                    list_of_turples=[]
                substring_turple=(len(buff)-start,L)
                list_of_turples.append(substring_turple)
                i+=L-1
                k+=1
            


            else:       #single
                if(k>0):        #turple not empty
                    data2.append(int('0b'+bin(k)[2:],2))
                    for j in list_of_turples:
                        if(j[0]>127):                            #takes 2 bytes  
                            y=j[0].to_bytes(2, "big")
                            data2.append(int.from_bytes(y[0:1], byteorder="big"))
                            data2.append(int.from_bytes(y[1:2], byteorder="big"))                           
                        else:                                       #takes 1 byte
                            data2.append(int('0b'+bin(j[0]|128)[2:],2))
                        if(j[1]>127):                              
                            y=j[1].to_bytes(2, "big")
                            data2.append(int.from_bytes(y[0:1], byteorder="big"))
                            data2.append(int.from_bytes(y[1:2], byteorder="big"))
                        else:
                            data2.append(int('0b'+bin(j[1]|128)[2:],2))
                    k=0
                    list_of_turples=[]
                elif(q==127):           #out of range
                    data2.append(int('0b'+bin(q|128)[2:],2))
                    q=0
                    for j in data3:
                        data2.append(i)
                    data3=bytearray()
                q+=1
                data3.append(data[i])
            i+=1
            

            

    if(mode==1):    #bytes
        if(k>0):        #left turple
            data2.append(int('0b'+bin(k)[2:],2))
            for j in list_of_turples:
                if(j[0]>127):                            #takes 2 bytes  
                    y=j[0].to_bytes(2, "big")
                    data2.append(int.from_bytes(y[0:1], byteorder="big"))
                    data2.append(int.from_bytes(y[1:2], byteorder="big"))
                    dt.append(int.from_bytes(y[0:1], byteorder="big"))
                    dt.append(int.from_bytes(y[1:2], byteorder="big"))
                else:                                       #takes 1 byte
                    data2.append(int('0b'+bin(j[0]|128)[2:],2))
                if(j[1]>127):                              
                    y=j[0].to_bytes(2, "big")
                    data2.append(int.from_bytes(y[0:1], byteorder="big"))
                    data2.append(int.from_bytes(y[1:2], byteorder="big"))
                else:
                    data2.append(int('0b'+bin(j[1]|128)[2:],2))
        else:       #left single
            data2.append(int('0b'+bin(q|128)[2:],2))
            for j in data3:
                data2.append(j)
    
    
    file2.write(data2)
    file.close()
    file2.close()


















def decode_LZ77():                  #decode LZ77

    mode=1
    print("\nchoose open:\n1 - back_Huffman.txt\n2 - other\n")
    f2=ask(1,2)
    if(f2==1):
        name="back_Huffman.txt"
    elif(f2==2):
        print("\nenter name\n")
        name=input()

    name2="back_LZ77.txt"     
    file=open(name, "rb")
    file2=open(name2, "wb")
   
    
    data=file.read()
    data2=bytearray()

    
    i=0
    if(mode==1):        #with bytes
        while(i<len(data)):
            if((data[i]>>7) & 1 == 0):       #turple
                k=data[i]
                i+=1
                for j in range(k):
                    if((data[i]>>7) &1 == 1):       #takes 1 byte
                        shift=data[i]&127
                        i+=1
                    else:       #takes 2 bytes
                        shift=data[i]<<8
                        i+=1
                        shift+=data[i]
                        i+=1
                        
                    if((data[i]>>7) &1 == 1):      
                        L=data[i]&127
                    else:    
                        L=data[i]<<8
                        i+=1
                        L+=data[i]
                    dt=data2.copy()
                    p=1
                    while(True):
                        data2.append(dt[-1-shift+p])
                        yy=dt[-1-shift+p]
                        p+=1
                        if(p>L):
                            break
                    i+=1
                
            else:           #single
                k=data[i]&127
                i+=1
                for j in range(k):               
                    data2.append(data[i])
                    i+=1
                    

    
           


    file2.write(data2)
    file.close()
    file2.close()


























from PIL import Image           #start
from io import BytesIO
import numpy as np
from decimal import Decimal
import math



f=0
f2=0
p=False
sign=0
while(True):        #main cycle    
    print("\nchoose action:\n1 - use LZ77+Huffman\n2 - decode LZ77+Huffman\n9 - exit program\n")   #main options
    f = ask(1,3)
    print("")



    if(f==1):
        LZ77()
        Huffman()




    elif(f==2):     #decode
        decode_Huffman()
        decode_LZ77()




    elif(f==3):     #exit program       
        break
    
