from flask import Flask, render_template, request
import requests
import json
from classes import finnhub_call
from key import api_key
from urls import BASE_URL, BASE_URL_NAME, BASE_URL_QUOTE, BASE_URL_LOBBY
from date import DATE_PAST, DATE_NOW

# Defining the Flask app
app = Flask(__name__)

# Route for the stock info, uses the POST method to show info
@app.route("/stock_info", methods=["POST"])
def display():
    
    # Requests the ticker/symbol that was entered in the index
    ticker = request.form['tick']
    
    params_price = dict(token=api_key, symbol=ticker, metric='all')
    params_info = dict(token=api_key, symbol=ticker)
    params_lobby = {"token":api_key, "symbol":ticker, "from":DATE_PAST, "to":DATE_NOW}
    quote_info = finnhub_call(params_info, BASE_URL_QUOTE)
    company_info = finnhub_call(params_price, BASE_URL_NAME)
    lobby_info = finnhub_call(params_lobby, BASE_URL_LOBBY)

    # Checks to see if the info taken from the api call is correct and viewable, other wise returns a KeyError due to info not being found
    try:
        c_price, h_price, l_price, corp, lobby_inc = quote_info.get_json()['c'], quote_info.get_json()['h'], quote_info.get_json()['l'], company_info.get_json()['name'], lobby_info.average_lobby()
    except KeyError:
        # Renders the error html file
        return render_template('error.html', wrong=ticker)
    # Renders the html file that displays all the info
    return render_template('stock_info.html', current=c_price, high=h_price, low=l_price, company=corp, money=lobby_inc)    

        
# Route for the index
@app.route("/")
def index():
    # Renders the index html file
    return render_template('index.html')

# Route used for testing
@app.route("/test")
# Function to return and display the full json file
def testing():
    ticker = 'MSFT'
    params_lobby = {"token":api_key, "symbol":ticker, "from":DATE_PAST, "to":DATE_NOW}
    lobby_info = finnhub_call(params_lobby, BASE_URL_LOBBY)
    return lobby_info.get_full_json()


# runs the code if the file is being run
if __name__ == "__main__":
    app.run(debug=True)
