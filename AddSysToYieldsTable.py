from math import *

def AddSys(MeanValue,StatsError,ListOfSys):
    if MeanValue==0.0: return 0.0
    NewError2=StatsError**2
    for i in ListOfSys:
        NewError2+=(MeanValue*i/100)**2
    print "Original Values=", MeanValue, "+-", StatsError
    print "New Values=", MeanValue, "+-", sqrt(NewError2)
    print "Stats error is", StatsError*100/MeanValue, "% relative to mean value!"
    print "New error is", sqrt(NewError2)*100/MeanValue, "% relative to mean value!"
    return sqrt(NewError2)

def ReadTable(FileWithTable,NewFile,Sys):
    A=open(FileWithTable,'r')
    B=A.readlines()
    A.close()
    AfterSys=[]
    for i in B:
        #i.replace("\\","").replace("\n","")
        C=i.split('&')
        #print C
        if len(Sys)!=len(C): 
            "Wrong size of Sys vector"
            return 0
        ThisLine=''
        for j in xrange(len(C)):
            #C[j].split('$\\pm$')
            MeanValue=float(C[j].split('$\\pm$')[0][:C[j].split('$\\pm$')[0].find('.')+2])
            UncValue=float(C[j].split('$\\pm$')[1][:C[j].split('$\\pm$')[1].find('.')+2])
            NewError=AddSys(MeanValue,UncValue,Sys[j])
            NewError='%.1f ' % NewError
            ThisLine=ThisLine+' '+str(MeanValue)+' $\\pm$ '+NewError+'& '
        
        ThisLine=ThisLine[:-2]+"\\\ \n"
        AfterSys.append(ThisLine)
    A=open(NewFile,'w')
    A.writelines(AfterSys)
    #for i in AfterSys: A.write(i)
    A.close()

