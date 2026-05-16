from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Bot:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("YOUR_FORM_URL")

    def fill_form(self, patient):

        d = self.driver

        d.find_element(By.ID, "firstName").clear()
        d.find_element(By.ID, "firstName").send_keys(patient["first_name"])

        d.find_element(By.ID, "lastName").clear()
        d.find_element(By.ID, "lastName").send_keys(patient["last_name"])

        d.find_element(By.ID, "email").clear()
        d.find_element(By.ID, "email").send_keys(patient["email"])

        d.find_element(By.ID, "cellPhone").clear()
        d.find_element(By.ID, "cellPhone").send_keys(patient["phone"])

    def close(self):
        self.driver.quit()