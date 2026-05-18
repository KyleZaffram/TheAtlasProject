from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdSGzUG6vzwP3tzJoxXpIrYEv48MtZUcueEmFrBZzIWOgM6hg/viewform"

# Paste your entry IDs here once you find them
ENTRY_FIRST_NAME = "entry.XXXXXXXXX"
ENTRY_LAST_NAME  = "entry.XXXXXXXXX"
ENTRY_DOB        = "entry.XXXXXXXXX"
ENTRY_SEX        = "entry.XXXXXXXXX"
ENTRY_MRN        = "entry.XXXXXXXXX"
ENTRY_EMAIL      = "entry.XXXXXXXXX"
ENTRY_PHONE      = "entry.XXXXXXXXX"
ENTRY_PHYSICIAN  = "entry.XXXXXXXXX"

class Bot:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(FORM_URL)
        time.sleep(2)

    def fill_form(self, patient):
        d = self.driver
        wait = WebDriverWait(d, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))

        # First Name
        d.find_element(By.NAME, ENTRY_FIRST_NAME).send_keys(patient["first_name"])

        # Last Name
        d.find_element(By.NAME, ENTRY_LAST_NAME).send_keys(patient["last_name"])

        # Date of Birth — Google's date field has 3 separate boxes (MM / DD / YYYY)
        dob = str(patient["DOB"])  # expects format like "03/28/1955"
        parts = dob.split("/")
        if len(parts) == 3:
            dob_fields = d.find_elements(By.NAME, ENTRY_DOB)
            dob_fields[0].send_keys(parts[0])  # MM
            dob_fields[1].send_keys(parts[1])  # DD
            dob_fields[2].send_keys(parts[2])  # YYYY
        else:
            d.find_element(By.NAME, ENTRY_DOB).send_keys(dob)

        # Sex — radio button, click the matching label
        # Options on your form: Male, Female, Unknown, Other
        sex_value = patient.get("sex", "")
        if sex_value:
            try:
                d.find_element(By.XPATH, f"//span[text()='{sex_value}']").click()
            except:
                print(f"  Could not find sex option: {sex_value}")

        # MRN
        d.find_element(By.NAME, ENTRY_MRN).send_keys(str(patient["Act_Num"]))

        # Email
        email = patient.get("email", "")
        if email and str(email) != "nan":
            d.find_element(By.NAME, ENTRY_EMAIL).send_keys(str(email))

        # Cell Phone
        phone = patient.get("phone", "")
        if phone and str(phone) != "nan":
            d.find_element(By.NAME, ENTRY_PHONE).send_keys(str(phone))

        # Physician dropdown
        # Options: Fahrback John, Levy Elad, Meyers Joshua,
        #          Moreland Doug, Mullin Jeffery, Pollina John, Stoffman Michael
        physician = patient.get("physician", "")
        try:
            d.find_element(By.XPATH, "//div[@role='listbox']").click()
            time.sleep(0.5)
            d.find_element(By.XPATH, f"//span[text()='{physician}']").click()
        except:
            print(f"  Could not select physician: {physician}")

        # Submit
        d.find_element(By.XPATH, "//span[text()='Submit']").click()
        time.sleep(2)

        # Reload for next patient
        d.get(FORM_URL)
        time.sleep(2)

    def close(self):
        self.driver.quit()