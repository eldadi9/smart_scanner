import requests

RAINFOREST_API_KEY = "38479FE55DB942CE93FB21C6BE0D0C3B"

def search_amazon(query):
    url = "https://api.rainforestapi.com/request"
    params = {
        "api_key": RAINFOREST_API_KEY,
        "type": "search",
        "amazon_domain": "amazon.com",
        "search_term": query
    }

    response = requests.get(url, params=params)
    print("RAINFOREST AMAZON:", response.status_code, response.text)

    if response.status_code == 200:
        return response.json().get("search_results", [])
    else:
        return []
