from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Just messing around with Selenium
driver = webdriver.Chrome()

# # Navigate to address
# driver.get("https://www.amazon.com.br/Apple-iPhone-14-256-GB/dp/B0BDJJ7VGQ/ref=sr_1_3_sspa?__mk_pt_BR="
#            "%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=iphone&qid=1682025128&sr=8-3-spons&ufe=app_do%"
#            "3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNEg1T0lSV"
#            "zk4QVhDJmVuY3J5cHRlZElkPUEwOTYyODU0MUFKVjNDUlhWQkxKSSZlbmNyeXB0ZWRBZElkPUEwMDQyNjEwMVJSWkFMM"
#            "jVRN1gzWCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1")
#
# # Find element by name
# search_bar = driver.find_element(by="name", value="field-keywords")
# print(search_bar.get_attribute("placeholder"))
#
# # Find element by ID
# price = driver.find_element(By.ID, "productTitle")
# print(price.text)
#
# # Find elements by CSS
# links = driver.find_elements(By.CSS_SELECTOR, ".navFooterLinkCol a")
# for link in links:
#     print(link.get_attribute("href"))
#
# # Find elements by XPATH
# p = driver.find_element(By.XPATH, '//*[@id="tech"]/div[3]/div/div[2]/div/table/tbody/tr[1]/td[2]/p')
# print(p.text)
#
# # Find element by Class Name
# driver.get("https://maistocadas.mus.br/1996/")
# gospel_list = driver.find_element(By.CLASS_NAME, "lista")
# print(gospel_list.text)
#
# # Challenge 1: create a dict from Upcoming Events section on python.org website
# upcoming_events = {}
# driver.get("https://python.org")
# events = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu li")
# for index, event in enumerate(events):
#     upcoming_events[index] = {"time": event.find_element(By.TAG_NAME, "time").text,
#                               "name": event.find_element(By.TAG_NAME, "a").text}
# print(upcoming_events)
#
# # Clicking links (1st option)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# # article_count.click()
#
# # Clicking links (2nd option)
# create_account = driver.find_element(By.LINK_TEXT, "Create account")
# create_account.click()
#
# # Typing in the search bar
# search_bar = driver.find_element(By.NAME, "search")
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)
#
# # Challenge 2: Fill and submit form
# driver.get("https://www.appbrewery.co/p/newsletter")
# driver.find_element(By.XPATH, '//*[@id="blocks"]/section[2]/div/a').click()
# driver.implicitly_wait(10)
# driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Davi")
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("dadafrossard@gmail.com")
# driver.find_element(By.CSS_SELECTOR, "#gdpr input").click()
# driver.find_element(By.LINK_TEXT, "Subscribe to list").click()

# Challenge 3: Play Cookie Game
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element(By.ID, "cookie")

# Get upgrade item ids.
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Get all upgrade <b> tags
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break

# Close tab
# driver.close()

# Close chrome
# driver.quit()