if __name__ == '__main__':
    
    """TestSys=[
    [2.5,3.0,1.0,14.0,8.0,1.0,1.0,4.0,22.0],
    [2.5,1.0,1.0,1.0,3.0,1.0,14.0,8.0,1.0,1.0,4.0,4.8,1.0,10.0],
    [2.5,1.0,1.0,1.0,3.0,1.0,14.0,8.0,1.0,1.0,4.0,4.2,1.0,10.0],
    [2.5,1.0,1.0,1.0,3.0,7.0,14.0,8.0,1.0,1.0,4.0,4.2,3.5,10.0],
    [2.5,1.0,1.0,1.0,3.0,1.0,14.0,8.0,1.0,1.0,4.0,3.5,10.0],
    [2.5,1.0,1.0,1.0,3.0,1.0,14.0,8.0,1.0,1.0,4.0,3.5,10.0],
    [2.5,1.0,1.0,2.0,3.0,1.0,14.0,8.0,1.0,1.0,4.0,6.5,2.0,10.0]
    ]
    ReadTable('/home/jose/Dropbox/Vandy/VBF_DM/TableLineTest.txt','TestUnc.txt',TestSys)"""
    
    SSysy=[2.5,1.0,1.0,2.0,3.0,1.0,14.0,8.0,1.0,1.0,6.5,2.0]
    
    """SigSys=[
    SSysy,
    SSysy,
    SSysy,
    SSysy,
    SSysy,
    SSysy,
    SSysy,
    SSysy,
    SSysy,
    SSysy,
    ]
    ReadTable('/home/jose/Dropbox/Vandy/VBF_DM/FromMarchConvenersComments/QCD_estimation/SignalsTable.txt','/home/jose/Dropbox/Vandy/VBF_DM/FromMarchConvenersComments/QCD_estimation/SignalsTableWithUnc.txt',SigSys)"""
    
    
    WJets_ListOfSys=[2.5,1.0,1.0,1.0,3.0,1.0,14.0,8.0,1.0,1.0,4.0,4.8,1.0,10.0]
    DY_ListOfSys=[2.5,1.0,1.0,1.0,3.0,1.0,14.0,8.0,1.0,1.0,4.0,4.2,1.0,10.0]
    QCD_ListOfSys=[2.5,3.0,1.0,14.0,8.0,1.0,1.0,4.0,22.0]
    TT_ListOfSys=[2.5,1.0,1.0,1.0,3.0,7.0,14.0,8.0,1.0,1.0,4.0,4.2,3.5,10.0]
    VV_ListOfSys=[2.5,1.0,1.0,1.0,3.0,1.0,14.0,8.0,1.0,1.0,4.0,3.5,10.0]
    
    WJetsSys1=[
        WJets_ListOfSys[:],
        WJets_ListOfSys[:],
        WJets_ListOfSys[:],
        WJets_ListOfSys[:],
        WJets_ListOfSys[:],
        WJets_ListOfSys[:],
        WJets_ListOfSys[:],
        WJets_ListOfSys[:],
        WJets_ListOfSys[:],
        WJets_ListOfSys[:]
    ]
    
    WJetsSys1[0].append(28.0)
    WJetsSys1[1].append(27.0),
    WJetsSys1[2].append(26.0),
    WJetsSys1[3].append(25.0),
    WJetsSys1[4].append(24.0),
    WJetsSys1[5].append(23.0),
    WJetsSys1[6].append(22.0),
    WJetsSys1[7].append(21.0),
    WJetsSys1[8].append(20.0),
    WJetsSys1[9].append(19.0)
    
    WJetsSys2=[
        WJets_ListOfSys[:],
        WJets_ListOfSys[:],
        WJets_ListOfSys[:],
        WJets_ListOfSys[:],
        WJets_ListOfSys[:],
        WJets_ListOfSys[:],
        WJets_ListOfSys[:],
        WJets_ListOfSys[:],
        WJets_ListOfSys[:],
        WJets_ListOfSys[:]
    ]
    
    WJetsSys2[0].append(18.0),
    WJetsSys2[1].append(17.0),
    WJetsSys2[2].append(16.0),
    WJetsSys2[3].append(15.0),
    WJetsSys2[4].append(14.0),
    WJetsSys2[5].append(13.0),
    WJetsSys2[6].append(12.0),
    WJetsSys2[7].append(11.0),
    WJetsSys2[8].append(10.0),
    WJetsSys2[9].append(9.0)
    
    
    #print WJetsSys1, WJetsSys2
    
    ReadTable('/home/jose/Dropbox/Vandy/VBF_DM/FromMarchConvenersComments/QCD_estimation/WTable1.txt','/home/jose/Dropbox/Vandy/VBF_DM/FromMarchConvenersComments/QCD_estimation/WTable1WithUnc.txt',WJetsSys1)
    ReadTable('/home/jose/Dropbox/Vandy/VBF_DM/FromMarchConvenersComments/QCD_estimation/WTable2.txt','/home/jose/Dropbox/Vandy/VBF_DM/FromMarchConvenersComments/QCD_estimation/WTable2WithUnc.txt',WJetsSys2)
    
    
    DYSys1=[
        DY_ListOfSys[:],
        DY_ListOfSys[:],
        DY_ListOfSys[:],
        DY_ListOfSys[:],
        DY_ListOfSys[:],
        DY_ListOfSys[:],
        DY_ListOfSys[:],
        DY_ListOfSys[:],
        DY_ListOfSys[:],
        DY_ListOfSys[:]
    ]
    
    DYSys1[0].append(28.0),
    DYSys1[1].append(27.0),
    DYSys1[2].append(26.0),
    DYSys1[3].append(25.0),
    DYSys1[4].append(24.0),
    DYSys1[5].append(23.0),
    DYSys1[6].append(22.0),
    DYSys1[7].append(21.0),
    DYSys1[8].append(20.0),
    DYSys1[9].append(19.0)
    
    
    DYSys2=[
        DY_ListOfSys[:],
        DY_ListOfSys[:],
        DY_ListOfSys[:],
        DY_ListOfSys[:],
        DY_ListOfSys[:],
        DY_ListOfSys[:],
        DY_ListOfSys[:],
        DY_ListOfSys[:],
        DY_ListOfSys[:],
        DY_ListOfSys[:]
    ]
    
    DYSys2[0].append(18.0),
    DYSys2[0].append(17.0),
    DYSys2[0].append(16.0),
    DYSys2[0].append(15.0),
    DYSys2[0].append(14.0),
    DYSys2[0].append(13.0),
    DYSys2[0].append(12.0),
    DYSys2[0].append(11.0),
    DYSys2[0].append(10.0),
    DYSys2[0].append(9.0)
    
    
    ReadTable('/home/jose/Dropbox/Vandy/VBF_DM/FromMarchConvenersComments/QCD_estimation/ZTable1.txt','/home/jose/Dropbox/Vandy/VBF_DM/FromMarchConvenersComments/QCD_estimation/DYTable1WithUnc.txt',DYSys1)
    ReadTable('/home/jose/Dropbox/Vandy/VBF_DM/FromMarchConvenersComments/QCD_estimation/ZTable2.txt','/home/jose/Dropbox/Vandy/VBF_DM/FromMarchConvenersComments/QCD_estimation/DYTable2WithUnc.txt',DYSys2)
    
    QCDSys1=[
        QCD_ListOfSys[:],
        QCD_ListOfSys[:],
        QCD_ListOfSys[:],
        QCD_ListOfSys[:],
        QCD_ListOfSys[:],
        QCD_ListOfSys[:],
        QCD_ListOfSys[:],
        QCD_ListOfSys[:],
        QCD_ListOfSys[:],
        QCD_ListOfSys[:]
    ]
    
    QCDSys1[0].append(10.0),
    QCDSys1[1].append(8.0),
    QCDSys1[2].append(7.0),
    QCDSys1[3].append(7.0),
    QCDSys1[4].append(8.0),
    QCDSys1[5].append(8.0),
    QCDSys1[6].append(9.0),
    QCDSys1[7].append(10.0),
    QCDSys1[8].append(11.0),
    QCDSys1[9].append(12.0)
    
    QCDSys2=[
        QCD_ListOfSys[:],
        QCD_ListOfSys[:],
        QCD_ListOfSys[:],
        QCD_ListOfSys[:],
        QCD_ListOfSys[:],
        QCD_ListOfSys[:],
        QCD_ListOfSys[:],
        QCD_ListOfSys[:],
        QCD_ListOfSys[:],
        QCD_ListOfSys[:]
    ]
    
    QCDSys2[0].append(14.0),
    QCDSys2[1].append(15.0),
    QCDSys2[2].append(16.0),
    QCDSys2[3].append(19.0),
    QCDSys2[4].append(23.0),
    QCDSys2[5].append(22.0),
    QCDSys2[6].append(23.0),
    QCDSys2[7].append(28.0),
    QCDSys2[8].append(28.0),
    QCDSys2[9].append(33.0)
    
    
    ReadTable('/home/jose/Dropbox/Vandy/VBF_DM/FromMarchConvenersComments/QCD_estimation/QCDDataTable1.txt','/home/jose/Dropbox/Vandy/VBF_DM/FromMarchConvenersComments/QCD_estimation/QCDDataTable1WithUnc.txt',QCDSys1)
    ReadTable('/home/jose/Dropbox/Vandy/VBF_DM/FromMarchConvenersComments/QCD_estimation/QCDDataTable2.txt','/home/jose/Dropbox/Vandy/VBF_DM/FromMarchConvenersComments/QCD_estimation/QCDDataTable2WithUnc.txt',QCDSys2)
    
    
    TTSys=[
        TT_ListOfSys[:],
        TT_ListOfSys[:],
        TT_ListOfSys[:],
        TT_ListOfSys[:],
        TT_ListOfSys[:],
        TT_ListOfSys[:],
        TT_ListOfSys[:],
        TT_ListOfSys[:],
        TT_ListOfSys[:],
        TT_ListOfSys[:]
    ]
    
    ReadTable('/home/jose/Dropbox/Vandy/VBF_DM/FromMarchConvenersComments/QCD_estimation/TTTable.txt','/home/jose/Dropbox/Vandy/VBF_DM/FromMarchConvenersComments/QCD_estimation/TTTableWithUnc.txt',TTSys)
    
    
    VVSys=[
        VV_ListOfSys[:],
        VV_ListOfSys[:],
        VV_ListOfSys[:],
        VV_ListOfSys[:],
        VV_ListOfSys[:],
        VV_ListOfSys[:],
        VV_ListOfSys[:],
        VV_ListOfSys[:],
        VV_ListOfSys[:],
        VV_ListOfSys[:]
    ]
    
    ReadTable('/home/jose/Dropbox/Vandy/VBF_DM/FromMarchConvenersComments/QCD_estimation/VVTable.txt','/home/jose/Dropbox/Vandy/VBF_DM/FromMarchConvenersComments/QCD_estimation/VVTableWithUnc.txt',VVSys)
    
    SigSys=[
        SSysy[:],
        SSysy[:],
        SSysy[:],
        SSysy[:],
        SSysy[:],
        SSysy[:],
        SSysy[:],
        SSysy[:],
        SSysy[:],
        SSysy[:]
]
    ReadTable('/home/jose/Dropbox/Vandy/VBF_DM/FromMarchConvenersComments/QCD_estimation/SlepTable.txt','/home/jose/Dropbox/Vandy/VBF_DM/FromMarchConvenersComments/QCD_estimation/SlepTableWithUnc.txt',SigSys)
    ReadTable('/home/jose/Dropbox/Vandy/VBF_DM/FromMarchConvenersComments/QCD_estimation/SWZTable.txt','/home/jose/Dropbox/Vandy/VBF_DM/FromMarchConvenersComments/QCD_estimation/SWZTableWithUnc.txt',SigSys)
