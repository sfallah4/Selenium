from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()
chromeOptions.add_argument("--kiosk")

driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://www.ikea.com/se/sv/")


ele = driver.find_element_by_name("q")
time.sleep(2)
ele.clear()
ele.send_keys("stoense")
ele.send_keys(Keys.RETURN)

driver.close()