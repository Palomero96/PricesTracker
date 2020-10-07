import requests
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd
import os.path

def main():

    #Create dataframe to save all the collected data
    if(os.path.isfile("prices.csv")):
        df = pd.read_csv("prices.csv")
    else:
        df = pd.DataFrame(columns=["Name","Shop","Link", "Price", "Date"])

    #Using user agent in order to do the get request
    header= { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}

    
    
    #df = pccomponentesAll(header,df)
    print("PcComponentes finished")
    df=mediamarktAll(header,df) 
    print("Mediamark finished")
    df = amazonAll(header,df)
    print("Amazon finished")
    df.to_csv("prices.csv", index=False)

def pccomponentesAll(header,df):
    #Monitors
    df=pccomponentesPrice("https://www.pccomponentes.com/aoc-gaming-24g2u-24-led-ips-fullhd-144hz-freesync",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/benq-zowie-xl2411p-24-led-144hz-e-sports",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/aoc-gaming-c24g1-24-led-fullhd-144hz-freesync-curva",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/aoc-g2590fx-245-led-fullhd-144hz-freesync",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/msi-optix-g24c4-236-led-fullhd-144hz-freesync-curva",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/viewsonic-vx-series-vx2458-mhd-236-led-fullhd-144hz-freesync",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/msi-optix-g271-27-led-ips-fullhd-144hz-freesync",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/keep-out-xgm24c-236-led-fullhd-144hz-freesync-curvo",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/samsung-lc24rg50fqu-235-led-fullhd-144hz-freesync-curva",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/msi-optix-g241-238-led-ips-fullhd-144hz-freesync",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/asus-vg248qz-24-led-fullhd-144hz",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/asus-vg248qe-24--led-3d-144hz",header,df)

    #Laptops
    df=pccomponentesPrice("https://www.pccomponentes.com/msi-prestige-15-a10sc-044xes-intel-core-i7-10710u-16gb-512gb-ssd-gtx-1650-156",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/msi-prestige-15-a10sc-293xes-intel-core-i7-10710u-32gb-1tb-ssd-gtx-1650-156",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/dell-xps-7390-intel-core-i7-10510u-16gb-512gb-ssd-133",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/dell-xps-15-7590-intel-core-i7-9750h-16gb-512gb-ssd-gtx-1650-156",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/asus-zenbook-14-ux431fl-am049t-intel-core-i7-10510u-16gb-512gb-ssd-mx250-14",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/asus-zenbook-14-ux431fa-am128-intel-core-i7-10510u-16gb-512gb-ssd-14",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/asus-zenbook-14-ux434fac-a5188t-intel-core-i7-10510u-16gb-512gb-ssd-14",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/asus-zenbook-ux325ja-eg007t-intel-core-i7-1065g7-16gb-512gb-ssd-133",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/asus-zenbook-14-bx425ja-bm145r-intel-core-i7-1065g7-16gb-512gb-ssd-14",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/lenovo-thinkpad-e490-intel-core-i5-8265u-8gb-512gb-ssd-14",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/lenovo-thinkpad-e595-amd-ryzen-5-3500u-16gb-512gb-ssd-156",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/lenovo-thinkpad-e14-intel-core-i5-10210u-8gb-512gb-ssd-14",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/lenovo-thinkpad-e15-intel-core-i5-10210u-8gb-512gb-ssd-156",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/lenovo-thinkpad-e15-intel-core-i5-10210u-8gb-256gb-ssd-156",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/lenovo-thinkpad-e14-intel-core-i5-10210u-8gb-256gb-ssd-14",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/lenovo-thinkpad-e14-amd-ryzen-5-4500u-16gb-512gb-ssd-14",header,df)
    df=pccomponentesPrice("",header,df)
    df=pccomponentesPrice("",header,df)
    df=pccomponentesPrice("",header,df)
    df=pccomponentesPrice("",header,df)
    df=pccomponentesPrice("",header,df)
    df=pccomponentesPrice("",header,df)
    df=pccomponentesPrice("",header,df)

    #Processors
    df=pccomponentesPrice("https://www.pccomponentes.com/amd-ryzen-5-3600-36ghz-box",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/amd-ryzen-5-3400g-37ghz-box",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/amd-ryzen-5-3600x-38ghz-box",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/amd-ryzen-5-3500x-36ghz-box",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/procesador-amd-ryzen-5-2600-34-ghz",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/amd-ryzen-7-3700x-36ghz-box",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/intel-core-i5-9400f-29ghz",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/procesador-amd-ryzen-5-2600x-36-ghz",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/intel-core-i5-9600k-37ghz",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/intel-core-i7-10700k-380-ghz",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/intel-core-i7-9700k-36ghz",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/intel-core-i7-9700f-3ghz",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/amd-ryzen-9-3900x-38-ghz-box",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/intel-core-i7-9700-3-ghz",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/intel-core-i9-9900k-36-ghz",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/intel-core-i9-10900kf-370-ghz",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/intel-core-i9-10900k-370-ghz",header,df)


    #Graphic card
    df=pccomponentesPrice("https://www.pccomponentes.com/zotac-gaming-geforce-rtx2060-6gb-gddr6",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/gigabyte-geforce-rtx-2060-oc-6gb-gddr6",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/evga-geforce-rtx-2060-ko-gaming-6gb-gddr6",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/evga-geforce-rtx-2060-ko-ultra-gaming-6gb-gddr6",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/gigabyte-geforce-rtx-2060-super-gaming-oc-3x-8gb-gddr6",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/msi-geforce-rtx-2060-super-gaming-x-8gb-gddr6",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/msi-geforce-rtx-2060-super-ventus-gp-oc-8gb-gddr6",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/asus-geforce-rtx-3070-dual-8gb-gddr6",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/asus-geforce-rtx-3070-dual-oc-edition-8gb-gddr6",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/asus-rog-strix-gaming-geforce-rtx-3070-8gb-gddr6",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/gigabyte-geforce-rtx-3080-gaming-oc-10g-10gb-gddr6x",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/msi-geforce-rtx-3080-ventus-3x-oc-10gb-gddr6x",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/msi-geforce-rtx-3080-gaming-x-trio-10gb-gddr6x",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/zotac-gaming-geforce-rtx-3090-trinity-24gb-gddr6x",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/gigabyte-geforce-rtx-3090-gaming-oc-24g-24gb-gddr6x",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/asus-tuf-geforce-rtx-3090-gaming-oc-24gb-gddr6x",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/tarjetas-graficas/gf-2080-series",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/gigabyte-geforce-rtx-2070-super-gaming-oc-3x-8gb-gddr6",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/gigabyte-geforce-rtx-2070-super-windforce-oc-3x-8gb-gddr6",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/asus-dual-geforce-rtx-2070-super-evo-oc-edition-8gb-gddr6",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/gigabyte-geforce-rtx-2080-super-gaming-oc-waterforce-wb-8gb-gddr6",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/msi-geforce-rtx-2080-super-gaming-x-trio-8-gb-gddr6",header,df)
    df=pccomponentesPrice("https://www.pccomponentes.com/asus-dual-geforce-rtx-2080-super-evo-v2-oc-edition-8gb-gddr6",header,df)
    return df

def pccomponentesPrice(url,header,df):
    #Getting the page
    page = requests.get(url, headers=header)
    #Creating BeautifulSoup Object
    soup = BeautifulSoup(page.content, "html.parser")
    #Product Name
    name = soup.find("div", {"class": "articulo"})
    name = name.find("strong").get_text()
    #Product price
    price = soup.find("span", {"class": "baseprice"})
    if (price == None):
        price = soup.find(id="precio-main").get_text()
        price=price.replace("€","")
    else:
        price = price.get_text()
    #Date of request
    dateRequest = date.today()

    #write in the csv file
    newRow= {"Name":name,"Shop": "PcComponentes","Link":url, "Price": price, "Date":dateRequest}
    df = df.append(newRow,ignore_index=True)
    return df

def mediamarktAll(header,df):
    #Monitors
    df=mediamarkt("https://www.mediamarkt.es/es/product/_monitor-gaming-samsung-lc24rg50-24-curvo-full-hd-4-ms-144-hz-negro-1452823.html",header,df)
    df=mediamarkt("https://www.mediamarkt.es/es/product/_monitor-gaming-aoc-g2460pf-full-hd-144hz-1ms-24-1310405.html",header,df)
    df=mediamarkt("https://www.mediamarkt.es/es/product/_monitor-gaming-msi-optix-g241-23-8-led-ips-full-hd-1-ms-144hz-freesync-hdmi-negro-1475191.html",header,df)
    df=mediamarkt("https://www.mediamarkt.es/es/product/_monitor-gaming-hp-24x-23-8-full-hd-1-ms-144-hz-negro-1467147.html",header,df)
    df=mediamarkt("https://www.mediamarkt.es/es/product/_monitor-gaming-asus-vg248qe-gaming-24-tn-fhd-144-hz-1ms-350-nits-displayport-1187193.html",header,df)

    #Laptops
    df=mediamarkt("https://www.mediamarkt.es/es/product/_port%C3%A1til-gaming-msi-prestige-15-15-6-fhd-intel%C2%AE-core%E2%84%A2-i7-10710u-16gb-512-512-gb-gtx1650-w10h-plata-1485804.html",header,df)


    return df

def mediamarkt(url,header,df): 
    #Getting the page
    page = requests.get(url, headers=header)
    #Creating BeautifulSoup Object
    soup = BeautifulSoup(page.content, "html.parser")

    #Product Name   <h1 itemprop="name">Monitor gaming - HP OMEN 25, 24.5" Full HD, 144Hz, LED, HDMI, USB, Negro (Jack Black)</h1>
    name= soup.find("h1", itemprop="name")
    name = name.get_text()
    #Product price  <meta itemprop="price" content="206">
    price= soup.find("meta", itemprop="price")
    price = price['content']
    
    #Date of request 
    dateRequest = date.today()

    #write in the csv file 
    newRow= {"Name":name,"Shop": "MediaMarkt","Link": url, "Price": price, "Date":dateRequest}
    df = df.append(newRow,ignore_index=True)
    return df

def amazonAll(header,df):
    #Monitors
    df = amazonPrices("https://www.amazon.es/BenQ-ZOWIE-XL2411P-Sport-DisplayPort/dp/B075JGL4WV/ref=sr_1_1?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3H3OEELUC7P8V&dchild=1&keywords=monitores+144+hz&qid=1602066197&sprefix=monitores+144%2Caps%2C172&sr=8-1",header,df)
    df = amazonPrices("https://www.amazon.es/Samsung-C24RG52-Monitor-FreeSync-Flicker-Free/dp/B083T2NH8P/ref=sr_1_2?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3H3OEELUC7P8V&dchild=1&keywords=monitores+144+hz&qid=1602069903&refinements=p_n_feature_browse-bin%3A949750031%7C949751031&rnid=949747031&s=computers&sprefix=monitores+144%2Caps%2C172&sr=1-2",header,df)
    df = amazonPrices("https://www.amazon.es/AOC-24G2U-BK-Ajustable-FlickerFree/dp/B07Y3RYLVH/ref=sr_1_4?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3H3OEELUC7P8V&dchild=1&keywords=monitores+144+hz&qid=1602069903&refinements=p_n_feature_browse-bin%3A949750031%7C949751031&rnid=949747031&s=computers&sprefix=monitores+144%2Caps%2C172&sr=1-4",header,df)
    df = amazonPrices("https://www.amazon.es/Mon-24-1920X1080-16-144HZ/dp/B07H5GNR18/ref=sr_1_5?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3H3OEELUC7P8V&dchild=1&keywords=monitores+144+hz&qid=1602069903&refinements=p_n_feature_browse-bin%3A949750031%7C949751031&rnid=949747031&s=computers&sprefix=monitores+144%2Caps%2C172&sr=1-5",header,df)
    df = amazonPrices("https://www.amazon.es/ASUS-VG248QE-1920x1080-Altavoces-DisplayPort/dp/B00B19T7QC/ref=sr_1_9?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3H3OEELUC7P8V&dchild=1&keywords=monitores+144+hz&qid=1602069903&refinements=p_n_feature_browse-bin%3A949750031%7C949751031&rnid=949747031&s=computers&sprefix=monitores+144%2Caps%2C172&sr=1-9",header,df)
    df = amazonPrices("https://www.amazon.es/AOC-Gaming-G2590FX-Pantalla-Plana/dp/B07D377Q6D/ref=sr_1_11?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3H3OEELUC7P8V&dchild=1&keywords=monitores+144+hz&qid=1602069903&refinements=p_n_feature_browse-bin%3A949750031%7C949751031&rnid=949747031&s=computers&sprefix=monitores+144%2Caps%2C172&sr=1-11",header,df)
    df = amazonPrices("https://www.amazon.es/Lenovo-G25-Pantalla-respuesta-FreeSync/dp/B082MZM43X/ref=sr_1_15?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3H3OEELUC7P8V&dchild=1&keywords=monitores+144+hz&qid=1602069903&refinements=p_n_feature_browse-bin%3A949750031%7C949751031&rnid=949747031&s=computers&sprefix=monitores+144%2Caps%2C172&sr=1-15",header,df)
    df = amazonPrices("https://www.amazon.es/Prechen-Pulgadas-1920x1080-Inteligente-Ultrafino/dp/B08CX74C45/ref=sr_1_16?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3H3OEELUC7P8V&dchild=1&keywords=monitores+144+hz&qid=1602069903&refinements=p_n_feature_browse-bin%3A949750031%7C949751031&rnid=949747031&s=computers&sprefix=monitores+144%2Caps%2C172&sr=1-16",header,df)
    df = amazonPrices("https://www.amazon.es/Thinlerain-Monitor-Pulgadas-Pantalla-Juegos/dp/B089XYB72K/ref=sr_1_18?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3H3OEELUC7P8V&dchild=1&keywords=monitores+144+hz&qid=1602069903&refinements=p_n_feature_browse-bin%3A949750031%7C949751031&rnid=949747031&s=computers&sprefix=monitores+144%2Caps%2C172&sr=1-18",header,df)
    #Laptops
    
    #Processors
    df = amazonPrices("https://www.amazon.es/AMD-Ryzen-2700X-Procesador-disipador/dp/B07B428M7F/ref=sr_1_1?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=procesadores+amd&qid=1602070275&sr=8-1",header,df)
    df = amazonPrices("https://www.amazon.es/AMD-Ryzen-3400G-Procesador-Disipador/dp/B07SXNDKNM/ref=sr_1_2?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=procesadores+amd&qid=1602070275&sr=8-2",header,df)
    df = amazonPrices("https://www.amazon.es/AMD-Ryzen-3600-Procesador-disipador/dp/B07STGGQ18/ref=sr_1_3?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=procesadores+amd&qid=1602070275&sr=8-3",header,df)
    df = amazonPrices("https://www.amazon.es/AMD-Ryzen-3600X-Procesador-ventilador/dp/B07SQBFN2D/ref=sr_1_5?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=procesadores+amd&qid=1602070275&sr=8-5",header,df)
    df = amazonPrices("https://www.amazon.es/AMD-Ryzen-3700X-Procesador-Disipador/dp/B07SXMZLPK/ref=sr_1_8?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=procesadores+amd&qid=1602070275&sr=8-8",header,df)
    df = amazonPrices("https://www.amazon.es/AMD-Ryzen-3900X-Procesador-ventilador/dp/B07SXMZLP9/ref=sr_1_9?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=procesadores+amd&qid=1602070275&sr=8-9",header,df)
    df = amazonPrices("https://www.amazon.es/AMD-Ryzen-3800X-Procesador-Disipador/dp/B07SXMZLPJ/ref=sr_1_12?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=procesadores+amd&qid=1602070275&sr=8-12",header,df)
    df = amazonPrices("https://www.amazon.es/AMD-Ryzen-3950x-Retail-100-100000051WOF/dp/B07ZTYKLZW/ref=sr_1_16?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=procesadores+amd&qid=1602070275&sr=8-16",header,df)
    df = amazonPrices("https://www.amazon.es/Intel-BX80684I59600K-I5-9600K-3-70Ghz-Lga1151/dp/B07HHLX1R8/ref=sr_1_2?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=procesador+intel&qid=1602070578&sr=8-2",header,df)
    df = amazonPrices("https://www.amazon.es/Intel-BX80684I79700K-I7-9700K-3-60GHZ-LGA1151/dp/B07HHN6KBZ/ref=sr_1_4?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=procesador+intel&qid=1602070578&sr=8-4",header,df)
    df = amazonPrices("https://www.amazon.es/Intel-i5-9400F-procesador-Smart-Cache/dp/B07S9M32FG/ref=sr_1_5?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=procesador+intel&qid=1602070578&sr=8-5",header,df)
    df = amazonPrices("https://www.amazon.es/I5-9400F-2-90GHZ-LGA1151-Graphics-BX80684I59400F/dp/B07MRCGQQ4/ref=sr_1_8?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=procesador+intel&qid=1602070578&sr=8-8",header,df)
    df = amazonPrices("https://www.amazon.es/Intel-Core-i9-10900-Procesador-BX8070110900/dp/B0883P56BM/ref=sr_1_15?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=procesador+intel&qid=1602070578&sr=8-15",header,df)
    df = amazonPrices("https://www.amazon.es/Intel-Bx80684I99900K-I9-9900K-3-60Ghz-Lga1151/dp/B005404P9I/ref=sr_1_13?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=procesador+intel&qid=1602070578&sr=8-13",header,df)
    df = amazonPrices("https://www.amazon.es/Intel-Core-i5-10400-Procesador-LGA1200/dp/B0883NPQST/ref=sr_1_14?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=procesador+intel&qid=1602070578&sr=8-14",header,df)
    df = amazonPrices("https://www.amazon.es/Intel-Core-i7-10700K-Procesador-Casquillo/dp/B0883P8CNM/ref=sr_1_16?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=procesador+intel&qid=1602070578&sr=8-16",header,df)
    df = amazonPrices("https://www.amazon.es/Intel-Core-i9-10900X-LGA2066-X299/dp/B07YP69HTM/ref=sr_1_28?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=procesador+intel&qid=1602070578&sr=8-28",header,df)
    df = amazonPrices("https://www.amazon.es/Procesador-Intel-i9-10900X-n%C3%BAcleos-LGA2066/dp/B07ZQN8V6S/ref=sr_1_32?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=procesador+intel&qid=1602070578&sr=8-32",header,df)
    
    #Graphic card
    df = amazonPrices("https://www.amazon.es/EVGA-GeForce-Gaming-06G-P4-2068-KR-Backplate/dp/B083JX52VG/ref=sr_1_3?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=nvidia+rtx+2060&qid=1602070744&sr=8-3",header,df)
    df = amazonPrices("https://www.amazon.es/ASUS-ROG-Strix-RTX-2060-A6G-EVO-GAMING-Tarjeta-DisplayPort/dp/B086FX185S/ref=sr_1_6?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=nvidia+rtx+2060&qid=1602070744&sr=8-6",header,df)
    df = amazonPrices("https://www.amazon.es/ASUS-RTX2060-Dual-GDDR6-HDMI/dp/B07V1Y6Y2J/ref=sr_1_5?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=nvidia+rtx+2060&qid=1602070744&sr=8-5",header,df)
    df = amazonPrices("https://www.amazon.es/Gigabyte-GeForce-WINDFORCE-Tarjeta-refrigeraci%C3%B3n/dp/B07X51LTKK/ref=sr_1_2?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=nvidia+rtx+2070&qid=1602070776&sr=8-2",header,df)
    df = amazonPrices("https://www.amazon.es/MSI-GeForce-2070-Super-Gaming/dp/B07TWX22ZQ/ref=sr_1_3?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=nvidia+rtx+2070&qid=1602070776&sr=8-3",header,df)
    df = amazonPrices("https://www.amazon.es/GeForce-RTX-2070-Ventus-GP/dp/B0817726L8/ref=sr_1_4?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=nvidia+rtx+2070&qid=1602070776&sr=8-4",header,df)
    df = amazonPrices("https://www.amazon.es/EVGA-GeForce-Super-Gaming-08G-P4-2083-KR/dp/B086VWDVZ9/ref=sr_1_3?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=nvidia+rtx+2080&qid=1602070783&sr=8-3",header,df)
    df = amazonPrices("https://www.amazon.es/ASUS-Strix-GeForce-Super-GDDR6/dp/B07VN6D5JB/ref=sr_1_6?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=nvidia+rtx+2080&qid=1602070783&sr=8-6",header,df)
    df = amazonPrices("https://www.amazon.es/MSI-RTX2080S-Gaming-GDDR6-USB-C/dp/B07VGM29BZ/ref=sr_1_10?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=nvidia+rtx+2080&qid=1602070783&sr=8-10",header,df)

    return df

def amazonPrices(url,header,df):

    #Getting the page
    page = requests.get(url, headers=header)

    #Creating BeautifulSoup Object
    #Need to install lxml package (pip install lxml)
    soup = BeautifulSoup(page.content, "lxml")

    #Name
    name = soup.find('span', id="productTitle")
    name = name.get_text()
    name = name.replace("\n","")
    print(name)
    
    #Price
    price = soup.find('span', id="priceblock_ourprice")
    price = price.get_text()
    price = price.replace("€","")
    price = price.replace(" ","")
    price= price.replace(",",".")

    #Date of request 
    dateRequest = date.today()
    
    #write in the csv file 
    newRow= {"Name":name,"Shop": "Amazon","Link": url, "Price": price, "Date":dateRequest}
    df = df.append(newRow,ignore_index=True)
    return df
    
if __name__ == "__main__":
    main()