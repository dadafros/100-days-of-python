from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Scrap data
option = webdriver.ChromeOptions()
option.add_argument("User-Agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44")
option.add_argument("Accept-Language=en-US,en;q=0.9")
option.add_argument("Accept-Encoding=gzip, deflate, br")
option.add_argument("Accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                    "application/signed-exchange;v=b3;q=0.7")
option.add_argument("upgrade-insecure-requests=1")
option.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=option)
driver.get("https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A"
           "%7B%22west%22%3A-123.279276265625%2C%22east%22%3A-121.587381734375%2C%22south%22%3A37.27319626455797%2C"
           "%22north%22%3A38.273999739197215%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A"
           "%7B%22max%22%3A526060%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C"
           "%22mp%22%3A%7B%22max%22%3A2600%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22"
           "%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22"
           "%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C"
           "%22mapZoom%22%3A9%7D")
input()
soup = BeautifulSoup(driver.page_source, 'html.parser')
rent_list = soup.select(selector="#grid-search-results li")

# Fill form
for rent in rent_list:
    try:
        price = rent.find("span", {"data-test": "property-card-price"}).getText()
        address = rent.find("address", {"data-test": "property-card-addr"}).getText().split(" | ")[-1]
        url = rent.find("a", {"data-test": "property-card-link"}).get("href")
    except Exception as e:
        print(e)
    else:
        if not url.startswith("https"):
            url = "https://www.zillow.com" + url
        print(price, address, url)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSf2QMEM9uMGgAjuuWq5HLdZ6TBwIMw9XyKMRYxzlSAhkA5u1A/viewform")
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(address)
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(price)
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(url)
        driver.find_element(By.CSS_SELECTOR, "div.DE3NNc.CekdCb div.lRwqcd div").click()
driver.quit()
