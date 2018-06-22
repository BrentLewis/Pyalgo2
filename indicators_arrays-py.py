import numpy as np
import pandas as pd

#!!!!!Almost all the arrays need a function to pull the data in


#for that period of time. Still need to declare a function to push into the array
def Current_Gain():
        #How to pull data for that time period, and calculate current gain?
return CG.append()
CG[]


#For that period of time. Still need to declare a function to push into the array
def Current_Loss():
    #How to pull data for that time period, and calculate current loss?
return CL.append()
CL[]

#unctions for MFI
def High_Price():
    return HPrice.append()
HPrice[]

def Low_Price():
    return LPrice.append()
LPrice[]

def Typical_price(HPrice[], LPrice[], DCP[]):
    a = (HPrice + LPrice + DCP) /3
    TPrice.append(a)
    return TPrice[]
TPrice[]

def Volume():
    return Vol.append()
Vol[]

def Raw_Money_Flow(TPrice[], Vol[]):
    a = TPrice * Vol
    RMF.append(a)
    return RMF[]
RMF[]

def Positive_Negative_Money_Flow(Tprice[]):
    for PMF, NMF in Tprice:
        if TPrice[a] > TPrice[b]:
            PMF.append(TPrice[a])
            sum(PMF)
            return PMF[]
        #I feel this combination doesn't work. How to add the variable to the array inside the function, then sum the array, and push the result to PMF/NMF
        elif TPrice[a] < TPrice[b]:
             NMF.append(TPrice[a])
             sum(NMF)
             return NMF[]
        else:
            'Do nothing'
        break
    break
PMF[]
NMF[]

def Money_Flow_Ratio(PMF[], NMF[]):
    b = PMF / NMF
    MoneyFR.append(b)
    return MoneyFR[]
MoneyFR[]
#end array/function group for MFI


#!!!!!!!!!!!!!!!!!! If Average Loss, and gain push into the array of PA loss and Gain, how does the function know to renew?

#Previous Average Gain
PAGain[]
def Average_Gain(PAGain[0], CG[0]):
    c = (PAGain * 13 + CG) / 14 #for a 14 day period
    PAGain.append(c)
    return PAGain[]

#Previous Average Loss
PALoss[]
def Average_Loss(PALoss[0], CL[0]):
    d = (PALoss * 13 + CL) / 14 # for a 14 day period
    PALoss.append(d)
    return PALoss[]

#Parameter for RSI
def RS(PAGain[0], PALoss[0]):
    e = PAGain / PALoss
    RS.append(e)
    return RS[]
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
    return Lowest_L.append(low)
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
    return Highest_H.append(max)
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
    return LLRSI.append(low)
LLRSI[]

#Highest High for RSI in that period of time
def Highest_high_RSI(RSI[], HHRSI[0]):
    max= max(RSI)#highest integer in RSI
    for HHRSI in max:
        if Highest_H >= max:
            max= HHRSI
        else:
            HHRSI = max
    return HHRSI.append(max)
# ^^^ Do I need to slice out the previous variable in HHRSI?
HHRSI[]

def K(DCP[0], Lowest_L[0], Highest_H[0]):
    f = (DCP - Lowest_L) / (Highest_H - Lowest_L) * 100
    %K.append(f)
    return %K[]
%K[]

def D(%k[0:2]):
    while len(%k) >= 0:
        g = (%K[0] + %K[1] + %K[2]) / 3
        len(%K) - 1
        %D.append(g)
    return %D[]
%D[]

stochRSI[]

stochastic[]

SMA10[]