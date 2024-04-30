import os
import json
import requests
from selectolax.parser import HTMLParser
from multiprocessing import Pool
import time

def login(session):
    username = input("Bnet Username: ")
    password = input("Bnet Password: ")

    login_url = "https://us.battle.net/login/en/"
    login_payload = {
        "accountName": username,
        "password": password,
        "submit": "Log in"
    }

    login_response = session.post(login_url, data=login_payload)
    if login_response.status_code == 200:
        print("Login successful!")
        return True
    else:
        print("Login failed.")
        print(f"Status code: {login_response.status_code}")
        print(f"Response content: {login_response.text}")
        return False
    
def fetch_data(args):
    session, num = args
    base_url = "https://us.battle.net/shop/en/checkout/buy/"
    url = base_url + str(num)
    try:
        response = session.get(url)
        if response.status_code == 200:
            parser = HTMLParser(response.text)
            title_element = parser.css_first("p.product-name")
            if title_element:
                title = title_element.text()
                return (url, title.strip())
            else:
                print(f"Title not found for URL: {url}")
        else:
            print(f"Failed to fetch URL: {url}")
    except requests.exceptions.ChunkedEncodingError as e:
        print(f"ChunkedEncodingError occurred for URL: {url}")
        print(f"Error message: {str(e)}")
    except Exception as e:
        print(f"An error occurred while fetching URL: {url}")
        print(f"Error message: {str(e)}")
    return None

def save_data(data, start_num, end_num):
    filename = f"{start_num}-{end_num}.json"
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    start_num = 400000
    end_num = 500000
    num_processes = 5

    start_time = time.time()

    session = requests.Session()
    login(session)

    with Pool(processes=num_processes) as pool:
        results = pool.map(fetch_data, [(session, num) for num in range(start_num, end_num + 1)])

    data = {}
    for result in results:
        if result:
            url, title = result
            data[url] = title

    save_data(data, start_num, end_num)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds")
