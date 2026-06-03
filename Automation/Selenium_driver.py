from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdSGzUG6vzwP3tzJoxXpIrYEv48MtZUcueEmFrBZzIWOgM6hg/viewform"

ENTRY_FIRST_NAME = "entry.369071062"
ENTRY_LAST_NAME  = "entry.108580576"
ENTRY_DOB        = "entry.1071432235"
ENTRY_SEX        = "entry.108793413"
ENTRY_MRN        = "entry.1457600634"
ENTRY_EMAIL      = "entry.1162067483"
ENTRY_PHONE      = "entry.1487571513"
ENTRY_PHYSICIAN  = "entry.101874347"

print("Bot initializing...")
class Bot:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(FORM_URL)
        time.sleep(2)

    print("Bot initialized and form loaded.")
    def fill_form(self, patient):
        print(patient)

        d = self.driver
        wait = WebDriverWait(d, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))

        # First Name
        elements = d.find_elements(By.NAME, ENTRY_FIRST_NAME)

        print("Found", len(elements), "elements")

        for i, e in enumerate(elements):
            print(
                i,
                "tag=", e.tag_name,
                "displayed=", e.is_displayed(),
                "enabled=", e.is_enabled()
            )

        # Last Name
        d.find_element(By.NAME, ENTRY_LAST_NAME).send_keys(patient.get("lname", ""))

        # Date of Birth — 3 separate boxes (Month / Day / Year)
        dob = str(patient["DOB"])
        parts = dob.split("/")
        dob_fields = d.find_elements(By.NAME, ENTRY_DOB)
        if len(parts) == 3 and len(dob_fields) >= 3:
            dob_fields[0].send_keys(parts[0])  # Month
            dob_fields[1].send_keys(parts[1])  # Day
            dob_fields[2].send_keys(parts[2])  # Year
        else:
            dob_fields[0].send_keys(dob)

        # Sex — radio button (options: Male, Female, Unkown)
        # Note: your form has "Unkown" (typo) not "Unknown"
        sex_map = {"M": "Male", "F": "Female", "U": "Unkown"}
        sex_raw = str(patient.get("sex", "")).strip()
        sex_value = sex_map.get(sex_raw, sex_raw)  # handles M/F or full word
        if sex_value:
            try:
                d.find_element(By.XPATH, f"//span[text()='{sex_value}']").click()
            except Exception:
                print(f"  Warning: could not select sex '{sex_value}'")

        # MRN
        d.find_element(By.NAME, ENTRY_MRN).send_keys(str(patient["Act_Num"]))

        # Email
        email = str(patient.get("email", ""))
        if email and email.lower() != "nan":
            d.find_element(By.NAME, ENTRY_EMAIL).send_keys(email)

        # Cell Phone
        phone = str(patient.get("Phone", ""))
        if phone and phone.lower() != "nan":
            d.find_element(By.NAME, ENTRY_PHONE).send_keys(phone)

        # Physician — dropdown
        # Options: Fahrback, John / Levy, Elad / Meyers, Joshua /
        #          Moreland, Doug / Mullin, Jeffery / Pollina, John / Stoffman, Michael
        physician = patient.get("physician", "")
        try:
            d.find_element(By.XPATH, "//div[@role='listbox']").click()
            time.sleep(0.5)
            d.find_element(By.XPATH, f"//span[text()='{physician}']").click()
        except Exception:
            print(f"  Warning: could not select physician '{physician}'")

        # Submit
        d.find_element(By.XPATH, "//span[text()='Submit']").click()
        time.sleep(2)

        # Reload for next patient
        d.get(FORM_URL)
        time.sleep(2)

    def close(self):
        self.driver.quit()