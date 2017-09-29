#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#This file cotains codes I used in the HW#

#3.13 code is in the last, it requires graphviz, please install that before running#

import matplotlib.pyplot as plt
import graphviz as gv
import random
import pandas as pd
import numpy as np


# =============================================================================
# #3.3
# =============================================================================

age=[13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]
len(age)

#smooth by bin average

for i in range(0, len(age), 3):
    print float((age[i]+age[i+1]+age[i+2]))/3

df = pd.DataFrame(age, columns=['age'])
df.plot()
df.plot.hist(bins=5)
plt.savefig('33hist.eps',format='eps', dpi=600)

df.plot()
df.plot.box()
plt.savefig('33box.eps', format='eps', dpi=600)

# =============================================================================
# #3.7
# =============================================================================
#calculate age mean
np.mean(age)

# =============================================================================
# #3.10
# =============================================================================
df.plot()
df.plot.hist(bins=10)
plt.savefig('37hist.eps',format='eps', dpi=600)

# =============================================================================
# #3.11
# =============================================================================
age



# =============================================================================
# 3.13
# =============================================================================

# =============================================================================
# (a) this is for the nominal data
# assume the data is stored in a dictorary
# =============================================================================

#use an example of location similar to the book's
#in the dictionary attribute is key, number of distinct values is stored as
# dict value

locData={}
locData['city']=4416
locData['state/province']=1232
locData['country']=195

#sort the dict based on its value
locHie=sorted(locData.iteritems(), key=lambda d:d[1], reverse=True)

#we can show this in a directed graph
G = gv.Digraph(format='svg')  
for i in range(len(locHie)):
    G.node(locHie[i][0])
    if i>0:
        G.edge(locHie[i][0],locHie[i-1][0])      
#save hierarchy in a graph
G.render('img/nominaldata')


# =============================================================================
# (b)
# this is for  The automatic generation of a concept hierarchy for 
# numeric data based on the equal-width partitioning rule.
# 
# =============================================================================

#suppose data is in a list
#generate some random numbers as an example
numData=random.sample(xrange(1000), 100)
#specify how many intervals/bins
bins=5
#caluate width of each bin
width=(max(numData)-min(numData))/bins+1


#store values in bins
#store final concept hieracry in dictionary, key as bin #
numHie={}
#initilize dict
for key in range(bins):
    numHie[key]=[]
    
for i in range(len(numData)):
    key = (numData[i]-min(numData))/width
    numHie[key].append(numData[i])


#save hierarchy in a graph
#since the direction is not specified in the exercise, just use one as example,
#I'll put largest values on the root 
#name the node by its value range [ , )
    
G = gv.Digraph(format='svg')  
for i in range(0,len(numHie)):
    nodeCurrent='['+str(min(numData)+i*width)+','+str(min(numData)+(i+1)*width)+')'
    G.node(nodeCurrent)
    if i>0:
        G.edge(nodeCurrent, nodeLast)
    nodeLast = nodeCurrent
G.render('img/numerical_euqalpartition')


# =============================================================================
# (c)this is for  The automatic generation of a concept hierarchy for 
#  numeric data based on the equal-frequency partitioning rule.
# =============================================================================

#suppose data is in a list
#generate some random numbers as an example
numData=random.sample(xrange(1000), 100)
#specify how many intervals/bins
bins=10
#caluate frequency of each bin
freq=len(numData)/bins
#store values to bins
#store final concept hieracry in dictionary, key as bin #
numHie={}
#initilize dict
for key in range(bins):
    numHie[key]=[]
    
numData=sorted(numData)
#put values to bins
flag=0
for i in numData:
    key = flag/freq
    numHie[key].append(i)
    flag += 1

#save hierarchy in a graph
#since the direction is not specified in the exercise, just use one as example,
#I'll put largest values on the root 
#name the node by its value range [ , ]
    
G = gv.Digraph(format='svg')
for i in range(0,len(numHie)):
    nodeCurrent ='['+str(numHie[i][0])+','+str(numHie[i][freq-1])+']'
    G.node(nodeCurrent)
    if i>0:
        G.edge(nodeCurrent, nodeLast)
    nodeLast = nodeCurrent
G.render('img/numerical_freq')





