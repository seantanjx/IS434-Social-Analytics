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

count = 500  # number of profiles you want to scrap
page = "followers"  # from following or followers

yourusername = "" #your Instagram username
yourpassword = ""  #your Instagram password

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57"')

driver = webdriver.Chrome(ChromeDriverManager().install())

# === Functions ===
def read_file(filename):
    result = []
    with open(filename, 'r') as f:
        for line in f:
            result.append(line.strip())
    return result

def get_next_target(filename):
    with open(filename, 'r') as f:
        target = f.readline().strip()
    with open(filename, 'r') as r:
        lines = r.readlines()
    with open(filename, 'w') as w:
        w.writelines(lines[1:])
    print(target)
    return target

def write_file(write_list, filename):
    with open(filename, 'w') as f:
        result = ''
        for line in write_list:
            have_emoji = False
            for ch in line:
                if len(ch) != len(ch.encode()):
                    have_emoji = True
            if not have_emoji:
                result += line + '\n'
        f.write(result.strip())

def append_file(follower, filename):
    with open(filename, 'a') as f:
        result = follower + '\n'
        f.write(result)

def user_tracked(profile_name):
    # Track if user has been scraped
    tracked_list = read_file("tracked_list.txt")
    if profile_name in tracked_list:
        return True
    return False

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


profile_name = get_next_target("targets.txt") #targets.txt
while profile_name != "":
  try: 
    # Track if user has been scraped
    user_tracked_check = user_tracked(profile_name)
    if user_tracked_check:
        print("user tracked: " + profile_name)
        profile_name = get_next_target("targets.txt")
        continue
    # === Go to profile ===
    driver.get('https://www.instagram.com/%s' % profile_name)
    sleep(3) 
    driver.find_element_by_xpath('//a[contains(@href, "%s")]' % page).click()
    scr2 = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
    sleep(3)
    followers_text = scr2.text
    # follower_count = int(followers_text.split()[0])
    # print(follower_count)
    print(followers_text)
    x = datetime.datetime.now()
    print(x)

    # === Scrape followers ===
    for i in range(1,count):
      scr1 = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[%s]' % i)
      driver.execute_script("arguments[0].scrollIntoView();", scr1)
      sleep(1)
      text = scr1.text
      list = text.encode('utf-8').split()

      #Add to csv
      dirname = os.path.dirname(os.path.abspath(__file__))
      # csvfilename = os.path.join(dirname, profile_name + "-" + page + "magical" + ".csv") #filename
      csvfilename = "freshfruitslab_followers.csv" #freshfruitslab_followers.csv
      file_exists = os.path.isfile(csvfilename)


      with open(csvfilename, 'a', newline='') as followerCSV:
        follower = str(list[0])[2:-1]
        followerWriter = csv.writer(followerCSV, delimiter=',')
        rowData = profile_name + " " + follower
        print(rowData)
        followerWriter.writerow([rowData]) #write into csv
        append_file(follower, "targets.txt") #write into targets.txt
      
      if count == 10000:
        break

    print("end of max loop")
    profile_name = get_next_target("targets.txt") #targets.txt
    # profile_name = get_next_target("test.txt") #targets.txt

      # f = open(csvfilename,'a')
      # follower = str(list[0])[2:-1]
      # f.write(str(profile_name) + "-" + follower + "\r\n")
      # f.close()
      # print('{};{}'.format(i, list[0]))
      # if i == (count-1):
      #   print(x)
  except Exception as e:
    print(e)
    print("end of follower list")
    profile_name = get_next_target("targets.txt") #targets.txt
    continue
