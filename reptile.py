from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import converter
url ='https://tw.carousell.com/categories/women-s-fashion-4/'

options = webdriver.ChromeOptions()
options.add_argument('--headless')

chrome = webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')
chrome.get(url)
soup=BeautifulSoup(chrome.page_source,"html.parser")



    

    

    


