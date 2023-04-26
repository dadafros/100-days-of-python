from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import ElementClickInterceptedException
import time
import os

INSTAGRAM_PASS = os.environ.get("INSTAGRAM_PASS")
INSTAGRAM_USER = "dadafros"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.scrollable_popup = None

    def login(self):
        self.driver.get("https://instagram.com")
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(INSTAGRAM_USER)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(INSTAGRAM_PASS)
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        time.sleep(3)

    def find_followers(self):
        self.driver.get("https://instagram.com/otvlink/followers")
        time.sleep(5)
        self.scrollable_popup = self.driver.find_element(By.CSS_SELECTOR, "div > div > div._aano")
        count = 0
        while True:
            scroll_height = self.scrollable_popup.get_property("scrollHeight")
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.scrollable_popup)
            time.sleep(1)
            count += 1
            if count % 5 == 0 and scroll_height == self.scrollable_popup.get_property("scrollHeight"):
                break

    def follow(self):
        follow_buttons = self.scrollable_popup.find_elements(By.TAG_NAME, "button")
        for button in follow_buttons:
            try:
                button.click()
            except ElementClickInterceptedException:
                ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(1)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
