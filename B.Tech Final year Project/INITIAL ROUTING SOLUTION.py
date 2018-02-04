"""
Created on Wed Jan 31 20:27:55 2018

@author: KAUSHIK
"""

"""..................... python version 3.6 ..................."""

import sys
import re


fhcg=open("output_HCG_HNCG_1.txt","w")
firs=open("output_Inital Routing Solution_1.txt","w")
fvcg=open("output_VCG_1.txt","w")
f=open("ip1.txt")
fout=open("input.txt",'w')
l=0
lequalto4=True
no_of_channel_instance=0

def IRS(no_of_channel_instance):

    #Reading input from file
    text = open("input.txt","r")    #text=input file handaler
    a = []
    for line in text:
        a.append( line.rstrip().split() )          #storing inputs line by line in a list
    a = [[int(int(j)) for j in i] for i in a]     ##converting input patterns string to int
    text.close()
    print("Given input : " , a)
    fvcg.write("\nGiven channel input :\n\n "+str(a))


    print ("\n\n.................V    C    G....................\n")
    fvcg.write("\n\n.................V    C    G....................\n")
    no_of_col=len(a[0])                         #no_of_col=number of columns in the given channel
    netlist=[[] for i in range(no_of_col)]
    for i in range(0,no_of_col):
        netlist[i].append(a[0][i])
        netlist[i].append(a[1][i])
        if a[0][i]==0 or a[1][i]==0:
            netlist[i].remove(0)                #if pin no. is 0 i.e there is no connection, then removing from the list
        if a[0][i]==a[1][i]:
            netlist[i].remove(a[1][i])          #if in same column top row pin no and bottom row pin number is same then removing from the list
