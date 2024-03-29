import requests
from bs4 import BeautifulSoup
import time

url = "https://www.jumia.co.ke/generic-smartwatch-business-bluetooth-waterproof-sport-115543616.html"  # Replace with product URL
desired_price = 50.00  # Set your target price

while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    current_price_str = soup.find(class_="price").text  #  Might need to adjust the class
    current_price = float(current_price_str.strip("$"))

    if current_price <= desired_price:
        print("Price dropped! Go grab it.")
        break  # Stop checking once price is low enough

    time.sleep(3600)  # Check price every hour 