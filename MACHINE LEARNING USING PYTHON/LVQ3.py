# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 19:43:38 2017
@author: KAUSHIK


                            LEARNING VECTOR QUANTIZATION(LVQ)
                          ------------------------------------
'''
'''
Algorithm LVQ-learning
There are p-number of m-dimensional training patterns s1, s2, ..., sp, and n number of clusters C1, C2, ..., Cn. 
The training set consists of the pairs (s1,t1), (s2,t2), ..., (sp,tp) where the pair (si,ti) indicates that the pattern si 
belongs to cluster ti belongs to { C1, C2, ..., Cn }. We have to make an ( m-input n-output ) LVQ net learn these training sets.
'''
'''
The code only trains the neural network and updates weights. The application of the trained network to unknown 
input sets is done in another program.
'''
# ---------------------------------------------------------------------------------------------------------------------
'''
Step 0: Initialize
		i) The weight matrix, i.e., w(i,j) for all i and j. A simple technique is to select one training vector from 
			each known cluster and assign them directly to the columns of the weight matrix so that each of them becomes
			a code vector. Rest of the input patterns are used for training.
		ii) The learning rate n.
Step 1: While stopping condition is not satisfied Do Step 2 to Step 7.

Step 2: For each input training vector s Do steps 3 to Step 5.

Step 3: Find the distance D(j) of s from each exemplar / code vector W(*,j).
				D(j) = SUM { ( x(i) - w(i,j) ) ^ 2 } for i  = 1, ..., m.

Step 4: Find the index J for which D(J) is minimum.

Step 5: Update code-vector W(*,J).
						If t == C(J) Then /* bring C(J) closer to s */
							w(*,J)(new) = w(*,J)(old) + n * [ s - w(*,J)(old) ]
						Else /* take C(J) away from s */
							w(*,J)(new) = w(*,J)(old) - n * [ s - w(*,J)(old) ]

Step 6: Reduce the learning rate, n = k * n, 0 < k < 1.

Step 7: Test for stopping condition.

'''
"""                          
    

import re as regex
import sys
import traceback

w=[0]      #list for weight matrix
s=[]       #list for input pattern
t=[]       #list for true output value
l=[0]      # list to hold the the selected input pattern for weight matrix 
d=[0]      # list is used to hold the value of euclidian distance
cluster_out=[0]   #output cluster
eta=0.2       #learning rate
k=0.5        # k value is used to reduce the eta value


try:
   f=open('input3.txt','r')
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
file=open("output3.txt",'w')
file.write("Given set of input pattern:\n"+str(s)+"\n\nGiven true output value: "+str(t))
p=len(s)                      # p be the number of trainig patterns                                   
x= regex.findall('[01]+',s[0])
no_of_clusters=len(set(t))              # number of clusters                                
m=len(x)                               #  m be the number of dimension of input
wcol=no_of_clusters                   # wcol be the number of column in weight matrix i.e. the number of clusters
l*=wcol             # upgrading the column of list l by wcol
w*=wcol             # upgrading the column of list w by wcol
d*=no_of_clusters   # upgrading the column of list d by no_of_clusters 
cluster_out*=p     # upgrading the column of list cluster_out by p 

# Taking the selected input pattern which will be used as weight matrix

for i in range(wcol):
    l[i]=int(input("Number "+str(i+1)+ " input pattern that will be used as weight:"))-1
    w[i]= regex.findall('[01]+',s[l[i]])
    cluster_out[l[i]]=t[l[i]]

#converting the string value of weight matrix to integer value
    
for i in range(len(w)):
    for j in range(len(w[0])):
        w[i][j]=int(w[i][j])

file.write("\n\nInitial weight"+str(w)+"\n")

epoch=0
while True:
    epoch+=1
    file.write("\nepoch="+str(epoch)+"\n\n")
    for i in range(p): # for each input pattern do the following step
        if i not in l:  # checking for the pattern is in list of weight matrix or not
            x= regex.findall('[01]+',s[i])  #extracting each input pattern 
            file.write("\nInput pattern:"+str(i+1)+" "+str(x)+"\n")
            # calcuting the eucledian distance 
            for j in range(no_of_clusters):     #for every cluster  
                sumation=0
                for k in range(m):            # for every input 
                    sumation+=pow((int(x[k])-int(w[j][k])),2)     #evaluate the eucledian distance
                    d[j]=sumation
                file.write("\nEcludian distance for D"+str(j)+"="+str(d[j]))
            cluster=d.index(min(d))+1      #choosing the index of minimum valued distance 
            file.write("\n\nEvaluated cluster=minimum of D value="+str(cluster))
           # if i==1 and epoch==1:
            #    cluster=2
            cluster_out[i]=cluster
            #checking the true output cluster and evaluated cluster
            if t[i]==cluster:  #if both the clusters are same
                for k in range(m):
                    w[cluster-1][k]+=eta*(int(x[k])-w[cluster-1][k])   #update the weight of the evaluated cluster 
                file.write("\n\nUpdated weight:"+str(w)+"\n")    
            else:             #if both the clusters are not same
                 for k in range(m):
                    w[cluster-1][k]-=eta*(int(x[k])-w[cluster-1][k]) #update the weight of the evaluated cluster 
                 file.write("\n\nUpdated weight:"+str(w)+"\n")    
    file.write("\n\nAfter epoch "+str(epoch)+" Given true output cluster :"+str(t)+" Evaluated output cluster :"+
               str(cluster_out))
    #checking for both the list true output cluster value and evaluated cluster value
    f=0
    for k in range(p):
        # if any one cluster is not matched then set flag value f to 1 and reduce the learning rate eta
        if t[k]!=cluster_out[k]:
           f=1
           eta*=k
           break
       
    if f==0:
        file.write ("\n\nvalue matched:'\n\n'Total no. of epoch:"+str(epoch)+"\nFinal weight= "+str(w))
        break
file.close()                       