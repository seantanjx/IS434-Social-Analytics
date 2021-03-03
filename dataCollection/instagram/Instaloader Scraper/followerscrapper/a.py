import time
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

# The account you want to check
account = "freshfruitslab"

# Chrome executable
options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--lang=en-GB")
options = webdriver.ChromeOptions()
chrome_driver_binary = "/usr/local/bin/chromedriver"
input_driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)


def login(driver):
    username = "jackthesmurffff2"   # Your username
    password = "jack555"   # Your password

    # Load page
    driver.get("https://www.instagram.com/accounts/login/")

    # Login
    driver.find_element_by_xpath("/div/input[@name='username']").send_keys(username)
    driver.find_element_by_xpath("/div/input[@name='password']").send_keys(password)
    driver.find_element_by_xpath("/span/button").click()

    popup = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div/div/button[contains(., Close)]')))
    driver.find_element_by_xpath("//div/div/button[contains(., Close)]").click()

    # # Wait for the login page to load
    # WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.LINK_TEXT, "See All")))

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.Szr5J.coreSpriteHeartOpen')))


def scrape_followers(driver, account):
    # Load account page
    driver.get("https://www.instagram.com/{0}/".format(account))

    # Click the 'Follower(s)' link
    driver.find_element_by_partial_link_text("follower").click()

    # Wait for the followers modal to load
    xpath = "/html/body/div[4]/div/div/div[2]/div/div[2]"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath)))

    SCROLL_PAUSE = 0.5  # Pause to allow loading of content
    driver.execute_script("followersbox = document.getElementsByClassName('_gs38e')[0];")
    last_height = driver.execute_script("return followersbox.scrollHeight;")

    # We need to scroll the followers modal to ensure that all followers are loaded
    while True:
        driver.execute_script("followersbox.scrollTo(0, followersbox.scrollHeight);")

        # Wait for page to load
        time.sleep(SCROLL_PAUSE)

        # Calculate new scrollHeight and compare with the previous
        new_height = driver.execute_script("return followersbox.scrollHeight;")
        if new_height == last_height:
            break
        last_height = new_height

    # Finally, scrape the followers
    xpath = "/html/body/div[4]/div/div/div[2]/div/div[2]/ul/li"
    followers_elems = driver.find_elements_by_xpath(xpath)

    followers_temp = [e.text for e in followers_elems]  # List of followers (username, full name, follow text)
    followers = []  # List of followers (usernames only)

    # Go through each entry in the list, append the username to the followers list
    for i in followers_temp:
        username, sep, name = i.partition('\n')
        followers.append(username)

    print("______________________________________")
    print("FOLLOWERS")

    return followers

def scrape_following(driver, account):
    # Load account page
    driver.get("https://www.instagram.com/{0}/".format(account))

    # Click the 'Following' link
    driver.find_element_by_partial_link_text("following").click()

    # Wait for the following modal to load
    xpath = "/html/body/div[4]/div/div/div[2]/div/div[2]"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath)))

    SCROLL_PAUSE = 0.5  # Pause to allow loading of content
    driver.execute_script("followingbox = document.getElementsByClassName('_gs38e')[0];")
    last_height = driver.execute_script("return followingbox.scrollHeight;")

    # We need to scroll the following modal to ensure that all following are loaded
    while True:
        driver.execute_script("followingbox.scrollTo(0, followingbox.scrollHeight);")

        # Wait for page to load
        time.sleep(SCROLL_PAUSE)

        # Calculate new scrollHeight and compare with the previous
        new_height = driver.execute_script("return followingbox.scrollHeight;")
        if new_height == last_height:
            break
        last_height = new_height

    # Finally, scrape the following
    xpath = "/html/body/div[4]/div/div/div[2]/div/div[2]/ul/li"
    following_elems = driver.find_elements_by_xpath(xpath)

    following_temp = [e.text for e in following_elems]  # List of following (username, full name, follow text)
    following = []  # List of following (usernames only)

    # Go through each entry in the list, append the username to the following list
    for i in following_temp:
        username, sep, name = i.partition('\n')
        following.append(username)

    print("\n______________________________________")
    print("FOLLOWING")
    return following


if __name__ == "__main__":
    options = wd.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("--lang=en-GB")
    chrome_driver_binary = "/usr/local/bin/chromedriver"
    input_driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
    driver_binary = "/usr/local/bin/chromedriver"
    driver = wd.Chrome(driver_binary, chrome_options=options)
    try:
        login(driver)
        followers = scrape_followers(driver, account)
        print(followers)
        following = scrape_following(driver, account)
        print(following)
    finally:
        driver.quit()