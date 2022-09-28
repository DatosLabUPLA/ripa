#from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument('--headless')

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)

urls = ["https://scholar.google.com/citations?hl=es&user=gQb_tFMAAAAJ",
"https://scholar.google.com/citations?hl=es&user=hvjk24EAAAAJ"]

locators = "//button[.//span[text()='Mostrar más'] and not(@disabled)]" 
wait_time = 3

wait = W(driver,wait_time)

for url in urls:
    try:      
        driver.get(url)  
    except Exception as e:
        print(e)
      
    while True:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_bdy')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_lcl'})
            time.sleep(2)
            
            botton = wait.until(EC.element_to_be_clickable((By.XPATH,locators)))
            botton.click()

        except Exception as e:
            print(e)
driver.quit()
