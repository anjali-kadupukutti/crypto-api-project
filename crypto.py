import requests

def get_crypto(search):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    
    params = {
        "vs_currency": "usd",
        "per_page": 20,
        "page": 1
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    results = [coin for coin in data if search.lower() in coin["name"].lower()]
    
    if results:
        for coin in results:
            print(f"Name  : {coin['name']}")
            print(f"Price : ${coin['current_price']}")
            print("-------------------")
    else:
        print("No coin found!")

search = input("Enter coin name to search: ")
get_crypto(search)