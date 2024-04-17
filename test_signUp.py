from selenium import webdriver
from userInfo import firstName, lastName, email, password, passwordAgain, telephone
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from constants.globalConstants import *
from time import sleep
import pytest

class Test_Register():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def test_signup(self):
        signup_button = self.waitForElementVisible((By.XPATH, "/html/body/div[1]/div/section[1]/nav/div/div/a[2]"))
        signup_button.click()
        name_input = self.waitForElementVisible((By.NAME, "firstName"))
        lastname_input = self.waitForElementVisible((By.NAME, "lastName"))
        email_input = self.waitForElementVisible((By.NAME, "email"))
        password_input = self.waitForElementVisible((By.NAME, "password"))
        password_again_input = self.waitForElementVisible((By.NAME, "passwordAgain"))

        actions = ActionChains(self.driver)
        actions.send_keys_to_element(name_input, firstName) \
               .send_keys_to_element(lastname_input, lastName) \
               .send_keys_to_element(email_input, email) \
               .send_keys_to_element(password_input, password) \
               .send_keys_to_element(password_again_input, passwordAgain) \
               .perform()
        
        signup_button=self.waitForElementVisible((By.XPATH,signup_button_id))
        signup_button.click()
        checkbox1=self.waitForElementVisible((By.XPATH,checkbox1_id))
        checkbox1.click()
        checkbox2=self.waitForElementVisible((By.XPATH,checkbox2_id))
        checkbox2.click()
        checkbox3=self.waitForElementVisible((By.XPATH,checkbox3_id))
        checkbox3.click()
        checkbox4=self.waitForElementVisible((By.XPATH,checkbox4_id))
        checkbox4.click()
        telephone_input=self.waitForElementVisible((By.XPATH,telephone_id))
        telephone_input.send_keys(telephone)
        sleep(5)
        
        continue_button=self.waitForElementVisible((By.XPATH,continue_button_id))
        continue_button.click()
        sleep(15)
        activation_message = self.waitForElementVisible((By.XPATH,activationMessage_id ))
        assert activation_message == activation_message_text