from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
import time
import os
import datetime
from webdriver_manager.chrome import ChromeDriverManager
import csv

yourusername = "jackthesmurffff2" #your Instagram username
yourpassword = "jack555"  #your Instagram password

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57"')

driver = webdriver.Chrome(ChromeDriverManager().install())

# === login ===
driver.get('https://www.instagram.com/accounts/login/')
sleep(3)
username_input = driver.find_element_by_css_selector("input[name='username']")
password_input = driver.find_element_by_css_selector("input[name='password']")
username_input.send_keys(yourusername)
password_input.send_keys(yourpassword)
login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Not Now')]"))).click()
sleep(3)

def get_next_target(filename):
    with open(filename, 'r') as f:
        target = f.readline().strip()
    with open(filename, 'r') as r:
        lines = r.readlines()
    with open(filename, 'w') as w:
        w.writelines(lines[1:])
    print(target)
    return target

profile_name = get_next_target("test.txt") #targets.txt
while profile_name != "":
  try: 
    # === Go to profile ===
    driver.get('https://www.instagram.com/%s' % profile_name)
    sleep(2) 
    # driver.find_element_by_xpath('//a[contains(@href, "%s")]' % page).click()
    # scr2 = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
    # sleep(2)
    # text1 = scr2.text
    # print(text1)
    # x = datetime.datetime.now()
    # print(x)
    # driver.find_element_by_xpath('//a[contains(@href, "%s")]' % page).click()
    followers= driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
    followers_text = followers.text
    print(followers_text)
    follower_count = int(followers_text.split()[0])
    print(follower_count)
    # print(followers)
    print("success")
    profile_name = get_next_target("test.txt") #targets.txt
  except Exception as e:
    print(e)
    print("error go next")
    profile_name = get_next_target("test.txt") #targets.txt
