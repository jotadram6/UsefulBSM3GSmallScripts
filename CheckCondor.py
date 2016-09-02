#!/bin/python

import commands as cmd
import sys

if len(sys.argv)!=2:
    print "Correct usage is python CheckCondor.py FOLDER" 
    exit()

FolderToBeChecked=sys.argv[1]

CONDORSTATUS=cmd.getoutput("eval `condor_q | grep jruizalv`")
if len(CONDORSTATUS)!=0: print CONDORSTATUS
Errors=cmd.getoutput("wc -w "+FolderToBeChecked+"/*.stderr")
ErrorAlarm=cmd.getoutput("wc -w MET_Run2016B_PromptReco_v2_MINIAODv2_0000/*.stderr | grep 'total'")
if len(ErrorAlarm)!=0: print "There are jobs with ERRORS!"
ErrorsList=Errors.split("\n")
#print ErrorsList[-1]
for i in ErrorsList:
    ByColumn=i.split(" ")
    k=0
    for j in ByColumn:
        #if j!="" and j!="0": print j
        if j!="": k+=1
        if k==1 and j!="0": print i
        #if (j!="" and j!="0") and k==0: 
        #    k+=1
        #    print j, k

