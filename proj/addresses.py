from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time

def addresses():
    driver=webdriver.Firefox()
    driver.get('http://localhost:8080/loginPage')
    driver.find_element_by_id('email').send_keys('manager1@gmail.com')
    driver.find_element_by_id('password').send_keys('Admin123')
    driver.find_element_by_id('Login_button').click()
    try:
       WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[1]/div/div[3]/div/ul/li[1]/a')))
       print("Page is ready!")
    except TimeoutException:
       print("Loading took too much time!")
    driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[3]/div/ul/li[1]/a').click()
    try:
       WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'second-tab')))
       print("Page is ready!")
    except TimeoutException:
       print("Loading took too much time!")
    driver.find_element_by_id('second-tab').click()
    time.sleep(5)
    driver.close()
