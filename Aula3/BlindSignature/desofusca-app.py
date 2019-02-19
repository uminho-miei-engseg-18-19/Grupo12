import sys
from eVotUM.Cripto import eccblind


def printUsage():
    print("Usage: python desofusca-app.py -s blind_signature -RDash pRDashComponents")

def parseArgs():
    if (len(sys.argv) != 5):
        printUsage()
    elif(sys.argv[1] != "-s" or sys.argv[3] != "-RDash"):
        printUsage()
    else:
        main()

def showResults(errorCode, signature):
    print("Output")
    if (errorCode is None):
        print("Signature: %s" % signature)
    elif (errorCode == 1):
        print("Error: pRDash components are invalid")
    elif (errorCode == 2):
        print("Error: blind components are invalid")
    elif (errorCode == 3):
        print("Error: invalid blind signature format")

def main():
    blindSignature = sys.argv[2]
    blindComponents = getBlindComponents()
    pRDashComponents = sys.argv[4]
    errorCode, signature = eccblind.unblindSignature(blindSignature, pRDashComponents, blindComponents)
    showResults(errorCode, signature)

def getBlindComponents():
    file = open("req_file","r")
    components = file.read()
    blindComponents_unnormalized = components.split("\n")
    blindComponents = blindComponents_unnormalized[0].split(":")[1].strip()
    return blindComponents

if __name__ == "__main__":
    parseArgs()
