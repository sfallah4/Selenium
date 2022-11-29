from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.ikea.com/se/sv/")
driver.close()