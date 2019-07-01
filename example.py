from plapi.client import PetroAPI
import pandas as pd

apiclient = PetroAPI(
            api_url="https://secure.petro-logistics.com/api/v2/aggregatemovementsdata",
            api_key="37rspm6j39td23nh0o2v0h78",
            api_hash="P0iwW39qaMvTjFRdcmsiKmD9OxGEquHNXapwbSQr8gbuV2ssqjbt0Vy7Yelyi4C1",
            http_user="testuser_http_CuH68Omfx17R",
            http_pass="X9PV5EmJPr88lEyjD2I2IE26b9ElQCX0"
        )

print("Executing PetroAPI Query")
result = apiclient.execute("Angola_Test_Data")

print(result["envelope"]["header"])

df = pd.DataFrame.from_dict(result["envelope"]["movements"])

print(df)
