# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 10:21:02 2017

@author: KAUSHIK
"""
import re as regex

w=[[0.2,0.3,0.2],[0.3,0.2,0.1]]
zin=[0,0]
zout=[0,0]
v=[0.5,0.5,0.5]
s=[]
t=[]
eta=0.5

lines =[line.rstrip().split('\t') for line in open('input4.txt')]
n=len(lines) 
for i in range(n):
    s.append(lines[i][0])
    t.append(int(lines[i][1]))

epoch=0
while True:
    epoch+=1
    flag=0
    for i in range(len(s)):
        x=regex.findall('[-11]+',s[i])
        for j in range(2):
            for k in range(3):
                zin[j]+=int(x[k])*w[j][k]
                if zin[j]>=0:
                    zout[j]=1
                else:
                    zout[j]=-1
        yin=1*v[0]+zout[0]*v[1]+zout[1]*v[2]
        if yin>=0 :
           yout=1
        else:
           yout=-1   
        if yout!=t[i]:
            flag=1
            if t[i]==1:
                if abs(zin[0]) < abs(zin[1]):
                    index=0
                else:
                    index=1
                for j in range(len(w[0])):
                    w[index][j]+=eta*(1-zin[index])*int(x[j])
            if t[i]==-1:
                for k in range(len(zin)):
                    if zin[k]>0:
                         for j in range(len(w[0])):
                             w[k][j]+=eta*(-1-zin[k])*int(x[j])
    if flag==0:
        print("epoch:"+str(epoch)+"\nFinal weight:\n"+str(w))
        break                  