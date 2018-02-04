# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 18:52:44 2017

@author: KAUSHIK

MAXNET
A MAXNET of size m with, with cluster units Y1,...,Ym is given. 
All interconnection links have an inhibitory weight of -d and all self loops have weight 1. 
The given pattern x = [x1,x2,...,xm] is to be clustered.
"""
import sys
import traceback


x=[]           #set of inputs
yout=[0]      # List of output
delta=0.2     #inhibitor weights
flag=True    #condition for while loop 

try:
   f=open('input2.txt','r')
   try:
      # pick up each line in f at a time
     for line in f:
         lines=[line.rstrip().split(',')]     
   finally:
      f.close()  #closing the file
      print(' file closed')
except IOError as e:
    traceback.print_exc()
    sys.exit(0)

m=len(lines[0])                   #number of input to the input pattern
for i in range(m):
    x.append(float(lines[0][i])) #casting the input elemnt from string to float and storing into a list
yin=x.copy()                    #copying the x input to y input yin
yout*=m                         #upgrading the list the output by m value
f=open('output2.txt','w')
while flag:                  #initially the falg is true 
    flag=False              # flag is made as float
    #computing the activation function for every input
    for i in range(len(yin)) : 
        if yin[i] > 0:
           yout[i]=yin[i]
        else:
           yout[i]=0
    if yout.count(0) != m-1:  #counting the number of zero output and checking
        flag=True             #if the number of zero output is not equal to number of input-1 then make 
                              # flag =true
        for i in range(m):       #updating the yout value
            yin[i]=yout[i]-delta*(sum(yout)-yout[i])
    f.write("updated output="+str(yout)+"\n")        
           
   #print("Y input:"+str(yin))
f.write("\nFinal y output:"+str(yout))
f.write("\nThe winner is node "+str(yout.index(max(yout))+1))        
f.close()    