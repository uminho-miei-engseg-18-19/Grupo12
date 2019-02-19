from eVotUM.Cripto import utils
import sys
from eVotUM.Cripto import eccblind

def printUsage():
    print("Usage: python blindSignature-app.py -key private-key.pem -bmsg blind_message")

def parseArgs():
    if (len(sys.argv) != 5):
        printUsage()
    elif(sys.argv[1] != "-key" or sys.argv[3] != "-bmsg"):
        printUsage()
    else:
        eccPrivateKeyPath = sys.argv[2]
        main(eccPrivateKeyPath)

def showResults(errorCode, blindSignature):
    print("Output")
    if (errorCode is None):
        print("Blind signature: %s" % blindSignature)
    elif (errorCode == 1):
        print("Error: it was not possible to retrieve the private key")
    elif (errorCode == 2):
        print("Error: init components are invalid")
    elif (errorCode == 3):
        print("Error: invalid blind message format")

def main(eccPrivateKeyPath):
    pemKey = utils.readFile(eccPrivateKeyPath)
    passphrase = raw_input("Input your passphrase: ")
    blindM = sys.argv[4]
    initComponents = getInitComponents()
    errorCode, blindSignature = eccblind.generateBlindSignature(pemKey, passphrase, blindM, initComponents)
    showResults(errorCode, blindSignature)

def getInitComponents():
    signers_file = open("signer_file","r")
    components = signers_file.read()
    initComponents_unnormalized = components.split("\n")
    initComponents = initComponents_unnormalized[0].split(":")[1].strip()
    return initComponents    

if __name__ == "__main__":
    parseArgs()