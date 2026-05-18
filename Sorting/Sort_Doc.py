DOCTOR_MAP = {
    "MORELAND, DOUGLAS B, MD": "Moreland, Doug",
    "FAHRBACK, JOHN, MD":      "Fahrback, John",
    "LEVY, ELAD, MD":          "Levy, Elad",
    "MEYERS, JOSHUA, MD":      "Meyers, Joshua",
    "MULLIN, JEFFERY, MD":     "Mullin, Jeffery",
    "POLLINA, JOHN, MD":       "Pollina, John",
    "STOFFMAN, MICHAEL, MD":   "Stoffman, Michael",
}

# Then in sort_by_doctor(), when building the patient dict:
"physician": DOCTOR_MAP.get(row["SB Doctor Name"], row["SB Doctor Name"])

def sort_by_doctor(df):

    doctor_patients = {}

    for _, row in df.iterrows():

        doctor = row["SB Doctor Name"]

        patient = {
            "Act_Num": row["P Account Number"],
            "fname": row["P First Name"],
            "lname": row["P Last Name"],
            "DOB": row["P Date of Birth"],
            "DOS": row["SB Appointment Date"],
            "Procedure": row["SB Surgical Code 1"],
            "Prod_xtra": row["SB Surgical Code 2"],
            "Phone": row["P Cell Phone Number"],
            "email": row["P Email Address"]
        }

        if doctor not in doctor_patients:
            doctor_patients[doctor] = []

        doctor_patients[doctor].append(patient)

    return doctor_patients