import ROOT
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from array import array
import time
import os
import commands as cmd

#From rootnotes
def canvas(name="icanvas", size=(800, 600)):
    """Helper method for creating canvas"""

    # Check if icanvas already exists
    canvas = ROOT.gROOT.FindObject(name)
    assert len(size) == 2
    if canvas:
        return canvas
    else:
        return ROOT.TCanvas(name, name, size[0], size[1])

#Style functions
def SetAxis(Histo,Axis,TOffset,TSize,LOffset,LSize,Ndiv):
    """Sets offset and size of an axis in the histogram. Axis must be 'X' or 'Y', and Histo should be a valid root histogram"""
    if Axis=='X':
        Histo.GetXaxis().SetTitleSize(TSize)
        Histo.GetXaxis().SetTitleOffset(TOffset)
        Histo.GetXaxis().SetLabelSize(LSize)
        Histo.GetXaxis().SetLabelOffset(LOffset)
        Histo.GetXaxis().SetNdivisions(Ndiv)
    elif Axis=='Y':
        Histo.GetYaxis().SetTitleSize(TSize)
        Histo.GetYaxis().SetTitleOffset(TOffset)
        Histo.GetYaxis().SetLabelSize(LSize)
        Histo.GetYaxis().SetLabelOffset(LOffset)
        Histo.GetYaxis().SetNdivisions(Ndiv)
    else: print "Please correct axis selection: Valid values are 'X' or 'Y'"

def SetCos(Hist,FillColor,FillStyle,LineColor,LineWidth,LineStyle,MarkerStyle):
    """Hist, FillColor, FillStyle, LineColor, LineWidth, LineStyle, MarkerStyle"""
    Hist.SetLineStyle(LineStyle); Hist.SetLineWidth(LineWidth); Hist.SetLineColor(LineColor)
    Hist.SetFillStyle(FillStyle); Hist.SetFillColor(FillColor)
    Hist.SetMarkerStyle(MarkerStyle)

#Propagation of error functions
def DivE(x,y,dx,dy):
    if x!=0 and y!=0: return (x/y)*((dx/x)+(dy/y))
    else: return 0.0

def MulE(x,y,dx,dy):
    if x!=0 and y!=0: return (x*y)*((dx/x)+(dy/y))
    else: return 0.0

def SqrtE(x,dx):
    if x!=0: return np.sqrt(x)*0.5*(dx/x)
    else: return 0.0

def LnE(x,dx):
    if x!=0: return (dx/x)
    else: return 0.0

def SmlbE(s,b,ws,wb):
    if s!=0 and b!=0:
        ds=ws*np.sqrt(s); db=wb*np.sqrt(b)
        return DivE(s,np.sqrt(b),ds,SqrtE(b,db))
    else: return 0.0

def AsimovE(s,b,ws,wb):
    #np.sqrt(2*((Ns+Nb)*np.log(1.+(Ns/Nb))-Ns))
    if s!=0 and b!=0:
        ds=ws*np.sqrt(s); db=wb*np.sqrt(b)
        FractionE=DivE(s,b,ds,db)
        LogE=LnE(1.+(s/b),FractionE)
        MultipliE=MulE((s+b),np.log(1.+(s/b)),(ds+db),LogE)
        InsidesqrtE=(2*MultipliE)+ds
        return SqrtE(np.sqrt(2*((s+b)*np.log(1.+(s/b))-s)),InsidesqrtE)
    else: return 0.0

def EffE(eff,N):
    if N!=0: return np.sqrt((eff*(1-eff))/N)
    else: return 0.0

def EffV(a,b):
    if b!=0: return a/b
    else: return 0.0

#Getting Info strings
def GetMR(Histo):
    return "Mean={0:.2f}".format(Histo.GetMean())+"#pm{0:.2f}".format(Histo.GetMeanError())+" RMS={0:.2f}".format(Histo.GetRMS())+"#pm{0:.2f}".format(Histo.GetRMSError())