#fvcg.write("a"+str(netlist))
    for i in range(no_of_col):
        if len(netlist[i])==1:
            for j in range(no_of_col):
                if j!=i and netlist[i][0] in netlist[j]:
                    netlist[i]=[0]
               
    print(netlist)
    newlist=netlist
    def zero_elemination():
        index_of_list_with_element_0_in_vcg=[]
        for i in range(len(newlist)):
            if newlist[i].__contains__(0):
               index_of_list_with_element_0_in_vcg.append(i)
        for index in sorted(index_of_list_with_element_0_in_vcg, reverse=True):
            del newlist[index]

    def empty_list_elemination():
        index_of_emplty_list_in_vcg=[]
        for i in range(len(newlist)):
            if len(newlist[i])==0:
                index_of_emplty_list_in_vcg.append(i)
        for index in sorted(index_of_emplty_list_in_vcg, reverse=True):
            del newlist[index]

    empty_list_elemination()
    zero_elemination()
    #fvcg.write("\nb"+str(newlist)) 
    print ("\n",newlist,"\nVCG is :\n")
    def vcg():
        newlist_col=len(newlist)
        for i in range(newlist_col):
            sec_index=len(newlist[i])-1
            if len(newlist[i])>1 :
                count=0
                for j in range (newlist_col):
                    if newlist[i][sec_index]==newlist[j][0]:
                        count+=1            
                for j in range (newlist_col):
                    if newlist[i][sec_index]==newlist[j][0]:
                        if count==1:
                            length_of_jlist=len(newlist[j])
                            for k in range(1,length_of_jlist):
                                newlist[i].append(newlist[j][k])
                        else:
                            temp_list=[]
                            length_of_jlist=len(newlist[j])
                            for k in range(len(newlist[i])):
                                temp_list.append(newlist[i][k])
                            for k in range(1,length_of_jlist):
                                temp_list.append(newlist[j][k])
                            newlist.append(temp_list)
                            newlist_col+=1
                        
    vcg()
    vcg()
    vcg()   #for cycle checking

    print (newlist,"\n")

    flag=0
    for i in range(len(newlist)):
        for j in range(len(newlist[i])):
            if newlist[i].count(newlist[i][j])>1:
                flag=1
                break
        
    if flag==1:
        print ("Cycle present\n\n!!!!Exiting!!!!")
        fvcg.write("\nCycle present\n\n!!!!Exiting!!!!")
        fvcg.write("\n\nVCG:\n\n")
        fvcg.write(str(newlist))
        fvcg.write("\n\nCycle in the VCG is:\n\n")
        fvcg.write(str(newlist[i]))
        fvcg.close()
        sys.exit()
    else:
        print ("Cycle is not present\n")
        fvcg.write("\nCycle is not present\n")
        fvcg.write("\n\nFinal VCG is:\n\n")
        newlist_col=len(newlist)
    
    def consecutive_checking(l1,l2):
        if len(l1)<=len(l2) and l1[0] in l2:
            k=l2.index(l1[0])
            for i in range(1,len(l1)):
                k=k+1
                if k >= len(l2):
                    return False
                if l1[i]!=l2[k]:
                   return False
            return True
        return False
            
    def sublist(lst1, lst2):
        return set(lst1) <= set(lst2)
    
    for i in range(newlist_col):
        for j in range(newlist_col):
            if i!=j and consecutive_checking(newlist[i],newlist[j]):
                sublist(newlist[i],newlist[j])
                newlist[i]=[0]
                break

    zero_elemination()
    print (newlist[0])
    fvcg.write(str(newlist[0]))
    #vmax=len(newlist[0])    
    for i in range (1,len(newlist)):
        #temp=len(newlist[i])
        #if vmax < temp:
        #vmax=temp
        if newlist[i][0]!=0:
            print(newlist[i])
            fvcg.write(str(newlist[i]))
            fvcg.write("\n")

    def finding_vmax_of_vcg(newlist):
        vmax1=len(newlist[0])
        for i in range (1,len(newlist)):
            temp=len(newlist[i])
            if vmax1 < temp:
                vmax1=temp
        return vmax1

    vmax = finding_vmax_of_vcg(newlist)
    print("\nVmax=",vmax)
    fvcg.write("\n\nVmax = "+str(vmax))
    

    fhcg.write("\nGiven input channel :\n\n "+str(a))
    #fhncg.write("\nGiven channel input :\n\n "+str(a))
    firs.write("\n************************************************************\n\n")
    firs.write("Channel ID:"+str(no_of_channel_instance)+"\n")
    firs.write("\nGiven channel instance : ")
    firs.write("\nTOP :"+str(a[0]))        
    firs.write("\nBOTTOM :"+str(a[1]))
    
    print ("\n\n...............H    C    G....................\n")
    fhcg.write("\n\n...............H    C    G....................\n")

    no_of_col=len(a[0])
    s=[set() for i in range(0,no_of_col)]
    for i in range(0,no_of_col):
        s[i].add(a[0][i])
        s[i].add(a[1][i]) 
        s[i].discard(0)
    def search(item,col):
        for k in range(col+1,no_of_col):
            if item==a[0][k] or item==a[1][k]:
                return 1                           
    j=0
    print ('\nset  0 =',s[0],'\n')
    fhcg.write("\nset 0 ="+str(s[0])+"\n")

    for i in range(1,no_of_col):

        for j in range(0,i):
 
            if a[0][j]!=0:
                t=a[0][j]
                if search(t,i):
                    s[i].add(t)                             
            if a[1][j]!=0:
                b=a[1][j]  
                if search(b,i):
                    s[i].add(b)
            
        print ("Set ",i,"=",s[i],'\n')
        fhcg.write("Set "+str(i)+"="+str(s[i])+"\n")
         
    for i in range(no_of_col):
        for j in range(i+1, no_of_col):
            if s[i].issubset(s[j]):
                s[i]={}
                break
    for i in range(-1,-(no_of_col),-1):
        for j in range(i-1,-(no_of_col),-1):
            if len(s[i])>0 and len(s[j])>0 and s[i].issubset(s[j]):
                s[i]={}
                break
    print ("Vertex set of HCG:\n")
    fhcg.write("\n\nVertex set of HCG : \n\n")

    hcg=[]
    for i in range(no_of_col):
        if len(s[i])>0 :
            hcg.append(s[i])
            print (s[i],' is a clique')
            fhcg.write(str(s[i])+' is a clique\n')

    print("HCG =",hcg) 
    fhcg.write("\n\nHCG :")
    fhcg.write(str(hcg))       
           
    def finding_dmax(s1):
        dmax1=0
        for i in range(len(s1)):
            c=len(s1[i])
            if dmax1 < c:
                dmax1=c
        return dmax1

    dmax = finding_dmax(hcg)        
    print("\n\nThe channel density (dmax) is=",dmax)   
    fhcg.write("\n\nThe channel density (dmax) is = "+str(dmax)) 
    

    print ("\n\n...............H    N    C    G....................\n\n")
    fhcg.write("\n\n\n\n...............H    N    C    G....................\n\n")

    sets={0}
 
    for i in range(no_of_col):
        if len(s[i])>0:
            sets=sets.union(s[i])
    sets.discard(0)

    hncg={} #empty dictionary for hncg 

    for i in range(len(sets)):
        item=list(sets)[i]
        temp={0}  
        for j in range(no_of_col):
            if item in s[j]:
                temp=temp.union(s[j])
        set_diff=sets.difference(temp)       
        print ("Net ",item,"will connect",set_diff)
        fhcg.write("\nNet "+str(item)+" will connect "+str(set_diff))       
        hncg[item]=list(set_diff)         

    def find_first_index(item):
        if item in a[0] and item in a[1]:
            top_index=a[0].index(item)
            bottom_index=a[1].index(item)
            return(min(top_index,bottom_index))
        elif item in a[0]:   
            top_index=a[0].index(item)
            return(top_index)
        elif item in a[1]:   
            bottom_index=a[1].index(item)
            return(bottom_index)   

    oriented_hncg={}
    oriented_hncg_key_vertices=[]       
    print("\nThe oriented HNCG is as follows:")  
    fhcg.write("\n\n\n------------------------------ORIENTED HNCG----------------------------------------------\n")
    fhcg.write("\nThe ORIENTED HNCG is as follows:")   
    for key,value in hncg.items():
        index_of_key=find_first_index(key)
        keys_value=hncg[key]
        print("\n")
        fhcg.write("\n")
        t=[] #temporary list to hold value of particular key
        for j in range(len(keys_value)):
            index_of_value=find_first_index(keys_value[j])
            if index_of_key < index_of_value:
                print("edge from vertex ",key," to vertex ",keys_value[j])
                fhcg.write("\nedge from vertex "+str(key)+" to vertex "+str(keys_value[j]))
                t.append(keys_value[j])       
                oriented_hncg[key]=t
            
    for key,value in oriented_hncg.items():
        oriented_hncg_key_vertices.append(key)

    fhcg.write("\n\nList of Vertices from those there are edges in oriented HNCG : \n\n")
    fhcg.write(str(oriented_hncg_key_vertices))
    fhcg.write("\n\nFinal oriented HNCG is :\n\n")
    fhcg.write(str(oriented_hncg))
    

    def finding_no_of_MaxDensityZone(s1):
        no_of_MaxDensityZone=0
        for i in range(len(s1)):
            count=len(s1[i])
            if count>0:
                if count==dmax:
                    no_of_MaxDensityZone=no_of_MaxDensityZone+1
        return no_of_MaxDensityZone

    maxdenszone = finding_no_of_MaxDensityZone(hcg)

    print("\n-------W  E  I  G  H  T---------C  A  L  C  U  L  A  T  I  O  N --------\n")

    def find_sum_of_ZonalDensity(i,s1):
        sum=0
        for k in range(len(s1)):
            if i in s1[k]:
                sum=sum+len(s1[k])
        return sum        

    def find_sum_of_height(i):
        sum=0
        for k in range(len(newlist)):
            if newlist[k][0]==i:
                sum=sum+len(newlist[k])
        return sum        

    def havingheightvmax(i):
        no_of_paths=0
        for k in range(len(newlist)):
            if i in newlist[k] and len(newlist[k])==vmax:
                no_of_paths=no_of_paths+1
        return no_of_paths   

    def explore(v):
    
    #print("KEY VERTICES",oriented_hncg_key_vertices)
        if v not in oriented_hncg_key_vertices:
            source_vertices_cummulative_weight[v]=source_vertices_weight[v]
     #   print("V=",v,"Cumulative weight=",source_vertices_weight[v])
            path[v]=[v]
            return
        else:
            flag=1
            adjacent_vertices=oriented_hncg[v]
            temp_source_vertices_cummulative_weight={}
            #print("adjacent vertex:",adjacent_vertices)
            for i in range(len(adjacent_vertices)):
                if adjacent_vertices[i] in source_vertices:
                        #print("explore call",adjacent_vertices[i])
                        explore(adjacent_vertices[i])
                        flag=0
                        #print("Cumulative weight",source_vertices_cummulative_weight) 
            if len(adjacent_vertices)==0 or flag==1:
                source_vertices_cummulative_weight[v]=source_vertices_weight[v]
            else:            
                for key,value in source_vertices_cummulative_weight.items():
                    if key in adjacent_vertices:
                        temp_source_vertices_cummulative_weight[key]=source_vertices_cummulative_weight[key]
                max_weight_vertex=max(temp_source_vertices_cummulative_weight, key=lambda j: source_vertices_cummulative_weight[j])            
                source_vertices_cummulative_weight[v]=source_vertices_weight[v]+source_vertices_cummulative_weight[max_weight_vertex]                
                for i in range(len(path[max_weight_vertex])):
                    path[v].append(path[max_weight_vertex][i])
            print("Cumulative weights are:",source_vertices_cummulative_weight)
            firs.write("\n\nCumulative weights are:"+str(source_vertices_cummulative_weight))
            return
 
         
    def maximum_weighted_clique(v):
        source_to_sink_path={}
        global source_vertices_cummulative_weight
        source_vertices_cummulative_weight={}
        global max_weighted_vertex
        #print("vertices are:",v)
        global path
        path={}
        for i in range(len(v)):
            path[v[i]]=[v[i]]   
        for i in range(len(v)):
            explore(v[i])
            source_to_sink_path[v[i]]=path[v[i]]
        max_weighted_vertex=max(source_vertices_cummulative_weight, key=lambda j: source_vertices_cummulative_weight[j])
        global clique
        t=source_to_sink_path[max_weighted_vertex]
        clique=[]
        for i in t:
            if i not in clique:
                clique.append(i)
        print("\nThe maximum weighted clique is:",clique)
        firs.write("\n\n\nThe maximum weighted clique is:"+str(clique))

    def remove_from_hncg_value(item):
        for key,value in oriented_hncg.items():
            if item in oriented_hncg[key]:
                oriented_hncg[key].remove(item)
            
    firs.write("\n\nInitially, dmax = "+str(dmax)+", vmax = "+str(vmax)+", No. of maximum density zone = "+str(maxdenszone))         
    zero_elemination()            
    no_of_track=0 
    net_TrackAssignment={}
    track_NetAssignment={}
    while len(newlist)!=0: 
        source_vertices=[]
        source_vertices_weight={}
        for i in range (len(newlist)):
            if newlist[i][0]>0 and newlist[i][0] not in source_vertices:
                source_vertices.append(newlist[i][0])
                source_vertices_weight[newlist[i][0]]=0
        print("\n---------\n","VCG is:",newlist)
        firs.write("\n\n\n--------------------------ITERATION----------------------------------\n\n"+"VCG is:\n\n"+str(newlist))
        print("\n\nHCG is:\n\n",str(hcg))
        firs.write("\n\nHCG is:\n\n"+str(hcg))
        firs.write("\n\ndmax = "+str(dmax)+", vmax = "+str(vmax))
        firs.write("\n\nNo. of maximum density zone = "+str(maxdenszone))
        print("\nOriented HNCG:",oriented_hncg) 
        firs.write("\n\nOriented HNCG:\n\n"+str(oriented_hncg))        
        print("\n\nSource vertices are:",source_vertices,"\n")
        firs.write("\n\nSource vertices are:"+str(source_vertices)+"\n")
    
    
        if dmax > vmax :        
            for i in range(len(source_vertices)):
                weight=0
                for j in range(len(hcg)):
                    count=len(hcg[j])
                    if count ==dmax and source_vertices[i] in hcg[j]: 
                        weight=find_sum_of_ZonalDensity(source_vertices[i],hcg)*pow(maxdenszone,2)+find_sum_of_height(source_vertices[i])                
                    elif count >0 and source_vertices[i] in hcg[j]:                  
                        weight= find_sum_of_ZonalDensity(source_vertices[i],hcg)+find_sum_of_height(source_vertices[i])
                print("\nWeight of the source vertex ",source_vertices[i],"=",weight,"\n") 
                firs.write("\nWeight of the source vertex "+str(source_vertices[i])+" = "+str(weight))
                source_vertices_weight[source_vertices[i]]=weight
        elif dmax <= vmax :
            for i in range(len(source_vertices)):
                weight=0
                no_of_paths=havingheightvmax(source_vertices[i])
                if no_of_paths > 0:              
                    weight=find_sum_of_height(source_vertices[i])*pow(no_of_paths,2)+find_sum_of_ZonalDensity(source_vertices[i],hcg)
                    # print("weight of the source vertex ",source_vertices[i],"=",weight) 
                else :
                    weight=find_sum_of_height(source_vertices[i])+find_sum_of_ZonalDensity(source_vertices[i],s)
                print("\nWeight of the source vertex ",source_vertices[i],"=",weight,"\n")
                firs.write("\nWeight of the source vertex "+str(source_vertices[i])+" = "+str(weight))
                source_vertices_weight[source_vertices[i]]=weight
    
        maximum_weighted_clique(source_vertices)  
        no_of_track+=1
        print("\nNet ",clique," is assigned to track : ",no_of_track)
        firs.write("\n\nNet "+str(clique)+" is assigned to track : "+str(no_of_track))
        track_NetAssignment[no_of_track]=clique
        for i in range(len(clique)):
            net_TrackAssignment[clique[i]]=no_of_track
        print("\nBefore deleting the maximum weighted clique's vertices from VCG",newlist) 
        firs.write("\n\n\nBefore deleting the maximum weighted clique's vertices from VCG : \n\n"+str(newlist))     
        print("\nBefore deleting the maximum weighted clique's vertices from HCG",hcg) 
        firs.write("\n\n\nBefore deleting the maximum weighted clique's vertices from HCG : \n\n"+str(hcg))
    
    
        #Removing from VCG
        for i in range(len(clique)):
            for j in range(len(newlist)):
                if clique[i] in newlist[j]:
                    newlist[j].remove(clique[i])
        print("\nAfter deleteing source vertices from VCG:")
        print(newlist)
           
        zero_elemination()       
        empty_list_elemination() 
        print("after deleting empty list and 0 element set:")
        print(newlist)
    
        #Finding sublist and removing     
        index_of_sublist=[]          
        for j in range(len(newlist)):
            for k in range(j+1,len(newlist)):
                if set(newlist[j]).issubset(set(newlist[k])) or set(newlist[k]).issubset(set(newlist[j])):
                    if len(newlist[j]) <= len(newlist[k]):
                        index_of_sublist.append(j)
                    elif len(newlist[k]) <= len(newlist[j]):
                        index_of_sublist.append(k) 
        print("Index of sublist",index_of_sublist)
        index_of_sublist=set(index_of_sublist)
        for index in sorted(index_of_sublist, reverse=True):
            del newlist[index] 
        print("\nAfter deleting the maximum weighted clique's vertices from VCG:")
        firs.write("\n\n\n\nAfter deleting the maximum weighted clique's vertices from VCG :\n\n")
        print(newlist)
        firs.write(str(newlist))
        print()
        firs.write("\n")
        
        #updated vmax from new vcg
        if(len(newlist)>0):
            vmax = finding_vmax_of_vcg(newlist)
            firs.write("\nNew vmax = "+str(vmax))
            firs.write("\n")
    
        #removing from HCG
        for i in range(len(clique)):
            for j in range(len(hcg)):
                if clique[i] in hcg[j]:
                    hcg[j].remove(clique[i])
  
        for i in range(len(hcg)):
            for j in range(i+1, len(hcg)):
                if set(hcg[i]).issubset(set(hcg[j])):
                    hcg[i]={}
                    break
        for i in range(-1,-(len(hcg)),-1):
            for j in range(i-1,-(len(hcg)),-1):
                if len(hcg[i])>0 and len(hcg[j])>0 and hcg[i].issubset(set(hcg[j])):
                    hcg[i]={}
                    break
    
        print("\nAfter deleteing source vertices from HCG:")
        print(hcg)
        firs.write("\n\n\nAfter deleting source vertices from HCG:\n\n")
        firs.write(str(hcg))
      
        #updated dmax from new hcg
        dmax = finding_dmax(hcg)
        maxdenszone = finding_no_of_MaxDensityZone(hcg)
        firs.write("\n\nNew dmax = "+str(dmax)+"\n\n")
        firs.write("\nNew no. of maximum density zones = "+str(maxdenszone)+"\n")
    
        #Removing from oriented hncg  
        for i in range(len(clique)):
            if clique[i] not in oriented_hncg_key_vertices: 
                remove_from_hncg_value(clique[i])
         
            else:
                del oriented_hncg[clique[i]]
                remove_from_hncg_value(clique[i])    
        print("\nAfter net assignment to track Oriented HNCG:")
        firs.write("\n\n\nAfter net assignment to track Oriented HNCG : \n\n")
        print(oriented_hncg)               
        firs.write(str(oriented_hncg))


    firs.write("\n\n\n\nFINALLY NUMBER OF TRACKS REQUIRED = "+str(no_of_track))

    """...........................Wire length calculation..........................."""
    firs.write("\n\n\n................................................Counting Wirelength...........................................\n\n")
    total_vertical_wirelength=0   
    total_horizontal_wirelength=0
    net_span={}
    
    for key,value in net_TrackAssignment.items():
        firs.write("\n")
        #vertical wirelength calculation
        vertical_wirelength=0
        no_of_wire_above_track=a[0].count(key)*value
        no_of_wire_below_track=a[1].count(key)*(no_of_track+1-value)
        vertical_wirelength=no_of_wire_above_track+no_of_wire_below_track
    
        print("vertical length for ",key," = ",vertical_wirelength)
        firs.write("\n\nVertical wirelength for "+str(key)+" = "+str(vertical_wirelength))
    
        total_vertical_wirelength+=vertical_wirelength
    
        #horizontal wirelength calculation
        horizontal_wirelength=0
        nets_index=set()
        if(key in a[0]):
            lowest_index_from_top_vector=a[0].index(key)
            highest_index_from_top_vector=len(a[0])-1-a[0][ ::-1].index(key)
            nets_index.add(lowest_index_from_top_vector)
            nets_index.add(highest_index_from_top_vector)
        
        if(key in a[1]):
            lowest_index_from_bottom_vector=a[1].index(key)
            highest_index_from_bottom_vector=len(a[1])-1-a[1][ ::-1].index(key)
            nets_index.add(lowest_index_from_bottom_vector)
            nets_index.add(highest_index_from_bottom_vector)
    
        nets_index=list(nets_index)
        nets_index.sort()
        #print(nets_index)
        temp=set()
        for i in range(nets_index[0],nets_index[len(nets_index)-1]+1):
            temp.add(i)
        net_span[key]=temp  #It will be used for calculating horizontal crosstalk
        horizontal_wirelength=nets_index[len(nets_index)-1]-nets_index[0]
        print("horizontal length for ",key," = ",horizontal_wirelength)
        firs.write("\n\nHorizontal wirelength for "+str(key)+" = "+str(horizontal_wirelength))
        total_horizontal_wirelength+= horizontal_wirelength
    
    print("\nTotal horizontal wirelength=",total_horizontal_wirelength)
    print("\nTotal vertical wirelength=",total_vertical_wirelength) 
    firs.write("\n\n\nTotal Horizontal Wirelength = "+str(total_horizontal_wirelength))
    firs.write("\n\n\nTotal Vertical Wirelength = "+str(total_vertical_wirelength))
        
    """.......................Calculation of horizontal crosstalk..........................."""
    t={}
    
    horizontal_crosstalk=0
    for key,value in track_NetAssignment.items():
        if key< no_of_track:
         #print("Track=",key)
             for first_track_item in track_NetAssignment[key]:
                 for second_track_item in track_NetAssignment[key+1]:
                     t=net_span[first_track_item].intersection(net_span[second_track_item])
                     if len(t)>0:
                         horizontal_crosstalk+=len(t)-1
                         #       print(t)
    print("\nHorizontal Crosstalk is=",horizontal_crosstalk)
    firs.write("\n\nHorizontal Crosstalk is="+str(horizontal_crosstalk))
                      
    """.......................Calculation of vertical crosstalk..........................."""
    vertical_crosstalk=0
    for i in range(len(a[0])-1):
        
        first_set_of_track_top_net=set()
        second_set_of_track_top_net=set()
    
        first_set_of_track_bottom_net=set()
        second_set_of_track_bottom_net=set()
    
        first_track_of_top_net=0
        first_track_of_bottom_net=0
        second_track_of_top_net=0
        second_track_of_bottom_net=0
        
        if a[0][i] !=0:
            first_track_of_top_net=net_TrackAssignment[a[0][i]]
            for j in range(0,first_track_of_top_net+1):
                first_set_of_track_top_net.add(j)
        if a[1][i] !=0:
            first_track_of_bottom_net=net_TrackAssignment[a[1][i]]
            for j in range(first_track_of_bottom_net,no_of_track+2):
                first_set_of_track_bottom_net.add(j)   
        if a[0][i+1] !=0:
            second_track_of_top_net=net_TrackAssignment[a[0][i+1]]
            for j in range(0,second_track_of_top_net+1):
                second_set_of_track_top_net.add(j) 
        if a[1][i+1] !=0:
            second_track_of_bottom_net=net_TrackAssignment[a[1][i+1]]
            for j in range(second_track_of_bottom_net,no_of_track+2):
                second_set_of_track_bottom_net.add(j)
   
        if a[0][i]!=a[0][i+1]:   
            temp1=first_set_of_track_top_net.intersection(second_set_of_track_top_net)
            #print("\n")
            #print(i)
            #print(temp1)
            if len(temp1)!=0:
               vertical_crosstalk+=(len(temp1)-1)
               temp1=set()  
        temp2=first_set_of_track_top_net.intersection(second_set_of_track_bottom_net)
        #print(temp2)
        if len(temp2)!=0:
            vertical_crosstalk+=(len(temp2)-1)
            temp2=set()
   
        temp3=first_set_of_track_bottom_net.intersection(second_set_of_track_top_net)
        #print(temp3)
        if len(temp3)!=0:
            vertical_crosstalk+=(len(temp3)-1)
            temp3=set()
        if a[1][i]!=a[1][i+1]: 
            temp4=first_set_of_track_bottom_net.intersection(second_set_of_track_bottom_net)
            #print(temp4)
            if len(temp4)!=0:
                vertical_crosstalk+=(len(temp4)-1)
                temp4=set()     
           
    print("\nVertical crosstalk=",vertical_crosstalk)            
    firs.write("\n\nVertical Crosstalk is="+str(vertical_crosstalk))

for line in f:
     l+=1
     if lequalto4==True :
        fout=open("input.txt",'w')
        lequalto4=False
     numbers = re.findall(r"[-+]?\d*\.\d+|\d+", line)
     if len(numbers)>1:
         for i in range(len(numbers)):
             fout.write(str(numbers[i])+" ")
         fout.write("\n")
     if l==4:
        l=0 
        fout.close() 
        lequalto4=True
        no_of_channel_instance+=1
        IRS(no_of_channel_instance)

f.close()
firs.write("\n\nCOMPLETE")            
firs.close() 
fvcg.close()
fhcg.close()
print("\nCOMPLETE")               