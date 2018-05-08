import ROOT

"""
Script developed to include a histogram from data driven methods here: LargestDiJetMass__DataDrivenQCD
into normal BKG root file expected by the plotter, in order to hack the plotter to include it. 
Number of entries is not important! The plotter has been also hacked to not rescale the output of this script
"""

def getall(d, basepath="/"):
    "Generator function to recurse into a ROOT file/dir and yield (path, obj) pairs"
    for key in d.GetListOfKeys():
        kname = key.GetName()
        if key.IsFolder():
            # TODO: -> "yield from" in Py3
            for i in getall(d.Get(kname), basepath+kname+"/"):
                yield i
        else:
            readThis = 0
            yield basepath+kname, d.Get(kname)


#Histo to be hacked in
LargestDiJetMass__DataDrivenQCD =  ROOT.TH1D("LargestDiJetMass","LargestDiJetMass",23,400,5000)
LargestDiJetMass__DataDrivenQCD.SetBinContent(4,211.3107)
LargestDiJetMass__DataDrivenQCD.SetBinContent(5,308.9594)
LargestDiJetMass__DataDrivenQCD.SetBinContent(6,292.2501)
LargestDiJetMass__DataDrivenQCD.SetBinContent(7,295.3514)
LargestDiJetMass__DataDrivenQCD.SetBinContent(8,201.0664)
LargestDiJetMass__DataDrivenQCD.SetBinContent(9,273.0902)
LargestDiJetMass__DataDrivenQCD.SetBinContent(10,138.5872)
LargestDiJetMass__DataDrivenQCD.SetBinContent(11,78.08275)
LargestDiJetMass__DataDrivenQCD.SetBinContent(12,44.51777)
LargestDiJetMass__DataDrivenQCD.SetBinContent(13,50.14642)
LargestDiJetMass__DataDrivenQCD.SetBinContent(14,76.47452)
LargestDiJetMass__DataDrivenQCD.SetBinContent(15,51.10457)
LargestDiJetMass__DataDrivenQCD.SetBinContent(16,9.804428)
LargestDiJetMass__DataDrivenQCD.SetBinContent(17,36.23764)
LargestDiJetMass__DataDrivenQCD.SetBinContent(18,8.38006)
LargestDiJetMass__DataDrivenQCD.SetBinContent(19,11.30333)
LargestDiJetMass__DataDrivenQCD.SetBinContent(20,34.98336)
LargestDiJetMass__DataDrivenQCD.SetBinContent(21,11.03311)
LargestDiJetMass__DataDrivenQCD.SetBinContent(22,11.69563)
LargestDiJetMass__DataDrivenQCD.SetBinContent(23,1.921066)
LargestDiJetMass__DataDrivenQCD.SetBinContent(24,14.83603)
"""LargestDiJetMass__DataDrivenQCD.SetBinError(4,55.95334)
LargestDiJetMass__DataDrivenQCD.SetBinError(5,81.17142)
LargestDiJetMass__DataDrivenQCD.SetBinError(6,72.62606)
LargestDiJetMass__DataDrivenQCD.SetBinError(7,80.16883)
LargestDiJetMass__DataDrivenQCD.SetBinError(8,56.74208)
LargestDiJetMass__DataDrivenQCD.SetBinError(9,77.44262)
LargestDiJetMass__DataDrivenQCD.SetBinError(10,46.54988)
LargestDiJetMass__DataDrivenQCD.SetBinError(11,30.4808)
LargestDiJetMass__DataDrivenQCD.SetBinError(12,17.43455)
LargestDiJetMass__DataDrivenQCD.SetBinError(13,25.21888)
LargestDiJetMass__DataDrivenQCD.SetBinError(14,39.80917)
LargestDiJetMass__DataDrivenQCD.SetBinError(15,29.72514)
LargestDiJetMass__DataDrivenQCD.SetBinError(16,7.243199)
LargestDiJetMass__DataDrivenQCD.SetBinError(17,31.68333)
LargestDiJetMass__DataDrivenQCD.SetBinError(18,7.814866)
LargestDiJetMass__DataDrivenQCD.SetBinError(19,11.47808)
LargestDiJetMass__DataDrivenQCD.SetBinError(20,62.96689)
LargestDiJetMass__DataDrivenQCD.SetBinError(21,10.31622)
LargestDiJetMass__DataDrivenQCD.SetBinError(22,19.71461)
LargestDiJetMass__DataDrivenQCD.SetBinError(23,3.765784)
LargestDiJetMass__DataDrivenQCD.SetBinError(24,8.422422)"""
LargestDiJetMass__DataDrivenQCD.SetEntries(35867.0)
#LargestDiJetMass__DataDrivenQCD.SetEntries(107.466)
#LargestDiJetMass__DataDrivenQCD.SetStats(0)
            
# Demo
ROOT.gROOT.SetBatch(True)
f = ROOT.TFile("QCD.root")
CopyF = ROOT.TFile("DataDrivenQCD.root","RECREATE")
CopyF.cd()
for k, o in getall(f):
    #print o.ClassName(), k
    #ROOT.gDirectory.pwd()
    NeededDirectory=k[1:].split("/")[0]
    PWD=ROOT.gDirectory.GetPath()
    #print PWD, "------------------------------------------------------> Testing pwd"
    if NeededDirectory not in PWD:
        CopyF.cd()
        #print "------------------------------------------------------> Making subdirectory"
        ROOT.gDirectory.mkdir(NeededDirectory)
        ROOT.gDirectory.cd(NeededDirectory)
    if k=="/NLeadJetCombinations/LargestDiJetMass":
        print "Found it!----------------------------------------------------------->", k
        LargestDiJetMass__DataDrivenQCD.Write(k[1:].split("/")[1])
        print "Histo Hacked! Muajajajajajajajajajajaja!!!!!!!!!!!!!!!!"
    else:
        o.Write(k[1:].split("/")[1])
 
CopyF.Close()
