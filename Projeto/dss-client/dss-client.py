import requests
import argparse
import menu

def getDataToSign():
    PARAMS = {
        "signWithExpiredCertificate" : "false",
        "generateTBSWithoutCertificate" : "false",
        "signatureLevel" : "CAdES_BASELINE_B",
        "signaturePackaging" : "ENVELOPING",
        "signatureAlgorithm" : "RSA_SHA256",
        "encryptionAlgorithm" : "RSA",
        "digestAlgorithm" : "SHA256",
        "referenceDigestAlgorithm" : "null",
        "maskGenerationFunction" : "null",
        "contentTimestampParameters" : {
            "digestAlgorithm" : "SHA256",
            "canonicalizationMethod" : "http://www.w3.org/2001/10/xml-exc-c14n#"
        },
        "signatureTimestampParameters" : {
            "digestAlgorithm" : "SHA256",
            "canonicalizationMethod" : "http://www.w3.org/2001/10/xml-exc-c14n#"
        },
        "archiveTimestampParameters" : {
            "digestAlgorithm" : "SHA256",
            "canonicalizationMethod" : "http://www.w3.org/2001/10/xml-exc-c14n#"
        },
        "signingCertificate" : {
            "encodedCertificate" : "MIIC6jCCAdKgAwIBAgIGLtYU17tXMA0GCSqGSIb3DQEBCwUAMDAxGzAZBgNVBAMMElJvb3RTZWxmU2lnbmVkRmFrZTERMA8GA1UECgwIRFNTLXRlc3QwHhcNMTcwNjA4MTEyNjAxWhcNNDcwNzA0MDc1NzI0WjAoMRMwEQYDVQQDDApTaWduZXJGYWtlMREwDwYDVQQKDAhEU1MtdGVzdDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMI3kZhtnipn+iiZHZ9ax8FlfE5Ow/cFwBTfAEb3R1ZQUp6/BQnBt7Oo0JWBtc9qkv7JUDdcBJXPV5QWS5AyMPHpqQ75Hitjsq/Fzu8eHtkKpFizcxGa9BZdkQjh4rSrtO1Kjs0Rd5DQtWSgkeVCCN09kN0ZsZ0ENY+Ip8QxSmyztsStkYXdULqpwz4JEXW9vz64eTbde4vQJ6pjHGarJf1gQNEc2XzhmI/prXLysWNqC7lZg7PUZUTrdegABTUzYCRJ1kWBRPm4qo0LN405c94QQd45a5kTgowHzEgLnAQI28x0M3A59TKC+ieNc6VF1PsTLpUw7PNI2VstX5jAuasCAwEAAaMSMBAwDgYDVR0PAQH/BAQDAgEGMA0GCSqGSIb3DQEBCwUAA4IBAQCK6LGA01TR+rmU8p6yhAi4OkDN2b1dbIL8l8iCMYopLCxx8xqq3ubZCOxqh1X2j6pgWzarb0b/MUix00IoUvNbFOxAW7PBZIKDLnm6LsckRxs1U32sC9d1LOHe3WKBNB6GZALT1ewjh7hSbWjftlmcovq+6eVGA5cvf2u/2+TkKkyHV/NR394nXrdsdpvygwypEtXjetzD7UT93Nuw3xcV8VIftIvHf9LjU7h+UjGmKXG9c15eYr3SzUmv6kyOI0Bvw14PWtsWGl0QdOSRvIBBrP4adCnGTgjgjk9LTcO8B8FKrr+8lHGuc0bp4lIUToiUkGILXsiEeEg9WAqm+XqO"
        },
        "certificateChain" : [ ],
        "detachedContents" : "null",
        "asicContainerType" : "null",
        "blevelParams" : {
            "trustAnchorBPPolicy" : "true",
            "signingDate" : "1542794107033",
            "claimedSignerRoles" : "null",
            "signaturePolicy" : "null",
            "commitmentTypeIndications" : "null",
            "signerLocation" : "null"
        },
        "toSignDocument" : {
            "bytes" : "SGVsbG8=",
            "digestAlgorithm" : "null",
            "name" : "merdas.txt",
            "mimeType" : "null"
        }
    }
    resp = requests.post('http://localhost:8080/services/rest/signature/one-document/getDataToSign', json=PARAMS)
    print(resp)

