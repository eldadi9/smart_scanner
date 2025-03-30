from flask import Flask, request, jsonify, render_template
from api_services import search_amazon

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'Missing query'}), 400

    amazon_results = search_amazon(query)

    return jsonify({
        "amazon": amazon_results
    })

if __name__ == '__main__':
    app.run(debug=True)
