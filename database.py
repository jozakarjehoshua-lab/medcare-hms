import sqlite3
import os
from datetime import datetime


class Database:

    # ======================================================
    # INITIALIZATION
    # ======================================================

    def __init__(self):

        # ======================================================
        # DATABASE LOCATION
        # ======================================================

        self.base_folder = os.path.dirname(
            os.path.abspath(__file__)
        )

        self.data_folder = os.path.join(
            self.base_folder,
            "data"
        )

        os.makedirs(
            self.data_folder,
            exist_ok=True
        )

        self.database_path = os.path.join(
            self.data_folder,
            "hospital.db"
        )
        print("DATABASE:", self.database_path)

        self.create_tables()
        self.add_patient_status_column()
        self.create_doctors_table()
        self.add_medical_record_appointment_column()

    # ======================================================
    # DATABASE CONNECTION
    # ======================================================

    def connect(self):

        return sqlite3.connect(
            self.database_path
        )

    # ======================================================
    # CREATE TABLES
    # ======================================================

    def create_tables(self):

        connection = self.connect()
        cursor = connection.cursor()

        # ==================================================
        # PATIENTS TABLE
        # ==================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS patients (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                patient_id TEXT UNIQUE NOT NULL,

                full_name TEXT NOT NULL,

                gender TEXT NOT NULL,

                date_of_birth TEXT NOT NULL,

                phone TEXT NOT NULL,

                address TEXT NOT NULL,

                blood_group TEXT NOT NULL,

                emergency_contact TEXT NOT NULL,

                status TEXT DEFAULT 'Active',

                created_at TIMESTAMP
                    DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        # ==================================================
        # MEDICAL RECORDS TABLE
        # ==================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS medical_records (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                record_id TEXT UNIQUE NOT NULL,

                patient_id TEXT NOT NULL,

                visit_date TEXT NOT NULL,

                symptoms TEXT NOT NULL,

                diagnosis TEXT NOT NULL,

                treatment TEXT NOT NULL,

                doctor TEXT NOT NULL,

                notes TEXT,

                created_at TIMESTAMP
                    DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (patient_id)
                    REFERENCES patients(patient_id)
            )
            """
        )
        # ==================================================
        # APPOINTMENTS TABLE
        # ==================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS appointments (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                appointment_id TEXT UNIQUE NOT NULL,

                patient_id TEXT NOT NULL,

                doctor_id TEXT NOT NULL,

                appointment_date TEXT NOT NULL,

                appointment_time TEXT NOT NULL,

                reason TEXT NOT NULL,

                status TEXT DEFAULT 'Scheduled',

                notes TEXT,

                created_at TIMESTAMP
                    DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (patient_id)
                    REFERENCES patients(patient_id),

                FOREIGN KEY (doctor_id)
                    REFERENCES doctors(doctor_id)
            )
            """
        )

        
        # ======================================================
        # BILLS TABLE
        # ======================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS bills (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                bill_id TEXT UNIQUE NOT NULL,
                patient_id TEXT NOT NULL,
                appointment_id TEXT,
                bill_date TEXT NOT NULL,
                total_amount REAL DEFAULT 0,
                amount_paid REAL DEFAULT 0,
                balance REAL DEFAULT 0,
                status TEXT DEFAULT 'Pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (patient_id)
                    REFERENCES patients(patient_id),

                FOREIGN KEY (appointment_id)
                    REFERENCES appointments(appointment_id)
            )
            """
        )
        # ======================================================
        # BILL ITEMS TABLE
        # ======================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS bill_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                bill_item_id TEXT UNIQUE NOT NULL,
                bill_id TEXT NOT NULL,
                description TEXT NOT NULL,
                quantity INTEGER DEFAULT 1,
                unit_price REAL NOT NULL,
                total_price REAL NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (bill_id)
                    REFERENCES bills(bill_id)
            )
            """
        )
        connection.commit()
        connection.close()    
    # ======================================================
    # ADD PATIENT STATUS COLUMN
    # ======================================================

    def add_patient_status_column(self):

        connection = self.connect()
        cursor = connection.cursor()

        # Check existing columns
        cursor.execute("PRAGMA table_info(patients)")

        columns = cursor.fetchall()

        column_names = [
            column[1]
            for column in columns
        ]

        # Add status column if it does not exist
        if "status" not in column_names:

            cursor.execute(
                """
                ALTER TABLE patients
                ADD COLUMN status TEXT DEFAULT 'Active'
                """
            )

        # Make sure existing patients have a valid status
        cursor.execute(
            """
            UPDATE patients
            SET status = 'Active'
            WHERE status IS NULL
               OR status = ''
            """
        )

        connection.commit()
        connection.close()
        # ======================================================
    # CREATE DOCTORS TABLE
    # ======================================================

    def create_doctors_table(self):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS doctors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                doctor_id TEXT UNIQUE NOT NULL,
                full_name TEXT NOT NULL,
                gender TEXT NOT NULL,
                specialization TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT,
                address TEXT NOT NULL,
                license_number TEXT UNIQUE NOT NULL,
                status TEXT DEFAULT 'Active',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        connection.commit()
        connection.close()
    # ======================================================
    # ADD APPOINTMENT ID TO MEDICAL RECORDS
    # ======================================================

    def add_medical_record_appointment_column(self):

        connection = self.connect()
        cursor = connection.cursor()

        # Check existing columns
        cursor.execute(
            "PRAGMA table_info(medical_records)"
        )

        columns = cursor.fetchall()

        column_names = [
            column[1]
            for column in columns
        ]

        # Add appointment_id if it does not exist
        if "appointment_id" not in column_names:

            cursor.execute(
                """
                ALTER TABLE medical_records
                ADD COLUMN appointment_id TEXT
                """
            )

        connection.commit()
        connection.close()            
