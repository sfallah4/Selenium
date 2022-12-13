import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logins import Login
import time

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.logins = Login()
chromeOptions = Options()
chromeOptions.add_argument("--kiosk")

driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://sv-se.facebook.com/r.php?locale=sv_SE&display=page")

ele = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="cookie-policy-manage-dialog-accept-button"]'))).click();
time.sleep(1)

first_name = driver.find_element(By.NAME, "firstname")
first_name.clear()
first_name.send_keys("Sofia")
def test_lookup_by_firstname(self):
    self.logins.add("Sofia", "sofia.fallah@iths.se")
    login = self.logins.lookup("Sofia")
    self.assertEqual("sofia.fallah@iths.se", login)
time.sleep(1)
last_name = driver.find_element(By.NAME, "lastname")
last_name.clear()
last_name.send_keys("Fallah")
def test_lookup_by_lastname(self):
    self.logins.add("Fallah", "sofia.fallah@iths.se")
    login = self.logins.lookup("Fallah")
    self.assertEqual("sofia.fallah@iths.se", login)
time.sleep(1)
email = driver.find_element(By.NAME, "reg_email__")
email.clear()
email.send_keys("sofia.fallah@iths.se")
def test_lookup_by_email(self):
    self.logins.add("sofia.fallah@iths.se", "sofia.fallah@iths.se")
    login = self.logins.lookup("sofia.fallah@iths.se")
    self.assertEqual("sofia.fallah@iths.se", login)
time.sleep(1)
conf_email = driver.find_element(By.NAME, "reg_email_confirmation__")
conf_email.clear()
conf_email.send_keys("sofia.fallah@iths.se")
def test_lookup_by_confemail(self):
    self.logins.add("sofia.fallah@iths.se", "sofia.fallah@iths.se")
    login = self.logins.lookup("sofia.fallah@iths.se")
    self.assertEqual("sofia.fallah@iths.se", login)
time.sleep(1)
def test_missing_name_raises_error(self):
    with self.assertRaises(KeyError):
        self.logins.lookup("missing")

    def test_empty_logins_is_consistent(self):
        self.assertTrue(self.logins.is_consistent())

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
    if option.get_attribute("value") == "11":
        option.click()
time.sleep(1)
year_element = driver.find_element(By.XPATH, "//select[@aria-label='År']")
all_options = year_element.find_elements(By.TAG_NAME, "option")
for option in all_options:
    if option.get_attribute("value") == "1989":
        option.click()

checkbox = driver.find_element(By.XPATH, "//label[@class='_58mt']")
checkbox.click()

submit_ele = driver.find_element(By.XPATH, "//button[@type='submit']").click();
time.sleep(10)
driver.delete_all_cookies()
driver.quit()