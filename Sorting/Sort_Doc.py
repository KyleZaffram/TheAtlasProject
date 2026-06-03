import pandas as pd

DOCTOR_MAP = {
    "MORELAND, DOUGLAS B, MD": "Moreland, Doug",
    "FAHRBACK, JOHN, MD":      "Fahrback, John",
    "LEVY, ELAD, MD":          "Levy, Elad",
    "MEYERS, JOSHUA, MD":      "Meyers, Joshua",
    "MULLIN, JEFFERY, MD":     "Mullin, Jeffery",
    "POLLINA, JOHN, MD":       "Pollina, John",
    "STOFFMAN, MICHAEL, MD":   "Stoffman, Michael",
}

def sort_by_doctor(df):
    doctor_patients = {}

    for _, row in df.iterrows():
        doctor = row["SB Doctor Name"]

        def safe(col):
            val = row.get(col, "")
            return "" if pd.isna(val) else val

        patient = {
            "Act_Num":    safe("P Account Number"),
            "fname": safe("P First Name"),       # fixed from fname
            "lname":  safe("P Last Name"),        # fixed from lname
            "DOB":        safe("P Date of Birth"),
            "DOS":        safe("SB Appointment Date"),
            "Procedure":  safe("SB Surgical Code 1"),
            "Prod_xtra":  safe("SB Surgical Code 2"),
            "Phone":      safe("P Cell Phone Number"), # fixed from Phone
            "email":      safe("P Email Address"),
            "physician":  DOCTOR_MAP.get(str(doctor).strip(), str(doctor).strip()),
        }

        if doctor not in doctor_patients:
            doctor_patients[doctor] = []
        doctor_patients[doctor].append(patient)

    return doctor_patients