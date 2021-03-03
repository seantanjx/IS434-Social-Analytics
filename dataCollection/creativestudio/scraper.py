from selenium import webdriver
import pandas as pd
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("..\\burpple\\chromedriver.exe")

url = "https://business.facebook.com/creatorstudio/?tab=instagram_content_posts&collection_id=all_pages&content_table=INSTAGRAM_POSTS"


def main():
    data = []
    
    driver.get(url)
    driver.find_element_by_css_selector('#u_0_0 > div.owos4q6p.i13oxjmd.lcadhjjw.szx3xb1e.smvj6ueq.kjd6ay9q > div > div.tn4wt7vy > div > div > div > div:nth-child(2) > div > div > span > div > div > div').click()
    time.sleep(2)
    
    # TODO: Change the username and password
    driver.find_element_by_css_selector("#email").send_keys("")
    driver.find_element_by_css_selector("#pass").send_keys("")
    time.sleep(1)
    
    driver.find_element_by_css_selector("#loginbutton").click()

    # Switch to Instagram Content Instead
    url = "https://business.facebook.com/creatorstudio/?tab=instagram_content_posts&collection_id=all_pages&content_table=INSTAGRAM_POSTS"
    time.sleep(1)
    driver.get(url)

    # Div spacing is 3 each in intervals
    for i in range(3, 100, 3):
        
        print("the loop is now {}:{}".format(i//3, i))
        time.sleep(2)
        content_xpath = '//*[@id="js_20"]/div/div/div/div[1]/div/div/div[3]/div/div/div[{}]/div/div/span'.format(i)
        
        # Check if this content element is available
        contents = driver.find_elements_by_xpath(content_xpath)
        if contents == []:
            break

        content = contents[0]


        # Move/scroll to that element in order to interact with that element
        print("Moving to the content element now!")
        actions = ActionChains(driver) # Defining action chain to make the action to scroll to the element
        actions.move_to_element(content).perform()

        # Click the content, which will see the pop up at the side
        content.click()
        time.sleep(2)

        
        # Pull and print the content and impressions
        try:
            # 1.0 Original Content
            image = driver.find_element_by_xpath('//*[@id="creator_studio_sliding_tray_root"]/div/div/div[2]/div[1]/div/div[2]/div/div/div/div/div[1]/div/div/div/img')
            image_link = image.get_attribute("src")

            caption = driver.find_element_by_xpath('//*[@id="creator_studio_sliding_tray_root"]/div/div/div[2]/div[1]/div/div[3]/div/p/span').text

            print("link:", image_link)
            print("caption:", caption)

            # 2.0 Stats
            stats = driver.find_elements_by_xpath('//*[@id="creator_studio_sliding_tray_root"]/div/div/div[2]/div[2]/div[4]')[0]

            stats_list = stats.text.split("\n")

            # estimate count
            if len(stats_list) > 8:
                print("Follows:", stats_list[5])
                print("Reached:", stats_list[7])
                print("Impression:", stats_list[9])
                print("From Account:", stats_list[11])
                
                # since if run until here means there are stats, so lets append it into data
                data.append({
                    "image_link": image_link,
                    "caption": caption,
                    "follows": stats_list[5],
                    "reached": stats_list[7],
                    "impression": stats_list[9],
                    "from_account": stats_list[11]
                })
                
        except:
            print("No stats available for this port")


        # close the popup content stats
        print('\nclosing\n')
        driver.find_element_by_xpath('//*[@id="creator_studio_sliding_tray_root"]/div/div/div[1]/div[1]').click()
        time.sleep(3)


    print('done')

