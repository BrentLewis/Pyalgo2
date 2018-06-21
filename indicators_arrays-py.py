import numpy as np
import pandas as pd

#!!!!!Almost all the arrays need a function to pull the data in


#for that period of time. Still need to declare a function to push into the array
def Current_Gain():
        #How to pull data for that time period, and calculate current gain?
return CG.append()
CG[]

#Previous Average Gain
PAGain[]
def Average_Gain(PAGain[0], CG[0]):
    (PAGain * 13 + CG) / 14 #for a 14 day period
    return PAGain.append()


#For that period of time. Still need to declare a function to push into the array
def Current_Loss():
    #How to pull data for that time period, and calculate current loss?
return CL.append()
CL[]

#!!!!!!!!!!!!!!!!!! If Average Loss, and gain push into the array of PA loss and Gain, how does the function know to renew?


#Previous Average Loss
PALoss[]
def Average_Loss(PALoss[0], CL[0]):
    (PALoss * 13 + CL) / 14 # for a 14 day period
    return PALoss.append()

#Parameter for RSI
def RS(PAGain[0], PALoss[0]):
    PAGain / PALoss
    return RS.append()
RS[]

#Daily Closing Price
DCP[]

#For that symbol, in that period of time
def Lowest_Low(x, Lowest_L[0]):
    low = min(x) #lowest integer in x
    for Lowest_L in low:
        if Lowest_L <= x:
            low = Lowest_L
        else:
            Lowest_L = low
    return Lowest_L.append()
#Lowest_L= lowest for the look back period
Lowest_L[]

#For that symbol, in that period of time
def Highest_High(x, Highest_H[0]):
    max= max(x)#highest integer in x
    for Highest_H in max:
        if Highest_H >= max:
            max= Highest_H
        else:
            Highest_H = max
    return Highest_H.append()
# ^^^ Do I need to slice out the previous variable in Highest_H?
#Highest_H- Highest high for that look back period
Highest_H[]

RSI[]
#Loswest Low for RSI in that period of time
def Lowest_Low_RSI(RSI[], LLRSI[0]):
    Low = min(RSI) #smallest integer in RSI
    for LLRSI in low:
        if LLRSI <= low:
            low = LLRSI
        else:
            LLRSI = low
    return LLRSI.append()
LLRSI[]

#Highest High for RSI in that period of time
def Highest_high_RSI(RSI[], HHRSI[0]):
    max= max(RSI)#highest integer in RSI
    for HHRSI in max:
        if Highest_H >= max:
            max= HHRSI
        else:
            HHRSI = max
    return HHRSI.append()
# ^^^ Do I need to slice out the previous variable in HHRSI?
HHRSI[]

def K(DCP[0], Lowest_L[0], Highest_H[0]):
    (DCP - Lowest_L) / (Highest_H - Lowest_L) * 100
    return %k.append()
%k[]

def D(%k[0:2]):
    while %k >= 0:
        (%k[0] + %k[1] + %k[2]) / 3
    return %D.append()
%D[]

stochRSI[]

stochastic[]

SMA10[]