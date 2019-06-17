import sys
import requests
import argparse
import menu
import json
import base64

sig_levels = {'CAdES': ['CAdES_BASELINE_T', 'CAdES_BASELINE_LT', 'CAdES_BASELINE_LTA'],
              'PAdES': ['PAdES_BASELINE_T', 'PAdES_BASELINE_LT', 'PAdES_BASELINE_LTA'], 
              'XAdES': ['XAdES_BASELINE_T', 'XAdES_BASELINE_LT', 'XAdES_BASELINE_LTA']}


def extendDocumentMenu():
    signed_file = input('Signed file: ')
    original_file = input('Original file: ')
    container = input('Container (No, ASiC-S, ASiC-E): ')
    while True:
        sig_format = input('Signature format (CAdES, PAdES, XAdES): ')
        if verify(container,sig_format):
            break
        else:
            print("If you choose the container ASiC-S or ASiC-E, you can't choose the PAdES signature format.")
    level = input('Level {}:'.format(sig_levels[sig_format]))
    extendDocument(signed_file, original_file, container, sig_format, level)
    print("press enter to continue")
    input()

def verify(container,sig_format):
    if (container == 'ASiC-S' or container == 'ASiC-E') and sig_format == 'PAdES':
        return False
    else:
         return True
    
def extendDocument(signed_file, original_file, container, sig_format, level):

    #Reading file to be signed in byte format
    with open(signed_file, 'rb') as f:
        file_bytes = f.read()

    if(not level in sig_levels[sig_format]):
        raise Exception('Level {} not valid for signature format {}. Select between {}'.format(level, sig_format, sig_levels[sig_format]))

    #Reading JSON from a File
    with open('application/json/extendDocumentRequest.json', 'r') as json_file:
        params = json.load(json_file)
        params['toExtendDocument']['bytes'] = base64.encodebytes(file_bytes).decode('ascii')
        if(container == 'No'):
            params['parameters']['asicContainerType'] = None
        else:
            params['parameters']['asicContainerType'] = container
        params['parameters']['signatureLevel'] = level
        file_name_parts = signed_file.split('/')
        file_name = file_name_parts[len(file_name_parts) - 1]
        params['toExtendDocument']['name'] = file_name
    
    resp = requests.post('http://10.0.0.101:8080/services/rest/signature/one-document/extendDocument', json=params)

    with open('application/extend_resp.json','w') as json_ex:
        json_ex.write(json.dumps(resp.json(), indent=4, sort_keys=True))

    print(resp.status_code)

def validateSignatureMenu():
    signed_file = input('Signed file: ')
    original_file = input('Original file: ')
    validateSignature(signed_file, original_file)
    print("press enter to continue")
    input()

def validateSignature(signed_file, original_file):

    #Reading file to be signed in byte format
    with open(signed_file, 'rb') as f:
        file_bytes = f.read()

    #Reading JSON from a File
    with open('application/json/validateSignatureRequest.json', 'r') as json_file:
        params = json.load(json_file)
        params['signedDocument']['bytes'] = base64.encodebytes(file_bytes).decode('ascii')
        file_name_parts = signed_file.split('/')
        file_name = file_name_parts[len(file_name_parts) - 1]
        params['signedDocument']['name'] = file_name

    resp = requests.post('http://10.0.0.101:8080/services/rest/validation/validateSignature', json=params)
    resp = resp.json()
    signature_simple_report = resp["simpleReport"]
    signature_details = signature_simple_report["signature"][0]
    print("--------------------------------------------------------------------------------------------------")
    print("\t Validation results for signature " + signature_simple_report["documentName"] + ":")
    print("\t Validation status: " + signature_details["indication"])
    print("\t Validation status description: " + signature_details["signatureLevel"]["description"])
    print("\t File signed by: " + signature_details["signedBy"])
    print("\n")
    print("\t CERTIFICATE CHAIN:")
    certificates = signature_details["certificateChain"]["certificate"]
    i = 1
    for cert in certificates:
        print("\t\t Certificate " + str(i) + ":")
        print("\t\t\t ID: " + cert["id"])
        print("\t\t\t Entity Name: " + cert["qualifiedName"])
        i += 1
    warnings = signature_details["warnings"]
    if warnings:
        print("\n")
        print("\t WARNINGS: ")
        i = 1
        for w in warnings:
            print("\t\t Warning " + str(i))
            print("\t\t\t" + w)
            i += 1



    print("--------------------------------------------------------------------------------------------------")

def main(args):
    if args.service is None:
        options = [("Extend a signature",   extendDocumentMenu),
                   ("Validate a signature", validateSignatureMenu),
                   ("Close",                menu.Menu.CLOSE)]
        mainMenu = menu.Menu(title="DSS : Digital Signature Service", options=options)
        mainMenu.open()
    elif args.service == 'extendDocument':
        extendDocument(args.signed_file, args.original_file, args.container, args.sig_format, args.level)
    elif args.service == 'validateSignature':
        validateSignature(args.signed_file, args.original_file)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='DSS : Digital Signature Service')
    subparsers = parser.add_subparsers(title='service', dest='service', help='rest web service')

    extendDocument_parser = subparsers.add_parser('extendDocument',
                                                    help='the method allows to extend an existing signature to a stronger level')
    extendDocument_parser.add_argument('--signed-file', '-f', required=True, metavar='signed-file', help='signed file')
    extendDocument_parser.add_argument('--original-file', '-o', required=False, metavar='original-file', help='original file(s)')
    extendDocument_parser.add_argument('--container', '-c', choices=['No', 'ASiC-S', 'ASiC-E'], default='No', metavar='container', help='container')
    extendDocument_parser.add_argument('--sig-format', choices=['CAdES', 'PAdES', 'XAdES'], required=True, metavar='sig-format', help='signature format')
    extendDocument_parser.add_argument('--level', '-l', required=True, metavar='level', help='level')
    
    validateSignature_parser = subparsers.add_parser('validateSignature',
                                                    help='this service allows to validate signature (all formats/types) against a validation policy.')
    validateSignature_parser.add_argument('--signed-file', '-f', required=True, metavar='signed-file', help='signed file')
    validateSignature_parser.add_argument('--original-file', '-o', required=True, metavar='original-file', help='original file(s)')
    
    args = parser.parse_args()
    main(args)