from selenium import webdriver
from userInfo import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from constants.globalConstants import *
# from PIL import Image
from time import sleep
import pytest

class Test_My_Competentences():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(LOGIN_URL)
        # self.valid_login()

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def valid_login(self):
        loginInputButton= self.waitForElementVisible((By.XPATH,login_input_button))
        loginInputButton.click()
        emailInput = self.waitForElementVisible((By.XPATH, email_xpath))
        emailInput.send_keys(email_tuba)
        passwordInput = self.waitForElementVisible((By.XPATH, password_xpath))
        passwordInput.send_keys(password_tuba)
        loginButton = self.waitForElementVisible((By.XPATH, login_button_xpath))
        loginButton.click()
        alert_quit = self.waitForElementVisible((By.XPATH, alert_login_text))
        alert_quit.click()


    #Sertifikalarım ,belge yükleme
    def test_myCertificates(self):
        self.valid_login()
        myProfilePage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, my_profile_page)))
        myProfilePage.click()
        myProfileEdit =  WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, my_profile_edit)))
        myProfileEdit.click()
        sleep(2)
        myCertificatesPage= self.waitForElementVisible((By.XPATH, my_certificates_xpath))
        myCertificatesPage.click()
        sleep(2)
        certificateFileLoad = WebDriverWait(self.driver,20).until(ec.visibility_of_element_located((By.CSS_SELECTOR,certificates_file_load)))
        certificateFileLoad.click()
        sleep(3)
        # certificateBrowseButton = self.waitForElementVisible((By.CSS_SELECTOR, certificate_browse_button ))
        # certificateBrowseButton.click()
        # sleep(3)
        # certificateFileInput = self.waitForElementVisible((By.XPATH, "//input[@type='file']"))
        # certificateFileInput.send_keys(r"C:\Users\Desktop\Certificates")
        profile_file_input = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]")
        profile_file_input.send_keys(file_path)
        sleep(2)
        file_load_button=self.waitForElementVisible((By.CSS_SELECTOR,"#__next > div > main > section > div > div > div.col-12.col-lg-9 > div > div:nth-child(2) > div > div.col-12.tobeto-light-bg > div > div:nth-child(3) > div > div > div > div.uppy-Dashboard-inner > div > div.uppy-Dashboard-progressindicators > div.uppy-StatusBar.is-waiting > div.uppy-StatusBar-actions > button"))
        file_load_button.click()
        sleep()


    #Sertifikalarım ,yüklü olan sertifikayı indirme
    def test_myCertificatesDownload(self):
        self.valid_login()
        myProfilePage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, my_profile_page)))
        myProfilePage.click()
        myProfileEdit =  WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, my_profile_edit)))
        myProfileEdit.click()
        sleep(2)
        myCertificatesPage= self.waitForElementVisible((By.XPATH, my_certificates_xpath))
        myCertificatesPage.click()
        sleep(2)
        certificateFileLoad = WebDriverWait(self.driver,20).until(ec.visibility_of_element_located((By.CSS_SELECTOR,certificates_file_load)))
        certificateFileLoad.click()
        sleep(3)    
        certificateDownload = self.waitForElementVisible((By.CSS_SELECTOR,certificates_download_icon))
        certificateDownload.click() 
        sleep(3)                                                                                       

    #Sertifika Silme
    def test_myCertificatesDelete(self):
        self.valid_login()
        myProfilePage = self.waitForElementVisible((By.XPATH, my_profile_page))
        myProfilePage.click()
        myProfileEdit = self.waitForElementVisible((By.CSS_SELECTOR, my_profile_edit))
        myProfileEdit.click()
        sleep(2)
        myCertificatesPage= self.waitForElementVisible((By.XPATH, my_certificates_xpath))
        myCertificatesPage.click()
        sleep(2)
        certificateFileLoad = self.waitForElementVisible((By.CSS_SELECTOR,certificates_file_load))
        certificateFileLoad.click()
        sleep(3)
        certificateDeleteIcon =self.waitForElementVisible((By.CSS_SELECTOR, certificate_delete_icon))
        certificateDeleteIcon.click()
        sleep(2)
        deleteCertificateChoose = self.waitForElementVisible((By.CSS_SELECTOR, certificate_choose_button))
        deleteCertificateChoose.click()
        yesButtonCertificate = self.waitForElementVisible((By.CSS_SELECTOR,yes_button_certificate))
        yesButtonCertificate.click()
        sleep(2)
        alertCertificateDeleted = self.waitForElementVisible((By.CSS_SELECTOR, alert_certificate_deleted))
        assert alertCertificateDeleted.text == "• Dosya kaldırma işlemi başarılı.."
        sleep(3)
   

