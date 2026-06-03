# Crypto Price Checker 🪙
 
A Python script that fetches live cryptocurrency prices using the CoinGecko API.
 
## What it does
- Fetches real-time crypto prices from CoinGecko API
- Lets you search for any cryptocurrency by name
- Displays the current price in USD
## Requirements
- Python 3.x
- `requests` library
## Installation
 
1. Clone the repo:
```
git clone https://github.com/anjali-kadupukutti/crypto-api-project
```
 
2. Install the required library:
```
pip install requests
```
 
## How to Run
 
```
python crypto.py
```
 
Then type a coin name like `bitcoin`, `ethereum`, `dogecoin`, or `solana`.
 
## Sample Output
 
```
Enter coin name to search: bitcoin
Name  : Bitcoin
Price : $66974
-------------------
 
Enter coin name to search: ethereum
Name  : Ethereum
Price : $1865.45
-------------------
```
 
## Code
 
```python
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
```
 
## API Used
- [CoinGecko API](https://api.coingecko.com) - Free, no API key needed!
## GitHub
[https://github.com/anjali-kadupukutti/crypto-api-project](https://github.com/anjali-kadupukutti/crypto-api-project)
