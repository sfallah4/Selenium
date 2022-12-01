from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chromeOptions = Options()
chromeOptions.add_argument("--kiosk")

driver=webdriver.Chrome(options=chromeOptions)
driver.get("https://sv-se.facebook.com/r.php?locale=sv_SE&display=page")

ele = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "firstname")))

first_name = driver.find_element(By.NAME, "firstname")
first_name.clear()
first_name.send_keys("Sofia")
last_name = driver.find_element(By.NAME, "lastname")
last_name.clear()
last_name.send_keys("Fallah")
email = driver.find_element(By.NAME, "reg_email__")
email.clear()
email.send_keys("sofia.fallah@iths.se")
conf_email = driver.find_element(By.NAME, "reg_email_confirmation__")
conf_email.clear()
conf_email.send_keys("sofia.fallah@iths.se")
new_pass = driver.find_element(By.NAME, "reg_passwd__")
new_pass.clear()
new_pass.send_keys("Sofia6738!")
time.sleep(1)
day_element = driver.find_element(By.XPATH, "//select[@aria-label='Dag']")
all_options = day_element.find_elements(By.TAG_NAME, "option")
for option in all_options:
    if option.get_attribute("value") == "4":
        option.click()
time.sleep(1)
month_element = driver.find_element(By.XPATH, "//select[@aria-label='Månad']")
all_options = month_element.find_elements(By.TAG_NAME, "option")
for option in all_options:
    if option.get_attribute("value") == "nov":
        option.click()
time.sleep(1)
year_element = driver.find_element(By.XPATH, "//select[@aria-label='År']")
all_options = year_element.find_elements(By.TAG_NAME, "option")
for option in all_options:
    if option.get_attribute("value") == "1989":
        option.click()
time.sleep(1)
checkbox = driver.find_element(By.XPATH, "//label[@class='_58mt']")
checkbox.click()

submit_ele = driver.find_element(By.XPATH, "//button[@type='submit']").click();
#time.sleep(1)
#submit_ele.click()

#name = driver.find_element(By.NAME, "q")
#time.sleep(2)
#name.clear()
#name.send_keys("matta")
#name.send_keys(Keys.RETURN)

driver.quit()