# ======================================================
# ADD APPOINTMENT ID TO MEDICAL RECORDS
# ======================================================

    def add_medical_record_appointment_column(self):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            "PRAGMA table_info(medical_records)"
        )

        columns = cursor.fetchall()

        column_names = [
            column[1]
            for column in columns
        ]

        if "appointment_id" not in column_names:

            cursor.execute(
                """
                ALTER TABLE medical_records
                ADD COLUMN appointment_id TEXT
                """
            )

        connection.commit()
        connection.close()

    # ======================================================
    # PATIENT STATUS
    # ======================================================

    def add_patient_status_column(self):

        connection = None

        try:

            connection = self.connect()
            cursor = connection.cursor()

            cursor.execute(
                "PRAGMA table_info(patients)"
            )

            columns = [
                column[1]
                for column in cursor.fetchall()
            ]

            if "status" not in columns:

                cursor.execute(
                    """
                    ALTER TABLE patients
                    ADD COLUMN status
                    TEXT DEFAULT 'Active'
                    """
                )

            # Ensure existing patients have a status
            cursor.execute(
                """
                UPDATE patients

                SET status = 'Active'

                WHERE status IS NULL
                   OR status = ''
                """
            )

            connection.commit()

            return True

        except Exception as e:

            print(
                "Status initialization error:",
                e
            )

            return False

        finally:

            if connection:
                connection.close()

    # ======================================================
    # CREATE DOCTORS TABLE
    # ======================================================

    def create_doctors_table(self):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS doctors (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                doctor_id TEXT UNIQUE NOT NULL,

                full_name TEXT NOT NULL,

                gender TEXT NOT NULL,

                specialization TEXT NOT NULL,

                phone TEXT NOT NULL,

                email TEXT,

                address TEXT NOT NULL,

                license_number TEXT UNIQUE NOT NULL,

                status TEXT DEFAULT 'Active',

                created_at TIMESTAMP
                    DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        connection.commit()
        connection.close()

    # ======================================================
    # ADD PATIENT
    # ======================================================

    def add_patient(
        self,
        patient_id,
        full_name,
        gender,
        date_of_birth,
        phone,
        address,
        blood_group,
        emergency_contact
    ):

        connection = self.connect()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                INSERT INTO patients (

                    patient_id,
                    full_name,
                    gender,
                    date_of_birth,
                    phone,
                    address,
                    blood_group,
                    emergency_contact,
                    status

                )

                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,

                (
                    patient_id,
                    full_name,
                    gender,
                    date_of_birth,
                    phone,
                    address,
                    blood_group,
                    emergency_contact,
                    "Active"
                )
            )

            connection.commit()

            return True

        except sqlite3.IntegrityError:

            return False

        except Exception as e:

            print(
                "Add patient error:",
                e
            )

            return False

        finally:

            connection.close()

    # ======================================================
    # GET ALL PATIENTS
    # ======================================================

    def get_all_patients(self):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT

                patient_id,
                full_name,
                gender,
                date_of_birth,
                phone,
                address,
                blood_group,
                emergency_contact,
                status

            FROM patients

            ORDER BY id DESC
            """
        )

        patients = cursor.fetchall()

        connection.close()

        return patients

    # ======================================================
    # GET ACTIVE PATIENTS
    # ======================================================

    def get_active_patients(self):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT

                patient_id,
                full_name,
                gender,
                date_of_birth,
                phone,
                address,
                blood_group,
                emergency_contact,
                status

            FROM patients

            WHERE status = 'Active'

            ORDER BY id DESC
            """
        )

        patients = cursor.fetchall()

        connection.close()

        return patients

    # ======================================================
    # GET ARCHIVED PATIENTS
    # ======================================================

    def get_archived_patients(self):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT

                patient_id,
                full_name,
                gender,
                date_of_birth,
                phone,
                address,
                blood_group,
                emergency_contact,
                status

            FROM patients

            WHERE status = 'Archived'

            ORDER BY id DESC
            """
        )

        patients = cursor.fetchall()

        connection.close()

        return patients

    # ======================================================
    # SEARCH PATIENTS
    # ======================================================

    def search_patients(self, search_term):

        connection = self.connect()
        cursor = connection.cursor()

        search_pattern = f"%{search_term}%"

        cursor.execute(
            """
            SELECT

                patient_id,
                full_name,
                gender,
                date_of_birth,
                phone,
                address,
                blood_group,
                emergency_contact,
                status

            FROM patients

            WHERE patient_id LIKE ?
               OR full_name LIKE ?
               OR phone LIKE ?

            ORDER BY id DESC
            """,

            (
                search_pattern,
                search_pattern,
                search_pattern
            )
        )

        patients = cursor.fetchall()

        connection.close()

        return patients

    # ======================================================
    # GET SINGLE PATIENT
    # ======================================================

    def get_patient(self, patient_id):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT

                patient_id,
                full_name,
                gender,
                date_of_birth,
                phone,
                address,
                blood_group,
                emergency_contact,
                status

            FROM patients

            WHERE patient_id = ?
            """,

            (patient_id,)
        )

        patient = cursor.fetchone()

        connection.close()

        return patient

    # ======================================================
    # UPDATE PATIENT
    # ======================================================

    def update_patient(
        self,
        patient_id,
        full_name,
        gender,
        date_of_birth,
        phone,
        address,
        blood_group,
        emergency_contact
    ):

        connection = self.connect()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                UPDATE patients

                SET

                    full_name = ?,
                    gender = ?,
                    date_of_birth = ?,
                    phone = ?,
                    address = ?,
                    blood_group = ?,
                    emergency_contact = ?

                WHERE patient_id = ?
                """,

                (
                    full_name,
                    gender,
                    date_of_birth,
                    phone,
                    address,
                    blood_group,
                    emergency_contact,
                    patient_id
                )
            )

            connection.commit()

            return cursor.rowcount > 0

        except Exception as e:

            print(
                "Database update error:",
                e
            )

            return False

        finally:

            connection.close()

    # ======================================================
    # ARCHIVE PATIENT
    # ======================================================

    def archive_patient(self, patient_id):

        connection = self.connect()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                UPDATE patients

                SET status = 'Archived'

                WHERE patient_id = ?
                """,

                (patient_id,)
            )

            connection.commit()

            return cursor.rowcount > 0

        except Exception as e:

            print(
                "Archive patient error:",
                e
            )

            return False

        finally:

            connection.close()

    # ======================================================
    # RESTORE PATIENT
    # ======================================================

    def restore_patient(self, patient_id):

        connection = self.connect()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                UPDATE patients

                SET status = 'Active'

                WHERE patient_id = ?
                """,

                (patient_id,)
            )

            connection.commit()

            return cursor.rowcount > 0

        except Exception as e:

            print(
                "Restore patient error:",
                e
            )

            return False

        finally:

            connection.close()

    # ======================================================
    # DELETE PATIENT
    # ======================================================

    def delete_patient(self, patient_id):

        connection = self.connect()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                DELETE FROM patients

                WHERE patient_id = ?
                """,

                (patient_id,)
            )

            connection.commit()

            return cursor.rowcount > 0

        except Exception as e:

            print(
                "Delete patient error:",
                e
            )

            return False

        finally:

            connection.close()

    # ======================================================
    # PATIENT COUNT
    # ======================================================

    def get_patient_count(self):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)

            FROM patients

            WHERE status = 'Active'
            """
        )

        count = cursor.fetchone()[0]

        connection.close()

        return count

    # ======================================================
    # ARCHIVED PATIENT COUNT
    # ======================================================

    def get_archived_patient_count(self):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)

            FROM patients

            WHERE status = 'Archived'
            """
        )

        count = cursor.fetchone()[0]

        connection.close()

        return count

    # ======================================================
    # ADD MEDICAL RECORD
    # ======================================================

    def add_medical_record(
    self,
    record_id,
    patient_id,
    visit_date,
    symptoms,
    diagnosis,
    treatment,
    doctor,
    notes,
    appointment_id=None
):

        connection = self.connect()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                INSERT INTO medical_records (

                    record_id,
                    patient_id,
                    visit_date,
                    symptoms,
                    diagnosis,
                    treatment,
                    doctor,
                    notes

                )

                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,

                (
                    record_id,
                    patient_id,
                    visit_date,
                    symptoms,
                    diagnosis,
                    treatment,
                    doctor,
                    notes
                )
            )

            connection.commit()

            return True

        except sqlite3.IntegrityError:

            return False

        except Exception as e:

            print(
                "Add medical record error:",
                e
            )

            return False

        finally:

            connection.close()

    # ======================================================
    # GET PATIENT MEDICAL RECORDS
    # ======================================================

    def get_patient_medical_records(self, patient_id):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT

                record_id,
                patient_id,
                visit_date,
                symptoms,
                diagnosis,
                treatment,
                doctor,
                notes,
                created_at

            FROM medical_records

            WHERE patient_id = ?

            ORDER BY id DESC
            """,

            (patient_id,)
        )

        records = cursor.fetchall()

        connection.close()

        return records

    # ======================================================
    # GET SINGLE MEDICAL RECORD
    # ======================================================

    def get_medical_record(self, record_id):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT

                record_id,
                patient_id,
                visit_date,
                symptoms,
                diagnosis,
                treatment,
                doctor,
                notes,
                created_at

            FROM medical_records

            WHERE record_id = ?
            """,

            (record_id,)
        )

        record = cursor.fetchone()

        connection.close()

        return record

    # ======================================================
    # MEDICAL RECORD COUNT
    # ======================================================

    def get_medical_record_count(self):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)

            FROM medical_records
            """
        )

        count = cursor.fetchone()[0]

        connection.close()

        return count

    # ======================================================
    # ADD DOCTOR
    # ======================================================

    def add_doctor(
        self,
        doctor_id,
        full_name,
        gender,
        specialization,
        phone,
        email,
        address,
        license_number
    ):

        connection = self.connect()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                INSERT INTO doctors (

                    doctor_id,
                    full_name,
                    gender,
                    specialization,
                    phone,
                    email,
                    address,
                    license_number,
                    status

                )

                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,

                (
                    doctor_id,
                    full_name,
                    gender,
                    specialization,
                    phone,
                    email,
                    address,
                    license_number,
                    "Active"
                )
            )

            connection.commit()

            return True

        except sqlite3.IntegrityError:

            return False

        except Exception as e:

            print(
                "Add doctor error:",
                e
            )

            return False

        finally:

            connection.close()

    # ======================================================
    # GET ALL DOCTORS
    # ======================================================

    def get_all_doctors(self):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT

                doctor_id,
                full_name,
                gender,
                specialization,
                phone,
                email,
                address,
                license_number,
                status

            FROM doctors

            ORDER BY id DESC
            """
        )

        doctors = cursor.fetchall()

        connection.close()

        return doctors

    # ======================================================
    # GET ACTIVE DOCTORS
    # ======================================================

    def get_active_doctors(self):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT

                doctor_id,
                full_name,
                gender,
                specialization,
                phone,
                email,
                address,
                license_number,
                status

            FROM doctors

            WHERE status = 'Active'

            ORDER BY id DESC
            """
        )

        doctors = cursor.fetchall()

        connection.close()

        return doctors

    # ======================================================
    # DOCTOR COUNT
    # ======================================================

    def get_doctor_count(self):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)

            FROM doctors

            WHERE status = 'Active'
            """
        )

        count = cursor.fetchone()[0]

        connection.close()

        return count

    # ======================================================
    # SEARCH DOCTORS
    # ======================================================

    def search_doctors(self, search_term):

        connection = self.connect()
        cursor = connection.cursor()

        search_pattern = f"%{search_term}%"

        cursor.execute(
            """
            SELECT

                doctor_id,
                full_name,
                gender,
                specialization,
                phone,
                email,
                address,
                license_number,
                status

            FROM doctors

            WHERE doctor_id LIKE ?
               OR full_name LIKE ?
               OR specialization LIKE ?
               OR phone LIKE ?
               OR license_number LIKE ?

            ORDER BY id DESC
            """,

            (
                search_pattern,
                search_pattern,
                search_pattern,
                search_pattern,
                search_pattern
            )
        )

        doctors = cursor.fetchall()

        connection.close()

        return doctors

    # ======================================================
    # UPDATE DOCTOR
    # ======================================================

    def update_doctor(
        self,
        doctor_id,
        full_name,
        gender,
        specialization,
        phone,
        email,
        address,
        license_number
    ):

        connection = self.connect()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                UPDATE doctors

                SET

                    full_name = ?,
                    gender = ?,
                    specialization = ?,
                    phone = ?,
                    email = ?,
                    address = ?,
                    license_number = ?

                WHERE doctor_id = ?
                """,

                (
                    full_name,
                    gender,
                    specialization,
                    phone,
                    email,
                    address,
                    license_number,
                    doctor_id
                )
            )

            connection.commit()

            return cursor.rowcount > 0

        except sqlite3.IntegrityError:

            return False

        except Exception as e:

            print(
                "Doctor update error:",
                e
            )

            return False

        finally:

            connection.close()

    # ======================================================
    # DEACTIVATE DOCTOR
    # ======================================================

    def deactivate_doctor(self, doctor_id):

        connection = self.connect()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                UPDATE doctors

                SET status = 'Inactive'

                WHERE doctor_id = ?
                """,

                (doctor_id,)
            )

            connection.commit()

            return cursor.rowcount > 0

        except Exception as e:

            print(
                "Deactivate doctor error:",
                e
            )

            return False

        finally:

            connection.close()

    # ======================================================
    # ACTIVATE DOCTOR
    # ======================================================

    def activate_doctor(self, doctor_id):

        connection = self.connect()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                UPDATE doctors

                SET status = 'Active'

                WHERE doctor_id = ?
                """,

                (doctor_id,)
            )

            connection.commit()

            return cursor.rowcount > 0

        except Exception as e:

            print(
                "Activate doctor error:",
                e
            )

            return False

        finally:

            connection.close()

    # ======================================================
    # GET SINGLE DOCTOR
    # ======================================================

    def get_doctor(self, doctor_id):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT

                doctor_id,
                full_name,
                gender,
                specialization,
                phone,
                email,
                address,
                license_number,
                status

            FROM doctors

            WHERE doctor_id = ?
            """,

            (doctor_id,)
        )

        doctor = cursor.fetchone()

        connection.close()

        return doctor
        # ======================================================
    # ADD APPOINTMENT
    # ======================================================

    def add_appointment(
        self,
        appointment_id,
        patient_id,
        doctor_id,
        appointment_date,
        appointment_time,
        reason,
        notes
    ):

        connection = self.connect()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                INSERT INTO appointments (

                    appointment_id,
                    patient_id,
                    doctor_id,
                    appointment_date,
                    appointment_time,
                    reason,
                    status,
                    notes

                )

                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,

                (
                    appointment_id,
                    patient_id,
                    doctor_id,
                    appointment_date,
                    appointment_time,
                    reason,
                    "Scheduled",
                    notes
                )
            )

            connection.commit()

            return True

        except sqlite3.IntegrityError:

            return False

        except Exception as e:

            print(
                "Add appointment error:",
                e
            )

            return False

        finally:

            connection.close()
        # ======================================================
    # GET ALL APPOINTMENTS
    # ======================================================

    def get_all_appointments(self):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT

                appointment_id,
                patient_id,
                doctor_id,
                appointment_date,
                appointment_time,
                reason,
                status,
                notes,
                created_at

            FROM appointments

            ORDER BY id DESC
            """
        )

        appointments = cursor.fetchall()

        connection.close()

        return appointments
        # ======================================================
    # APPOINTMENT COUNT
    # ======================================================

    def get_appointment_count(self):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)

            FROM appointments

            WHERE status = 'Scheduled'
            """
        )

        count = cursor.fetchone()[0]

        connection.close()

        return count
        # ======================================================
    # SEARCH APPOINTMENTS
    # ======================================================

    def search_appointments(self, search_term):

        connection = self.connect()
        cursor = connection.cursor()

        search_pattern = f"%{search_term}%"

        cursor.execute(
            """
            SELECT

                appointment_id,
                patient_id,
                doctor_id,
                appointment_date,
                appointment_time,
                reason,
                status,
                notes,
                created_at

            FROM appointments

            WHERE appointment_id LIKE ?
               OR patient_id LIKE ?
               OR doctor_id LIKE ?
               OR appointment_date LIKE ?
               OR reason LIKE ?

            ORDER BY id DESC
            """,

            (
                search_pattern,
                search_pattern,
                search_pattern,
                search_pattern,
                search_pattern
            )
        )

        appointments = cursor.fetchall()

        connection.close()

        return appointments
        # ======================================================
    # APPOINTMENT CONFLICT CHECK
    # ======================================================

    def check_appointment_conflict(self, doctor_id, appointment_date, appointment_time, exclude_appointment_id=None):
        """
        Checks whether a doctor already has a scheduled appointment
        at the specified date and time.

        Returns:
            True  -> Conflict exists
            False -> No conflict
        """

        connection = self.connect()
        cursor = connection.cursor()

        query = """
            SELECT COUNT(*)
            FROM appointments
            WHERE doctor_id = ?
            AND appointment_date = ?
            AND appointment_time = ?
            AND status = 'Scheduled'
        """

        parameters = [
            doctor_id,
            appointment_date,
            appointment_time
        ]

        # --------------------------------------------------
        # When updating an existing appointment, exclude it
        # from the conflict check.
        # --------------------------------------------------

        if exclude_appointment_id:
            query += " AND appointment_id != ?"
            parameters.append(exclude_appointment_id)

        cursor.execute(query, parameters)

        count = cursor.fetchone()[0]

        connection.close()

        return count > 0
        # ======================================================
    # GET SINGLE APPOINTMENT
    # ======================================================

    def get_appointment(self, appointment_id):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT

                appointment_id,
                patient_id,
                doctor_id,
                appointment_date,
                appointment_time,
                reason,
                status,
                notes,
                created_at

            FROM appointments

            WHERE appointment_id = ?
            """,

            (appointment_id,)
        )

        appointment = cursor.fetchone()

        connection.close()

        return appointment

    # ======================================================
    # UPDATE APPOINTMENT
    # ======================================================

    def update_appointment(
        self,
        appointment_id,
        patient_id,
        doctor_id,
        appointment_date,
        appointment_time,
        reason,
        notes
    ):

        connection = self.connect()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                UPDATE appointments

                SET

                    patient_id = ?,
                    doctor_id = ?,
                    appointment_date = ?,
                    appointment_time = ?,
                    reason = ?,
                    notes = ?

                WHERE appointment_id = ?
                """,

                (
                    patient_id,
                    doctor_id,
                    appointment_date,
                    appointment_time,
                    reason,
                    notes,
                    appointment_id
                )
            )

            connection.commit()

            return cursor.rowcount > 0

        except Exception as e:

            print(
                "Update appointment error:",
                e
            )

            return False

        finally:

            connection.close()

    # ======================================================
    # CANCEL APPOINTMENT
    # ======================================================

    def cancel_appointment(self, appointment_id):

        connection = self.connect()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                UPDATE appointments

                SET status = 'Cancelled'

                WHERE appointment_id = ?
                """,

                (appointment_id,)
            )

            connection.commit()

            return cursor.rowcount > 0

        except Exception as e:

            print(
                "Cancel appointment error:",
                e
            )

            return False

        finally:

            connection.close()

    # ======================================================
    # COMPLETE APPOINTMENT
    # ======================================================

    def complete_appointment(self, appointment_id):

        connection = self.connect()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                UPDATE appointments

                SET status = 'Completed'

                WHERE appointment_id = ?
                """,

                (appointment_id,)
            )

            connection.commit()

            return cursor.rowcount > 0

        except Exception as e:

            print(
                "Complete appointment error:",
                e
            )

            return False

        finally:

            connection.close()

    # ======================================================
    # RESTORE APPOINTMENT
    # ======================================================

    def restore_appointment(self, appointment_id):

        connection = self.connect()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                UPDATE appointments

                SET status = 'Scheduled'

                WHERE appointment_id = ?
                """,

                (appointment_id,)
            )

            connection.commit()

            return cursor.rowcount > 0

        except Exception as e:

            print(
                "Restore appointment error:",
                e
            )

            return False

        finally:

            connection.close()

        # ======================================================
    # APPOINTMENT DASHBOARD STATISTICS
    # ======================================================

    def get_todays_appointment_count(self):

        today = datetime.now().strftime("%d/%m/%Y")

        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM appointments
            WHERE appointment_date = ?
            """,
            (today,)
        )

        count = cursor.fetchone()[0]

        conn.close()

        return count
        # ======================================================
    # UPCOMING APPOINTMENT COUNT
    # ======================================================

    def get_upcoming_appointment_count(self):

        current_datetime = datetime.now()

        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT appointment_date, appointment_time
            FROM appointments
            WHERE status = 'Scheduled'
            """
        )

        appointments = cursor.fetchall()

        conn.close()

        count = 0

        for appointment in appointments:

            appointment_date = appointment[0]
            appointment_time = appointment[1]

            try:

                appointment_datetime = datetime.strptime(
                    f"{appointment_date} {appointment_time}",
                    "%d/%m/%Y %H:%M"
                )

            except ValueError:

                continue

            if appointment_datetime >= current_datetime:

                count += 1

        return count
        # ======================================================
    # APPOINTMENT STATUS COUNT
    # ======================================================

    def get_appointment_status_count(self, status):

        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM appointments
            WHERE status = ?
            """,
            (status,)
        )

        count = cursor.fetchone()[0]

        conn.close()

        return count

        # ======================================================
    # GET PATIENT APPOINTMENT HISTORY
    # ======================================================

    def get_patient_appointments(self, patient_id):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT

                appointment_id,
                patient_id,
                doctor_id,
                appointment_date,
                appointment_time,
                reason,
                status,
                notes,
                created_at

            FROM appointments

            WHERE patient_id = ?

            ORDER BY id DESC
            """,

            (patient_id,)
        )

        appointments = cursor.fetchall()

        connection.close()

        return appointments
# ======================================================
# GET MEDICAL RECORD FROM APPOINTMENT
# ======================================================

    def get_appointment_medical_record(self, appointment_id):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                record_id,
                patient_id,
                visit_date,
                symptoms,
                diagnosis,
                treatment,
                doctor,
                notes,
                appointment_id,
                created_at
            FROM medical_records
            WHERE appointment_id = ?
            ORDER BY id DESC
            LIMIT 1
            """,
            (appointment_id,)
        )

        record = cursor.fetchone()

        connection.close()

        return record
        # ======================================================
    # ADD BILL
    # ======================================================

    def add_bill(
        self,
        bill_id,
        patient_id,
        appointment_id,
        bill_date
    ):

        connection = self.connect()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                INSERT INTO bills (
                    bill_id,
                    patient_id,
                    appointment_id,
                    bill_date,
                    total_amount,
                    amount_paid,
                    balance,
                    status
                )
                VALUES (?, ?, ?, ?, 0, 0, 0, 'Pending')
                """,
                (
                    bill_id,
                    patient_id,
                    appointment_id,
                    bill_date
                )
            )

            connection.commit()

            return True

        except sqlite3.IntegrityError:

            return False

        finally:

            connection.close()
        # ======================================================
    # ADD BILL ITEM
    # ======================================================

    def add_bill_item(
        self,
        bill_item_id,
        bill_id,
        description,
        quantity,
        unit_price
    ):

        total_price = quantity * unit_price

        connection = self.connect()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                INSERT INTO bill_items (
                    bill_item_id,
                    bill_id,
                    description,
                    quantity,
                    unit_price,
                    total_price
                )
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    bill_item_id,
                    bill_id,
                    description,
                    quantity,
                    unit_price,
                    total_price
                )
            )

            connection.commit()

            return True

        except sqlite3.IntegrityError:

            return False

        finally:

            connection.close()
        # ======================================================
    # UPDATE BILL TOTAL
    # ======================================================

    def update_bill_total(self, bill_id):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT COALESCE(SUM(total_price), 0)
            FROM bill_items
            WHERE bill_id = ?
            """,
            (bill_id,)
        )

        total = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT amount_paid
            FROM bills
            WHERE bill_id = ?
            """,
            (bill_id,)
        )

        result = cursor.fetchone()

        if result:

            amount_paid = result[0]

        else:

            amount_paid = 0

        balance = total - amount_paid

        if amount_paid >= total and total > 0:

            status = "Paid"

        elif amount_paid > 0:

            status = "Partially Paid"

        else:

            status = "Pending"

        cursor.execute(
            """
            UPDATE bills
            SET
                total_amount = ?,
                balance = ?,
                status = ?
            WHERE bill_id = ?
            """,
            (
                total,
                balance,
                status,
                bill_id
            )
        )

        connection.commit()
        connection.close()

        return total
        # ======================================================
    # GET ALL BILLS
    # ======================================================

    def get_all_bills(self):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                bill_id,
                patient_id,
                appointment_id,
                bill_date,
                total_amount,
                amount_paid,
                balance,
                status,
                created_at
            FROM bills
            ORDER BY id DESC
            """
        )

        bills = cursor.fetchall()

        connection.close()

        return bills
        # ======================================================
    # GET BILL
    # ======================================================

    def get_bill(self, bill_id):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                bill_id,
                patient_id,
                appointment_id,
                bill_date,
                total_amount,
                amount_paid,
                balance,
                status,
                created_at
            FROM bills
            WHERE bill_id = ?
            """,
            (bill_id,)
        )

        bill = cursor.fetchone()

        connection.close()

        return bill
        # ======================================================
    # GET BILL ITEMS
    # ======================================================

    def get_bill_items(self, bill_id):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                bill_item_id,
                bill_id,
                description,
                quantity,
                unit_price,
                total_price,
                created_at
            FROM bill_items
            WHERE bill_id = ?
            ORDER BY id ASC
            """,
            (bill_id,)
        )

        items = cursor.fetchall()

        connection.close()

        return items
