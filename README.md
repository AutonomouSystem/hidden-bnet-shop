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

- `start_num`: The starting product ID for the range of products to scrape (default: 1700000).
- `end_num`: The ending product ID for the range of products to scrape (default: 1800000).

## Output

A JSON file named `battle_net_data.json` is generated in the same directory. Keys are the product URLs and the values are the corresponding product titles.

Example output:
```json
{
    "https://us.battle.net/shop/en/checkout/buy/1705487": "World of Warcraft\u00ae: Lunar Pack",
    "https://us.battle.net/shop/en/checkout/buy/1705488": "Hearthstone\u00ae: Whizbang's Catch-Up Starter Bundle",
    "https://us.battle.net/shop/en/checkout/buy/1705489": "Hearthstone\u00ae: Whizbang's Catch-Up Starter Bundle",
    "https://us.battle.net/shop/en/checkout/buy/1705520": "Ultimate Battle Pass Bundle: Season 10",
    "https://us.battle.net/shop/en/checkout/buy/1705522": "Hearthstone\u00ae: Whizbang's Catch-Up Starter Bundle",
    "https://us.battle.net/shop/en/checkout/buy/1705559": "10 Mythic Prisms",
    "https://us.battle.net/shop/en/checkout/buy/1705560": "40 (+10 Bonus) Mythic Prisms",
    "https://us.battle.net/shop/en/checkout/buy/1705561": "75 (+25 Bonus) Mythic Prisms",
    "https://us.battle.net/shop/en/checkout/buy/1705588": "PVP Rations - Undead",
    "https://us.battle.net/shop/en/checkout/buy/1705589": "PvP Rations - Horde",
    "https://us.battle.net/shop/en/checkout/buy/1705590": "PVP Rations - Blackrock",
    "https://us.battle.net/shop/en/checkout/buy/1705591": "PVP Rations - Beast",
    "https://us.battle.net/shop/en/checkout/buy/1705592": "PVP Rations - Alliance",
    "https://us.battle.net/shop/en/checkout/buy/1705593": "Gadgetzan's Grandeur",
    "https://us.battle.net/shop/en/checkout/buy/1705802": "Hearthstone\u00ae: Darkmoon Races Golden Mini-Set",
    "https://us.battle.net/shop/en/checkout/buy/1705963": "Knee-slapper",
    "https://us.battle.net/shop/en/checkout/buy/1705965": "Talon Accelerator",
    "https://us.battle.net/shop/en/checkout/buy/1705969": "Talon's Cannon",
    "https://us.battle.net/shop/en/checkout/buy/1705977": "Tracer - Operative Oxton",
    "https://us.battle.net/shop/en/checkout/buy/1705996": "Talon Tracer",
    "https://us.battle.net/shop/en/checkout/buy/1705998": "Zarya - Talon",

 ...
}
