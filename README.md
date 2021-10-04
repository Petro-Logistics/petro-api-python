[![License](https://img.shields.io/github/license/petro-logistics/petro-api-python.svg)](LICENSE)

# Python API CLient of Petro-Logistics
This module is a Python API client (with examples) for retrieving data with the [Petro-Logistics API](https://secure.petro-logistics.com/client/api).

## Setup

To install the module, follow the instructions based on your operating system:
- [Windows](instructions/windows.md)
- [Ubuntu](instructions/ubuntu.md)
- [RHES & CentOS](instructions/rhes_centos.md)

## Examples
To test and have a base to start using our API with Python scripts, you can use the following examples:
- [Simple Example](https://github.com/Petro-Logistics/petro-api-python/blob/master/examples/test_example.py)
- [Pandas Example](https://github.com/Petro-Logistics/petro-api-python/blob/master/examples/test_example_pandas.py)

## Troubleshooting
### Unauthorized HTTP error 401
- _**Message:**_
  ```
  requests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://secure.petro-logistics.com/api/v2/aggregatemovementsdata.php
  ```
- _**Solution:**_ Update firewall settings to trust the PL domain

### SSLError: certificate verify failed
- _**Message:**_
  ```
  SSLError: HTTPSConnectionPool(host=‘secure.petro-logistics.com’, port=443): Max retries exceeded with url: /api/v2/aggregatemovementsdata.php (Caused by SSLError(SSLError(“bad handshake: Error([(‘SSL routines’, ‘tls_process_server_certificate’, ‘certificate verify failed’)])“)))
  ```
- _**Additional infos:**_ The problem seems to be the same as above. Possible reasons:
  - You are using a self signed certificate for the resource you are accessing.
  - Your company intercepts and inspects HTTPS traffic; hence adding its own certificates at the top of the certificate chain.
- _**Solution:**_ Contact company’s IT team with above error and possible reasons.

### Certificate revocation error
- _**Message:**_
  ```
  fatal: unable to access ’https://github.com/Petro-Logistics/petro-api-python/’: schannel: next InitializeSecurityContext failed: Unknown error (0x80092012) - The revocation function was unable to check revocation for the certificate.
  ```
- _**Additional infos:**_ The problem seems to be in the Windows git configuration, or in the settings of the firewall. Possible solutions:
  - https://github.com/desktop/desktop/issues/2187#issuecomment-313309981
  - https://stackoverflow.com/questions/45556189/git-the-revocation-function-was-unable-to-check-revocation-for-the-certificate
- _**Solution:**_ Contact company’s IT team with above error and possible reasons.