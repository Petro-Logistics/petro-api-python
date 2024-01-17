###### [Python API CLient of Petro-Logisitics](../README.md) > RHES & CentOS Instructions

# RHES & CentOS Instructions

## Index
[[_TOC_]]

## Install
1. Open a terminal in RHES/CentOS and and follow the steps below
2. Install `Python 3`, `PIP 3` and `Git`
    ```bash
    sudo yum install python3 python3-pip git
    ```
3. Install `Pandas` (Only if you want to use the Pandas example)
    ```bash
    sudo pip3 install pandas
    ```
4. Install `OpenPyXL` (Only if you want to export data to excel)
    ```bash
    sudo pip3 install openpyxl
    ```
5. Install `Python API CLient of Petro-Logisitics`
    - With `PIP 3`:
      ```bash
      pip3 install git+https://github.com/Petro-Logistics/petro-api-python
      ```
    - Manually
      ```bash
      git clone https://github.com/Petro-Logistics/petro-api-python.git
      cd petro-api-python
      python3 setup.py install
      ```

## Use
1. Download one of the following examples:
    - [Simple Example](https://github.com/Petro-Logistics/petro-api-python/blob/master/examples/test_example.py)
    - [Pandas Example](https://github.com/Petro-Logistics/petro-api-python/blob/master/examples/test_example_pandas.py)
2. Go to the downloaded file path
    ```bash
    cd path/to/downloaded/file
    ```
3. Execute the example without making modification
    ```bash
    python3 test_example.py
    ```
     or/and
    ```bash
    python3 test_example_pandas.py
    ```
4. Create a copy of the required example, renaming it
    ```bash
    cp test_example.py your_file_name.py
    ```
     or/and
    ```bash
    cp test_example_pandas.py your_file_name.py
    ```
5. Edit `your_file_name.py` and replace **`PLAPIClient`** example parameters with your required personal parameters
    - Initialized with 5 parameters: [^1] [^2]
      ```python
      plapiclient = PLAPIClient(
        api_url="https://secure.petro-logistics.com/api/v4/desired_report_type",
        api_key="your_api_key",
        api_hash="your_api_hash",
        http_user="your_http_user",
        http_pass="your_http_password"
      )
      ```
    - Called with 1 parameter: [^3]
      ```python
      result = plapiclient.execute("query_name")
      ```
6. Execute your copied file
    ```bash
    python3 your_file_name.py
    ```

---
---
[^1]:
    > - If you don't find your credentials, please contact our support!

[^2]:
    > - If you don't know what the **desired_report_type**, please contact our support
    > - e.g. of **desired_report_type**: ".../aggregatemovementsdata", ".../movementsdata", etc.

[^3]:
    > - If you don't find your **query_name**, please contact our support!
