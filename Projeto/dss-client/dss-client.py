import sys
import requests
import argparse
import menu
import json
import base64
import os

sig_levels = {'CAdES': ['CAdES_BASELINE_T', 'CAdES_BASELINE_LT', 'CAdES_BASELINE_LTA'],
              'PAdES': ['PAdES_BASELINE_T', 'PAdES_BASELINE_LT', 'PAdES_BASELINE_LTA'], 
              'XAdES': ['XAdES_BASELINE_T', 'XAdES_BASELINE_LT', 'XAdES_BASELINE_LTA']}

# Interactive menu for document's signature extension
def extendDocumentMenu():
    signed_file = input('Signed file: ')

    # Read container and signature format information with error control to prevent unexpected program crashing.
    while True:
        container = input('Container (No, ASiC-S, ASiC-E): ')
        sig_format = input('Signature format (CAdES, PAdES, XAdES): ')
        result = verify(container,sig_format)
        if result == None:
            break
        elif result == "SIGNATURE_FORMAT_ERR":
            print("\nThe signature format must be one of the three: PAdES, CAdES, XAdES\n")
        elif result == "CONTAINER_SIG_FORMAT_ERR":
            print("\nIf you choose the container ASiC-S or ASiC-E, you can't choose the PAdES signature format.\n")
        elif result == "CONTAINER_ERR":
            print('\nContainer must be one of the three: No, ASiC-S, ASiC-E.\n')
    
    # Read signature level information with error control to prevent unexpected program crashing.
    while True:
        level = input('Level {}:'.format(sig_levels[sig_format]))
        if verify_level(sig_format,level):
            break
        else:
            print('\nPlease choose one of the signature levels presented on screen when demanded.\n')
    
    # Call function that request the web service for signature extension on the document with the received information.
    extendDocument(signed_file, container, sig_format, level)
    print("press enter to continue")
    input()

# Verifies that the signature level is correspondent to the signature format chosen.
def verify_level(sig_format,level):
    if level not in sig_levels[sig_format]:
        return False
    else: return True

# Verifies that both the container and the signature format are ok and are permitted together.
def verify(container,sig_format):
    if (container == 'ASiC-S' or container == 'ASiC-E') and sig_format == 'PAdES':
        return "CONTAINER_SIG_FORMAT_ERR"
    elif not(sig_format == 'PAdES' or sig_format == 'CAdES' or sig_format == 'XAdES'):
        return "SIGNATURE_FORMAT_ERR"
    elif not(container == 'No' or container == 'ASiC-S' or container == 'ASiC-E'):
        return "CONTAINER_ERR"
    else:
        return None


def extendDocument(signed_file, container, sig_format, level):

    # Read signed file, print error message and allow to return to menu if the path is not ok.
    if os.path.isfile(signed_file):
        with open(signed_file, 'rb') as f:
            file_bytes = f.read()
        
        signed_file_parts = signed_file.split('.')
        file_extension = signed_file_parts[len(signed_file_parts) - 1]

        # Read the JSON file representing an extension request to the web service and changing the information accordingly.
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

        # Fulfill the request to the webservice
        resp = requests.post('http://10.0.0.101:8080/services/rest/signature/one-document/extendDocument', json=params)
        print(resp.status_code)
        if resp:
            resp = resp.json()
            with open('application/extend_resp.' + file_extension,'wb') as pdf:
                # Save the document with the extended signature in the required format.
                pdf.write(base64.decodebytes(resp['bytes'].encode('ascii')))
                print('Document with extended signature saved in application/extends_resp.' + file_extension)
    else:
        print('\n The path inserted to the signed file is not correct!')

# Interactive menu for document's signature validation
def validateSignatureMenu():
    signed_file = input('Signed file: ')
    original_file = input('Original file: ')
    validateSignature(signed_file, original_file)
    print("press enter to continue")
    input()

def validateSignature(signed_file, original_file):

    # Read signed file, print error message if path is not ok.
    if os.path.isfile(signed_file):
        with open(signed_file, 'rb') as f:
            file_bytes = f.read()
        of = False
        
        # Read original file if information is given.
        if os.path.isfile(original_file):
            with open(signed_file,'rb') as f:
                original_file_bytes = f.read()
                of = True

        # Read the JSON file representing a validation request to the web service and changing the information accordingly.
        with open('application/json/validateSignatureRequest.json', 'r') as json_file:
            params = json.load(json_file)
            params['signedDocument']['bytes'] = base64.encodebytes(file_bytes).decode('ascii')
            file_name_parts = signed_file.split('/')
            file_name = file_name_parts[len(file_name_parts) - 1]
            params['signedDocument']['name'] = file_name
            if of:
                params['originalDocuments'][0]['bytes'] = base64.encodebytes(original_file_bytes).decode('ascii')
        # Fulfill the request to the web service
        resp = requests.post('http://10.0.0.101:8080/services/rest/validation/validateSignature', json=params)

        # Print a report of the validation properties in stdout.
        if resp:
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
    else:
        print('The path to the signed file is not correct!')

# Main function, providing different usage forms.
def main(args):
    if args.service is None:
        options = [("Extend a signature",   extendDocumentMenu),
                   ("Validate a signature", validateSignatureMenu),
                   ("Close",                menu.Menu.CLOSE)]
        mainMenu = menu.Menu(title="DSS : Digital Signature Service", options=options)
        mainMenu.open()
    elif args.service == 'extendDocument':
        extendDocument(args.signed_file, args.container, args.sig_format, args.level)
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