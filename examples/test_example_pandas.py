# Copyright (c) 2021 Petro-Logistics S.A., All rights reserved.
# 
# This work is licensed under the terms of the MIT license.  
# For a copy, see <https://opensource.org/licenses/MIT>.

# To run this example you need to install the 'pandas' package (Check the corresponding instalaltion procedure)
from plapi.client import PLAPIClient
import pandas as pd

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

# Initialize pandas object with API result
df = pd.DataFrame.from_dict(result["envelope"]["movements"])

# Export pandas dataframe object to a "JSON" file: df.to_json(r"filename.json")
# Uncomment next line to test JSON export
# df.to_json(r"today.json")

# Export pandas dataframe object to a "CSV" file: df.to_csv(r"filename.csv")
# Uncomment next line to test CSV export
# df.to_csv(r"today.csv")

# Export pandas dataframe object to a "XLSX" file: df.to_excel(r"filename.xlsx")
# To run this example you need to install the 'openpyxl' package (Check the corresponding instalaltion procedure)
# Uncomment next line to test XLSX export
# df.to_excel(r"today.xlsx")

print(df)
