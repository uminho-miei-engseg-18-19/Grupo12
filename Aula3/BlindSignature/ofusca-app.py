import sys
from eVotUM.Cripto import eccblind


def printUsage():
    print("Usage: python generateBlindData-app.py")

def parseArgs():
    if (len(sys.argv) > 1):
        printUsage()
    else:
        main()

def showResults(errorCode, result):
    print("Output")
    if (errorCode is None):
        blindComponents, pRComponents, blindM = result
        print("Blind message: %s" % blindM)
        print("Blind components: %s" % blindComponents)
        print("pRComponents: %s" % pRComponents)
    elif (errorCode == 1):
        print("Error: pRDash components are invalid")

def main():
    print("Input")
    data = raw_input("Data: ")
    pRDashComponents = raw_input("pRDash components: ")
    errorCode, result = eccblind.blindData(pRDashComponents, data)
    showResults(errorCode, result)

if __name__ == "__main__":
    parseArgs()
