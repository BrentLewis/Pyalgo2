import pandas as pd 
import numpy as np 

#Accumulation/Distribution Line
#def ADL():

#def ADX():

#def Aroon():
 
#def CCI():
 
#def Chaikin Oscillator():
 
#def CMF():
 
#def DMI():
 
#Still need a function to go through the whole data sets
def EMA12(DCP[], EMA12[]):
    while len(DCP) >= 0:
        multiplier == (2 / 12 + 1)
        EMA = (DCP[0] - EMA12[0]) * multiplier + EMA12[0]
       #!!! Which one?? -SMA10
       DCP[] = DCP.pop(0)
       EMA12[] = EMA12.pop(0)
        return EMA12.append(EMA)
    return EMA12[]
#!!!!This is not the finished product. Figre out how to cycle through the previous day, and DCP, or make multiple functions.
EMA12[]

# .pop() Is close.. But it still won't cycle through the whole data set.. no? 
# create seperate array in the function to isolate data and then merge the array with EMA12/26?

#Simple moving average 10 day 
def SMA10(DCP[]):
    while len(DCP) >= 0:
        f = (DCP[0]+ DCP[1] + DCP[2] + DCP[3] + DCP[4]) + DCP[5] + DCP[6] + DCP[7] + DCP[8] + DCP[9] / 10
        #!!!Which one???!! - EMA12
        SMA10.append(f)
        DCP[] = DCP.pop(0)
        #The .pop() will stay localized to the function, no?
    return SMA10[]
SMA10[]
   #This is not the finished product. DCP( Daily closing price) need to loop through all the data sets of the DCPes
   #figure out how to loop through, and keep the code clean. DCP[] = len(DCP) - 1 below the formula MIGHT work. Figure out if there is better alternative!!


def EMA26(DCP[], EMA26[]):
    while len(DCP) >= 0:
        multiplier == (2 / 26 + 1)
        EMA = (DCP[0] - EMA26[0]) * multiplier + EMA26[0]
        DCP[] = DCP.pop(0)
        EMA26[] = EMA26.pop(0)
        return EMA26.append(EMA)
    return EMA26[]
EMA26[]
#def KAMA():

#Next 3 functions are for the MACD
##Still need a function to go through the whole data sets
 def MACD_Line(EMA12[], EMA26[]):
     while len(EMA12) and len(EMA26) >= 0:
         a = EMA12[0] - EMA26[0]
         EMA12.pop(0)
         EMA26.pop(0)
         MACDL.append(a)
    return MACDL[]
MACDL[]

def Signal_Line(DCP[], MACDL[]):
    while len(MACDL) >= 0:
        multiplier == (2 / 9 + 1)
        EMA = (DCP[0] - MACDL[0]) * multiplier + MACDL[0]
        DCP.pop(0)
        MACDL.pop(0)
        SignalL.append(EMA)
        print signalL[]
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
        ValueError('Error in Money Flow Index')
 MFI[]
#def MMA():
 
#def Parabolic SAR():
 
def RSI(RS[], RSI[]):
    while len(RS) >= 0:
       d = 100 - (100/(1+RS))
       RS[] = RSI.pop(0)
       RSI.append(d)
    if RSI >= 0 and  <= 100:
        return RSI[0]
    else:
        ValueError('Error in RSI') 
RSI[]

#def ROC():

#how would the declaration of the array end up coming out? data points need to be formated well 

#This function is supposed to combine the arrays, but they are supposed to be listed side by side, not together... it is probably the wrong way?
def Stochastic(%D[], %K[]):
    1= %D[]
    2= %K[]
    for 1, 2 in zip(1, 2):
        Stochastic.append(1, 2)
        Stochastic = np.array(Stochastic)
        if Stochastic[0] >= 0 and <= 100:
            return Stochastic[]
        else:
            ValueError('error in stochastic')
Stochastic[]

# %D = 3-day SMA of %K
# %K is multiplied by 100 to move the decimal point 2 places

def StochRSI(RSI[], LLRSI[], HHRSI[]):
    while len(RSI) >= 0:
        e = (RSI[0] - LLRSI) / (HHRSI - LLRSI)
        StochRSI.append(e)
        RSI[] = RSI.pop(0)
        if StochRSI[0] >= 0 and  <= 100:
            return StochRSI[]
        else:
            ValueError('error in StochRSI')

StochRSI[]
 
#def WilliamsR():