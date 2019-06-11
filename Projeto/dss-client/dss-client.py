import sys
import requests
import argparse
import menu
import json

sig_levels = {'CAdES': ['CAdES-BASELINE-T', 'CAdES-BASELINE-LT', 'CAdES-BASELINE-LTA'],
              'PAdES': ['PAdES-BASELINE-T', 'PAdES-BASELINE-LT', 'PAdES-BASELINE-LTA'], 
              'XAdES': ['XAdES-BASELINE-T', 'XAdES-BASELINE-LT', 'XAdES-BASELINE-LTA']}


def extendDocumentMenu():
    signed_file = input('Signed file: ')
    original_file = input('Original file: ')
    container = input('Container (No, ASiC-S, ASiC-E): ')
    sig_format = input('Signature format (CAdES, PAdES, XAdES): ')
    level = input('Level {}:'.format(sig_levels[sig_format]))
    extendDocument(signed_file, original_file, container, sig_format, level)
    print("press enter to continue")
    input()
    
def extendDocument(signed_file, original_file, container, sig_format, level):
    #Temos que passar um certificado para extender a assinatura do documento?

    if(not level in sig_levels[sig_format]):
        raise Exception('Level {} not valid for signature format {}. Select between {}'.format(level, sig_format, sig_levels[sig_format]))

    #Reading JSON from a File
    with open('application/json/extendDocumentRequest.json', 'r') as json_file:
        params = json.load(json_file)
        params['asicContainerType'] = str(container)
        params['signatureLevel'] = str(level)
    
    #Request Headers
    #POST /services/rest/signature/one-document/extendDocument HTTP/1.1
    #Accept: application/json, application/javascript, text/javascript, text/json
    #Content-Type: application/json; charset=UTF-8
    #Host: localhost:8080
    #Content-Length: 8677
    
    resp = requests.post('http://localhost:8080/services/rest/signature/one-document/extendDocument', json=params)
    
    #Response Headers
    #HTTP/1.1 200 OK
    #Date: Wed, 21 Nov 2018 09:55:05 GMT
    #Content-Type: application/json
    #Transfer-Encoding: chunked
    #Content-Length: 10552

    print(resp.status_code)

def validateSignatureMenu():
    params = dict()
    params['service'] = 'validateSignature'
    main(params)

def validateSignature():

    #Reading JSON from a File
    with open('application/json/validateSignatureRequest.json', 'r') as json_file:
        params = json.load(json_file)

    #Request Headers
    #POST /services/rest/validation/validateSignature HTTP/1.1
    #Accept: application/json, application/javascript, text/javascript, text/json
    #Content-Type: application/json; charset=UTF-8
    #Host: localhost:8080
    #Content-Length: 7495

    resp = requests.post('http://localhost:8080/services/rest/validation/validateSignature', json=params)

    #Response Headers
    #HTTP/1.1 200 OK
    #Date: Wed, 21 Nov 2018 09:55:06 GMT
    #Content-Type: application/json
    #Transfer-Encoding: chunked
    #Content-Length: 31957

    print(resp)

def main(args):
    # Falta executar direito quando apenas se executa o programa como: python3 dss-client.py. Se inserirmos 1 para assinar, o programa crasha.
    if args.service is None:
        options = [("Extend a signature",   extendDocumentMenu),
                   ("Validate a signature", validateSignatureMenu),
                   ("Close",                menu.Menu.CLOSE)]
        mainMenu = menu.Menu(title="DSS : Digital Signature Service", options=options)
        mainMenu.open()
    elif args.service == 'extendDocument':
        extendDocument(args.signed_file, args.original_file, args.container, args.sig_format, args.level)
    elif args.service == 'validateSignature':
        validateSignature()
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='DSS : Digital Signature Service')
    subparsers = parser.add_subparsers(title='service', dest='service', help='rest web service')

    extendDocument_parser = subparsers.add_parser('extendDocument',
                                                    help='the method allows to extend an existing signature to a stronger level')
    extendDocument_parser.add_argument('--signed-file', '-f', required=True, metavar='signed-file', help='signed file')
    extendDocument_parser.add_argument('--original-file', '-o', required=True, metavar='original-file', help='original file(s)')
    extendDocument_parser.add_argument('--container', '-c', choices=['No', 'ASiC-S', 'ASiC-E'], default='No', metavar='container', help='container')
    extendDocument_parser.add_argument('--sig-format', choices=['CAdES', 'PAdES', 'XAdES'], required=True, metavar='sig-format', help='signature format')
    extendDocument_parser.add_argument('--level', '-l', required=True, metavar='level', help='level')
    
    validateSignature_parser = subparsers.add_parser('validateSignature',
                                                    help='this service allows to validate signature (all formats/types) against a validation policy.')
    validateSignature_parser.add_argument('--signed-file', '-f', required=True, metavar='signed-file', help='signed file')
    validateSignature_parser.add_argument('--original-file', '-o', required=True, metavar='original-file', help='original file(s)')
    
    args = parser.parse_args()
    main(args)