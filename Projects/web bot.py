from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="C:/Users/user/Desktop/chromedriver")
driver.get("https://instagram.com/")
sleep(5)

driver.find_element_by_xpath(('/button[@type="submit"]'))\
	.click()