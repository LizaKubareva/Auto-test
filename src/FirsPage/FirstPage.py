import random
import string
import time


class FirstPage:
    _browser = ''

    def __init__(self, browser):
        self._browser = browser

    def testButtonGetMyPlan(self):
        try:
            button = self._browser.find_element("xpath", '//*[@id="prise_1"]/div/div/div/div/div[2]/div/div[4]/a')
            button.click()
            print("clicButton:success")
            time.sleep(3)
            self._stepOneTestInput()
            self._stepTwoTestButtonNext()
        except Exception as error:
            print(error)
            print("testButtonGetMyPlan:error")

    def _stepOneTestInput(self):
        try:
            input_email = self._browser.find_element("xpath", '//*[@id="exampleModal"]/div/div/form/div[2]/input[1]')
            input_email.send_keys(self._generationEmail())
            print("inputEmail:success")
        except Exception as error:
            print(error)
            print("inputEmail:error")

    def _stepTwoTestButtonNext(self):
        try:
            further = self._browser.find_element("xpath", '//*[@id="exampleModal"]/div/div/form/div[3]/button')
            further.click()
            print("clicButton:success")
            time.sleep(3)
        except Exception as error:
            print(error)
            print("clicButton: error")

    def _generationEmail(self):
        N_NAME = 10
        N_POST = 6
        N_END = 2

        allowedChars = string.ascii_letters

        return ''.join(random.choice(allowedChars) for _ in range(N_NAME)) \
                   + '@' \
                   + ''.join(random.choice(allowedChars) for _ in range(N_POST)) \
                   + '.' \
                   + ''.join(random.choice(allowedChars) for _ in range(N_END))


