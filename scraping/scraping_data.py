# File in folder 'Scraping'
PATH_LINKS_SCRAPED_CLEAN = ""
# Place '/' at the end
PATH_NORMAL_FOLDER = ""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from utils.scrape import page_scrape
import time

service = Service(executable_path="chromedriver.exe")
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

driver.implicitly_wait(2)
time.sleep(5)
try:
    f = open(PATH_LINKS_SCRAPED_CLEAN, 'r')

    all_url_animals = f.readlines()
    start_point= None
    next_one = True
    double_dot = [j for j in all_url_animals if ":" in j]
    print(double_dot)
    for last_url_link_animal in all_url_animals:
        if  (start_point in last_url_link_animal) or next_one:
         #if last_url_link_animal in battles:
            next_one = True
            print("link " + last_url_link_animal)
            name_animal = last_url_link_animal.replace(":", "_")[last_url_link_animal.rfind('/')+1:-1]

            print("nome cosa " + name_animal)

            wiki_link = "https://it.wikipedia.org"
            viki_link = "https://it.vikidia.org"
            print("start--------------------")
            
            page_scrape(last_url_link_animal,
                        wiki_link,
                        By.ID,
                        "mw-content-text",
                        driver,
                        PATH_NORMAL_FOLDER + "wiki-" + name_animal + ".html",
                        "wiki")
            
            page_scrape(last_url_link_animal,
                        viki_link,
                        By.ID,
                        "bodyContent",
                        driver,
                        PATH_NORMAL_FOLDER + "viki-" + name_animal + ".html",
                        "viki")
            

except Exception as inst:
    print("problems")
    print(inst)
finally:
    f.close()
