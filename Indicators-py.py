import numpy as np 
import pandas as pd 


#Accumulation/Distribution Line
#def ADL():

#def ADX():

#def Aroon():
 
#def CCI():
 
#def Chaikin Oscillator():
 
#def CMF():
 
#def DMI():
 
#Still need a function to go through the whole data sets
def EMA12(DCP[0], EMA12[0]):
    while len(DCP) >= 0:
        multiplier == (2 / 12 + 1)
        EMA = (DCP[] - EMA12[0]) * multiplier + EMA12[0]
       #!!! Which one?? -SMA10
       DCP[]= len(DCP) - 1
        return EMA12.append(EMA)
    return EMA12[]
#!!!!This is not the finished product. Figre out how to cycle through the previous day, and DCP, or make multiple functions.
EMA12[]

#Still need a function to go through the whole data sets

def EMA26(DCP[0], EMA26[0]):
    while len(DCP) >= 0:
        multiplier == (2 / 26 + 1)
        EMA = (DCP[0] - EMA26[0]) * multiplier + EMA26[0]
        DCP[]= len(DCP) - 1
        return EMA26.append(EMA)
    return EMA26[]
EMA26[]
#def KAMA():

#Next 3 functions are for the MACD
##Still need a function to go through the whole data sets
 def MACD_Line(EMA12[0], EMA26[0]):
    a = EMA12[0] - EMA26[0]
    return MACDL.append(a)
MACDL[]

def Signal_Line(DCP[0], MACDL[0]):
    while len(MACDL) >= 0:
        multiplier == (2 / 9 + 1)
        EMA = (DCP[0] - MACDL[0]) * multiplier + MACDL[0]
        MACDL[]= len(MACDL) - 1
        return SignalL.append(EMA)
    return SignalL[]
SignalL[]

def MACD_Histogram(MACDL[0], SignalL[0], MACDH):
    b = MACDL - SignalL
    return MACDH.append(b)
MACDH[]

#This function is supposed to combine the arrays, but they are supposed to be listed side by side, not together... it is probably the wrong way?
def MACD(MACDL[], SignalL[], MACDH[]):
    1= MACDL 
    2= SignalL
    3= MACDH
    for 1, 2, 3, in zip(1, 2, 3):
        MACD.append(1, 2, 3)
    MACD = np.array(MACD)
    return MACD[]
MACD[]
#Money Flow Index
def MoneyFI(MoneyFR[]):
    c = 100 - 100 / (1+ MoneyFR)
    MFI.append(c)
    if MFI[0] <= 100:
        return MFI[]
    else:
        print('Error in Money Flow Index')
 MFI[]
#def MMA():
 
#def Parabolic SAR():
 
def RSI(RS[0:?, RSI[]):
    while len(RS) >= 0:
       d = 100 - (100/(1+RS))
       RS[] = len(RS) - 1
       RSI.append(d)
    if RSI <= 100:
        return RSI[0]
    else:
        print('error in RSI')
    break 

#def ROC():

#how would the declaration of the array end up coming out? data points need to be formated well 

#This function is supposed to combine the arrays, but they are supposed to be listed side by side, not together... it is probably the wrong way?
def Stochastic(%D[], %K[]):
    1= %D[]
    2= %K[]
    for 1, 2 in zip(1, 2):
        Stochastic.append(1, 2)
        Stochastic = np.array(Stochastic)
        if Stochastic[0]<= 100:
            return Stochastic[]
        else:
            print('error in stochastic')
        break
Stochastic[]
# %D = 3-day SMA of %K
# %K is multiplied by 100 to move the decimal point 2 places

def StochRSI(RSI[], LLRSI[], HHRSI[]):
    while len(RSI) >= 0:
        e = (RSI - LLRSI) / (HHRSI - LLRSI)
        StochRSI.append(e)
        RSI[] = len(RSI) - 1
        if StochRSI[0] <= 100:
            return StochRSI[]
        else:
            print('error in StochRSI')
        break

#Simple moving average 10 day 
def SMA10(DCP[0:9]):
    while len(DCP) >= 0:
        f = (DCP[0]+ DCP[1] + DCP[2] + DCP[3] + DCP[4]) + DCP[5] + DCP[6] + DCP[7] + DCP[8] + DCP[9] / 10
        #!!!Which one???!! - EMA12
        SMA10.append(f)
        DCP[] = len(DCP) - 1
    return SMA10[]
   #This is not the finished product. DCP( Daily closing price) need to loop through all the data sets of the DCPes
   #figure out how to loop through, and keep the code clean. DCP[] = len(DCP) - 1 below the formula MIGHT work. Figure out if there is better alternative!!
 
#def WilliamsR():