import numpy as np

def PoissonEffError(k,N):
    """k=eff*N --> N: total events, k: passed events, eff:efficiency of the cut(s)"""
    if N==0: print "Total number of events is zero"
    print "Efficiency is:", float(k)/N, "+-", np.sqrt(((float(k)**2)*(N+k))/(N**3))

def BinomialEffError(k,N):
    """k=eff*N --> N: total events, k: passed events, eff:efficiency of the cut(s)"""
    if N==0: print "Total number of events is zero"
    print "Efficiency is:", float(k)*100/N, "+-", (1/N)*np.sqrt(k*(1-(k/N)))*100

def DivE(x,y,dx,dy):
    if x!=0 and y!=0: return (x/y)*((dx/x)+(dy/y))
    else: return 0.0

def MulE(x,y,dx,dy):
    if x!=0 and y!=0: return (x*y)*((dx/x)+(dy/y))
    else: return 0.0

def SFCR2_noVBF(NCR2_Data,ListNonProcessCR2,D_ListNonProcessCR2,NCR2_MC,D_NCR2_MC):
    D_NCR2_Data=np.sqrt(NCR2_Data)
    TotalNonProcess=sum(ListNonProcessCR2)
    D_TotalNonProcess=sum(D_ListNonProcessCR2)
    TotalNumerator=NCR2_Data-TotalNonProcess
    D_TotalNumerator=D_NCR2_Data+D_TotalNonProcess
    print "SF_CR2_noVBF=", (TotalNumerator/NCR2_MC), "+-", DivE(TotalNumerator,NCR2_MC,D_TotalNumerator,D_NCR2_MC)

def Purity1(N_Data,N_MC,D_Data,D_MC):
    print "Purity 1=", N_MC/N_Data, "+/-", DivE(N_MC,N_Data,D_MC,D_Data)

def Purity2(N_Data,N_MC,D_Data,D_MC):
    Numerator=N_Data-N_MC
    DNumerator=D_Data+D_MC
    print "Purity 2=", Numerator/N_Data, "+/-", DivE(Numerator,N_Data,DNumerator,D_Data)
"""
def AllFunction(NCR2_Data,ListNonProcessCR2,D_ListNonProcessCR2,NCR2_MC,D_NCR2_MC,Signal,DSignal):
    SFCR2_noVBF(NCR2_Data,ListNonProcessCR2,D_ListNonProcessCR2,NCR2_MC,D_NCR2_MC)
    print "For Data:"
    BinomialEffError()
    print "For Data-MC:"
    BinomialEffError(k,N)
    print "For MC:"
    BinomialEffError(k,N)
"""

def PurityMC(BKGofInt,D_BKGofInt,TotalBKG,D_TotalBKG):
    TotalProcess=sum(TotalBKG)
    D_TotalProcess=sum(D_TotalBKG)
    print "The total background is:", TotalProcess, "+/-", D_TotalProcess
    print "Purity MC=", BKGofInt/TotalProcess, "+/-", DivE(BKGofInt,TotalProcess,D_BKGofInt,D_TotalProcess)
