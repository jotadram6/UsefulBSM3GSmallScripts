import commands as cmd

TXTFiles = cmd.getoutput("ls list_Samples/")

ListTXTFiles = TXTFiles.split("\n")

OutputFile = open("SAMPLES_LIST.txt","write")

for i in ListTXTFiles: 
    OutputFile.write(i.split(".")[0]+"\n")
    print i.split(".")[0]

OutputFile.close()
