from HospitalService import HospitalService
from DBConnUtil import DBConnUtil

class HospitalServiceImpl(HospitalService):
    def execute_query(self, query, values=None):
        conn = None
        stmt = None
        try:
            conn = DBConnUtil.get_connection()
            stmt = conn.cursor(dictionary=True)
            stmt.execute(query, values)
            return stmt.fetchall()
        except Exception as e:
            print(f"Error executing query: {e}")
            return None
        finally:
            if conn:
                conn.close()

    def execute_update(self, query, values=None):
        conn = None
        stmt = None
        try:
            conn = DBConnUtil.get_connection()
            stmt = conn.cursor()
            stmt.execute(query, values)
            conn.commit()
            return True
        except Exception as e:
            print(f"Error executing update: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def get_appointment_by_id(self, appointment_id):
        query = "SELECT * FROM appointments WHERE appointment_id = %s"
        result = self.execute_query(query, (appointment_id,))
        return result[0] if result else None

    def get_appointments_for_patient(self, patient_id):
        query = "SELECT * FROM appointments WHERE patient_id = %s"
        return self.execute_query(query, (patient_id,))

    def get_appointments_for_doctor(self, doctor_id):
        query = "SELECT * FROM appointments WHERE doctor_id = %s"
        return self.execute_query(query, (doctor_id,))

    def schedule_appointment(self, appointment):
        query = "INSERT INTO appointments (patient_id, doctor_id, appointment_date, description) VALUES (%s, %s, %s, %s)"
        values = (appointment.patient_id, appointment.doctor_id, appointment.appointment_date, appointment.description)
        return self.execute_update(query, values)

    def update_appointment(self, date, new_description, appointment_id):
        query = "UPDATE appointments SET appointment_date = %s, description = %s WHERE appointment_id = %s"
        values = (date, new_description, appointment_id)
        return self.execute_update(query, values)

    def cancel_appointment(self, appointment_id):
        query = "DELETE FROM appointments WHERE appointment_id = %s"
        return self.execute_update(query, (appointment_id,))

