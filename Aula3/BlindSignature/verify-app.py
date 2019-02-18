import sys
from eVotUM.Cripto import eccblind
from eVotUM.Cripto import utils

def printUsage():
    print("Usage: python verifySignature-app.py public-key.pem")

def parseArgs():
    if (len(sys.argv) != 2):
        printUsage()
    else:
        eccPublicKeyPath = sys.argv[1]
        main(eccPublicKeyPath)

def showResults(errorCode, validSignature):
    print("Output")
    if (errorCode is None):
        if (validSignature):
            print("Valid signature")
        else:
            print("Invalid signature")
    elif (errorCode == 1):
        print("Error: it was not possible to retrieve the public key")
    elif (errorCode == 2):
        print("Error: pR components are invalid")
    elif (errorCode == 3):
        print("Error: blind components are invalid")
    elif (errorCode == 4):
        print("Error: invalid signature format")

def main(eccPublicKeyPath):
    pemPublicKey = utils.readFile(eccPublicKeyPath)
    print("Input")
    data = raw_input("Original data: ")
    signature = raw_input("Signature: ")
    blindComponents = raw_input("Blind components: ")
    pRComponents = raw_input("pR components: ")
    errorCode, validSignature = eccblind.verifySignature(pemPublicKey, signature, blindComponents, pRComponents, data)
    showResults(errorCode, validSignature)

if __name__ == "__main__":
    parseArgs()