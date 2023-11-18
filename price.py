import pandas as pd
import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.pricing as pricing

accountID = "101-001-26231816-001"
access_token = "e498e28946731fbce23b09fc3bd50d09-cea6d8762bafefb600198e685cad980b"
api = API(access_token = access_token)

params = {
    "instruments": "EUR_USD"
}

r = pricing.PricingInfo(accountID=accountID, params=params)
rv = api.request(r)
print(r.response)