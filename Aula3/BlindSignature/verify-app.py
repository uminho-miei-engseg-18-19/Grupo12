import sys
from eVotUM.Cripto import eccblind
from eVotUM.Cripto import utils

def printUsage():
    print("Usage: python verify-app.py -cert certificado -msg mensagem_original -sDash assinatura -f ficheiro_requerente")

def parseArgs():
    if (len(sys.argv) != 9):
        printUsage()
    elif(sys.argv[1] != "-cert" or sys.argv[3] != "-msg" or sys.argv[5]!= "-sDash" or sys.argv[7] != "-f"):
        printUsage()
    else:
        eccPublicKeyPath = sys.argv[2]
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
    data = sys.argv[4]
    signature = sys.argv[6]
    components = getReqComponents(sys.argv[8])
    blindComponents = components[0]
    pRComponents = components[1]
    #blindComponents = raw_input("Blind components: ")
    #pRComponents = raw_input("pR components: ")
    errorCode, validSignature = eccblind.verifySignature(pemPublicKey, signature, blindComponents, pRComponents, data)
    showResults(errorCode, validSignature)

def getReqComponents(path):
    file = open(path,"r")
    content = file.read()
    components = content.split("\n")
    components[0] = components[0].split(":")[1].strip()
    components[1] = components[1].split(":")[1].strip()
    return components

if __name__ == "__main__":
    parseArgs()