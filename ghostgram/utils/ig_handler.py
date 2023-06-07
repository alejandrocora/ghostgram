from time import sleep
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.selaux import *
from utils.constants import *


class IGWebdriverHandler:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.get(IG_LOGIN_URL)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        self.driver.find_element(By.NAME, 'username').send_keys(username)
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        self.driver.find_element(By.NAME, 'password').send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.current_url != IG_LOGIN_URL
        )

    def open_comments(self):
        self.driver.get('https://www.instagram.com/your_activity/interactions/comments')

    def select_mode(self):
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//span[text()="Select"]'))
        )
        self.driver.find_element(By.XPATH, '//span[text()="Select"]').click()

    def get_comments_tree(self):
        sleep(5)
        flexboxes = self.driver.find_elements(By.XPATH, '//div[@data-testid="comments_container_non_empty_state"]/div[@data-testid="comments_container_non_empty_state"]/div/div/div') # Selecting Full Container
        flexbox_tree = []
        branch = []
        for flexbox in flexboxes: # Splitting the flexboxes into branches
            if ('flex-grow: 1' not in flexbox.get_attribute('style')) and len(branch) > 0: # Opening of new branch and adding old one
                flexbox_tree.append(branch) # Adding branch to the tree
                branch = []
            branch.append(flexbox) # Adding to the branch
        if len(flexbox_tree) == 0:
            return False
        filtered_tree = []
        for branch in flexbox_tree:
            try:
                username = branch[0].find_element(By.XPATH, 'div/div/div[2]/div/div/span').text
            except: # This is unsafe, must be fixed
                pass
            if username != 'Instagram user':
                filtered_tree.append(branch)
        return filtered_tree

    def select_all(self):
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-bloks-name="ig.components.Icon"]'))
        )
        flexbox_tree = self.get_comments_tree()
        if flexbox_tree == False:
            return False
        for branch in flexbox_tree:
            for flexbox in branch[1:]:
                try:
                    flexbox.find_element(By.XPATH, 'div/div/div[2]/div').click()
                except (ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException) as E:
                    pass
        return True

    def delete_comments(self):
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//span[text()="Delete"]'))
        )
        self.driver.find_element(By.XPATH, '//span[text()="Delete"]').click()
        sleep(2)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//div[text()="Delete"]'))
        )
        self.driver.find_element(By.XPATH, '//div[text()="Delete"]').click()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//span[text()="Select"]'))
        )