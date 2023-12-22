from DBConnUtil import DBConnUtil
from datetime import date
class Appointment:
    def __init__(self, patient_id, doctor_id, appointment_date, description):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.description = description


    def __str__(self):
        return f"Patient ID: {self.patient_id}, Doctor ID: {self.doctor_id}, " \
               f"Date: {self.appointment_date}, Description: {self.description}"
