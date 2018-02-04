# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 08:45:11 2017
@author: KAUSHIK

                  P E R C E P T R O N    L E A R N I N G 
                 ---------------------  ------------------
  
Algorithm:
=========    
    Step 1: Initialize all the weights W[0], ..., W[num_of_input_unit].
            Here all the weights are fetched from a file.
    Step 2: Set learning rate such that 0 < learning_rate <= 1 and threshold.
    Step 3: For each training pair s:t do the following
    Step 4:   Activate the input units, x[i]=s[i], for i=0, ..., num_of_input_unit
    Step 5: Compute net input to the output unit
                  y_in = sum(W[i] * X[i]) for i=0, ..., num_of_input_unit
    Step 6: Compute the activation of output unit using the following function
               y_out = {    1, if y_in > threshold
                         or -1 if y_in < -threshold  
                         or 0,if -threshold <= y_in <= threshold }
    Step 7: If there is an error, i.e., y_out != t, then adjust the weights
                as follows
                    W[i] += (learning_rate * t * x[i])
                If no error has occurred, the weights are kept unchanged.
    Step 8: if there were no error, i.e., y_out = t for the entire set of training pair,
                then stop
            otherwise continue with the next iteration

"""

import re as regex
import traceback
import sys

w=[0]      # list of weights; initially initialized by zero  
yout=[0]   # list of output calculated using activation function from net input yin
t=[]       # list of output of given input pattern                                         
s=[]       # list of set of given input pattern
yin=0      # stores the value of net input calculated from weight and given input
eta=1      # learning rate
theta=1    # bias value
flag=True  # flag variable for while loop   


try:
   f=open('input1.txt','r')
   try:
      # pick up each line in f at a time
     for line in f:
         lines=[line.rstrip().split('\t')] 
         s.append(lines[0][0])   # pushing the each input pattern to the list
         t.append(lines[0][1])  # Inserting the corresponding true output value of each input pattern
   finally:
      f.close()
      print(' file closed')
except IOError as e:
    traceback.print_exc()
    sys.exit(0)

n=len(s)     # n be the number of s:t input pattern
yout*=n      # creating the size of the list as per number of input pattern
try:
   x= regex.findall('[-11]+',s[0])
except IOError as e:
    traceback.print_exc()
    print("Input is not in proper format")
    sys.exit(0)
   
m=len(x)    # m be the number of input                                                       
w*=m       # creating the size of the list as per number of input
f=open('output1.txt','w')    
count=1   # Tracks the number of epoch                
while flag:
    flag=False
    f.write("\nepoch: "+str(count)+"\n") 
    for i in range(m):
        try:
           x= regex.findall('[-11]+',s[i])      # Extracting each input pattern from the set  
        except IOError as e:
            traceback.print_exc()
            print("Input is not in proper format")
            sys.exit(0)
        f.write("x input:"+str(x)+"\n")    
        f.write(str("Y input:"+str(yin)+"\n"))
        yin=0
         # calculating net input
        for j in range(len(x)):
            yin+=int(x[j])*w[j] 
        # evaluating output value from net input     
        if yin > theta :
            yout[i]=1
        elif yin < (-1*theta):
            yout[i]=-1
        else:
            yout[i]=0
        f.write("Y output:"+str(yout[i])+"\n")    
        f.write("True output t:"+str(t[i])+"\n")
        # If given true output value and evaluated output value both are mismatchd
        # Then update the weight
        if yout[i] != int(t[i]):
            for j in range(m):
                wold=w[j]
                w[j]=wold+eta*int(x[j])* int(t[i])
                flag=True
        f.write("Updated weight: "+str(w)+"\n\n")
    count+=1
f.write("Final weight is :"+str(w)+"\n")    
f.close()