def GetEWI(Histo):
    INT=Histo.Integral(0,Histo.GetNbinsX()+1)
    ENT=Histo.GetEntries()
    if ENT!=0: W=INT/ENT
    else: W=0
    #return "Entries={0:.2f}".format(ENT)+" W={0:.2f}".format(W)+" Int={0:.2f}".format(INT)+"+-{0:.2f}".format(W*np.sqrt(ENT))
    return "Entries={0:.2f}".format(ENT)+" Int={0:.2f}".format(INT)+"#pm{0:.2f}".format(W*np.sqrt(ENT))

#Functions to work with histos
def TriggerEff(RootFile,Trigger1DenVar,Trigger2NumVar,RBin,PDFname):
    EffFile= ROOT.TFile(RootFile, "read")
    Numerator=ROOT.gDirectory.Get(Trigger2NumVar)
    Denominator=ROOT.gDirectory.Get(Trigger1DenVar)
    Numerator.Sumw2(); Denominator.Sumw2()
    Numerator.Rebin(RBin); Denominator.Rebin(RBin)
    EffAsymmErrors = ROOT.TGraphAsymmErrors(Numerator,Denominator,"cl=0.683 b(1,1) mode")
    CurCanv = canvas("MyPlot", (600, 600))
    EffAsymmErrors.Draw("ALP")
    CurCanv.Print(PDFname,"Title:"+Trigger2NumVar.split("/")[1])
    EffFile.Close()

def loopdir(dire):
    """//file loopdir.C
void loopdir (TDirectory *dir) {
   //loop on all keys of dir including possible subdirs
   //print a message for all keys with a class TH1

   TIter next (dir->GetListOfKeys());
   TKey *key;
   while ((key = (TKey*)next())) {
      if (strstr(key->GetClassName(),"TH1")) {
         printf (" key : %s is a %s in %s\n",
                 key->GetName(),key->GetClassName(),dir->GetPath());
      }
      if (!strcmp(key->GetClassName(),"TDirectory")) {
         dir->cd(key->GetName());
         TDirectory *subdir = gDirectory;
         loopdir(subdir);
         dir->cd();
      }
   }
}
"""
    #dire.ls()
    ListOfKeys=dire.GetListOfKeys()
    #print ListOfKeys
    nexti = ROOT.TIter(ListOfKeys)
    key = ROOT.TKey; key = nexti()
    while key:
        #print "Key infos", key.GetName(), key.GetClassName(), dire.GetPath()
        if "TH1" in key.GetClassName():
            print key.GetName(), key.GetClassName(), dire.GetPath()
        if "TDirectory" in key.GetClassName():
            dire.cd(key.GetName())
            subdir = ROOT.gDirectory
            loopdir(subdir)
            dire.cd()
        key = nexti()

def SearchHisto(dire,SubDir,histoName,histType):
    #dire.ls()
    ListOfKeys=dire.GetListOfKeys()
    #print ListOfKeys
    nexti = ROOT.TIter(ListOfKeys)
    key = ROOT.TKey; key = nexti()
    while key:
        #print "Key infos", key.GetName(), key.GetClassName(), dire.GetPath()
        if (histType in key.GetClassName()) and (histoName == key.GetName()) and (SubDir in  dire.GetPath()):
            print key.GetName(), key.GetClassName(), dire.GetPath()
            ToGet=dire.GetPath()+"/"+key.GetName(); print ToGet
            return ROOT.gDirectory.Get(ToGet.split(":")[-1][1:])
        if "TDirectory" in key.GetClassName():
            dire.cd(key.GetName())
            subdir = ROOT.gDirectory
            SearchHisto(subdir,SubDir,histoName,histType)
            dire.cd()
        key = nexti()

