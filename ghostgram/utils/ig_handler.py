from time import sleep
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

from ghostgram.utils.selaux import *
from ghostgram.utils.constants import *


class IGWebDriverHandler:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.get(IG_LOGIN_URL)
        wait_for_find(self.driver, '//input[@name="username"]')
        self.driver.find_element(By.NAME, 'username').send_keys(username)
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        self.driver.find_element(By.NAME, 'password').send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.current_url != IG_LOGIN_URL
        )

    def open_comments(self):
        self.driver.get('https://www.instagram.com/your_activity/interactions/comments')

    def select_comments(self):
        wait_for_find(self.driver,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/article/div/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div[2]/span',click=True)
        elems = wait_for_find(self.driver,'//div/div[2]/div/div/div/div/div/div[2]/div/div/div',criteria=By.XPATH,multiple=True)
        success_count = 0
        for e in elems:
            try:
                e.click()
                success_count += 1
            except ElementClickInterceptedException:
                continue
        return success_count


    def delete_comments(self):
        wait_for_find(self.driver, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/article/div/div[2]/div/div/div[1]/div/div/div/div/div/div[4]/div/div/div[2]/div/div/div[2]', click=True)
        sleep(2)
        wait_for_find(self.driver, '//div[text()="Delete"]', click=True)
        wait_for_find(self.driver, '//span[text()="Select"]')