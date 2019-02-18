import sys
from eVotUM.Cripto import eccblind


def printUsage():
    print("Usage: python unblindSignature-app.py")

def parseArgs():
    if (len(sys.argv) > 1):
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
    print("Input")
    blindSignature = raw_input("Blind signature: ")
    blindComponents = raw_input("Blind components: ")
    pRDashComponents = raw_input("pRDash components: ")
    errorCode, signature = eccblind.unblindSignature(blindSignature, pRDashComponents, blindComponents)
    showResults(errorCode, signature)

if __name__ == "__main__":
    parseArgs()
