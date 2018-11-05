from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time

def add():
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
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'addInspectorButton')))
      print("Page is ready!")
   except TimeoutException:
      print("Loading took too much time!")
   driver.find_element_by_id('addInspectorButton').click()
   try:
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/form/select/option')))
      print("Page is ready!")
   except TimeoutException:
      print("Loading took too much time!")
   driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/select/option').click()
   try:
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'addInspector')))
      print("Page is ready!")
   except TimeoutException:
      print("Loading took too much time!")
   driver.find_element_by_id('addInspector').click()
   time.sleep(3)
   driver.close()



