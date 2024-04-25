from selenium import webdriver
from userInfo import email, password
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from constants.globalConstants import *
import pytest
from time import sleep


class Test_My_Media_Accounts():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        self.valid_login()

    def teardown_method(self):
        self.driver.quit()

    def valid_login(self):
        emailInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, email_xpath)))
        emailInput.send_keys(self.email)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, password_xpath)))
        passwordInput.send_keys(self.password)
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, login_button_xpath)))
        loginButton.click()

    def test_myMediaAccounts(self):
        self.driver.get(PLATFORM_URL)
        my_profile = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.LINK_TEXT, "Profilim")))
        my_profile.click()
        my_profile_edit =  WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, my_profile_edit)))
        my_profile_edit.click()
        sleep(2)
    
    
        

