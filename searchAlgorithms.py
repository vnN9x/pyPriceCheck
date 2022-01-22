from bs4 import BeautifulSoup as bs
import requests
import datetime

from product import Product

def amazon_link_generator(raw_product_name: str) -> str:
    amazon_linked_product = 'https://www.amazon.com.br/s?k='
    raw_product_name = raw_product_name.split()
    amazon_search_complement = '&i=computers'
    
    for item in raw_product_name:
        amazon_linked_product += '+'+item if raw_product_name.index(item) > 0 else item 

    amazon_linked_product += amazon_search_complement

    return amazon_linked_product.lower()


def amazon_search_query(product_name: str) -> list:
    product_list = []
    response = requests.get(amazon_link_generator(product_name))    
    content = response.content
    soup = bs(content, 'html.parser')
    data = datetime.datetime.now()
    for texted_name, link, price in enumerate(soup.find_all()):
        product_list.append(Product(texted_name, link, price, data))

    return product_list
