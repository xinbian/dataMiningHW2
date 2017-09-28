#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 22:25:55 2017

@author: Xin

3.13
"""

#assume the data are stored in a dictorary
#use an example of location similar to the book
#in the dictionary attribute is key, number of distinct values is stored as
# dict value

import networkx as nx
import matplotlib.pyplot as plt
import graphviz as gv
import random
import math


G = gv.Digraph(format='svg')

#this is the nominal data
#in the dictionary attribute is key, number of distinct values is stored as
#dict value
locData={}
locData['city']=4416
locData['state/province']=1232
locData['country']=195

#sort the dict based on its value
locHie=sorted(locData.iteritems(), key=lambda d:d[1], reverse=True)
labels={}
for i in range(len(locHie)):
    G.node(locHie[i][0])
    if i>0:
        G.edge(locHie[i][0],locHie[i-1][0])


G.render('img/nominaldata')
filename = G.render(filename='img/nominaldata')




#this is for  The automatic generation of a concept hierarchy for 
#numeric data based on the equal-width partitioning rule.

#suppose data is in a list
#generate some random numbers as an example
numData=random.sample(xrange(1000), 100)
#specify how many intervals/bins
bins=5
#caluate width of each bin
width=(max(numData)-min(numData))/bins+1


#put values to bins
#store final concept hieracry in dictionary, key as bin #
numHie={}
#initilize dict
for key in range(bins):
    numHie[key]=[]
    
for i in range(len(numData)):
    key = (numData[i]-min(numData))/width
    numHie[key].append(numData[i])
    









