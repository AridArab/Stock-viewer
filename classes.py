from flask import Flask, render_template, request
import requests
import json
from key import api_key
from urls import BASE_URL, BASE_URL_NAME, BASE_URL_LOBBY, BASE_URL_QUOTE

class finnhub_call():
    '''Class system for calling the api'''
    def __init__(self, para, url):
        self.para = para
        self.url = url
    
    # Method to get the entire json file for the api
    def get_json(self):
        return requests.get(self.url, params = self.para).json()

    # Method to get the total amount of money that a company lobbys in one year total starting a year before.
    def average_lobby(self):
        total_lobby = int()
        for x in self.get_json()['data']:
            if x['income'] != None:
                total_lobby += int(x['income'])
        return total_lobby
