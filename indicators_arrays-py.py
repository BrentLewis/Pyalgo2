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
# something like this vvv for current loss? Take a mean, or subtract from high?
def Typical_price(HPrice[], LPrice[], DCP[]):
    a = (HPrice + LPrice + DCP) /3
    TPrice.append(a)
    return TPrice[]
TPrice[]

def Volume():
    #This information is mostly provided for by the exchanges.
    #Once the code to collect the data is built, it'll just need to interact with the time periods volume
    return Vol.append()
Vol[]

def Raw_Money_Flow(TPrice[], Vol[]):
    a = TPrice * Vol
    RMF.append(a)
    return RMF[]
RMF[]

def Positive_Negative_Money_Flow(TPrice[]):
    for PMF, NMF in Tprice while len(TPrice) >= 0:
        if TPrice[0] > TPrice[1]:
            PMF.append(TPrice[0])
            sum(PMF)
            TPrice.pop(0)
            return PMF[]
#will the sum(PMF/NMF) sum up the array and then push? Logically it seems so, but maybe I'm missing something
        elif TPrice[0] < TPrice[1]:
             NMF.append(TPrice[0])
             sum(NMF)
             TPrice.pop(0)
             return NMF[]
        else:
            TPrice.pop(0)
PMF[]
NMF[]

def Money_Flow_Ratio(PMF[0], NMF[0]):
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
def Daily_Closing_Price():
    return DCP[]
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
