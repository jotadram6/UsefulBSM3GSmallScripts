from SmallTools import *

#USING TRIGGER EFFICIENCY FUNCTION
Folder="/home/jose/ZPRIME_TAUTAU_ROOT_FILES/"
File="SingleMuon_Tauleg_TriggerEff.root"
FILETOOPEN=Folder+File

#DenVar="NRecoTriggers1/Met"
DenVar="NMuon1Tau1Combinations/TauJet1Pt"
NumVar="NRecoTriggers2/TauJet1Pt"
Rebinning=10
PDFfile="SingleMuon_Tauleg_TriggerEff.pdf"
TriggerEff(FILETOOPEN, DenVar, NumVar, Rebinning, PDFfile)
