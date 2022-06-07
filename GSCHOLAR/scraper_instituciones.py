from multiprocessing.connection import wait
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import exceptions as SE
from selenium.webdriver.chrome.options import Options
import time,datetime,csv
from bs4 import BeautifulSoup
import pandas as pd
datos = []
data = []

def uautonoma():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=6219877915722792561" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 6219877915722792561
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'uautonoma'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('autonoma.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad Autonoma')
            break
    driver.quit()
uautonoma()#Universidad Autonoma

def uadolfoi():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=10448777709790852446" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 10448777709790852446
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'uadolfoi'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('uadolfoi.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad Adolfo Ibañez')
            break
    driver.quit()
uadolfoi()#Adolfo Ibañez

def uandes():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=6615366460316766280" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 6615366460316766280
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'uandes'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('uandes.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad de los Andes')
            break
    driver.quit()
uandes()#Universidad de los Andes

def udd():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=4794720163447555879" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 4794720163447555879
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'udd'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('udd.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
udd()#Universidad del Desarrollo

def unab():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=13542589241086358186" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 13542589241086358186
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'unab'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('unab.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
unab()#Universidad Andres Bello

def uss():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=1812728570911196340" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 1812728570911196340
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'uss'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('uss.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
uss()#Universidad San Sebastian

def santotomas():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=14018219609791295521" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 14018219609791295521
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'santotomas'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('santotomas.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
santotomas()#Universidad Santo Tomas

def uc():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=7459009050823923954" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 7459009050823923954
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'uc'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('uc.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
uc()#Universidad Catolica de Chile

def pucv():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=7698552169257898503" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 7698552169257898503
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'pucv'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('pucv.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
pucv()#Universidad Catolica Valparaiso

def uach():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=16206413231987421209" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 16206413231987421209
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'uach'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('uach.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
uach()#Universidad Austral de Chile

def uahurtado():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=15469411678705648791" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 15469411678705648791
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'uahurtado'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('uahurtado.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
uahurtado()#Universidad Alberto Hurtado

def ucm():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=12968600147058256171" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 12968600147058256171
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'ucm'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('ucm.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
ucm()#Universidad Catolica del Maule

def ucn():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=17255630398072300451" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 17255630398072300451
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'ucn'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('ucn.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
ucn()#Universidad Catolica del Norte

def ucsc():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=3702576657308349741" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 3702576657308349741
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'ucsc'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('ucsc.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
ucsc()#Universidad Catolica de la Santisima Concepcion

def uct():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=12740943834737827853" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 12740943834737827853
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'uct'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('uct.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
uct()#Universidad Catolica de Temuco

def udec():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=4555896482842878823" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 4555896482842878823
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'udec'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('udec.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
udec()#Universidad de Concepcion

def udp():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=12216913016116922734" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 12216913016116922734
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'udp'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('udp.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
udp()#Universidad Diego Portales

def usm():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=9225498103198054248" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 9225498103198054248
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'usm'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('usm.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
usm()#Universidad Santa Maria

def uantof():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=7010446216104013295" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 7010446216104013295
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'uantof'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('uantof.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
uantof()#Universidad Antofagasta

def ubiobio():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=8365100606562762008" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 8365100606562762008
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'ubiobio'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('ubiobio.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
ubiobio()#Universidad Bio Bio

def uchile():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=9232372474901007921" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 9232372474901007921
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'uchile'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('uchile.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
uchile()#Universidad de Chile

def ufrontera():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=13908003347799972066" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 13908003347799972066
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'ufrontera'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('ufrontera.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
ufrontera()#Universidad de la Frontera

def ulagos():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=13824009975929506544" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 13824009975929506544
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'ulagos'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('ulagos.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
ulagos()#Universidad de los Lagos

def userena():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=6030355530770144394" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 6030355530770144394
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'userena'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('userena.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
userena()#Universidad de la Serena

def umag():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=14351944662178497517" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 14351944662178497517
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'umag'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('umag.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
umag()#Universidad Magallanes

def unap():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=18273373707046377092" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 18273373707046377092
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'unap'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('unap.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
unap()#Universidad Arturo Prat

def upla():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=8337597745079551909" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 8337597745079551909
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'upla'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('upla.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
upla()#universidad de Playa Ancha

def usach():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=605437563739143535" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 605437563739143535
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'usach'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('usach.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
usach()#Universidad Santiago de Chile

def uta():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=4727335469935944428" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 4727335469935944428
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'uta'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('uta.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
uta()#Universidad de Tarapaca

def utalca():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=7732664165981901274" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 7732664165981901274
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'utalca'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('utalca.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
utalca()#Universidad de Talca

def uv():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

    button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
    wait = WebDriverWait(driver,2)

    data= []
    url="https://scholar.google.cl/citations?view_op=view_org&org=17388732461633852730" 
    data.append(url)

    for url in data:
        driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                id_gs = 17388732461633852730
                autor = autores.find(class_='gs_ai_name').text
                cargo = autores.find(class_='gs_ai_aff').text
                id_institucion = 'uv'
                email = autores.find(class_='gs_ai_eml').text
                citaciones = autores.find(class_='gs_ai_cby').text
                intereses = autores.find(class_='gs_ai_int').text
                datos.append([id_gs,autor,cargo,id_institucion,email,citaciones,intereses])

            datas =  pd.DataFrame(datos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('uv.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()
uv()#Universidad de Valparaiso    