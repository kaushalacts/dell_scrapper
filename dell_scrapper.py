from bs4 import BeautifulSoup
import requests 
import pandas as pd 


 
# Open the link
url = "https://www.dell.com/en-us/shop/dell-laptops/sr/laptops?page=1"
 
response = requests.get(url)


 

 
soup = BeautifulSoup(response.text, 'lxml')

 
laptops = soup.find_all("section", class_="ps-show-hide")


for laptop in laptops:
    name = laptop.find("h3", class_="ps-title").text.strip()
    price = laptop.find("div", class_="ps-dell-price ps-simplified").text.strip()
    processor = laptop.find("span", class_="ps-iconography-specs-label").text.strip() 
    print(f"{name}: {price}")
    print(f"{processor}")
 
