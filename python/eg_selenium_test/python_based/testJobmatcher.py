# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class OpenPasteResumeForRecommendation(unittest.TestCase):


    # def getEnvDriver(self) :
    #     import os
    #     driver = os.environ.get("DRIVER")
    #     if(driver is None) : return None
    #     driver = re.sub(r'\"',"'",driver)
    #     ss= re.split(r'\s*\(\s*\'|\'\s*\)\s*',driver)
    #     driver_name = ss[0]
    #     driver_exe = ss[1]
    #     if(re.match("chrome$", driver_name, flags=re.IGNORECASE)) :
    #         return webdriver.Chrome(driver_exe)
    #     if(re.match("chrome$", driver_name, flags=re.IGNORECASE)) :
    #         return webdriver.PhantomJS(driver_exe)
    #     if(re.match("firefox$", driver_name, flags=re.IGNORECASE)) :
    #         return webdriver.Firefox(driver_exe)
    #     return None

    def setUp(self):
        #self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome('../chromedriver.exe')
        self.driver = self.getEnvDriver()
        if(self.driver is None) : self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://mo-d8c5e1a06.mo.sap.corp:9001/#/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_open_paste_resume_for_recommendation(self):
        driver = self.driver
        driver.get(self.base_url + "")
        driver.find_element_by_xpath("//form[@id='candidate-text-form']/div/textarea").clear()
        driver.find_element_by_xpath("//form[@id='candidate-text-form']/div/textarea").send_keys("spring")
        driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "button.btn.repeat"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_css_selector("button.btn.repeat").click()
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "//form[@id='candidate-text-form']/div/textarea"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
