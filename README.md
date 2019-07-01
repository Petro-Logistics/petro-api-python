README
======

This project is a Python API client (with example script) for retrieving data with Petro Logistics API.


Parameters
----------

**PetroAPI** is initialized with 5 parameters:

- api_url
- api_user
- api_password
- api_key
- api_hash


**PetroAPI** is called with 1 parameter:

- query_name


Usage
-----

### Initialization Example
    
    apiclient = PetroAPI(
            api_url="https://secure.petro-logistics.com/api/v2/movementsdata",
            api_key="api_key",
            api_hash="api_hash",
            http_user="user_http_123456",
            http_pass="user_password"
        )


### Execute Example

    result = apiclient.execute("xyz_query")


Example
-------
An example of how to test/use PetroAPI is available in **example.py** located [here](https://git.petro-logistics.com/api-examples/petro-api-python/tree/master)
