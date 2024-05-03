import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

"""profession_target = input("What are you looking for?: ")
location_target = input("Where are you looking for?: ")"""

"""split_profession= str(profession_target.split(' '))"""

driver = webdriver.Chrome(options=chrome_options)
driver.get(f"https://www.linkedin.com/jobs/search/?currentJobId=3900901589&f_LF=f_AL&geoId=100025096&keywords=financial%20analyst&location=Toronto%2C%20Ontario%2C%20Canada&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true")

sign_in = driver.find_element(By.XPATH,value="/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()
username_area = driver.find_element(By.ID,value="username")
password_area = driver.find_element(By.ID,value="password")
username = input("Enter Your Username: ")
password = input("Enter Your password: ")

username_area.send_keys(username)
password_area.send_keys(password)
password_area.send_keys(Keys.ENTER)
time.sleep(20)
apply_button= driver.find_element(By.CLASS_NAME,value="jobs-apply-button")
apply_button.click()
time.sleep(2)
next_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Continue to next step']")
next_button.click()
review_button = driver.find_element(By.CSS_SELECTOR,value="button[aria-label='Review your application'")
review_button.click()
submit_button = driver.find_element(By.CSS_SELECTOR,value="button[aria-label='Submit application'")
submit_button.click()

