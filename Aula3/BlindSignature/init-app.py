import sys
from eVotUM.Cripto import eccblind

def printUsage():
    print("Usage: python initSigner-app.py OR python initSigner-app.py -init")

def parseArgs():
    if (len(sys.argv) > 2):
        printUsage()
    elif(len(sys.argv) == 2 and sys.argv[1] != '-init'):
        printUsage()
    else:
        main()

def main():
    initComponents, pRDashComponents = eccblind.initSigner()
    if(len(sys.argv) == 1):
        print("pRDashComponents: %s" % pRDashComponents)
    else:
        file = open("signer_file","w")
        file.write("initComponents: " + initComponents + "\n")
        file.write("pRDashComponents: " + pRDashComponents)
        print("Components generated and saved!")    
if __name__ == "__main__":
    parseArgs()