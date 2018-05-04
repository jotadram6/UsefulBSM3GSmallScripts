from math import *

QCD_ListOfSys=[2.5,3.0,1.0,14.0,8.0,1.0,1.0,4.0,22.0]
WJets_ListOfSys=[2.5,1.0,1.0,1.0,3.0,1.0,14.0,8.0,1.0,1.0,4.0,4.8,1.0,10.0]
DY_ListOfSys=[2.5,1.0,1.0,1.0,3.0,1.0,14.0,8.0,1.0,1.0,4.0,4.2,1.0,10.0]
TT_ListOfSys=[2.5,1.0,1.0,1.0,3.0,7.0,14.0,8.0,1.0,1.0,4.0,4.2,3.5,10.0]
VV_ListOfSys=[2.5,1.0,1.0,1.0,3.0,1.0,14.0,8.0,1.0,1.0,4.0,3.5,10.0]
S_ListOfSys=[2.5,1.0,1.0,2.0,3.0,1.0,14.0,8.0,1.0,1.0,4.0,6.5,2.0,10.0]

def AddSys(MeanValue,StatsError,ListOfSys):
    NewError2=StatsError**2
    for i in ListOfSys:
        NewError2+=(MeanValue*i/100)**2
    print "Original Values=", MeanValue, "+-", StatsError
    print "New Values=", MeanValue, "+-", sqrt(NewError2)
    print "Stats error is", StatsError*100/MeanValue, "% relative to mean value!"
    print "New error is", sqrt(NewError2)*100/MeanValue, "% relative to mean value!"
    

Tags=["QCD","W","DY","TT","VV"]
MeanValues=[2146.3,3635.0,4116.8,665.0,87.0] #QCD, W, DY, TT, VV
AssociatedErrors=[150.0,88.0,74.8,30.4,10.8]
Sys=[QCD_ListOfSys,WJets_ListOfSys,DY_ListOfSys,TT_ListOfSys,VV_ListOfSys]

for j in xrange(len(MeanValues)):
    print "--------------------------------------------Processing:", Tags[j]
    AddSys(MeanValues[j],AssociatedErrors[j],Sys[j])
