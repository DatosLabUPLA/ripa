from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time,urllib,csv
from bs4 import BeautifulSoup
from selenium.common import exceptions as SE
import pandas as pd

def art_autonoma():

    options = webdriver.ChromeOptions() 
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    s = Service('chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    locators = "//button[.//span[text()='Mostrar más'] and not(@disabled)]" 
    wait_time = 3

    wait = W(driver,wait_time)

    urls = []
    datos = []
    coautores = []

    with open("DATA2/autonoma.csv", 'r') as f:
            reader = csv.DictReader(f)
            for i in reader:
                urls.append(i['detalles'])

    for url in urls:
        try:      
            driver.get(url)  
        except Exception as e:
            pass
                  
        while True:
            try:
                wait.until(EC.visibility_of_element_located((By.ID,'gsc_bdy')))
                soup = BeautifulSoup(driver.page_source,'lxml')
                posts = soup.find_all('div', attrs={'class': 'gsc_lcl'})
                time.sleep(2)

                for autores in posts:
                    
                    nombre = soup.find(id='gsc_prf_in').text or ''
                    name_attributes = soup.find('div', attrs={'class': 'gsc_prf_il'}).text or ''
                    mail = autores.find(id='gsc_prf_ivh')
                    z = str(mail)
                    correo = (z[74:82])
                    interes = autores.find(id='gsc_prf_int')
                    research_article = autores.find_all('tr',{'class':'gsc_a_tr'})

                    for article_info in research_article:
                        pub_details = article_info.find('td', attrs={'class': 'gsc_a_t'})
                        pub_ref = pub_details.a['href']
                        pub_meta = pub_details.find_all('div')
                        title_link = article_info.select_one('.gsc_a_at')['href']

                        id = 'autonoma'       
                        title = pub_details.a.text or ''
                        authors = pub_meta[0].text or ''
                        journal = pub_meta[1].text or ''
                        cited_by = article_info.find('td', attrs={'class': 'gsc_a_c'}).text or ''
                        year = article_info.find('td', attrs={'class': 'gsc_a_y'}).text or ''

                        linkpaper = urllib.parse.urljoin("https://scholar.google.com", title_link)
                        idp_a = linkpaper.split('=')[-1] or ''  # id paper-autor
                        id_a = idp_a.split(':')[-2] or '' # id autor
                
                        datos.append([id_a,id,nombre,name_attributes,correo,interes,title,authors,journal,cited_by,year])   
            
                    datas =  pd.DataFrame(datos, columns=['idgs','id','nombre','atributos','correo','intereses','titulo','autores','revista','citado por','año'])
                    datas.to_csv('ARTICULOS/articulos_autonoma.csv', index=False)

                try:
                    for coautho in soup.find('ul', class_='gsc_rsb_a'):
                        nameco = coautho.find('a', attrs={'tabindex': '-1'})
                        coautor = nameco.text or ''
                        l = nameco.get('href')
                        c = l.split('=')[1]
                        idco = c.split('&')[-2] or ''
                        inst = coautho.find('span', attrs={'class': 'gsc_rsb_a_ext'}).text or ''
                                
                        try: 
                            dominioc = coautho.find(class_='gsc_rsb_a_ext gsc_rsb_a_ext2').get_text()
                        except:
                            pass    
                        coautores.append([id_a,idco,coautor,dominioc,inst])        
            
                    data =  pd.DataFrame(coautores, columns=['id_gs','idco','nombre_coautor','dominio','cargo'])
                    data.to_csv('COAUTORES/coautores_autonoma.csv', index=False)     
                        
                except:
                    pass   
            
                botton = wait.until(EC.element_to_be_clickable((By.XPATH,locators)))
                botton.click()

            except SE.TimeoutException:
                break
    print('Termino con la Universidad Autonoma')
    driver.quit()

def art_upla():

    options = webdriver.ChromeOptions() 
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    s = Service('chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    locators = "//button[.//span[text()='Mostrar más'] and not(@disabled)]" 
    wait_time = 3

    wait = W(driver,wait_time)

    urls = []
    datos = []
    coautores = []

    with open("DATA2/upla.csv", 'r') as f:
            reader = csv.DictReader(f)
            for i in reader:
                urls.append(i['detalles'])

    for url in urls:
        try:      
            driver.get(url)  
        except Exception as e:
            pass
                  
        while True:
            try:
                wait.until(EC.visibility_of_element_located((By.ID,'gsc_bdy')))
                soup = BeautifulSoup(driver.page_source,'lxml')
                posts = soup.find_all('div', attrs={'class': 'gsc_lcl'})
                time.sleep(2)

                for autores in posts:
                    
                    nombre = soup.find(id='gsc_prf_in').text or ''
                    name_attributes = soup.find('div', attrs={'class': 'gsc_prf_il'}).text or ''
                    mail = autores.find(id='gsc_prf_ivh')
                    z = str(mail)
                    correo = (z[74:82])
                    interes = autores.find(id='gsc_prf_int')
                    research_article = autores.find_all('tr',{'class':'gsc_a_tr'})

                    for article_info in research_article:
                        pub_details = article_info.find('td', attrs={'class': 'gsc_a_t'})
                        pub_ref = pub_details.a['href']
                        pub_meta = pub_details.find_all('div')
                        title_link = article_info.select_one('.gsc_a_at')['href']

                        id = 'upla'       
                        title = pub_details.a.text or ''
                        authors = pub_meta[0].text or ''
                        journal = pub_meta[1].text or ''
                        cited_by = article_info.find('td', attrs={'class': 'gsc_a_c'}).text or ''
                        year = article_info.find('td', attrs={'class': 'gsc_a_y'}).text or ''

                        linkpaper = urllib.parse.urljoin("https://scholar.google.com", title_link)
                        idp_a = linkpaper.split('=')[-1] or ''  # id paper-autor
                        id_a = idp_a.split(':')[-2] or '' # id autor
                
                        datos.append([id_a,id,nombre,name_attributes,correo,interes,title,authors,journal,cited_by,year])   
            
                    datas =  pd.DataFrame(datos, columns=['idgs','id','nombre','atributos','correo','intereses','titulo','autores','revista','citado por','año'])
                    datas.to_csv('ARTICULOS/articulos_upla.csv', index=False)

                try:
                    for coautho in soup.find('ul', class_='gsc_rsb_a'):
                        nameco = coautho.find('a', attrs={'tabindex': '-1'})
                        coautor = nameco.text or ''
                        l = nameco.get('href')
                        c = l.split('=')[1]
                        idco = c.split('&')[-2] or ''
                        inst = coautho.find('span', attrs={'class': 'gsc_rsb_a_ext'}).text or ''
                                
                        try: 
                            dominioc = coautho.find(class_='gsc_rsb_a_ext gsc_rsb_a_ext2').get_text()
                        except:
                            pass    
                        coautores.append([id_a,idco,coautor,dominioc,inst])        
            
                    data =  pd.DataFrame(coautores, columns=['id_gs','idco','nombre_coautor','dominio','cargo'])
                    data.to_csv('COAUTORES/coautores_upla.csv', index=False)     
                        
                except:
                    pass   
            
                botton = wait.until(EC.element_to_be_clickable((By.XPATH,locators)))
                botton.click()

            except SE.TimeoutException:
                break
    print('Termino con la Universidad de Playa Ancha')
    driver.quit()
    
def art_adolfoi():

    options = webdriver.ChromeOptions() 
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')

    s = Service('chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    locators = "//button[.//span[text()='Mostrar más'] and not(@disabled)]" 
    wait_time = 3

    wait = W(driver,wait_time)

    urls = []
    datos = []
    coautores = []

    with open("DATA2/uadolfoi.csv", 'r') as f:
            reader = csv.DictReader(f)
            for i in reader:
                urls.append(i['detalles'])

    for url in urls:
        try:      
            driver.get(url)  
        except Exception as e:
            pass
                  
        while True:
            try:
                wait.until(EC.visibility_of_element_located((By.ID,'gsc_bdy')))
                soup = BeautifulSoup(driver.page_source,'lxml')
                posts = soup.find_all('div', attrs={'class': 'gsc_lcl'})
                time.sleep(2)

                for autores in posts:
                    
                    nombre = soup.find(id='gsc_prf_in').text or ''
                    name_attributes = soup.find('div', attrs={'class': 'gsc_prf_il'}).text or ''
                    mail = autores.find(id='gsc_prf_ivh')
                    z = str(mail)
                    correo = (z[74:82])
                    interes = autores.find(id='gsc_prf_int')
                    research_article = autores.find_all('tr',{'class':'gsc_a_tr'})

                    for article_info in research_article:
                        pub_details = article_info.find('td', attrs={'class': 'gsc_a_t'})
                        pub_ref = pub_details.a['href']
                        pub_meta = pub_details.find_all('div')
                        title_link = article_info.select_one('.gsc_a_at')['href']

                        id = 'adolfoi'       
                        title = pub_details.a.text or ''
                        authors = pub_meta[0].text or ''
                        journal = pub_meta[1].text or ''
                        cited_by = article_info.find('td', attrs={'class': 'gsc_a_c'}).text or ''
                        year = article_info.find('td', attrs={'class': 'gsc_a_y'}).text or ''

                        linkpaper = urllib.parse.urljoin("https://scholar.google.com", title_link)
                        idp_a = linkpaper.split('=')[-1] or ''  # id paper-autor
                        id_a = idp_a.split(':')[-2] or '' # id autor
                
                        datos.append([id_a,id,nombre,name_attributes,correo,interes,title,authors,journal,cited_by,year])   
            
                    datas =  pd.DataFrame(datos, columns=['idgs','id','nombre','atributos','correo','intereses','titulo','autores','revista','citado por','año'])
                    datas.to_csv('ARTICULOS/articulos_adolfo.csv', index=False)

                try:
                    for coautho in soup.find('ul', class_='gsc_rsb_a'):
                        nameco = coautho.find('a', attrs={'tabindex': '-1'})
                        coautor = nameco.text or ''
                        l = nameco.get('href')
                        c = l.split('=')[1]
                        idco = c.split('&')[-2] or ''
                        inst = coautho.find('span', attrs={'class': 'gsc_rsb_a_ext'}).text or ''
                                
                        try: 
                            dominioc = coautho.find(class_='gsc_rsb_a_ext gsc_rsb_a_ext2').get_text()
                        except:
                            pass    
                        coautores.append([id_a,idco,coautor,dominioc,inst])        
            
                    data =  pd.DataFrame(coautores, columns=['id_gs','idco','nombre_coautor','dominio','cargo'])
                    data.to_csv('COAUTORES/coautores_adolfo.csv', index=False)     
                        
                except:
                    pass   
            
                botton = wait.until(EC.element_to_be_clickable((By.XPATH,locators)))
                botton.click()

            except SE.TimeoutException:
                break
    print('Termino con la Universidad Adolfo Ibañez')
    driver.quit()


