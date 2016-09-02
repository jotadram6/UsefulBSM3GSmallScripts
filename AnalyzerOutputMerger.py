#!/bin/python

import commands as cmd
import sys

if len(sys.argv)!=2:
    print "Correct usage is python AnalyzerOutputMerger.py FOLDER"
    exit()

FolderToBeMerged=sys.argv[1]

MainFolderContent=cmd.getoutput("/usr/bin/eos root://cmseos.fnal.gov ls /eos/uscms/store/user/jruizalv/"+FolderToBeMerged)
print "I'll merge the following directories:", MainFolderContent
MainFolderContentList=MainFolderContent.split("\n")
for i in MainFolderContentList:
    print "Processing ", i
    print cmd.getoutput("hadd /tmp/"+i+"_Merged.root `/cvmfs/cms.cern.ch/slc6_amd64_gcc530/cms/cmssw/CMSSW_8_0_10/external/slc6_amd64_gcc530/bin/xrdfs root://cmseos.fnal.gov ls -u /eos/uscms/store/user/jruizalv/"+FolderToBeMerged+"/"+i+" | grep '\.root'`")
    #print cmd.getoutput("/usr/bin/eoscp /tmp/"+i+"_Merged.root /eos/uscms/store/user/jruizalv/"+FolderToBeMerged+"/"+i+"_Merged.root")
