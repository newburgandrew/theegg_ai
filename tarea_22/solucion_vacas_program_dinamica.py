#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 18:54:58 2021

@author:Jayant Verma en  https://www.askpython.com/author/jayant
acomodadoal caso por alberto-mac
"""

val = [40,35,43,28,12,13]
wt = [360,250,400,180,50,90]
W = 700


def knapSack(W, wt, val): 
    n=len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)] 
 
    for i in range(n + 1): 
        for j in range(W + 1): 
            if i == 0 or j == 0: 
                table[i][j] = 0
            elif wt[i-1] <= j: 
                table[i][j] = max(val[i-1] + table[i-1][j-wt[i-1]], table[i-1][j]) 
            else: 
                table[i][j] = table[i-1][j] 
   
    return table[n][W] 

print("La combinación óptima lograría:", knapSack(W, wt, val), "litros")
## T(n)=3+1+6n+6n+3n2+1
## O(n2)
## cuadrática