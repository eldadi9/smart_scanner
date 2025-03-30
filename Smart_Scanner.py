from flask import Flask, request, jsonify, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)  # ← יש להגדיר את app כאן למעלה

@app.route('/')
def home():
    return render_template('index.html')

def search_aliexpress(query):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    search_url = f"https://www.aliexpress.com/wholesale?SearchText={query}"
    response = requests.get(search_url, headers=headers)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    products = []

    for item in soup.select('.manhattan--container--1lP57Ag'):
        title = item.select_one('.manhattan--titleText--WccSjUS')
        price = item.select_one('.manhattan--price-sale--1CCSZfK')
        link = item.find('a', href=True)

        if title and price and link:
            products.append({
                'title': title.text.strip(),
                'price': price.text.strip(),
                'url': "https:" + link['href']
            })

    return products

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'Missing query'}), 400

    results = search_aliexpress(query)
    return jsonify({'results': results})




if __name__ == '__main__':
    app.run(debug=True)
