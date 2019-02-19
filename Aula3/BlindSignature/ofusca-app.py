import sys
from eVotUM.Cripto import eccblind


def printUsage():
    print("Usage: python ofusca-app.py -msg message -RDash pRDashComponents")

def parseArgs():
    if (len(sys.argv) != 5):
        printUsage()
    elif (sys.argv[1] != "-msg" or sys.argv[3] != "-RDash"):
        printUsage()
    else:
        main()

def showResults(errorCode, result):
    print("Output")
    if (errorCode is None):
        blindComponents, pRComponents, blindM = result
        file = open("req_file","w")
        file.write("blindComponents: " + blindComponents + "\n")
        file.write("pRComponents: " + pRComponents)
        print("Blind message: %s" % blindM)
        print("Components generated and saved!")
    elif (errorCode == 1):
        print("Error: pRDash components are invalid")

def main():
    data = sys.argv[2]
    pRDashComponents = sys.argv[4]
    errorCode, result = eccblind.blindData(pRDashComponents, data)
    showResults(errorCode, result)

if __name__ == "__main__":
    parseArgs()
