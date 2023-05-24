# Copyright (c) 2023 Petro-Logistics S.A., All rights reserved.
# 
# This work is licensed under the terms of the MIT license.  
# For a copy, see <https://opensource.org/licenses/MIT>.

# To run this example you need to install the 'pandas' package (Check the corresponding instalaltion procedure)
from plapi.client import PLAPIClient
import pandas as pd

# Initialize PLAPIClient object with "test user" credentials and "aggregatemovementsdata" report type
plapiclient = PLAPIClient(
            api_url="https://secure.petro-logistics.com/api/v3/aggregatemovementsdata",
            api_key="37rspm6j39td23nh0o2v0h78",
            api_hash="d1Npusz7BrVDauza7b7v5swgV20uiXQwiCG6nxiPseWRda6mTfJBeByKZsvp5sNX",
            http_user="testuser_http_kRQNk5878ezA",
            http_pass="F268DBvvPCBV83eT1vIeTpBGrJD604K2"
        )

print("Executing PLAPIClient Query")

# Execute PLAPIClient object with saved query "Angola_Test_Data"
result = plapiclient.execute("Angola_Test_Data")

print(result["envelope"]["header"])

# Initialize pandas object with API result
df = pd.DataFrame.from_dict(result["envelope"]["movements"])

print(df)

# [ EXPORTING TO JSON ]
# - Export pandas dataframe object to a "JSON" file: df.to_json(r"filename.json")
# - Uncomment next line to test JSON export
# df.to_json(r"today.json")

# [ EXPORTING TO CSV ]
# - Export pandas dataframe object to a "CSV" file: df.to_csv(r"filename.csv")
# - Uncomment next line to test CSV export
# df.to_csv(r"today.csv")

# [ EXPORTING TO XLSX ]
# - Export pandas dataframe to a "XLSX" file: df.to_excel(r"filename.xlsx")
# - To run this example you need to install the 'openpyxl' package (Check the corresponding instalaltion procedure)
# - Uncomment next line to test XLSX export
# df.to_excel(r"today.xlsx")

# [ EXECUTING MORE THAN 1 QUERY ]
# To execute more than one query/api, you can use 1 of the following proposals:
#   1. Creating copies of this example file for each desired query (By filling in the corresponding parameters on each file)
#
#   2. By repeating a part of the code in this same file to execute other queries for the same api_url, like this:
#
#      result = plapiclient.execute("query_2")
#      print(result["envelope"]["header"])
#      df = pd.DataFrame.from_dict(result["envelope"]["movements"])
#      print(df)
#
#   3. By repeating corresponding code in this same file to execute other queries for another api_url, like this:
#
#      plapiclient = PLAPIClient(
#                  api_url="https://secure.petro-logistics.com/api/v3/other_desired_api",
#                  api_key="37rspm6j39td23nh0o2v0h78",
#                  api_hash="P0iwW39qaMvTjFRdcmsiKmD9OxGEquHNXapwbSQr8gbuV2ssqjbt0Vy7Yelyi4C1",
#                  http_user="testuser_http_CuH68Omfx17R",
#                  http_pass="X9PV5EmJPr88lEyjD2I2IE26b9ElQCX0"
#              )
#
#      result = plapiclient.execute("other_desired_query")
#      print(result["envelope"]["header"])
#      df = pd.DataFrame.from_dict(result["envelope"]["movements"])
#      print(df)
