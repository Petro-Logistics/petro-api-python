# Copyright (c) 2021 Petro-Logistics S.A., All rights reserved.
# 
# This work is licensed under the terms of the MIT license.  
# For a copy, see <https://opensource.org/licenses/MIT>.

from plapi.client import PLAPIClient

# Initialize PLAPIClient object with "test user" credentials and "aggregatemovementsdata" report type
plapiclient = PLAPIClient(
            api_url="https://secure.petro-logistics.com/api/v2/aggregatemovementsdata",
            api_key="37rspm6j39td23nh0o2v0h78",
            api_hash="P0iwW39qaMvTjFRdcmsiKmD9OxGEquHNXapwbSQr8gbuV2ssqjbt0Vy7Yelyi4C1",
            http_user="testuser_http_CuH68Omfx17R",
            http_pass="X9PV5EmJPr88lEyjD2I2IE26b9ElQCX0"
        )

print("Executing PLAPIClient Query")

# Execute PLAPIClient object with saved query "Angola_Test_Data"
result = plapiclient.execute("Angola_Test_Data")

print(result["envelope"]["header"])
