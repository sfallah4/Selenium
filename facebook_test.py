import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time


class LoginTest:
    def __init__setup(self, login):
        self.login = login

    chromeOptions = Options()
    chromeOptions.add_argument("--kiosk")

    driver = webdriver.Chrome(options=chromeOptions)
    driver.get("https://sv-se.facebook.com/r.php?locale=sv_SE&display=page")

    ele = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="cookie-policy-manage-dialog-accept-button"]'))).click()
    time.sleep(1)

    first_name = driver.find_element(By.NAME, "firstname")
    first_name.clear()
    first_name.send_keys("Sofiaa")

    def test_first_name(self):
        first_name = self.driver.find_element(By.NAME, "firstname")
        first_name = first_name.text
        assert "Sofiaa" in first_name

    time.sleep(1)
    last_name = driver.find_element(By.NAME, "lastname")
    last_name.clear()
    last_name.send_keys("Fallaha")

    def test_last_name(self):
        last_name = self.driver.find_element(By.NAME, "lastname")
        last_name = last_name.text
        assert "Fallaha" in last_name

    email = driver.find_element(By.NAME, "reg_email__")
    email.clear()
    email.send_keys("sofiaa.fallaha@iths.se")

    def test_email(self):
        email = self.driver.find_element(By.NAME, "reg_email__")
        email = email.text
        assert "sofiaa.fallaha@iths.se" in email

    time.sleep(1)
    conf_email = driver.find_element(By.NAME, "reg_email_confirmation__")
    conf_email.clear()
    conf_email.send_keys("sofiaa.fallaha@iths.se")

    def conf_email(self):
        conf_email = self.driver.find_element(By.NAME, "reg_email_confirmation__")
        conf_email = conf_email.text
        assert "sofiaa.fallaha@iths.se" in conf_email

    new_pass = driver.find_element(By.NAME, "reg_passwd__")
    new_pass.clear()
    new_pass.send_keys("Sofia6738!")
    time.sleep(1)

    def test_new_pass(self):
        new_pass = self.driver.find_element(By.NAME, "reg_passwd__")
        new_pass = new_pass.text
        assert "Sofia6738!" in new_pass

    day_element = driver.find_element(By.XPATH, "//select[@aria-label='Dag']")
    all_options = day_element.find_elements(By.TAG_NAME, "option")
    for option in all_options:
        if option.get_attribute("value") == "4":
            option.click()
        time.sleep(1)

    def test_element(self):
        day_element = self.driver.find_element(By.XPATH, "//select[@aria-label='Dag']")
        assert "4" == day_element

    month_element = driver.find_element(By.XPATH, "//select[@aria-label='Månad']")
    all_options = month_element.find_elements(By.TAG_NAME, "option")
    for option in all_options:
        if option.get_attribute("value") == "11":
            option.click()
        time.sleep(1)

    def test_element(self):
        month_element = self.driver.find_element(By.XPATH, "//select[@aria-label='Månad']")
        assert "11" == month_element

    year_element = driver.find_element(By.XPATH, "//select[@aria-label='År']")
    all_options = year_element.find_elements(By.TAG_NAME, "option")
    for option in all_options:
        if option.get_attribute("value") == "1989":
            option.click()

    def test_element(self):
        year_element = self.driver.find_element(By.XPATH, "//select[@aria-label='År']")
        assert "1989" == year_element

    checkbox = driver.find_element(By.XPATH, "//label[@class='_58mt']")
    checkbox.click()

    def test_checkbox(self):
        checked = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Kvinna')]/parent::span").is_selected()
        return checked

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)
    driver.delete_all_cookies()
    driver.quit()
