from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

def main():
    driver = webdriver.Chrome(".\\chromedriver.exe")
    driver.get('https://www.burpple.com/ffl-fresh-fruits-lab')

    #Retrieving of restaurant details

    #location
    location_xpath = driver.find_elements_by_xpath('/html/body/div[3]/div[3]/div/div/div/div[2]/div[1]/a')
    #name
    name_xpath = driver.find_elements_by_xpath('/html/body/div[3]/div[3]/div/div/div/h1/a')
    #category
    categories_xpath = driver.find_elements_by_xpath('/html/body/div[3]/div[3]/div/div/div/div[3]/a')

    #category is in a list
    categories = []
    for category_xpath in categories_xpath:
        categories.append(category_xpath.text)


    # Start Scraping Reviews
    reviews = []


    #Loop to load all reviews
    num_of_review_xpath = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/div/div[1]/div[1]/a')

    # example of text = 43 REVIEWS
    num_of_reviews = int(num_of_review_xpath.text.split()[0])


    #mini logging
    print ('num of reviews', num_of_reviews)


    # get the load more reviews button
    #Loop to load all reviews, slowly click
    if num_of_reviews != 0:
        for i in range(1,num_of_reviews+1,3):
            time.sleep(1)
            try: 
                driver.find_element_by_css_selector('#load-more-reviews').click()
            except:
                pass

            
    review_xpath = driver.find_elements_by_xpath('//*[@id="foodMasonry"]/div/div[2]/div[2]/div[1]/div[2]')

    #Storing of reviews
    if review_xpath.count == 0:
        review = None
    else:
        for review in review_xpath:
            reviews.append({"review": review.text})

    value = None


    #checking empty value
    if num_of_reviews == 0 or len(name_xpath) == 0 or len(categories) == 0 or len(location_xpath) == 0 or review == None:
        #skip this restaurant
        pass
    else:
        #append
        value = (name_xpath[0].text, categories, location_xpath[0].text,num_of_reviews,reviews)

    #close active tab
    driver.close()

    print ('Loading done for FFL')

    return (value, reviews)


    