def signDocument(docpath, container, packaging, digest, allow_expired_certificate, add_timestamp):
    PARAMS = {
        "signWithExpiredCertificate" : "false",
        "generateTBSWithoutCertificate" : "false",
        "signatureLevel" : "CAdES_BASELINE_B",
        "signaturePackaging" : "ENVELOPING",
        "signatureAlgorithm" : "RSA_SHA256",
        "encryptionAlgorithm" : "RSA",
        "digestAlgorithm" : "SHA256",
        "referenceDigestAlgorithm" : "null",
        "maskGenerationFunction" : "null",
        "contentTimestampParameters" : {
            "digestAlgorithm" : "SHA256",
            "canonicalizationMethod" : "http://www.w3.org/2001/10/xml-exc-c14n#"
        },
        "signatureTimestampParameters" : {
            "digestAlgorithm" : "SHA256",
            "canonicalizationMethod" : "http://www.w3.org/2001/10/xml-exc-c14n#"
            },
        "archiveTimestampParameters" : {
            "digestAlgorithm" : "SHA256",
            "canonicalizationMethod" : "http://www.w3.org/2001/10/xml-exc-c14n#"
        },
        "signingCertificate" : {
            "encodedCertificate" :"MIIC6jCCAdKgAwIBAgIGLtYU17tXMA0GCSqGSIb3DQEBCwUAMDAxGzAZBgNVBAMMElJvb3RTZWxmU2lnbmVkRmFrZTERMA8GA1UECgwIRFNTLXRlc3QwHhcNMTcwNjA4MTEyNjAxWhcNNDcwNzA0MDc1NzI0WjAoMRMwEQYDVQQDDApTaWduZXJGYWtlMREwDwYDVQQKDAhEU1MtdGVzdDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMI3kZhtnipn+iiZHZ9ax8FlfE5Ow/cFwBTfAEb3R1ZQUp6/BQnBt7Oo0JWBtc9qkv7JUDdcBJXPV5QWS5AyMPHpqQ75Hitjsq/Fzu8eHtkKpFizcxGa9BZdkQjh4rSrtO1Kjs0Rd5DQtWSgkeVCCN09kN0ZsZ0ENY+Ip8QxSmyztsStkYXdULqpwz4JEXW9vz64eTbde4vQJ6pjHGarJf1gQNEc2XzhmI/prXLysWNqC7lZg7PUZUTrdegABTUzYCRJ1kWBRPm4qo0LN405c94QQd45a5kTgowHzEgLnAQI28x0M3A59TKC+ieNc6VF1PsTLpUw7PNI2VstX5jAuasCAwEAAaMSMBAwDgYDVR0PAQH/BAQDAgEGMA0GCSqGSIb3DQEBCwUAA4IBAQCK6LGA01TR+rmU8p6yhAi4OkDN2b1dbIL8l8iCMYopLCxx8xqq3ubZCOxqh1X2j6pgWzarb0b/MUix00IoUvNbFOxAW7PBZIKDLnm6LsckRxs1U32sC9d1LOHe3WKBNB6GZALT1ewjh7hSbWjftlmcovq+6eVGA5cvf2u/2+TkKkyHV/NR394nXrdsdpvygwypEtXjetzD7UT93Nuw3xcV8VIftIvHf9LjU7h+UjGmKXG9c15eYr3SzUmv6kyOI0Bvw14PWtsWGl0QdOSRvIBBrP4adCnGTgjgjk9LTcO8B8FKrr+8lHGuc0bp4lIUToiUkGILXsiEeEg9WAqm+XqO"
        },
        "certificateChain" : [ ],
        "detachedContents" : "null",
        "asicContainerType" : "null",
        "blevelParams" : {
            "trustAnchorBPPolicy" : "true",
            "signingDate" : "1542794106964",
            "claimedSignerRoles" : "null",
            "signaturePolicy" : "null",
            "commitmentTypeIndications" : "null",
            "signerLocation" : "null"
        },
        "signatureValue" : {
            "algorithm" : "RSA_SHA256",
            "value" : "AQIDBA=="
        },
        "toSignDocument" : {
            "bytes" : "SGVsbG8=",
            "digestAlgorithm" : "null",
            "name" : str(docpath),
            "mimeType" : "null"
        }
    }
    resp = requests.post('http://localhost:8080/services/rest/signature/one-document/signDocument', json=PARAMS)
    print(resp)
    
