import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options
import time

def scrape_website(website):
    print("launching chrome browser")

    options = Options()
    driver = webdriver.Chrome(options=options)  

    try:
        driver.get(website)
        print("Page Loaded...")
        html = driver.page_source
        time.sleep(10)
        return html
    finally:
        driver.quit()