# ======================================================
# ADD BILL
# ======================================================

def add_bill(self, bill_id, patient_id, appointment_id, bill_date):

    connection = self.connect()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO bills (
            bill_id,
            patient_id,
            appointment_id,
            bill_date,
            total_amount,
            amount_paid,
            balance,
            status
        )
        VALUES (?, ?, ?, ?, 0, 0, 0, 'Pending')
    """, (
        bill_id,
        patient_id,
        appointment_id,
        bill_date
    ))

    connection.commit()
    connection.close()
# ======================================================
# ADD BILL ITEM
# ======================================================

def add_bill_item(
    self,
    bill_item_id,
    bill_id,
    description,
    quantity,
    unit_price
):

    total_price = quantity * unit_price

    connection = self.connect()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO bill_items (
            bill_item_id,
            bill_id,
            description,
            quantity,
            unit_price,
            total_price
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        bill_item_id,
        bill_id,
        description,
        quantity,
        unit_price,
        total_price
    ))

    connection.commit()
    connection.close()
# ======================================================
# UPDATE BILL TOTAL
# ======================================================

def update_bill_total(self, bill_id):

    connection = self.connect()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COALESCE(SUM(total_price), 0)
        FROM bill_items
        WHERE bill_id = ?
    """, (bill_id,))

    total_amount = cursor.fetchone()[0]

    cursor.execute("""
        SELECT amount_paid
        FROM bills
        WHERE bill_id = ?
    """, (bill_id,))

    result = cursor.fetchone()

    if result is None:
        connection.close()
        return

    amount_paid = result[0]

    balance = total_amount - amount_paid

    if total_amount > 0 and amount_paid >= total_amount:

        status = "Paid"

    elif amount_paid > 0:

        status = "Partially Paid"

    else:

        status = "Pending"

    cursor.execute("""
        UPDATE bills
        SET
            total_amount = ?,
            balance = ?,
            status = ?
        WHERE bill_id = ?
    """, (
        total_amount,
        balance,
        status,
        bill_id
    ))

    connection.commit()
    connection.close()
