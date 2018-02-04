# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 10:31:35 2018
@author: KAUSHIK

                      ADALINE
                     --------- 
Algorithm:
=========    
    Step 1: Initialize all the weights W[0], ..., W[num_of_input_unit].
    Step 2: Set learning rate such that 0 < learning_rate <= 1
    Step 3: For each training pair s:t do the following
    Step 4:   Activate the input units, x[i]=s[i], for i=0, ..., num_of_input_unit
    Step 5: Compute net input to the output unit
                  y_in = sum(W[i] * X[i]) for i=0, ..., num_of_input_unit
    Step 6: Compute the activation of output unit using the following function
               y_out = {    1, if y_in >=0
                         or -1 if y_in < 0  
                       }
    Step 7: then adjust the weights as follows
                    W[i] = wold+(learning_rate *( t-y_in) * x[i])
                
    Step 8: if there were no error, i.e., y_out = t for the entire set of training pair,
                then stop
            otherwise continue with the next iteration

"""
import re as regex
import sys
import traceback

s=[] # list of set of given input pattern
t=[]  # list of output of given input pattern
w=[0.25]  #list of weight
yout=[0] #list for evaluated output
eta=0.2 #learning rate

try:
   f=open('input7.txt','r')
   try:
      # pick up each line in f at a time
     for line in f:
         lines=[line.rstrip().split('\t')] 
         s.append(lines[0][0])   # pushing the each input pattern to the list
         t.append(int(lines[0][1]))  # Inserting the corresponding true output value of each input pattern
   finally:
      f.close()
      print(' file closed')
except IOError as e:
    traceback.print_exc()
    sys.exit(0)

n=len(s)  # n be the number of s:t input
x= regex.findall('[-11]+',s[0]) #extracting one input from set of input pattern
m=len(x) #evaluating the number of input 
w*=m     #upgradin the column of list of the weight matrix by the number of input(m)
yout*=n   #upgradin the column of list of the output matrix by the number of input pattern s:t (n)
epoch=0   #used to hold number of epoch 
flag=True #flag is using as condition of while loop
file=open('output7.txt','w')
while flag:
    flag=False   
    epoch+=1       #increamenting epoch value
    #for each input pattern do the following step
    file.write("\n\nepoch="+str(epoch)+"\n")
    for i in range(n):
        x= regex.findall('[-11]+',s[i])  #Extracting each input pattern s
        yin=0
        #calculating the net input
        for j in range(m):
            yin+=int(x[j])*w[j]
        #upgrading the weight matrix   
        for j in range(m):
            w[j]+=eta*(t[i]-yin)*int(x[j])
        file.write("\nweight matrix:\n"+str(w)+"\n")       
    #Extracting each input pattern of s  
    for i in range(n):
        x= regex.findall('[-11]+',s[i])  #extracting each input pattern from the set of pattern s
        yin=0 
        #evaluating net input value yin
        for j in range(m):
            yin+=int(x[j])*w[j]
        file.write("\nyin:\n"+str(yin)+"\n")    
        #determining yout value from net input    
        if yin >=0:
            yout[i]=1
        else:
            yout[i]=-1
        file.write("\nyout:\n"+str(yout)+"\n")  
    #checking for true output value and evaluated output value
    for i in range(n):
        #if both the values do not match the  set the flag to true to continue the next epoch
        if yout[i]!=t[i]:     
            flag=True
file.write("\n\n\nepoch="+str(epoch)+"\nFinal weight matrix\n"+str(w))            
file.close()