from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()
chromeOptions.add_argument("--kiosk")

driver=webdriver.Chrome(options=chromeOptions)
driver.get("https://www.ikea.com/se/sv/")

ele = driver.find_element(By.NAME, "q")
time.sleep(2)
ele.clear()
ele.send_keys("matta")
ele.send_keys(Keys.RETURN)

ele_link = driver.find_element(By.LINK_TEXT, "stoense")
time.sleep(2)
ele_link.click()

driver.close()