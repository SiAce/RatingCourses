# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class RatingCourse(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://electsys.sjtu.edu.cn/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_rating_course(self):
        driver = self.driver

x = "1"
# ERROR: Caught exception [unknown command [while]]
driver.get(self.base_url + "/edu/N10_pingjiao/N4_pingjiaoXKLB.aspx")
driver.find_element_by_id("dgCourse_ctl02_HyperNew").click()
driver.find_element_by_xpath(u"//input[@value='下一步']").click()
driver.find_element_by_xpath(u"//input[@value='下一步']").click()
driver.find_element_by_xpath(u"//input[@value='下一步']").click()
driver.find_element_by_xpath(u"//input[@value='下一步']").click()
driver.find_element_by_xpath(u"//input[@value='下一步']").click()
driver.find_element_by_xpath(u"//input[@value='下一步']").click()
driver.find_element_by_xpath(u"//input[@value='下一步']").click()
driver.find_element_by_id("sText_2_1_railElement").click()
driver.find_element_by_id("sText_2_1").clear()
driver.find_element_by_id("sText_2_1").send_keys("10")
driver.find_element_by_id("sText_2_1").clear()
driver.find_element_by_id("sText_2_1").send_keys("10")
driver.find_element_by_id("sText_2_2_railElement").click()
driver.find_element_by_id("sText_2_2").clear()
driver.find_element_by_id("sText_2_2").send_keys("10")
driver.find_element_by_id("sText_2_3_railElement").click()
driver.find_element_by_id("sText_2_3").clear()
driver.find_element_by_id("sText_2_3").send_keys("10")
driver.find_element_by_id("sText_2_4_railElement").click()
driver.find_element_by_id("sText_2_4").clear()
driver.find_element_by_id("sText_2_4").send_keys("10")
driver.find_element_by_id("sText_2_5_railElement").click()
driver.find_element_by_id("sText_2_5").clear()
driver.find_element_by_id("sText_2_5").send_keys("10")
driver.find_element_by_id("sText_2_6_railElement").click()
driver.find_element_by_id("sText_2_6").clear()
driver.find_element_by_id("sText_2_6").send_keys("10")
driver.find_element_by_id("sText_2_7_railElement").click()
driver.find_element_by_id("sText_2_7").clear()
driver.find_element_by_id("sText_2_7").send_keys("10")
driver.find_element_by_id("sText_2_8_railElement").click()
driver.find_element_by_id("sText_2_8").clear()
driver.find_element_by_id("sText_2_8").send_keys("10")
driver.find_element_by_id("sText_2_9_railElement").click()
driver.find_element_by_id("sText_2_9").clear()
driver.find_element_by_id("sText_2_9").send_keys("10")
driver.find_element_by_id("sText_2_10_railElement").click()
driver.find_element_by_id("sText_2_10").clear()
driver.find_element_by_id("sText_2_10").send_keys("10")
driver.find_element_by_id("sText_1_1_railElement").click()
driver.find_element_by_id("sText_1_1").clear()
driver.find_element_by_id("sText_1_1").send_keys("100")
driver.find_element_by_id("sText_1_2_railElement").click()
driver.find_element_by_id("sText_1_2").clear()
driver.find_element_by_id("sText_1_2").send_keys("100")
driver.find_element_by_id("sText_1_3_railElement").click()
driver.find_element_by_id("sText_1_3").clear()
driver.find_element_by_id("sText_1_3").send_keys("100")
driver.find_element_by_id("btnSubmit").click()
driver.find_element_by_id("btnReturn").click()
x = x + "+1"
# ERROR: Caught exception [unknown command [endWhile]]
    
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
