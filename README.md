# README
---

## Python API CLient
This module is a Python API client (with an example script) for retrieving data with with the [Petro-Logistics API](https://secure.petro-logistics.com/client/api).


## Dependencies
### PLAPIClient is an Python module, so you need to install:
- Python3
- Python3-pip

## Install
### Installing dependencies
```
sudo apt-get install python3 python3-pip
git clone https://github.com/Petro-Logistics/petro-api-python-example.git
cd ./petro-api-python
sudo python3 setup.py install
```

### Running the example
```python
sudo python3 test_axample.py
```


## Parameters
**PLAPIClient** is initialized with 5 parameters:
- api_url
- api_user
- api_password
- api_key
- api_hash


**PLAPIClient** is called with 1 parameter:
- query_name


## Usage
### Initialization Example
```python
plapiclient = PLAPIClient(
    api_url="https://secure.petro-logistics.com/api/v2/requested_report_type",
    api_key="your_api_key",
    api_hash="your_api_hash",
    http_user="your_http_user",
    http_pass="your_http_password"
)
```


### Execute Example
```python
result = plapiclient.execute("query_name")

```


## Example
An example of how to test/use PLAPIClient is available in **test_example.py** located [here](test_example.py)
