from Reader.Reader import load_excel
from Sorting.Sort_Doc import sort_by_doctor
import pandas as pd

# Load data
df = load_excel()

# Sort patients
doctor_lists = sort_by_doctor(df)

# Print results
for doctor, patients in doctor_lists.items():

    print("\n" + "=" * 70)
    print(f"Doctor: {doctor}")
    print("=" * 70)

    patient_count = 1
    placement = 1

    for i, patient in enumerate(patients, start=1):
        
        Act_Num = patient.get('Act_Num', '')
        lname = patient.get('lname', '')
        fname = patient.get('fname', '')
        DOB = patient.get('DOB', '')
        DOS = patient.get('DOS', '')
        Procedure = patient.get('Procedure', '')
        Prod_xtra = patient.get('Prod_xtra', '')
        Phone = patient.get('Phone', '')
        email = patient.get('email', '')
        
        if pd.isna(Prod_xtra):
            print("")
            print(f"{placement}.) {Act_Num} - {lname}, {fname} - {DOB} - {DOS} - {Procedure} - {Phone} - {email}")
            print("")

        else:
            print("")
            print(f"{placement}.) {Act_Num} - {lname}, {fname} - {DOB} - {DOS} - {Procedure} with a {Prod_xtra} - {Phone} - {email}")
            print("")

        patient_count += 1
        placement += 1
        
    print("\n" + "=" * 50)
    print(f"Total patients for {doctor}: {len(patients)}")
    print("=" * 50)