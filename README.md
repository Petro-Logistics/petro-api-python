[![License](https://img.shields.io/github/license/petro-logistics/petro-api-python.svg)](LICENSE)
# README
---

## Python API CLient
This module is a Python API client (with examples) for retrieving data with with the [Petro-Logistics API](https://secure.petro-logistics.com/client/api).


## Dependencies
- Ubuntu
    ```
    sudo apt-get install python3 python3-pip git
    ```
- RHES & CentOS
    ```
    yum install python3 python3-pip git
    ```
- Windows
    - Download and install [Python 3](https://www.python.org/downloads/windows/) ("Python 3" & "pip" included in version 3.4 or greater).
    - Download and install [git](https://git-scm.com/download/win).

## Install
- With pip
    ```
    pip install git+https://github.com/Petro-Logistics/petro-api-python
    ```
- Manually
    ```
    git clone https://github.com/Petro-Logistics/petro-api-python.git
    cd petro-api-python
    python setup.py install
    ```


## Parameters
- **PLAPIClient** is initialized with 5 parameters:
    - api_url
    - api_user
    - api_password
    - api_key
    - api_hash


- **PLAPIClient** is called with 1 parameter:
    - query_name


## Usage
- ### Initialization
    ```python
    plapiclient = PLAPIClient(
        api_url="https://secure.petro-logistics.com/api/v2/requested_report_type",
        api_key="your_api_key",
        api_hash="your_api_hash",
        http_user="your_http_user",
        http_pass="your_http_password"
    )
    ```


- ### Execution
    ```python
    result = plapiclient.execute("query_name")

    ```


## Examples
1. An example of how to test/use PLAPIClient is available in **test_example.py** located [here](examples/test_example.py)
2. An other example of how to test/use PLAPIClient with "Pandas" Library is available in **test_example_pandas.py** located [here](examples/test_example_pandas.py)