# ======================================================
# GET ALL BILLS
# ======================================================

def get_all_bills(self):

    connection = self.connect()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            bill_id,
            patient_id,
            appointment_id,
            bill_date,
            total_amount,
            amount_paid,
            balance,
            status,
            created_at
        FROM bills
        ORDER BY id DESC
    """)

    bills = cursor.fetchall()

    connection.close()

    return bills
# ======================================================
# GET BILL
# ======================================================

def get_bill(self, bill_id):

    connection = self.connect()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            bill_id,
            patient_id,
            appointment_id,
            bill_date,
            total_amount,
            amount_paid,
            balance,
            status,
            created_at
        FROM bills
        WHERE bill_id = ?
    """, (bill_id,))

    bill = cursor.fetchone()

    connection.close()

    return bill
# ======================================================
# GET BILL ITEMS
# ======================================================

def get_bill_items(self, bill_id):

    connection = self.connect()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            bill_item_id,
            bill_id,
            description,
            quantity,
            unit_price,
            total_price,
            created_at
        FROM bill_items
        WHERE bill_id = ?
        ORDER BY id ASC
    """)

    items = cursor.fetchall()

    connection.close()

    return items
if __name__ == "__main__":

    db = Database()

    db.add_bill(
        "BILL-0001",
        "PAT-0001",
        None,
        "23/09/2026"
    )

    db.add_bill_item(
        "ITEM-0001",
        "BILL-0001",
        "Consultation",
        1,
        500
    )

    db.add_bill_item(
        "ITEM-0002",
        "BILL-0001",
        "Laboratory Test",
        2,
        300
    )

    db.update_bill_total("BILL-0001")

    print("\nBILL:")
    print(db.get_bill("BILL-0001"))

    print("\nBILL ITEMS:")

    for item in db.get_bill_items("BILL-0001"):
        print(item)

                            
