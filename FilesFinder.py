import sys

print "Reading:", sys.argv[1], "To extract:", sys.argv[2]

InputFile = open(sys.argv[1],"read")

InputLines=InputFile.readlines()

InputFile.close()

OutputFile = open(sys.argv[2]+".txt","write")

for i in InputLines:
    if sys.argv[2] in i: 
        OutputFile.write(i)

OutputFile.close()
