# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 11:27:08 2017

@author: KAUSHIK
"""
import re as regex

s=[]
w=[]
d=[0]
eta=0.8
k=0.5

lines =[line.rstrip().split('\t') for line in open('input5.txt')]
n=len(lines)
for i in range(n):
    s.append(lines[i][0])
    
p=len(s)
x=regex.findall('[0-1]+',s[0])
m=len(x)
  
lines =[line.rstrip().split('\t') for line in open('weight.txt')]
n=len(lines)

for i in range(n):
    w.append(lines[i][0]) 
y=regex.findall("\d+\.\d+",w[i])    
number_of_output=len(y)
weight_matrix = [[0 for x in range(number_of_output)] for y in range(n)]    

for i in range(n):
    y=regex.findall("\d+\.\d+",w[i]) 
    for j in range(number_of_output):
        weight_matrix[i][j]=float(y[j])
epoch=0
d*=number_of_output
while epoch<20:
    epoch+=1 
    for i in range(len(s)):
        x=regex.findall('[0-1]+',s[i])
        for j in range(len(d)):
            d[j]=0
            for k in range(n):
                d[j]+=pow((int(x[k])-weight_matrix[k][j]),2)
        index=d.index(min(d))
        print("i="+str(i)+" index="+str(index))
        for j in range(n):
            weight_matrix[j][index]+=eta*(int(x[j])-weight_matrix[j][index])
        print(weight_matrix)
    eta*=k   
print("\n\nFinal weight matrix:\n"+str(weight_matrix))            