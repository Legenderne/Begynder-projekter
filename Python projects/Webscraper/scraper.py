from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


page_url = "https://www.computersalg.dk/l/0/s?sq=cpu"


uClient = uReq(page_url)


page_soup = soup(uClient.read(), "html.parser")
uClient.close()


containers = page_soup.findAll("div", {"class": "item-container"})


out_filename = "processore.csv"

headers = "mærke,produkt_navn,fragt \n"


f = open(out_filename, "w")
f.write(headers)


for container in containers:
    make_rating_sp = container.div.select("a")
    mærke = make_rating_sp[0].img["title"].title()
    produkt_navn = container.div.select("a")[2].text
    fragt = container.findAll("li", {"class", "fragt"})[0].text.strip().replace("kr", "").replace(" fragt", "")

    print("mærke: " + mærke + "\n")
    print("produkt_navn: " + produkt_navn + "\n")
    print("fragt: " + fragt + "\n")

    f.write(mærke + ", " + produkt_navn.replace(",", "|") + ", " + fragt + "\n")

f.close()