def extendDocument():
    PARAMS = {
        "signWithExpiredCertificate" : "false",
        "generateTBSWithoutCertificate" : "false",
        "signatureLevel" : "XAdES_BASELINE_T",
        "signaturePackaging" : "null",
        "signatureAlgorithm" : "RSA_SHA256",
        "encryptionAlgorithm" : "RSA",
        "digestAlgorithm" : "SHA256",
        "referenceDigestAlgorithm" : "null",
        "maskGenerationFunction" : "null",
        "contentTimestampParameters" : {
            "digestAlgorithm" : "SHA256",
            "canonicalizationMethod" : "http://www.w3.org/2001/10/xml-exc-c14n#"
        },
        "signatureTimestampParameters" : {
            "digestAlgorithm" : "SHA256",
            "canonicalizationMethod" : "http://www.w3.org/2001/10/xml-exc-c14n#"
        },
        "archiveTimestampParameters" : {
            "digestAlgorithm" : "SHA256",
            "canonicalizationMethod" : "http://www.w3.org/2001/10/xml-exc-c14n#"
        },
        "signingCertificate" : "null",
        "certificateChain" : [ ],
        "detachedContents" : [ {
            "bytes" : "77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4NCjxoOnRhYmxlIHhtbG5zOmg9Imh0dHA6Ly93d3cudzMub3JnL1RSL2h0bWw0LyI+DQoJPGg6dHI+DQoJCTxoOnRkPkhlbGxvPC9oOnRkPg0KCQk8aDp0ZD5Xb3JsZDwvaDp0ZD4NCgk8L2g6dHI+DQo8L2g6dGFibGU+",
            "digestAlgorithm" : "null",
            "name" : "sample.xml",
            "mimeType" : {
                "mimeTypeString" : "text/xml"
            }
        } ],
        "asicContainerType" : "null",
        "blevelParams" : {
            "trustAnchorBPPolicy" : "true",
            "signingDate" : "1542794104583",
            "claimedSignerRoles" : "null",
            "signaturePolicy" : "null",
            "commitmentTypeIndications" : "null",
            "signerLocation" : "null"
        }
    }
    resp = requests.post('http://localhost:8080/services/rest/signature/one-document/extendDocument', json=PARAMS)
    print(resp)

def validateSignature():
    resp = requests.post('http://localhost:8080/services/rest/validation/validateSignature')
    print(resp)

def main(args):
    if args.service is None:
        options = [("Sign a document",      signDocument),
                   ("Extend a signature",   extendDocument),
                   ("Validate a signature", validateSignature),
                   ("Close",                menu.Menu.CLOSE)]
        mainMenu = menu.Menu(title="DSS : Digital Signature Service", options=options)
        mainMenu.open()
    elif args.service == 'signDocument':
        signDocument(args.doc, args.container, args.packaging, args.digest, args.allow_expired_certificate, args.add_timestamp)
    elif args.service == 'extendDocument':
        extendDocument()
    elif args.service == 'validateSignature':
        validateSignature()
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='DSS : Digital Signature Service')
    subparsers = parser.add_subparsers(title='service', dest='service', help='rest web service')
    
    signDocument_parser = subparsers.add_parser('signDocument',
                                                    help='the method allows to generate the signed document with the received signature value')
    signDocument_parser.add_argument('--doc', metavar='document', required=True, help='path to the document')
    signDocument_parser.add_argument('--container', '-c', choices=['CAdES', 'PAdES', 'XAdES'], default='null', metavar='container', help='container type')
    signDocument_parser.add_argument('--packaging', '-p', choices=['EVELOPED', 'ENVELOPING', 'DETACHED', 'INTERNALLY DETATCHED'], default='ENVELOPING', metavar='packaging')
    #Maybe level argument
    signDocument_parser.add_argument('--digest', '-d', choices=['SHA1', 'SHA224', 'SHA256', 'SHA384', 'SHA512'], default='SHA256', metavar='digest', help='digest algorithm')
    signDocument_parser.add_argument('--allow-expired-certificate', choices=['false', 'true'], default='false', help='allow expired certificate')
    signDocument_parser.add_argument('--add-timestamp', choices=['false', 'true'], default='false', help='add a content timestamp')
    
    extendDocument_parser = subparsers.add_parser('extendDocument',
                                                    help='the method allows to extend an existing signature to a stronger level')
    #extendDocument arguments go here
    
    validateSignature_parser = subparsers.add_parser('validateSignature',
                                                    help='this service allows to validate signature (all formats/types) against a validation policy.')
    #validateSignature arguments go here
    
    args = parser.parse_args()
    main(args)