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

def uautonoma():
    autonoma = []

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()
                identificador = str(text[33:46]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                autonoma.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(autonoma, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/autonoma.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad Autonoma')
            break
    driver.quit()


def uadolfoi():
    adolfo=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()
                identificador = str(text[33:40]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                adolfo.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])
            
            datas =  pd.DataFrame(adolfo, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/uadolfoi.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad Adolfo Ibañez')
            break
    driver.quit()


def uandes():
    andes=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()
                identificador = str(text[33:43]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                andes.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(andes, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/uandes.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad de los Andes')
            break
    driver.quit()


def udd():
    desarrollo=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()
                identificador = str(text[33:40]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                desarrollo.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(desarrollo, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/udd.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Desarrollo')
            break
    driver.quit()


def unab():
    unab=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:41]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                unab.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(unab, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/unab.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad Andres Bello')
            break
    driver.quit()


def uss():
    uss=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:40]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                uss.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(uss, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/uss.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad San Sebastian')
            break
    driver.quit()


def santotomas():
    santotomas=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:47]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                santotomas.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(santotomas, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/santotomas.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad Santo Tomas')
            break
    driver.quit()


def uc():
    uc=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:45]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                uc.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(uc, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/uc.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad Catolica')
            break
    driver.quit()


def pucv():
    pucv=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()               
                identificador = str(text[33:40]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                pucv.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(pucv, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/pucv.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad Catolica Valparaiso')
            break
    driver.quit()


def uach():
    uach=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()               
                identificador = str(text[33:49]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                uach.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(uach, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/uach.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad Austral')
            break
    driver.quit()


def uahurtado():
    hurtado=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:46]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                hurtado.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(hurtado, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/uahurtado.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad Alberto Hurtado')
            break
    driver.quit()


def ucm():
    ucm =[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:40]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                ucm.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(ucm, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/ucm.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad Catolica del Maule')
            break
    driver.quit()


def ucn():
    ucn=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:40]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                ucn.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(ucn, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/ucn.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad Catolica del Norte')
            break
    driver.quit()


def ucsc():
    ucsc=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:41]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                ucsc.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(ucsc, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/ucsc.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad Catolica de la Santisima Concepcion')
            break
    driver.quit()


def uct():
    uct=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:46]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                uct.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(uct, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/uct.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad Catolica de Temuco')
            break
    driver.quit()


def udec():
    udec=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:47]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                udec.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(udec, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/udec.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad de Concepcion')
            break
    driver.quit()


def udp():
    udp=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:47]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                udp.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(udp, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/udp.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad Diego Portales')
            break
    driver.quit()


def usm():
    usm=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:40]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                usm.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(usm, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/usm.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad Santa Maria')
            break
    driver.quit()


def uantof():
    uantof=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:43]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                uantof.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(uantof, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/uantof.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad de Antofagasta')
            break
    driver.quit()


def ubiobio():
    biobio=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:44]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                biobio.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(biobio, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/ubiobio.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad del Bio-Bio')
            break
    driver.quit()


def uchile():
    chile=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:44]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                chile.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(chile, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/uchile.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad de Chile')
            break
    driver.quit()


def ufrontera():
    frontera=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:46]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                frontera.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(frontera, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/ufrontera.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad de la Frontera')
            break
    driver.quit()


def ulagos():
    lagos=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:43]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                lagos.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(lagos, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/ulagos.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad de los Lagos')
            break
    driver.quit()


def userena():
    serena=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:44]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                serena.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(serena, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/userena.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad de la Serena')
            break
    driver.quit()


def umag():
    umag=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:41]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                umag.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(umag, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/umag.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad de Magallanes')
            break
    driver.quit()


def unap():
    unap=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:41]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                unap.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(unap, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/unap.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad Arturo Prat')
            break
    driver.quit()


def upla():
    upla=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:41]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                upla.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(upla, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/upla.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad de Playa Ancha')
            break
    driver.quit()


def usach():
    usach=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:42]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                usach.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(usach, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/usach.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad de Santiago de Chile')
            break
    driver.quit()


def uta():
    uta=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:51]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                uta.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(uta, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/uta.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad de Tarapaca')
            break
    driver.quit()


def utalca():
    talca=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:52]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                talca.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(talca, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/utalca.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad de Talca')
            break
    driver.quit()


def uv():
    uv=[]

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
                mail = autores.find_all(class_='gs_ai_eml')
                text=mail[0].get_text()                
                identificador = str(text[33:39]).strip(' ')
                citaciones = autores.find_all(class_='gs_ai_cby')
                cita=citaciones[0].get_text()
                cantidad = str(cita[11:17]).strip(' ')
                intereses = autores.find(class_='gs_ai_int').text
                uv.append([id_gs,autor,cargo,id_institucion,identificador,cantidad,intereses])

            datas =  pd.DataFrame(uv, columns=['id_gs','autor','cargo','id_institucion','email','citaciones','intereses'])
            datas.to_csv('DATA/uv.csv', index=False)    
            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Termino con la Universidad de Valparaiso')
            break
    driver.quit()  