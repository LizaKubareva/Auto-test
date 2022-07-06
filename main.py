from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
s=Service("C:\\Users\\e.kubareva\\PycharmProjects\\pythonProject\\drivers\\windows\\chromedriver.exe")
browser = webdriver.Chrome(service=s)
urls = ["https://fit.fitcoach4everyday.com/", "https://easysplits.fitcoach4everyday.com/","https://meditation.fitcoach4everyday.com/"]

try:
    for url in urls:
        print(url)
        browser.get(url=url)
        time.sleep(5)
        print("Лиза коцык")
except Exception as error:
    print(error)
finally:
    browser.close()
    browser.quit()