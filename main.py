from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
s=Service("C:\\Users\\e.kubareva\\PycharmProjects\\pythonProject\\drivers\\windows\\chromedriver.exe")
browser = webdriver.Chrome(service=s)
urls = ["https://myfitnessclub.ru/", "http://24fitnesshome.com", "https://dreambodyathome.com", "http://onlyfamilyplan.com "]


try:
    for url in urls:
        print(url)
        page = browser.get (url=url)
        time.sleep(4)
        btn_support = page.find_element_by_class('btn_support')
        btn_support.click()
        time.sleep(4)
except Exception as error:
    print(error)
finally:
    browser.close()
    browser.quit()


