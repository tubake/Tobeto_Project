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
        
      
       
    #Yetkinliklerim=Compentences
    #Yetkinlik ekle =Competence Add
    def test_myCompentences(self):
        self.valid_login()
        myProfilePage = self.waitForElementVisible((By.XPATH, my_profile_page))
        myProfilePage.click()
        myProfileEdit = self.waitForElementVisible((By.CSS_SELECTOR, my_profile_edit))
        myProfileEdit.click()
        sleep(2)
        myCompetencesButton = self.waitForElementVisible((By.XPATH, my_competences_xpath))
        myCompetencesButton.click()
        sectionCompetence = self.waitForElementVisible((By.XPATH, section_competence))
        sectionCompetence.click()
        sleep(1)
        sectionClick = ActionChains(self.driver)
        sectionClick.send_keys(Keys.ARROW_DOWN,Keys.ENTER).perform()     
        saveCompetence = self.waitForElementVisible((By.XPATH, save_competence_button))
        saveCompetence.click()
        alertCompencyAdded = self.waitForElementVisible((By.CSS_SELECTOR, alert_competence_added))
        assert alertCompencyAdded.text == "• Yetenek eklendi."
        sleep(2)
        #ekran görünütüsü ekle , eklenen yetkinlikler görüntülendi.
        self.driver.save_screenshot("screenshot.png")
        sleep(3)
        
    #Yetkinlik eklemeden kaydetme işlemi
    def test_myCompetences_noCompetence(self):
        self.valid_login()
        myProfilePage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, my_profile_page)))
        myProfilePage.click()
        myProfileEdit =  WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, my_profile_edit)))
        myProfileEdit.click()
        sleep(2)
        myCompetencesButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, my_competences_xpath)))
        myCompetencesButton.click()
        sleep(2)
        saveCompetence = self.waitForElementVisible((By.XPATH, save_competence_button))
        saveCompetence.click()
        alertNoCompetency = self.waitForElementVisible((By.XPATH, alert_competency_not_added))
        assert alertNoCompetency.text == "• Herhangi bir yetenek seçmediniz!"
        sleep(2)

    #Yetkinlik silme   
    def test_myCompetences_deleteCompetence(self):
        self.valid_login()
        myProfilePage = self.waitForElementVisible((By.XPATH, my_profile_page))
        myProfilePage.click()
        myProfileEdit = self.waitForElementVisible((By.CSS_SELECTOR, my_profile_edit))
        myProfileEdit.click()
        sleep(2)
        myCompetencesButton = self.waitForElementVisible((By.XPATH, my_competences_xpath))
        myCompetencesButton.click()
        self.driver.save_screenshot("screenshot.png")
        sleep(2)
        deleteCompetenceIcon = self.waitForElementVisible((By.CSS_SELECTOR, delete_competence_icon))
        deleteCompetenceIcon.click()
        sleep(1)
        deleteCompetenceChoose = self.waitForElementVisible((By.CSS_SELECTOR, delete_competence_choose_button))
        deleteCompetenceChoose.click()
        yes_button = self.waitForElementVisible((By.CSS_SELECTOR,yes_button_id))
        yes_button.click()
        sleep(2)
        alertCompencyDeleted = self.waitForElementVisible((By.CSS_SELECTOR, alert_competence_deleted))
        assert alertCompencyDeleted.text == "• Yetenek kaldırıldı."
        sleep(3)

        #Çalışıyor ama hata da veriyor :)
       
        
    #6 adetten fazla yetkinlik ekleme ve göz ikonu kontrolü
    def test_myCompetences_sixCompetence(self):
        self.valid_login()
        myProfilePage = self.waitForElementVisible((By.XPATH, my_profile_page))
        myProfilePage.click()
        myProfileEdit = self.waitForElementVisible((By.CSS_SELECTOR, my_profile_edit))
        myProfileEdit.click()
        myCompetencesButton = self.waitForElementVisible((By.XPATH, my_competences_xpath))
        myCompetencesButton.click()
        sleep(2)
        # sectionCompetence = self.waitForElementVisible((By.XPATH, section_competence))
        # sectionCompetence.click()
        # sleep(1)
        # sectionClick = ActionChains(self.driver)
        # sectionClick.send_keys(Keys.ARROW_DOWN,Keys.ENTER).perform()    
        # saveCompetence = self.waitForElementVisible((By.XPATH, save_competence_button))
        # saveCompetence.click()
        competenceCount = self.waitForElementVisible((By.CSS_SELECTOR,"#__next > div > main > section > div > div > div.col-12.col-lg-9 > div.col-12"))
        # competenceCount = int(competenceCount.text)
        # competenceCount değişkeninin içeriğini alın
        competenceCountText = competenceCount.text
        # Satırları ayırın
        lines = competenceCountText.split('\n')
        # Satır sayısını sayarak kurs sayısını bulun
        competenceCountNumber = len(lines)  
        print(competenceCountNumber)
        if  competenceCount >= 6:
          print("6 dan fazla yetkinlik var", competenceCount.split()[0])

        competenceSeeIcon = self.waitForElementVisible((By.CLASS_NAME,"cv-see-icon"))
        competenceSeeIcon.click()
        sleep(5)
        
        #bu kısma tekrar bak
      


