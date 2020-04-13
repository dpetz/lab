# Inspired by Amazon price scaper:  https://www.youtube.com/watch?v=Bg9r_yLk7VY

# A simple Python module to bypass Cloudflare's anti-bot page
import cfscrape

import requests
from bs4 import BeautifulSoup

# url = "https://www.medimops.de/forster-e-m-die-maschine-steht-still-gebundene-ausgabe-M03455405711.html"

url = 'https://www.medimops.de/juergen-osterhammel-die-verwandlung-der-welt-eine-geschichte-des-19-jahrhunderts-gebundene-ausgabe-M03406614817.html'

header = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) ' \
    'Chrome/80.0.3987.163 Safari/537.36'

# page = requests.get(url, header)

def scrape():
    session = requests.Session()
    session.headers = header
    scraper = cfscrape.create_scraper(sess=session)
    page = scraper.get(url).content

    soup = BeautifulSoup(page, 'html.parser')
    #print(f"Soup: {soup}")
    price = soup.find_all("div", class_="mxjs-variant-selector")

    for p in price:
        print(f"{50*'-'}\n{p}\n{50*'-'}\n")


good = """
<div class="mxjs-variant-selector mx-variant-selector mx-ga-sendOnClickEvent" data-condition="UsedGood" data-ga-action="click" data-ga-category="ChangeCondition" data-ga-label="UsedGood" data-issale="" data-listprice="28.00" data-listprice-text="Neu &lt;del&gt;28,00 €&lt;/del&gt; Sie sparen 6,95 € (25 %)" data-mpid="M03406614817" data-mxsourceurl="https://www.medimops.de/juergen-osterhammel-die-verwandlung-der-welt-eine-geschichte-des-19-jahrhunderts-gebundene-ausgabe-M03406614817.html?variant=UsedGood" data-price="21,05" data-stock="" data-stock-text="Nur noch  Artikel auf Lager" data-variant="M03406614817UsedGood" name="M03406614817UsedGood">
                                Gebraucht - Gut
                                <br/>
<span class="mx-price">21,05 €</span>
</div>
"""

very_good = """
<div class="mxjs-variant-selector mx-variant-selector mx-ga-sendOnClickEvent mx-variant-selector-selected" data-condition="UsedVeryGood" data-ga-action="click" data-ga-category="ChangeCondition" data-ga-label="UsedVeryGood" data-issale="" data-listprice="28.00" data-listprice-text="Neu &lt;del&gt;28,00 €&lt;/del&gt; Sie sparen 5,55 € (20 %)" data-mpid="M03406614817" data-mxsourceurl="https://www.medimops.de/juergen-osterhammel-die-verwandlung-der-welt-eine-geschichte-des-19-jahrhunderts-gebundene-ausgabe-M03406614817.html?variant=UsedVeryGood" data-price="22,45" data-stock="" data-stock-text="Nur noch  Artikel auf Lager" data-variant="M03406614817UsedVeryGood" name="M03406614817UsedVeryGood">
Gebraucht - Sehr gut
<br/>
<span class="mx-price">22,45 €</span>
</div>
 """

soup = BeautifulSoup(good, 'html.parser')
tag = soup.find_all("div", class_="mxjs-variant-selector")
print(tag[0]['data-condition'])
print(tag[0]['data-price'])


