import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/p/pl?d=graphics+cards"

# opening connection and grabbing the page
uClient = uReq(my_url)
# reading the page and saving the html data in page_html
page_html = uClient.read()

# Saving the parsing of page_html in variable page_soup
page_soup = soup(page_html, "html.parser")

# closing the connection
uClient.close()

# Saving all divs that have the class item-container in a variable
containers = page_soup.findAll("div", {"class": "item-container"})[4:]

# Opening the file
filename = "products.csv"
# setting the file status to writing
f = open(filename, "w")
# defining some headers that we want to have
headers = "brand, product_name, shipping\n"
# writing the first line of the files, our headers
f.write(headers)

# Looping through the containers for brands, product names and shipping
for container in containers:
    brand = container.div.div.a.img["title"]
    print("Brand: " + brand)

    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text
    print("Product name: " + product_name)

    shipping_container = container.findAll("li", {"class": "price-ship"})
    shipping = shipping_container[0].text.strip()
    print("Shipping: " + shipping)
    # Writing each row of our csv file
    f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")
# closing the file, otherwise we won't be able to read it :)
f.close()

# END OF THE FILE; FIRST SCRAPER DONE :)
