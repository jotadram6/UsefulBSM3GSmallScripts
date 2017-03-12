import sys

print "Reading:", sys.argv[1], "To extract:", sys.argv[2]

InputFile = open(sys.argv[1],"read")

InputLines=InputFile.readlines()

InputFile.close()

OutputFile = open(sys.argv[2]+".txt","write")

k=0
for i in InputLines:
    if sys.argv[2] in i:
        OutputFile.write(i)
        k=1

if not k: print "Output file EMPTY! The pattern was not found..."

OutputFile.close()
