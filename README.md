# Battle.net Hidden Shop 

Scrape product titles from the unlisted Battle.net shop using a range of product IDs. It logs in to your Battle.net account, fetches the HTML content of each product page, extracts the product titles, and saves the results to a JSON file.

## Prerequisites

To run this script, you need to have the following:

- Python 3.x installed on your system
- `requests` library installed (`pip install requests`)
- `selectolax` library installed (`pip install selectolax`)

## Usage

1. Clone the repository.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Install the required libraries, requests for handling login and selectolax for HTML parsing:

`pip install requests`

`pip install selectolax`

4. Run using the following command:
`python hidden.py`

5. When prompted, enter your Battle.net username and password.

6. After login you can scrape the product titles for the specified range of product IDs, and save the results to a file named `battle_net_data.json` in the same directory.

7. Once the script finishes executing, you will see a message indicating that the data has been saved to the JSON file.

## Configuration

You can adjust the start and end values to search through different listings.

- `start_num`: The starting product ID for the range of products to scrape (default: 879000).
- `end_num`: The ending product ID for the range of products to scrape (default: 900000).

## Output

A JSON file named `battle_net_data.json` is generated in the same directory. Keys are the product URLs and the values are the corresponding product titles.

Example output:
```json
{
 "https://us.battle.net/shop/en/checkout/buy/879000": "So good it's scary!",
 "https://us.battle.net/shop/en/checkout/buy/879001": "Did you hear something?",
 "https://us.battle.net/shop/en/checkout/buy/879002": "I'm not scared",
 "https://us.battle.net/shop/en/checkout/buy/879003": "Things are looking grim",
 "https://us.battle.net/shop/en/checkout/buy/879004": "I smell trouble brewing",
 "https://us.battle.net/shop/en/checkout/buy/879005": "I'm so scared\",
 "https://us.battle.net/shop/en/checkout/buy/879006": "Trick or treat",
 "https://us.battle.net/shop/en/checkout/buy/879008": "Spark",
 "https://us.battle.net/shop/en/checkout/buy/879009": "Combo",


 ...
}
