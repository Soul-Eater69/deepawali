
import requests


url1 = 'http://127.0.0.1:5000/historicData'
url = 'https://deepawali-api-test.up.railway.app/historicData'
hh = 'https://www.deepawaliseotips.com/'
gg = 'https://pmjandhanyojana.co.in/'
myobj = {'keywords':'tesla model s','country':'IN'}

x = requests.post(url1, json = myobj)

print(x.json())

""" 
import pandas as pd
import requests, json, itertools,time
import numpy as np


from pytrends.request import TrendReq
def related_keywords(keyword):
    trend = TrendReq()
    keyword = [f"{keyword}"]             
    trend.build_payload(kw_list=keyword,timeframe='2021-01-24 2023-01-15')    
    data = trend.interest_over_time()

    data['month'] = pd.to_datetime(data.index).to_period('M')
    data[keyword[0]] = data[keyword[0]].replace(0, np.nan)
    data[keyword[0]] = data[keyword[0]].fillna(data[keyword[0]].median())

    monthly_data = data.groupby(by='month').sum()

    monthly_data['percentage_difference'] = (monthly_data[keyword[0]]-monthly_data[keyword[0]].shift(1))/monthly_data[keyword[0]].shift(1)*100
    return monthly_data

print(related_keywords('tesla'))

#print(related_keywords('tesla model 3'))
def makeRequest(query,country):
    url = "http://suggestqueries.google.com/complete/search"
    params = {
        "client":"firefox",
        "hl":country,
        "q":query
    }
    headers = {'User-agent':'Mozilla/5.0'}
    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code == 200:
        searches = json.loads(response.content.decode('utf-8'))[1]
        return searches
    else:
        return 'ERR'

def getSuggests(keyword):
    time.sleep(4)
    charList = 'abcdefghijklmnopqrstuvwxyz0123456789'
    queryList = [keyword+' '+char for char in charList]
    suggestions = []
    for query in queryList:
        suggestion = makeRequest(query,'US')
        if suggestion!='ERR':
            suggestions.append(suggestion)
    suggestions = [x for sublist in suggestions for x in sublist]

    if "" in suggestions:
        suggestions.remove('')
    return suggestions

import requests
import re

def get_keywords(brands):
    # List of characters to loop through
    characters = list("abcdefghijklmnopqrstuvwxyz0123456789")

    # Initialize empty list to store keywords
    keywords = []

    # Loop through brand names
    for brand in brands:
        # Loop through characters
        for char in characters:
            # Send GET request to Google Autosuggest with brand name and character
            url = f"https://suggestqueries.google.com/complete/search?client=firefox&q={brand}+review+{char}"
            response = requests.get(url)

            # Extract keywords from response
            suggestions = response.json()[1]

            # Add suggestions to keywords list
            keywords.extend(suggestions)

    # Remove duplicates
    keywords = list(set(keywords))
    # Clean keywords using regular expressions
    pattern = re.compile(r"review")
    cleaned_keywords = [re.sub(pattern, "", keyword) for keyword in keywords]

    return cleaned_keywords


def get_valid_suggestions(keyword, suggestions):
    valid_suggestions = []
    for suggestion in suggestions:
        if keyword in suggestion:
            valid_suggestions.append(suggestion)
    return valid_suggestions

def get_search_suggestions(brands):
    characters = list("abcdefghijklmnopqrstuvwxyz0123456789")
    keywords = []
    for brand in brands:
        for char in characters:
            # Send GET request to Google Autosuggest with brand name and character
            url = f'https://clients1.google.com/complete/search?client=youtube&gs_ri=youtube&ds=yt&q={brand}+{char}'
            response = requests.get(url).text
            suggestions = re.findall(r'\"([^\"]+)\"', response)
            # Add suggestions to keywords list
            keywords.extend(suggestions)

        keywords = list(set(keywords))

        keywords = [keyword for keyword in keywords if brand in keyword]

    if " " in keywords:
        keywords.remove(' ')
    return keywords
 """


#print(get_search_suggestions(['hugo boss']))

