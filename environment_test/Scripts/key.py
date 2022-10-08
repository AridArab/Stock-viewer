api_key = "ccdm7m2ad3i9bqco35kg"

TICKER ="MSFT"

BASE_URL = 'https://finnhub.io/api/v1/quote'

PARAMS = dict(token=api_key, metric='all', symbol=TICKER)
print(BASE_URL, PARAMS)