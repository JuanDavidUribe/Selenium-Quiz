from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="Driver/chromedriver.exe")

driver.maximize_window()

time.sleep(2)