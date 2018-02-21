# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_new_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_add_new_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.log_in(wd, username="admin", password="secret")
        self.add_new_contact(wd, contact(name="Jane", lastname="Doe", title="Ms", address="1 Happy Lane, London, SW1 3VV", homeTelNo="123456789", mobileNo="987654321",
                             emailAddress="jane@doe.com"))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys("\\9")

    def add_new_contact(self, wd, contact):
        # init new contact creation
        wd.find_element_by_link_text("add new").click()
        # fill in new contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homeTelNo)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobileNo)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.emailAddress)
        # submit new contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost:8080/addressbook/")

    def log_in(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def test_add_another_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.log_in(wd, username="admin", password="secret")
        self.add_new_contact(wd, contact(name="John", lastname="Doe", title="Mr", address="1 Happy Lane, London, SW1 3VV", homeTelNo="123456780", mobileNo="0987654321",
                             emailAddress="john@doe.com"))
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
