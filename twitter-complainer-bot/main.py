from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

DOWNLOAD_CONTRACTED_SPEED = 3000
UPLOAD_MINIMUM_SPEED = 0.1 * DOWNLOAD_CONTRACTED_SPEED
DOWNLOAD_MINIMUM_SPEED = 0.8 * DOWNLOAD_CONTRACTED_SPEED
TWITTER_USER = "dadafros"
TWITTER_PASS = os.environ.get("TWITTER_PASS")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.up = 0
        self.down = 0
        self.link = ""
        self.driver = webdriver.Chrome()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        time.sleep(50)
        self.down = self.driver.find_element(By.CSS_SELECTOR, ".result-container-data span.download-speed").text
        self.up = self.driver.find_element(By.CSS_SELECTOR, ".result-container-data span.upload-speed").text
        time.sleep(3)
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        self.link = self.driver.find_element(By.CSS_SELECTOR, "a.social-icon").get_attribute("href")
        print("upload: ", self.up, "dowload: ", self.down)
        print("result: ", self.link)

    def tweet_at_provider(self):
        if float(self.up) < UPLOAD_MINIMUM_SPEED or float(self.down) < DOWNLOAD_MINIMUM_SPEED:
            self.driver.get("https://twitter.com/i/flow/login")
            time.sleep(3)
            self.driver.find_element(By.CSS_SELECTOR, "div.css-1dbjc4n > div > input").send_keys(TWITTER_USER)
            self.driver.find_element(By.CSS_SELECTOR, "div.css-1dbjc4n > div > div:nth-child(6)").click()
            time.sleep(3)
            ActionChains(self.driver).send_keys(TWITTER_PASS).perform()
            ActionChains(self.driver).send_keys(Keys.ENTER).perform()
            time.sleep(3)
            self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block").send_keys(
                f"Oi @ClaroBrasil, tudo bem? Por que vocês insistem em manter minha velociade de internet "
                f"abaixo do contratado ({DOWNLOAD_CONTRACTED_SPEED}mb)?\n{self.link}")
            input("Press enter to tweet")
            self.driver.find_element(By.CSS_SELECTOR, "div.css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf.r-sdzlij."
                                                      "r-1phboty.r-rs99b7.r-19u6a5r.r-2yi16.r-1qi8awa.r-1ny4l3l."
                                                      "r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr").click()
        else:
            print("Your internet speed is looking good.")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
