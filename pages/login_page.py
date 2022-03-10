from selenium.webdriver.common.by import By

import base.base_page
import utilities.files_reader

# this is an example page class describing the Test Project example page
# url: https://example.testproject.io/web/
# demonstrating returning elements options (using xpath locator):
#   writing the xpath  in the code as string
#   reading the xpath from .properties file
#   using a By tuple


class Login_Page(base.base_page.Base_Page):
    def __init__(self, driver):
        base.base_page.Base_Page.__init__(self, driver)

    def get_user_name_element(self):
        # return self.driver.find_element(By.XPATH, "//input[@id='name']")
        # return self.driver.find_element(By.XPATH, utilities.xml_reader.get_property_value('tp_login_page.user_name'))
        return self.driver.find_element(Login_Page.get_user_name_by()[0], Login_Page.get_user_name_by()[1])

    @staticmethod
    def get_user_name_by():
        # return By.XPATH, "//input[@id='name']"
        return By.XPATH, utilities.files_reader.get_property_value('tp_login_page.user_name')

    def get_password_element(self):
        return self.driver.find_element(By.XPATH, "//input[@id='password']")

    def get_login_element(self):
        # return self.driver.find_element(By.XPATH, "//button[@id='login']")
        return self.driver.find_element(self.get_login_by()[0], self.get_login_by()[1])

    @staticmethod
    def get_login_by():
        return (By.XPATH, "//button[@id='login']")

    def get_logout_element(self):
        return self.driver.find_element(By.XPATH, "//button[@id='logout']")

    def get_select_country_element(self):
        return self.driver.find_element(By.XPATH, utilities.files_reader.get_property_value('tp_login_page.country'))
