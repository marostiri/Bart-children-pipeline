PATH_CHROMEDRIVER = ""
# File in folder 'Scraping'
PATH_LINKS_SCRAPED = ""
from utils.recover import Crawler

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=PATH_CHROMEDRIVER)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.implicitly_wait(4)

url = "https://it.vikidia.org/wiki/Categoria:Enciclopedia"
part_url_check = "Categoria:"

crawler_vikidia = Crawler(driver, url, part_url_check)
crawler_vikidia.bfs()
crawler_vikidia.write_to_file(PATH_LINKS_SCRAPED)


driver.quit()