def RatioPlot(RootFile1,RootFile2,Subdir,NumVar,DenVar,RBin,PDFname):
    RFile1 = ROOT.TFile(RootFile1, "read")
    RFile1.ls()
    Keys1 = RFile1.GetListOfKeys()
    #NumeratorO=ROOT.gDirectory.Get(NumVar)
    #NumeratorO.DrawCopy("","_copy")
    #Numerator=ROOT.gDirectory.Get(NumVar+"_copy")
    #Numerator.Draw(NumVar+" >> NumeratorHistogram(50,1000,5000)")
    #RFile1.Close()
    #Numerator=ROOT.TH1F()
    #Numerator=ROOT.gDirectory.Get(NumVar)
    Numerator=SearchHisto(RFile1,Subdir,NumVar,"TH1F")
    RFile2 = ROOT.TFile(RootFile2, "read")
    RFile2.ls()
    #DenominatorO=ROOT.gDirectory.Get(DenVar)
    #DenominatorO.DrawCopy("","_copy")
    #Denominator=ROOT.gDirectory.Get(DenVar+"_copy")
    #RFile2.Close()
    #Denominator=ROOT.TH1F()
    #Denominator=ROOT.gDirectory.Get(DenVar)
    Denominator=SearchHisto(RFile2,Subdir,NumVar,"TH1F")
    Numerator.Sumw2(); Denominator.Sumw2()
    Numerator.Rebin(RBin); Denominator.Rebin(RBin)
    EffAsymmErrors = ROOT.TGraphAsymmErrors(Numerator,Denominator,"cl=0.683 b(1,1) mode")
    CurCanv = canvas("MyPlot", (600, 600))
    EffAsymmErrors.Draw("ALP")
    CurCanv.Print(PDFname,"Title:"+NumVar.split("/")[1])
    RFile1.Close()
    #RFile2.Close()

def ExtractHistos(RootFile,HistosList,RBinList,PDFname,DrawOpt,Norm1):
    if len(HistosList)!=len(RBinList): 
        print "ERROR: List of rebinning must have the same number of entries as histograms list"
        return 0
    RFile= ROOT.TFile(RootFile, "read")
    CurCanv = canvas("MyPlot", (600, 600))
    for i in xrange(len(HistosList)):
        HistoT=ROOT.gDirectory.Get(HistosList[i])
        HistoT.Sumw2()
        HistoT.Rebin(RBinList[i])
        if Norm1:
            HistoT.Scale(1./HistoT.Integral())
        HistoT.Draw(DrawOpt)
        if i!=0 and i!=(len(HistosList)-1):
            CurCanv.Print(PDFname,"Title:"+HistosList[i].split("/")[1])
        elif i==0 and len(HistosList)!=1:
            CurCanv.Print(PDFname+"(","Title:"+HistosList[i].split("/")[1])
        elif i==0 and len(HistosList)==1:
            CurCanv.Print(PDFname,"Title:"+HistosList[i].split("/")[1])
        elif i==(len(HistosList)-1):
            CurCanv.Print(PDFname+")","Title:"+HistosList[i].split("/")[1])
    RFile.Close()

def IntegrateHistos(RootFiles,HistosList,Min,Max):
    #if len(HistosList)!=len(RBinList): 
    #    print "ERROR: List of rebinning must have the same number of entries as histograms list"
    #    return 0
    for j in xrange(len(RootFiles)):
        RFile= ROOT.TFile(RootFiles[j], "read")
        print "Processing", RootFiles[j]
        for i in xrange(len(HistosList)):
            HistoT=ROOT.gDirectory.Get(HistosList[i])
            #HistoT.Sumw2()
            integral_error=ROOT.Double(0.)
            Integral=HistoT.IntegralAndError(HistoT.GetXaxis().FindBin(Min),HistoT.GetXaxis().FindBin(Max),integral_error)
            print "Integral: {0:.3f}+-{1:.3f}".format(Integral,integral_error)
            del(HistoT)
        RFile.Close()
