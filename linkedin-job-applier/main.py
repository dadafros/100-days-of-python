from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = "davi_bf@outlook.com"

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3578343703&f_AL=true&f_CR=106057199&f_E=4&"
           "f_TPR=r2592000&f_WT=2&geoId=106057199&keywords=python&location=Brasil&refresh=true&sortBy=R")
time.sleep(2)
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(2)
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
# password_field = driver.find_element(By.ID, "password")
# password_field.send_keys(ACCOUNT_PASSWORD)
# password_field.send_keys(Keys.ENTER)

# Pass security test manually and then press enter to continue
input("Press Enter to continue...")

pages = driver.find_elements(By.CSS_SELECTOR, ".artdeco-pagination__indicator button")
for index in range(len(pages)):
    pages = driver.find_elements(By.CSS_SELECTOR, ".artdeco-pagination__indicator button")
    pages[index].click()
    time.sleep(2)
    print(f"Page {index + 1}")

    all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
    for listing in all_listings:
        print("called")
        listing.click()
        time.sleep(2)

        # Try to locate the apply button, if can't locate then skip the job.
        try:
            apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button")
            apply_button.click()
            time.sleep(2)

            submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

            # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
            if submit_button.get_attribute("aria-label") == "Avançar para próxima etapa":
                close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
                close_button.click()
                time.sleep(2)
                discard_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
                discard_button.click()
                print("Complex application, skipped.")
                continue
            else:
                # Avoid following companies
                driver.find_element(By.CSS_SELECTOR, 'div.job-details-easy-apply-footer__section').click()
                # Submit application
                submit_button.click()

            # Once application completed, close the pop-up window.
            time.sleep(2)
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn").click()

        # If already applied to job or job is no longer accepting applications, then skip.
        except NoSuchElementException:
            print("No application button, skipped.")
            continue

driver.quit()
