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

def signDocument(docpath):
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
            "name" : "RemoteDocument",
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
    resp = requests.post('http://localhost:8080/services/rest/validation?_wadl')
    print('Validade Signature: ' + resp)

def main(service):
    if service is None:
        options = [("Sign a document",      signDocument),
                   ("Extend a signature",   extendDocument),
                   ("Validate a signature", validateSignature),
                   ("Close",                menu.Menu.CLOSE)]
        mainMenu = menu.Menu(title="DSS : Digital Signature Service", options=options)
        mainMenu.open()
    getDataToSign()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='DSS : Digital Signature Service')
    parser.add_argument('--service', help='Functionality: signDocument, extendDocument, validateSignature')
    args = parser.parse_args()
    main(**args.__dict__)