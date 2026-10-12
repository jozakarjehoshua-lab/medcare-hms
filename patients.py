import tkinter as tk
from tkinter import ttk, messagebox

from database import Database


class PatientsWindow:

    def __init__(self, parent):

        # ==================================================
        # COLORS
        # ==================================================

        self.BACKGROUND = "#F4F7FA"
        self.PRIMARY = "#1565C0"
        self.DARK = "#263238"
        self.WHITE = "#FFFFFF"
        self.GRAY = "#607D8B"
        self.SUCCESS = "#2E7D32"
        self.DANGER = "#C62828"

        # ==================================================
        # DATABASE
        # ==================================================

        self.db = Database()

        # ==================================================
        # WINDOW
        # ==================================================

        self.window = tk.Toplevel(parent)

        self.window.title(
            "MedCare HMS - Patient Management"
        )

        self.window.geometry(
            "1100x700"
        )

        self.window.minsize(
            950,
            600
        )

        self.window.configure(
            bg=self.BACKGROUND
        )

        # ==================================================
        # CREATE INTERFACE
        # ==================================================

        self.create_interface()

    # ======================================================
    # MAIN INTERFACE
    # ======================================================

    def create_interface(self):

        # ==================================================
        # HEADER
        # ==================================================

        header = tk.Frame(
            self.window,
            bg=self.PRIMARY,
            height=85
        )

        header.pack(fill="x")
        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="Patient Management",
            font=("Segoe UI", 22, "bold"),
            bg=self.PRIMARY,
            fg=self.WHITE
        )

        title.pack(
            side="left",
            padx=30,
            pady=20
        )

        subtitle = tk.Label(
            header,
            text="Register and manage patient information",
            font=("Segoe UI", 10),
            bg=self.PRIMARY,
            fg=self.WHITE
        )

        subtitle.pack(
            side="right",
            padx=30
        )

        # ==================================================
        # MAIN CONTENT
        # ==================================================

        main_frame = tk.Frame(
            self.window,
            bg=self.BACKGROUND
        )

        main_frame.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=20
        )

        # ==================================================
        # REGISTRATION FORM
        # ==================================================

        form_frame = tk.LabelFrame(
            main_frame,
            text="  Patient Registration  ",
            bg=self.WHITE,
            fg=self.DARK,
            font=("Segoe UI", 11, "bold"),
            padx=20,
            pady=15
        )

        form_frame.pack(fill="x")

        # ==================================================
        # FULL NAME
        # ==================================================

        ttk.Label(
            form_frame,
            text="Full Name"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=10,
            pady=8
        )

        self.name_entry = ttk.Entry(
            form_frame,
            width=30
        )

        self.name_entry.grid(
            row=0,
            column=1,
            padx=10,
            pady=8
        )

        # ==================================================
        # GENDER
        # ==================================================

        ttk.Label(
            form_frame,
            text="Gender"
        ).grid(
            row=0,
            column=2,
            sticky="w",
            padx=10,
            pady=8
        )

        self.gender_combo = ttk.Combobox(
            form_frame,
            values=[
                "Male",
                "Female"
            ],
            state="readonly",
            width=18
        )

        self.gender_combo.grid(
            row=0,
            column=3,
            padx=10,
            pady=8
        )

        # ==================================================
        # DATE OF BIRTH
        # ==================================================

        ttk.Label(
            form_frame,
            text="Date of Birth"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=10,
            pady=8
        )

        self.dob_entry = ttk.Entry(
            form_frame,
            width=30
        )

        self.dob_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=8
        )

        # ==================================================
        # PHONE
        # ==================================================

        ttk.Label(
            form_frame,
            text="Phone Number"
        ).grid(
            row=1,
            column=2,
            sticky="w",
            padx=10,
            pady=8
        )

        self.phone_entry = ttk.Entry(
            form_frame,
            width=20
        )

        self.phone_entry.grid(
            row=1,
            column=3,
            padx=10,
            pady=8
        )

        # ==================================================
        # ADDRESS
        # ==================================================

        ttk.Label(
            form_frame,
            text="Address"
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=10,
            pady=8
        )

        self.address_entry = ttk.Entry(
            form_frame,
            width=30
        )

        self.address_entry.grid(
            row=2,
            column=1,
            padx=10,
            pady=8
        )

        # ==================================================
        # BLOOD GROUP
        # ==================================================

        ttk.Label(
            form_frame,
            text="Blood Group"
        ).grid(
            row=2,
            column=2,
            sticky="w",
            padx=10,
            pady=8
        )

        self.blood_combo = ttk.Combobox(
            form_frame,
            values=[
                "A+",
                "A-",
                "B+",
                "B-",
                "AB+",
                "AB-",
                "O+",
                "O-"
            ],
            state="readonly",
            width=18
        )

        self.blood_combo.grid(
            row=2,
            column=3,
            padx=10,
            pady=8
        )

        # ==================================================
        # EMERGENCY CONTACT
        # ==================================================

        ttk.Label(
            form_frame,
            text="Emergency Contact"
        ).grid(
            row=3,
            column=0,
            sticky="w",
            padx=10,
            pady=8
        )

        self.emergency_entry = ttk.Entry(
            form_frame,
            width=30
        )

        self.emergency_entry.grid(
            row=3,
            column=1,
            padx=10,
            pady=8
        )

        # ==================================================
        # BUTTONS
        # ==================================================

        button_frame = tk.Frame(
            main_frame,
            bg=self.BACKGROUND
        )

        button_frame.pack(pady=15)

        register_button = tk.Button(
            button_frame,
            text="Register Patient",
            command=self.register_patient,
            bg=self.PRIMARY,
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=8
        )

        register_button.grid(
            row=0,
            column=0,
            padx=8
        )

        clear_button = tk.Button(
            button_frame,
            text="Clear Form",
            command=self.clear_form,
            bg=self.GRAY,
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=8
        )

        clear_button.grid(
            row=0,
            column=1,
            padx=8
        )

        view_button = tk.Button(
            button_frame,
            text="View Patient",
            command=self.view_patient,
            bg=self.SUCCESS,
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=8
        )

        view_button.grid(
            row=0,
            column=2,
            padx=8
        )

        edit_button = tk.Button(
            button_frame,
            text="Edit Patient",
            command=self.edit_patient,
            bg="#EF6C00",
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=8
        )

        edit_button.grid(
            row=0,
            column=3,
            padx=8
        )

        archive_button = tk.Button(
            button_frame,
            text="Archive Patient",
            command=self.archive_selected_patient,
            bg=self.DANGER,
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=8
        )

        archive_button.grid(
            row=0,
            column=4,
            padx=8
        )

        restore_button = tk.Button(
            button_frame,
            text="Restore Patient",
            command=self.restore_selected_patient,
            bg=self.SUCCESS,
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=8
        )

        restore_button.grid(
            row=0,
            column=5,
            padx=8
        )
       




        # ==================================================
        # SEARCH
        # ==================================================

        search_frame = tk.Frame(
            main_frame,
            bg=self.WHITE,
            padx=15,
            pady=12
        )

        search_frame.pack(fill="x")

        tk.Label(
            search_frame,
            text="Search Patient:",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).pack(
            side="left",
            padx=(0, 10)
        )

        self.search_entry = ttk.Entry(
            search_frame,
            width=35
        )

        self.search_entry.pack(
            side="left"
        )

        search_button = tk.Button(
            search_frame,
            text="Search",
            command=self.search_patient,
            bg=self.PRIMARY,
            fg=self.WHITE,
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=5
        )

        search_button.pack(
            side="left",
            padx=8
        )

        show_all_button = tk.Button(
            search_frame,
            text="Show All",
            command=self.display_patients,
            bg=self.GRAY,
            fg=self.WHITE,
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=5
        )

        show_all_button.pack(
            side="left"
        )

        # ==================================================
        # PATIENT TABLE
        # ==================================================

        table_frame = tk.Frame(
            main_frame,
            bg=self.WHITE
        )

        table_frame.pack(
            fill="both",
            expand=True,
            pady=(15, 0)
        )

        columns = (
            "id",
            "name",
            "gender",
            "dob",
            "phone",
            "blood",
            "emergency",
            "status"
        )

        self.patient_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        self.patient_table.heading(
            "id",
            text="Patient ID"
        )

        self.patient_table.heading(
            "name",
            text="Full Name"
        )

        self.patient_table.heading(
            "gender",
            text="Gender"
        )

        self.patient_table.heading(
            "dob",
            text="Date of Birth"
        )

        self.patient_table.heading(
            "phone",
            text="Phone"
        )

        self.patient_table.heading(
            "blood",
            text="Blood Group"
        )

        self.patient_table.heading(
            "emergency",
            text="Emergency Contact"
        )
        self.patient_table.heading(
    "status",
    text="Status"
)
        

        self.patient_table.column(
            "id",
            width=100
        )

        self.patient_table.column(
            "name",
            width=170
        )

        self.patient_table.column(
            "gender",
            width=80
        )

        self.patient_table.column(
            "dob",
            width=100
        )

        self.patient_table.column(
            "phone",
            width=120
        )

        self.patient_table.column(
            "blood",
            width=100
        )

        self.patient_table.column(
            "emergency",
            width=150
        )
        self.patient_table.column(
    "status",
    width=100
)

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.patient_table.yview
        )

        self.patient_table.configure(
            yscrollcommand=scrollbar.set
        )

        self.patient_table.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # ==================================================
        # LOAD EXISTING PATIENTS
        # ==================================================

        self.display_patients()

    # ======================================================
    # REGISTER PATIENT
    # ======================================================

    def register_patient(self):

        name = self.name_entry.get().strip()
        gender = self.gender_combo.get()
        dob = self.dob_entry.get().strip()
        phone = self.phone_entry.get().strip()
        address = self.address_entry.get().strip()
        blood = self.blood_combo.get()
        emergency = self.emergency_entry.get().strip()

        # ==================================================
        # VALIDATION
        # ==================================================

        if not all([
            name,
            gender,
            dob,
            phone,
            address,
            blood,
            emergency
        ]):

            messagebox.showerror(
                "Missing Information",
                "Please complete all patient fields."
            )

            return

        # ==================================================
        # GENERATE PATIENT ID
        # ==================================================

        existing_patients = self.db.get_all_patients()

        patient_number = len(existing_patients) + 1

        patient_id = f"PAT-{patient_number:04d}"

        # ==================================================
        # SAVE TO DATABASE
        # ==================================================

        saved = self.db.add_patient(
            patient_id,
            name,
            gender,
            dob,
            phone,
            address,
            blood,
            emergency
        )

        if not saved:

            messagebox.showerror(
                "Registration Error",
                "The patient could not be registered."
            )

            return

        # ==================================================
        # SUCCESS
        # ==================================================

        messagebox.showinfo(
            "Patient Registered",
            f"Patient registered successfully.\n\n"
            f"Patient ID: {patient_id}"
        )

        self.clear_form()

        # Refresh table
        self.display_patients()

    # ======================================================
    # CLEAR FORM
    # ======================================================

    def clear_form(self):

        self.name_entry.delete(
            0,
            tk.END
        )

        self.gender_combo.set("")

        self.dob_entry.delete(
            0,
            tk.END
        )

        self.phone_entry.delete(
            0,
            tk.END
        )

        self.address_entry.delete(
            0,
            tk.END
        )

        self.blood_combo.set("")

        self.emergency_entry.delete(
            0,
            tk.END
        )

    # ======================================================
    # SEARCH PATIENT
    # ======================================================

    def search_patient(self):

        search_term = (
            self.search_entry.get()
            .strip()
        )

        # Empty search = show everything

        if not search_term:

            self.display_patients()

            return

        # Clear current table

        for item in self.patient_table.get_children():
            self.patient_table.delete(item)

        # Search database

        patients = self.db.search_patients(
            search_term
        )

        # Display results

        for patient in patients:
            self.patient_table.insert(
                "",
                "end",
                values=(
                    patient[0],  # Patient ID
                    patient[1],  # Name
                    patient[2],  # Gender
                    patient[3],  # DOB
                    patient[4],  # Phone
                    patient[6],  # Blood Group
                    patient[7],  # Emergency Contact
                    patient[8]   # Status
                )
            )

    # ======================================================
    # DISPLAY ALL PATIENTS
    # ======================================================

    def display_patients(self):
        # Clear current table
        for item in self.patient_table.get_children():
            self.patient_table.delete(item)

        # Get patients from database
        patients = self.db.get_all_patients()

        # Display patients
        for patient in patients:

            self.patient_table.insert(
                "",
                "end",
                values=(
                    patient[0],
                    patient[1],
                    patient[2],
                    patient[3],
                    patient[4],
                    patient[6],
                    patient[7],
                    patient[8]
                )
            )

    # ======================================================
    # VIEW PATIENT PROFILE
    # ======================================================

    def view_patient(self):

        selected = self.patient_table.selection()

        if not selected:

            messagebox.showwarning(
                "No Patient Selected",
                "Please select a patient first."
            )

            return

        # --------------------------------------------------
        # Get selected patient ID
        # --------------------------------------------------

        patient_values = self.patient_table.item(
            selected[0],
            "values"
        )

        patient_id = patient_values[0]

        # --------------------------------------------------
        # Get patient information
        # --------------------------------------------------

        patient = self.db.get_patient(patient_id)

        if not patient:

            messagebox.showerror(
                "Patient Not Found",
                "The selected patient could not be found."
            )

            return

        # --------------------------------------------------
        # Create profile window
        # --------------------------------------------------

        profile_window = tk.Toplevel(
            self.window
        )

        profile_window.title(
            f"Patient Profile - {patient[0]}"
        )

        profile_window.geometry(
            "850x700"
        )

        profile_window.minsize(
            750,
            600
        )

        profile_window.configure(
            bg=self.BACKGROUND
        )

        # ==================================================
        # PROFILE HEADER
        # ==================================================

        header = tk.Frame(
            profile_window,
            bg=self.PRIMARY,
            height=85
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(
            False
        )

        title = tk.Label(
            header,
            text="Patient Profile",
            font=("Segoe UI", 22, "bold"),
            bg=self.PRIMARY,
            fg=self.WHITE
        )

        title.pack(
            side="left",
            padx=30
        )

        patient_id_label = tk.Label(
            header,
            text=f"Patient ID: {patient[0]}",
            font=("Segoe UI", 11, "bold"),
            bg=self.PRIMARY,
            fg=self.WHITE
        )

        patient_id_label.pack(
            side="right",
            padx=30
        )

        # ==================================================
        # SCROLLABLE CONTENT AREA
        # ==================================================

        container = tk.Frame(
            profile_window,
            bg=self.BACKGROUND
        )

        container.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        canvas = tk.Canvas(
            container,
            bg=self.BACKGROUND,
            highlightthickness=0
        )

        scrollbar = ttk.Scrollbar(
            container,
            orient="vertical",
            command=canvas.yview
        )

        content = tk.Frame(
            canvas,
            bg=self.BACKGROUND
        )

        content.bind(
            "<Configure>",
            lambda event: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window(
            (0, 0),
            window=content,
            anchor="nw"
        )

        canvas.configure(
            yscrollcommand=scrollbar.set
        )

        canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # ==================================================
        # PERSONAL INFORMATION
        # ==================================================

        personal_frame = tk.LabelFrame(
            content,
            text="  Personal Information  ",
            font=("Segoe UI", 11, "bold"),
            bg=self.WHITE,
            fg=self.DARK,
            padx=20,
            pady=15
        )

        personal_frame.pack(
            fill="x",
            pady=(0, 15)
        )

        for column in range(2):

            personal_frame.grid_columnconfigure(
                column,
                weight=1
            )

        information = [

            ("Patient ID", patient[0]),
            ("Full Name", patient[1]),
            ("Gender", patient[2]),
            ("Date of Birth", patient[3]),
            ("Phone Number", patient[4]),
            ("Address", patient[5]),
            ("Blood Group", patient[6]),
            ("Emergency Contact", patient[7]),
            ("Status", patient[8])

        ]

        for index, (label, value) in enumerate(information):

            row = index // 2
            column = index % 2

            field_frame = tk.Frame(
                personal_frame,
                bg=self.WHITE
            )

            field_frame.grid(
                row=row,
                column=column,
                sticky="ew",
                padx=10,
                pady=8
            )

            tk.Label(
                field_frame,
                text=label,
                font=("Segoe UI", 9),
                bg=self.WHITE,
                fg=self.GRAY
            ).pack(
                anchor="w"
            )

            tk.Label(
                field_frame,
                text=value,
                font=("Segoe UI", 10, "bold"),
                bg=self.WHITE,
                fg=self.DARK
            ).pack(
                anchor="w"
            )

        # ==================================================
        # MEDICAL HISTORY
        # ==================================================

        medical_frame = tk.LabelFrame(
            content,
            text="  Medical History  ",
            font=("Segoe UI", 11, "bold"),
            bg=self.WHITE,
            fg=self.DARK,
            padx=15,
            pady=15
        )

        medical_frame.pack(
            fill="both",
            expand=True,
            pady=(0, 15)
        )

        medical_columns = (
            "record_id",
            "visit_date",
            "doctor",
            "diagnosis",
            "treatment"
        )

        medical_table = ttk.Treeview(
            medical_frame,
            columns=medical_columns,
            show="headings",
            height=7
        )

        medical_table.heading(
            "record_id",
            text="Record ID"
        )

        medical_table.heading(
            "visit_date",
            text="Visit Date"
        )

        medical_table.heading(
            "doctor",
            text="Doctor"
        )

        medical_table.heading(
            "diagnosis",
            text="Diagnosis"
        )

        medical_table.heading(
            "treatment",
            text="Treatment"
        )

        medical_table.column(
            "record_id",
            width=100
        )

        medical_table.column(
            "visit_date",
            width=100
        )

        medical_table.column(
            "doctor",
            width=150
        )

        medical_table.column(
            "diagnosis",
            width=180
        )

        medical_table.column(
            "treatment",
            width=180
        )

        medical_scrollbar = ttk.Scrollbar(
            medical_frame,
            orient="vertical",
            command=medical_table.yview
        )

        medical_table.configure(
            yscrollcommand=medical_scrollbar.set
        )

        medical_table.pack(
            side="left",
            fill="both",
            expand=True
        )

        medical_scrollbar.pack(
            side="right",
            fill="y"
        )

        # --------------------------------------------------
        # Load medical records
        # --------------------------------------------------

        medical_records = (
            self.db.get_patient_medical_records(
                patient_id
            )
        )

        for record in medical_records:

            medical_table.insert(
                "",
                "end",
                values=(
                    record[0],
                    record[2],
                    record[6],
                    record[4],
                    record[5]
                )
            )

        # --------------------------------------------------
        # Empty medical history message
        # --------------------------------------------------

        if not medical_records:

            tk.Label(
                medical_frame,
                text="No medical records found for this patient.",
                font=("Segoe UI", 10),
                bg=self.WHITE,
                fg=self.GRAY
            ).pack(
                pady=10
            )

                # --------------------------------------------------
        # Medical record details
        # --------------------------------------------------

        def show_medical_record(event=None):

            selected_record = medical_table.selection()

            if not selected_record:
                return

            record_values = medical_table.item(
                selected_record[0],
                "values"
            )

            record_id = record_values[0]

            record = self.db.get_medical_record(
                record_id
            )

            if not record:
                messagebox.showerror(
                    "Record Not Found",
                    "The selected medical record could not be found."
                )
                return

            record_window = tk.Toplevel(
                profile_window
            )

            record_window.title(
                f"Medical Record - {record[0]}"
            )

            record_window.geometry(
                "650x600"
            )

            record_window.configure(
                bg=self.BACKGROUND
            )

            # ==============================================
            # HEADER
            # ==============================================

            header = tk.Frame(
                record_window,
                bg=self.PRIMARY,
                height=75
            )

            header.pack(
                fill="x"
            )

            header.pack_propagate(
                False
            )

            tk.Label(
                header,
                text="Medical Record",
                font=("Segoe UI", 20, "bold"),
                bg=self.PRIMARY,
                fg=self.WHITE
            ).pack(
                side="left",
                padx=25
            )

            tk.Label(
                header,
                text=record[0],
                font=("Segoe UI", 10, "bold"),
                bg=self.PRIMARY,
                fg=self.WHITE
            ).pack(
                side="right",
                padx=25
            )

            # ==============================================
            # RECORD INFORMATION
            # ==============================================

            details_frame = tk.LabelFrame(
                record_window,
                text="  Clinical Information  ",
                font=("Segoe UI", 11, "bold"),
                bg=self.WHITE,
                fg=self.DARK,
                padx=20,
                pady=15
            )

            details_frame.pack(
                fill="both",
                expand=True,
                padx=20,
                pady=20
            )

            details = [

                ("Record ID", record[0]),
                ("Patient ID", record[1]),
                ("Visit Date", record[2]),
                ("Doctor", record[6]),
                ("Diagnosis", record[4]),
                ("Treatment", record[5]),
                ("Symptoms", record[3]),
                ("Notes", record[7]),
                ("Created At", record[8])

            ]

            for index, (label, value) in enumerate(details):

                tk.Label(
                    details_frame,
                    text=label,
                    font=("Segoe UI", 9, "bold"),
                    bg=self.WHITE,
                    fg=self.GRAY
                ).grid(
                    row=index,
                    column=0,
                    sticky="nw",
                    padx=10,
                    pady=7
                )

                tk.Label(
                    details_frame,
                    text=value if value else "N/A",
                    font=("Segoe UI", 10),
                    bg=self.WHITE,
                    fg=self.DARK,
                    wraplength=400,
                    justify="left"
                ).grid(
                    row=index,
                    column=1,
                    sticky="nw",
                    padx=10,
                    pady=7
                )

            details_frame.grid_columnconfigure(
                1,
                weight=1
            )

            # ==============================================
            # CLOSE BUTTON
            # ==============================================

            tk.Button(
                record_window,
                text="Close",
                font=("Segoe UI", 10, "bold"),
                bg=self.GRAY,
                fg=self.WHITE,
                activebackground=self.GRAY,
                activeforeground=self.WHITE,
                relief="flat",
                padx=25,
                pady=8,
                command=record_window.destroy
            ).pack(
                side="right",
                padx=20,
                pady=(0, 20)
            )

        # --------------------------------------------------
        # Double-click medical record
        # --------------------------------------------------

        medical_table.bind(
            "<Double-1>",
            show_medical_record
        )    

        # ==================================================
        # APPOINTMENT HISTORY
        # ==================================================

        appointment_frame = tk.LabelFrame(
            content,
            text="  Appointment History  ",
            font=("Segoe UI", 11, "bold"),
            bg=self.WHITE,
            fg=self.DARK,
            padx=15,
            pady=15
        )

        appointment_frame.pack(
            fill="both",
            expand=True,
            pady=(0, 15)
        )

        appointment_columns = (
            "appointment_id",
            "date",
            "time",
            "doctor",
            "reason",
            "status"
        )

        appointment_table = ttk.Treeview(
            appointment_frame,
            columns=appointment_columns,
            show="headings",
            height=7
        )

        appointment_table.heading(
            "appointment_id",
            text="Appointment ID"
        )

        appointment_table.heading(
            "date",
            text="Date"
        )

        appointment_table.heading(
            "time",
            text="Time"
        )

        appointment_table.heading(
            "doctor",
            text="Doctor"
        )

        appointment_table.heading(
            "reason",
            text="Reason"
        )

        appointment_table.heading(
            "status",
            text="Status"
        )

        appointment_table.column(
            "appointment_id",
            width=120
        )

        appointment_table.column(
            "date",
            width=100
        )

        appointment_table.column(
            "time",
            width=80
        )

        appointment_table.column(
            "doctor",
            width=150
        )

        appointment_table.column(
            "reason",
            width=180
        )

        appointment_table.column(
            "status",
            width=100
        )

        appointment_scrollbar = ttk.Scrollbar(
            appointment_frame,
            orient="vertical",
            command=appointment_table.yview
        )

        appointment_table.configure(
            yscrollcommand=appointment_scrollbar.set
        )

        appointment_table.pack(
            side="left",
            fill="both",
            expand=True
        )

        appointment_scrollbar.pack(
            side="right",
            fill="y"
        )

        # --------------------------------------------------
        # Load patient's appointments
        # --------------------------------------------------

        patient_appointments = (
            self.db.get_patient_appointments(
                patient_id
            )
        )

        for appointment in patient_appointments:

            appointment_id = appointment[0]
            appointment_date = appointment[3]
            appointment_time = appointment[4]
            doctor_id = appointment[2]
            reason = appointment[5]
            status = appointment[6]

            # ----------------------------------------------
            # Get doctor's name
            # ----------------------------------------------

            doctor = self.db.get_doctor(
                doctor_id
            )

            if doctor:

                doctor_name = doctor[1]

            else:

                doctor_name = doctor_id

            appointment_table.insert(
                "",
                "end",
                values=(
                    appointment_id,
                    appointment_date,
                    appointment_time,
                    doctor_name,
                    reason,
                    status
                )
            )

        # --------------------------------------------------
        # Empty appointment history message
        # --------------------------------------------------

        if not patient_appointments:

            tk.Label(
                appointment_frame,
                text="No appointment history found for this patient.",
                font=("Segoe UI", 10),
                bg=self.WHITE,
                fg=self.GRAY
            ).pack(
                pady=10
            )

                # --------------------------------------------------
        # Appointment details
        # --------------------------------------------------

        def show_appointment_details(event=None):

            selected_appointment = appointment_table.selection()

            if not selected_appointment:
                return

            appointment_values = appointment_table.item(
                selected_appointment[0],
                "values"
            )

            appointment_id = appointment_values[0]

            appointment = self.db.get_appointment(
                appointment_id
            )

            if not appointment:
                messagebox.showerror(
                    "Appointment Not Found",
                    "The selected appointment could not be found."
                )
                return

            appointment_window = tk.Toplevel(
                profile_window
            )

            appointment_window.title(
                f"Appointment - {appointment[0]}"
            )

            appointment_window.geometry(
                "650x550"
            )

            appointment_window.configure(
                bg=self.BACKGROUND
            )

            # ==============================================
            # HEADER
            # ==============================================

            header = tk.Frame(
                appointment_window,
                bg=self.PRIMARY,
                height=75
            )

            header.pack(
                fill="x"
            )

            header.pack_propagate(
                False
            )

            tk.Label(
                header,
                text="Appointment Details",
                font=("Segoe UI", 20, "bold"),
                bg=self.PRIMARY,
                fg=self.WHITE
            ).pack(
                side="left",
                padx=25
            )

            tk.Label(
                header,
                text=appointment[0],
                font=("Segoe UI", 10, "bold"),
                bg=self.PRIMARY,
                fg=self.WHITE
            ).pack(
                side="right",
                padx=25
            )

            # ==============================================
            # APPOINTMENT INFORMATION
            # ==============================================

            details_frame = tk.LabelFrame(
                appointment_window,
                text="  Appointment Information  ",
                font=("Segoe UI", 11, "bold"),
                bg=self.WHITE,
                fg=self.DARK,
                padx=20,
                pady=15
            )

            details_frame.pack(
                fill="both",
                expand=True,
                padx=20,
                pady=20
            )

            doctor = self.db.get_doctor(
                appointment[2]
            )

            if doctor:

                doctor_name = doctor[1]

            else:

                doctor_name = appointment[2]

            details = [

                ("Appointment ID", appointment[0]),
                ("Patient ID", appointment[1]),
                ("Doctor", doctor_name),
                ("Appointment Date", appointment[3]),
                ("Appointment Time", appointment[4]),
                ("Reason", appointment[5]),
                ("Status", appointment[6]),
                ("Notes", appointment[7]),
                ("Created At", appointment[8])

            ]

            for index, (label, value) in enumerate(details):

                tk.Label(
                    details_frame,
                    text=label,
                    font=("Segoe UI", 9, "bold"),
                    bg=self.WHITE,
                    fg=self.GRAY
                ).grid(
                    row=index,
                    column=0,
                    sticky="nw",
                    padx=10,
                    pady=7
                )

                tk.Label(
                    details_frame,
                    text=value if value else "N/A",
                    font=("Segoe UI", 10),
                    bg=self.WHITE,
                    fg=self.DARK,
                    wraplength=400,
                    justify="left"
                ).grid(
                    row=index,
                    column=1,
                    sticky="nw",
                    padx=10,
                    pady=7
                )

            details_frame.grid_columnconfigure(
                1,
                weight=1
            )

            # ==============================================
            # CLOSE BUTTON
            # ==============================================

            tk.Button(
                appointment_window,
                text="Close",
                font=("Segoe UI", 10, "bold"),
                bg=self.GRAY,
                fg=self.WHITE,
                activebackground=self.GRAY,
                activeforeground=self.WHITE,
                relief="flat",
                padx=25,
                pady=8,
                command=appointment_window.destroy
            ).pack(
                side="right",
                padx=20,
                pady=(0, 20)
            )

        # --------------------------------------------------
        # Double-click appointment
        # --------------------------------------------------

        appointment_table.bind(
            "<Double-1>",
            show_appointment_details
        )        

        # ==================================================
        # CLOSE BUTTON
        # ==================================================

        button_frame = tk.Frame(
            profile_window,
            bg=self.BACKGROUND
        )

        button_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        tk.Button(
            button_frame,
            text="Close",
            font=("Segoe UI", 10, "bold"),
            bg=self.GRAY,
            fg=self.WHITE,
            activebackground=self.GRAY,
            activeforeground=self.WHITE,
            relief="flat",
            padx=25,
            pady=8,
            command=profile_window.destroy
        ).pack(
            side="right"
    )
    # ======================================================
    # EDIT PATIENT
    # ======================================================

    def edit_patient(self):

        # --------------------------------------------------
        # Check whether a patient was selected
        # --------------------------------------------------

        selected = self.patient_table.selection()

        if not selected:

            messagebox.showwarning(
                "No Patient Selected",
                "Please select a patient from the table first."
            )

            return

        # --------------------------------------------------
        # Get selected patient ID
        # --------------------------------------------------

        values = self.patient_table.item(
            selected[0],
            "values"
        )

        patient_id = values[0]

        # --------------------------------------------------
        # Find complete patient record
        # --------------------------------------------------

        patients = self.db.get_all_patients()

        patient = None

        for record in patients:

            if record[0] == patient_id:

                patient = record

                break

        if patient is None:

            messagebox.showerror(
                "Patient Not Found",
                "The selected patient could not be found."
            )

            return

        # --------------------------------------------------
        # EDIT WINDOW
        # --------------------------------------------------

        edit_window = tk.Toplevel(
            self.window
        )

        edit_window.title(
            f"Edit Patient - {patient_id}"
        )

        edit_window.geometry(
            "600x600"
        )

        edit_window.configure(
            bg=self.BACKGROUND
        )

        edit_window.resizable(
            False,
            False
        )

        # --------------------------------------------------
        # HEADER
        # --------------------------------------------------

        header = tk.Frame(
            edit_window,
            bg=self.PRIMARY,
            height=85
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        tk.Label(
            header,
            text="Edit Patient",
            font=("Segoe UI", 22, "bold"),
            bg=self.PRIMARY,
            fg=self.WHITE
        ).pack(
            anchor="w",
            padx=25,
            pady=(15, 0)
        )

        tk.Label(
            header,
            text=f"Patient ID: {patient_id}",
            font=("Segoe UI", 10),
            bg=self.PRIMARY,
            fg=self.WHITE
        ).pack(
            anchor="w",
            padx=27
        )

        # --------------------------------------------------
        # FORM
        # --------------------------------------------------

        form = tk.Frame(
            edit_window,
            bg=self.WHITE,
            padx=30,
            pady=25
        )

        form.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # --------------------------------------------------
        # NAME
        # --------------------------------------------------

        tk.Label(
            form,
            text="Full Name",
            bg=self.WHITE,
            fg=self.DARK,
            font=("Segoe UI", 10, "bold")
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=10,
            pady=10
        )

        name_entry = ttk.Entry(
            form,
            width=35
        )

        name_entry.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        name_entry.insert(
            0,
            patient[1]
        )

        # --------------------------------------------------
        # GENDER
        # --------------------------------------------------

        tk.Label(
            form,
            text="Gender",
            bg=self.WHITE,
            fg=self.DARK,
            font=("Segoe UI", 10, "bold")
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=10,
            pady=10
        )

        gender_combo = ttk.Combobox(
            form,
            values=[
                "Male",
                "Female"
            ],
            state="readonly",
            width=32
        )

        gender_combo.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        gender_combo.set(
            patient[2]
        )

        # --------------------------------------------------
        # DATE OF BIRTH
        # --------------------------------------------------

        tk.Label(
            form,
            text="Date of Birth",
            bg=self.WHITE,
            fg=self.DARK,
            font=("Segoe UI", 10, "bold")
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=10,
            pady=10
        )

        dob_entry = ttk.Entry(
            form,
            width=35
        )

        dob_entry.grid(
            row=2,
            column=1,
            padx=10,
            pady=10
        )

        dob_entry.insert(
            0,
            patient[3]
        )

        # --------------------------------------------------
        # PHONE
        # --------------------------------------------------

        tk.Label(
            form,
            text="Phone Number",
            bg=self.WHITE,
            fg=self.DARK,
            font=("Segoe UI", 10, "bold")
        ).grid(
            row=3,
            column=0,
            sticky="w",
            padx=10,
            pady=10
        )

        phone_entry = ttk.Entry(
            form,
            width=35
        )

        phone_entry.grid(
            row=3,
            column=1,
            padx=10,
            pady=10
        )

        phone_entry.insert(
            0,
            patient[4]
        )

        # --------------------------------------------------
        # ADDRESS
        # --------------------------------------------------

        tk.Label(
            form,
            text="Address",
            bg=self.WHITE,
            fg=self.DARK,
            font=("Segoe UI", 10, "bold")
        ).grid(
            row=4,
            column=0,
            sticky="w",
            padx=10,
            pady=10
        )

        address_entry = ttk.Entry(
            form,
            width=35
        )

        address_entry.grid(
            row=4,
            column=1,
            padx=10,
            pady=10
        )

        address_entry.insert(
            0,
            patient[5]
        )

        # --------------------------------------------------
        # BLOOD GROUP
        # --------------------------------------------------

        tk.Label(
            form,
            text="Blood Group",
            bg=self.WHITE,
            fg=self.DARK,
            font=("Segoe UI", 10, "bold")
        ).grid(
            row=5,
            column=0,
            sticky="w",
            padx=10,
            pady=10
        )

        blood_combo = ttk.Combobox(
            form,
            values=[
                "A+",
                "A-",
                "B+",
                "B-",
                "AB+",
                "AB-",
                "O+",
                "O-"
            ],
            state="readonly",
            width=32
        )

        blood_combo.grid(
            row=5,
            column=1,
            padx=10,
            pady=10
        )

        blood_combo.set(
            patient[6]
        )

        # --------------------------------------------------
        # EMERGENCY CONTACT
        # --------------------------------------------------

        tk.Label(
            form,
            text="Emergency Contact",
            bg=self.WHITE,
            fg=self.DARK,
            font=("Segoe UI", 10, "bold")
        ).grid(
            row=6,
            column=0,
            sticky="w",
            padx=10,
            pady=10
        )

        emergency_entry = ttk.Entry(
            form,
            width=35
        )

        emergency_entry.grid(
            row=6,
            column=1,
            padx=10,
            pady=10
        )

        emergency_entry.insert(
            0,
            patient[7]
        )

        # ==================================================
        # UPDATE FUNCTION
        # ==================================================

        def update_patient():

            name = name_entry.get().strip()
            gender = gender_combo.get()
            dob = dob_entry.get().strip()
            phone = phone_entry.get().strip()
            address = address_entry.get().strip()
            blood = blood_combo.get()
            emergency = emergency_entry.get().strip()

            # ----------------------------------------------
            # Validation
            # ----------------------------------------------

            if not all([
                name,
                gender,
                dob,
                phone,
                address,
                blood,
                emergency
            ]):

                messagebox.showerror(
                    "Missing Information",
                    "Please complete all patient fields.",
                    parent=edit_window
                )

                return

            # ----------------------------------------------
            # Update database
            # ----------------------------------------------

            updated = self.db.update_patient(
                patient_id,
                name,
                gender,
                dob,
                phone,
                address,
                blood,
                emergency
            )

            if not updated:

                messagebox.showerror(
                    "Update Error",
                    "The patient record could not be updated.",
                    parent=edit_window
                )

                return

            # ----------------------------------------------
            # Success
            # ----------------------------------------------

            messagebox.showinfo(
                "Patient Updated",
                f"Patient {patient_id} was updated successfully.",
                parent=edit_window
            )

            edit_window.destroy()

            # Refresh table
            self.display_patients()

        # ==================================================
        # BUTTONS
        # ==================================================

        tk.Button(
            form,
            text="Update Patient",
            command=update_patient,
            bg=self.PRIMARY,
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=8
        ).grid(
            row=7,
            column=0,
            padx=10,
            pady=20
        )

        tk.Button(
            form,
            text="Cancel",
            command=edit_window.destroy,
            bg=self.GRAY,
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=8
        ).grid(
            row=7,
            column=1,
            padx=10,
            pady=20
        ) 
            # ======================================================
    # ARCHIVE SELECTED PATIENT
    # ======================================================

    def archive_selected_patient(self):

        selected = self.patient_table.selection()

        if not selected:

            messagebox.showwarning(
                "No Patient Selected",
                "Please select a patient from the table first."
            )

            return

        values = self.patient_table.item(
            selected[0],
            "values"
        )

        patient_id = values[0]
        patient_name = values[1]
        current_status = values[7]

        # --------------------------------------------------
        # Check current status
        # --------------------------------------------------

        if current_status == "Archived":

            messagebox.showinfo(
                "Already Archived",
                f"{patient_name} is already archived."
            )

            return

        # --------------------------------------------------
        # Confirmation
        # --------------------------------------------------

        confirm = messagebox.askyesno(
            "Archive Patient",
            f"Are you sure you want to archive\n\n"
            f"Patient: {patient_name}\n"
            f"Patient ID: {patient_id}?"
        )

        if not confirm:

            return

        # --------------------------------------------------
        # Archive patient
        # --------------------------------------------------

        archived = self.db.archive_patient(
            patient_id
        )

        if not archived:

            messagebox.showerror(
                "Archive Error",
                "The patient could not be archived."
            )

            return

        # --------------------------------------------------
        # Success
        # --------------------------------------------------

        messagebox.showinfo(
            "Patient Archived",
            f"{patient_name} has been archived successfully."
        )

        # Refresh table
        self.display_patients()
            # ======================================================
    # RESTORE SELECTED PATIENT
    # ======================================================

    def restore_selected_patient(self):

        selected = self.patient_table.selection()

        if not selected:

            messagebox.showwarning(
                "No Patient Selected",
                "Please select a patient from the table first."
            )

            return

        values = self.patient_table.item(
            selected[0],
            "values"
        )

        patient_id = values[0]
        patient_name = values[1]
        current_status = values[7]

        # --------------------------------------------------
        # Check current status
        # --------------------------------------------------

        if current_status == "Active":

            messagebox.showinfo(
                "Already Active",
                f"{patient_name} is already active."
            )

            return

        # --------------------------------------------------
        # Confirmation
        # --------------------------------------------------

        confirm = messagebox.askyesno(
            "Restore Patient",
            f"Do you want to restore\n\n"
            f"Patient: {patient_name}\n"
            f"Patient ID: {patient_id}?"
        )

        if not confirm:

            return

        # --------------------------------------------------
        # Restore patient
        # --------------------------------------------------

        restored = self.db.restore_patient(
            patient_id
        )

        if not restored:

            messagebox.showerror(
                "Restore Error",
                "The patient could not be restored."
            )

            return

        # --------------------------------------------------
        # Success
        # --------------------------------------------------

        messagebox.showinfo(
            "Patient Restored",
            f"{patient_name} has been restored successfully."
        )

        # Refresh table
        self.display_patients()          