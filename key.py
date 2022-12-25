
#INSERT YOUR API KEY HERE!
#YOU CAN RECIEVE YOUR API KEY FROM https://finnhub.io
api_key = ""

TICKER ="MSFT"

BASE_URL = 'https://finnhub.io/api/v1/quote'

PARAMS = dict(token=api_key, metric='all', symbol=TICKER)
print(BASE_URL, PARAMS)