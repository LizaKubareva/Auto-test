from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
s=Service("C:\\Users\\e.kubareva\\PycharmProjects\\pythonProject\\drivers\\windows\\chromedriver.exe")
browser = webdriver.Chrome(service=s)
urls = ["https://myfitnessclub.ru/" ]


try:
    for url in urls:
        print(url)
        time.sleep(3)
        page = browser.get(url=url)
        button = browser.find_element("xpath",'//*[@id="prise_1"]/div/div/div/div/div[2]/div/div[4]/a')
        button.click()
        time.sleep(3)
        input_email= browser.find_element("xpath", '//*[@id="exampleModal"]/div/div/form/div[2]/input[1]')
        input_email.send_keys("lirfgehva@mskd.ckdk")
        further = browser.find_element("xpath", '//*[@id="exampleModal"]/div/div/form/div[3]/button')
        further.click()
        time.sleep(3)
        checbox = browser.find_element("xpath" , '//*[@id="usl"]')
        checbox.click()
        time.sleep(3)
        pay_button = browser.find_element("xpath", '//*[@id="payButton"]')
        pay_button.click()
        time.sleep(3)
        close = browser.find_element("xpath", '//*[@id="exampleModal"]/div/div/form/div[1]/button/span')
        close.click()
        time.sleep(3)
        bubbly_button = browser.find_element("xpath", '//*[@id="prise_1"]/div/div/div/div/div[2]/div/div[4]/a')
        bubbly_button.click()
        time.sleep(3)
        close_es = browser.find_element("xpath", '//*[@id="exampleModal"]/div/div/form/div[1]/button/span')
        close_es.click()
        time.sleep(3)
        button_z = browser.find_element("xpath", '//*[@id="prise_1"]/div/div/div/div/div[1]/div/div[4]/a')
        button_z.click()
        time.sleep(3)
        close_z = browser.find_element("xpath", '//*[@id="exampleModal"]/div/div/form/div[1]/button/span')
        close_z.click()
        time.sleep(3)
        button_s = browser.find_element("xpatrh", '/html/body/div[4]/div[1]/section[9]/div/div/div[1]/a')
        button_s.click()
        time.sleep(3)
        button_support = browser.find_element("xpath", '/html/body/div[4]/div[1]/section[2]/div/div/div[2]/div/a')
        button_support.click()
        time.sleep(3)
        privacy = browser.find_element("xpath", '/html/body/div[4]/footer/div/div/div[3]/div/a[1]')
        privacy.click()
        oferta = browser.find_element("xpath", '/html/body/div[4]/footer/div/div/div[3]/div/a[2]')
        oferta.click()
        support = browser.find_element("xpath", '/html/body/div[4]/footer/div/div/div[3]/div/a[3]')
        support.click()

except Exception as error:
    print(error)
finally:
    browser.close()
    browser.quit()


