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
        DCP[]= len(DCP) - 1
        return EMA12.append()
    return EMA12[]
#!!!!This is not the finished product. Figre out how to cycle through the previous day, and DCP, or make multiple functions.
EMA12[]

#Still need a function to go through the whole data sets

def EMA26(DCP[0], EMA26[0]):
    while len(DCP) >= 0:
        multiplier == (2 / 26 + 1)
        EMA = (DCP[0] - EMA26[0]) * multiplier + EMA26[0]
        DCP[]= len(DCP) - 1
        return EMA26.append()
    return EMA26[]
EMA26[]
#def KAMA():

#Next 3 functions are for the MACD
##Still need a function to go through the whole data sets
 def MACD_Line(EMA12[0], EMA26[0]):
    EMA12[0] - EMA26[0]
    return MACDL.append()
MACDL[]

def Signal_Line(DCP[0], MACDL[0]):
    while len(MACDL) >= 0:
        multiplier == (2 / 9 + 1)
        EMA = (DCP[0] - MACDL[0]) * multiplier + MACDL[0]
        MACDL[]= len(MACDL) - 1
        return Signal_Line.append()
    return Signal_Line[]
SignalL[]
def MACD_Histogram(MACDL[0], SignalL[0]):
    MACDL - SignalL
    return MACDH.append()
MACDH[]

#Money Flow Index
#def MFI():
 
#def MMA():
 
#def Parabolic SAR():
 
def RSI(RS[0:?]):
    while len(RS) >= 0:
       RSI = 100 - (100/(1+RS))
       #!!!Which one??! - SMA10
       RS[] = len(RS) - 1
       return RSI.append()
    return RSI[]

#def ROC():

#how would the declaration of the array end up coming out? data points need to be formated well 
def stochastic(%D[], %K[]):
    stochastic[] = %D and %K
    return stochastic.append()
# %D = 3-day SMA of %K
# %K is multiplied by 100 to move the decimal point 2 places

def stochRSI(RSI[], LLRSI[], HHRSI[]):
    while len(RSI) >= 0:
        (RSI - LLRSI) / (HHRSI - LLRSI)
        RSI[] = len(RSI) - 1
        return stochRSI.append()
    return stochRSI[]

#Simple moving average 10 day 
def SMA10(DCP[0:9]):
    while len(DCP) >= 0:
        (DCP[0]+ DCP[1] + DCP[2] + DCP[3] + DCP[4]) + DCP[5] + DCP[6] + DCP[7] + DCP[8] + DCP[9] / 10
        #!!!Which one???!! - RSI
        SMA10.append()
        DCP[] = len(DCP) - 1
    return SMA10[]
   #This is not the finished product. DCP( Daily closing price) need to loop through all the data sets of the DCPes
   #figure out how to loop through, and keep the code clean. DCP[] = len(DCP) - 1 below the formula MIGHT work. Figure out if there is better alternative!!
 
#def WilliamsR():