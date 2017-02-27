#include <iostream>
#include <cmath>
#include <TFile.h>
using namespace std;
 
void FileChecker()
{
  TFile *f = TFile::Open("root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/VBF-C1N2_leptonicDecays_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16Fast_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0215FD4B-42C0-E611-947F-10983627C3CE.root");
  if (f->IsZombie()) 
    {
      std::cout << "Error opening file" << std::endl;
    }
}
