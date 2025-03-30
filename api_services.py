import requests

RAINFOREST_API_KEY = "38479FE55DB942CE93FB21C6BE0D0C3B"

def search_amazon(query):
    from urllib.parse import quote_plus
    search_term = quote_plus(query)

    url = "https://api.rainforestapi.com/request"
    params = {
        "api_key": RAINFOREST_API_KEY,
        "type": "search",
        "amazon_domain": "amazon.com",
        "search_term": search_term,
        "language": "en",
        "page": 1
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        print("🔍 API Response:", data)  # 🟢 הוספת הדפסה

        results = []
        for product in data.get("search_results", []):
            results.append({
                "title": product.get("title"),
                "price": product.get("price", {}).get("value"),
                "currency": product.get("price", {}).get("currency"),
                "was_price": product.get("list_price", {}).get("value"),
                "coupon": product.get("coupon"),
                "rating": product.get("rating"),
                "brand": product.get("brand") or product.get("manufacturer"),
                "image": product.get("image"),
                "link": product.get("link")
            })

        return results

    except Exception as e:
        print("❌ Error:", e)
        return []
