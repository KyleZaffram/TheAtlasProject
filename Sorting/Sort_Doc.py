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