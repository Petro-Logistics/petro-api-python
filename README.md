# README
---

## Python API CLient
This module is a Python API client (with an example script) for retrieving data with with the [Petro-Logistics API](https://secure.petro-logistics.com/client/api).


## Install
### install with pip
#### Dependencies
_UBUNTU_
```
sudo apt-get install python3 python3-pip
```
_RED HAT_
```
yum install python3 python3-pip
```


#### Installation
_UBUNTU & RED HAT_
```
pip install git+https://github.com/Petro-Logistics/petro-api-python
```


### Install manually
#### Dependencies
_UBUNTU_
```
sudo apt-get install python3 git

```
_RED HAT_
```
yum install python3 git
```
_WINDOWS_    
Download and install [Python 3](https://www.python.org/downloads/windows/) ("Python 3" & "pip" included in version 3.4 or greater)


#### Installation
_Ubuntu & RED HAT_
```
git clone https://github.com/Petro-Logistics/petro-api-python-example.git
sudo python3 ../petro-api-python/setup.py install
```
_WINDOWS_    
1. Download and extract [petro-api-python](https://github.com/Petro-Logistics/petro-api-python/archive/master.zip) module
2. And finally install it:
```
python ..\petro-api-python-master\setup.py install
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
### Initialization
```python
plapiclient = PLAPIClient(
    api_url="https://secure.petro-logistics.com/api/v2/requested_report_type",
    api_key="your_api_key",
    api_hash="your_api_hash",
    http_user="your_http_user",
    http_pass="your_http_password"
)
```


### Execution
```python
result = plapiclient.execute("query_name")

```


## Example
An example of how to test/use PLAPIClient is available in **test_example.py** located [here](test_example.py)
### Dependencies
#### Install with pip
_UBUNTU & RED HAT & WINDOWS_
```
pip install pandas
```

#### Install manually
_UBUNTU_
```
sudo apt-get install python3-pandas
```
_RED HAT_
```
yum install python3-pandas
```

### Running example
```
sudo python3 test_axample.py
```
