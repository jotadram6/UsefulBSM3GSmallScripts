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
MeanValues=[840.4,4140.8,3709.9,687.1,86.8] #QCD, W, DY, TT, VV
AssociatedErrors=[154.7,818.5,731.6,129.0,18.2]
Sys=[QCD_ListOfSys,WJets_ListOfSys,DY_ListOfSys,TT_ListOfSys,VV_ListOfSys]

for j in xrange(len(MeanValues)):
    print "--------------------------------------------Processing:", Tags[j]
    AddSys(MeanValues[j],AssociatedErrors[j],Sys[j])
