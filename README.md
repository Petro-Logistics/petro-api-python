###### Python API CLient of Petro-Logisitics
[![License](https://img.shields.io/github/license/petro-logistics/petro-api-python.svg)](LICENSE)
# Python API CLient of Petro-Logisitics
This module is a Python API client (with examples) for retrieving data with the [Petro-Logistics API](https://secure.petro-logistics.com/client/api).

---

## Index
- [Windows Instructions](instructions/windows.md)
  - [Install](instructions/windows.md#install)
  - [Use](instructions/windows.md#use)
- [Ubuntu Instructions](instructions/ubuntu.md)
  - [Install](instructions/ubuntu.md#install)
  - [Use](instructions/ubuntu.md#use)
- [RHES & CentOS Instructions](instructions/rhes_centos.md)
  - [Install](instructions/rhes_centos.md#install)
  - [Use](instructions/rhes_centos.md#use)
- [Additional Informations](#additional-informations)
  - [Examples](#examples)
  - [PLAPIClient Parameters](#plapiclient-informations)

## Additional Informations
- ### Examples
  To test and have a base to start using our API with `Python` scripts, you can use this following examples
  - [Simple Example](https://github.com/Petro-Logistics/petro-api-python/blob/master/examples/test_example.py)
  - [Pandas Example](https://github.com/Petro-Logistics/petro-api-python/blob/master/examples/test_example_pandas.py)
- ### PLAPIClient Parameters
  To use examples or personal python files, you will need to initialize and call the object `PLAPIClient` according to the parameters below
  - 5 initialization parameters
    - api_url
    - api_user
    - api_password
    - api_key
    - api_hash
    ```
    plapiclient = PLAPIClient(
      api_url="https://secure.petro-logistics.com/api/v2/requested_report_type",
      api_key="your_api_key",
      api_hash="your_api_hash",
      http_user="your_http_user",
      http_pass="your_http_password"
    )
    ```
  - 1 call parameter
    - query_name
    ```
    result = plapiclient.execute("requested_query_name")
    ```
