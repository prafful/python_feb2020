from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req

url = "https://www.flipkart.com/search?q=mobiles"
uclient = req(url)
page = uclient.read()
uclient.close()

pagesoup = soup(page, 'html.parser')
allMobileHtml = pagesoup.findAll("div", {"class":"_3wU53n"})
allMobilePriceHtml = pagesoup.findAll("div", {"class":"_1vC4OE _2rQ-NK"})
counter = 0
while counter < len(allMobileHtml):
    eachtitlediv = allMobileHtml[counter]
    eachtitleprice = allMobilePriceHtml[counter]
    print("Title: " + eachtitlediv.text + "\n" + "Price: " + str(eachtitleprice.text))
    counter += 1