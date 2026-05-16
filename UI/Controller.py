import tkinter as tk

class Controller:

    def __init__(self, doctor_data, bot):

        self.data = doctor_data
        self.bot = bot

        self.doctors = list(doctor_data.keys())
        self.doc_index = 0
        self.patient_index = 0

        self.root = tk.Tk()
        self.root.title("Automation Controller")

        tk.Button(
            self.root,
            text="NEXT",
            command=self.next_patient,
            height=3,
            width=20
        ).pack(pady=20)

    def next_patient(self):

        if self.doc_index >= len(self.doctors):
            print("ALL DONE")
            return

        doctor = self.doctors[self.doc_index]
        patients = self.data[doctor]

        if self.patient_index >= len(patients):
            self.doc_index += 1
            self.patient_index = 0
            return self.next_patient()

        patient = patients[self.patient_index]

        print(f"Doctor: {doctor} | Patient {self.patient_index + 1}")

        self.bot.fill_form(patient)

        self.patient_index += 1

    def run(self):
        self.root.mainloop()