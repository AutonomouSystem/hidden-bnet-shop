import os
import json
import requests
from selectolax.parser import HTMLParser

username = input("Bnet Username")
password = intput("Bnet Password")

login_url = "https://us.battle.net/login/en/"
login_payload = {
    "accountName": username,
    "password": password,
    "submit": "Log in"
}

session = requests.Session()

login_response = session.post(login_url, data=login_payload)

if login_response.status_code == 200:
    print("Login successful!")
else:
    print("Login failed.")
    exit(1)

base_url = "https://us.battle.net/shop/en/checkout/buy/"
start_num = 879000
end_num = 900000 

data = {}

for num in range(start_num, end_num + 1):
    url = base_url + str(num)
    response = session.get(url)
    
    if response.status_code == 200:
        parser = HTMLParser(response.text)
        title_element = parser.css_first("p.product-name")
        if title_element:
            title = title_element.text()
            data[url] = title
        else:
            print(f"Title not found for URL: {url}")
    else:
        print(f"Failed to fetch URL: {url}")

with open("battle_net_data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("Data saved to battle_net_data.json")