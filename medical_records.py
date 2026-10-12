import tkinter as tk
from tkinter import ttk, messagebox

from database import Database

class MedicalRecordsWindow:

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
            "MedCare HMS - Medical Records"
        )

        self.window.geometry(
            "1150x750"
        )

        self.window.minsize(
            1000,
            650
        )

        self.window.configure(
            bg=self.BACKGROUND
        )

        # ==================================================
        # CREATE INTERFACE
        # ==================================================

        self.create_interface()

        # Load patients
        self.load_patients()

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

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        tk.Label(
            header,
            text="Medical Records",
            font=("Segoe UI", 22, "bold"),
            bg=self.PRIMARY,
            fg=self.WHITE
        ).pack(
            side="left",
            padx=30,
            pady=20
        )

        tk.Label(
            header,
            text="Record and manage patient medical history",
            font=("Segoe UI", 10),
            bg=self.PRIMARY,
            fg=self.WHITE
        ).pack(
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
        # PATIENT SELECTION
        # ==================================================

        patient_frame = tk.LabelFrame(
            main_frame,
            text="  Patient Selection  ",
            bg=self.WHITE,
            fg=self.DARK,
            font=("Segoe UI", 11, "bold"),
            padx=20,
            pady=15
        )

        patient_frame.pack(
            fill="x"
        )

        tk.Label(
            patient_frame,
            text="Patient",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=10,
            pady=8
        )

        self.patient_combo = ttk.Combobox(
            patient_frame,
            state="readonly",
            width=45
        )

        self.patient_combo.grid(
            row=0,
            column=1,
            padx=10,
            pady=8
        )

        self.patient_combo.bind(
            "<<ComboboxSelected>>",
            self.patient_selected
        )

        self.patient_info_label = tk.Label(
            patient_frame,
            text="No patient selected",
            font=("Segoe UI", 10),
            bg=self.WHITE,
            fg=self.GRAY
        )

        self.patient_info_label.grid(
            row=0,
            column=2,
            padx=20,
            pady=8,
            sticky="w"
        )

        # ==================================================
        # MEDICAL RECORD FORM
        # ==================================================

        form_frame = tk.LabelFrame(
            main_frame,
            text="  New Medical Record  ",
            bg=self.WHITE,
            fg=self.DARK,
            font=("Segoe UI", 11, "bold"),
            padx=20,
            pady=15
        )

        form_frame.pack(
            fill="x",
            pady=(15, 0)
        )

        # ==================================================
        # VISIT DATE
        # ==================================================

        tk.Label(
            form_frame,
            text="Visit Date",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=10,
            pady=8
        )

        self.visit_date_entry = ttk.Entry(
            form_frame,
            width=25
        )

        self.visit_date_entry.grid(
            row=0,
            column=1,
            padx=10,
            pady=8
        )

        # ==================================================
        # DOCTOR
        # ==================================================

        tk.Label(
            form_frame,
            text="Doctor",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).grid(
            row=0,
            column=2,
            sticky="w",
            padx=10,
            pady=8
        )

        self.doctor_entry = ttk.Entry(
            form_frame,
            width=30
        )

        self.doctor_entry.grid(
            row=0,
            column=3,
            padx=10,
            pady=8
        )

        # ==================================================
        # SYMPTOMS
        # ==================================================

        tk.Label(
            form_frame,
            text="Symptoms",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).grid(
            row=1,
            column=0,
            sticky="nw",
            padx=10,
            pady=8
        )

        self.symptoms_text = tk.Text(
            form_frame,
            width=35,
            height=4,
            font=("Segoe UI", 10),
            relief="solid",
            borderwidth=1
        )

        self.symptoms_text.grid(
            row=1,
            column=1,
            padx=10,
            pady=8
        )

        # ==================================================
        # DIAGNOSIS
        # ==================================================

        tk.Label(
            form_frame,
            text="Diagnosis",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).grid(
            row=1,
            column=2,
            sticky="nw",
            padx=10,
            pady=8
        )

        self.diagnosis_text = tk.Text(
            form_frame,
            width=35,
            height=4,
            font=("Segoe UI", 10),
            relief="solid",
            borderwidth=1
        )

        self.diagnosis_text.grid(
            row=1,
            column=3,
            padx=10,
            pady=8
        )

        # ==================================================
        # TREATMENT
        # ==================================================

        tk.Label(
            form_frame,
            text="Treatment",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).grid(
            row=2,
            column=0,
            sticky="nw",
            padx=10,
            pady=8
        )

        self.treatment_text = tk.Text(
            form_frame,
            width=35,
            height=4,
            font=("Segoe UI", 10),
            relief="solid",
            borderwidth=1
        )

        self.treatment_text.grid(
            row=2,
            column=1,
            padx=10,
            pady=8
        )

        # ==================================================
        # NOTES
        # ==================================================

        tk.Label(
            form_frame,
            text="Notes",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).grid(
            row=2,
            column=2,
            sticky="nw",
            padx=10,
            pady=8
        )

        self.notes_text = tk.Text(
            form_frame,
            width=35,
            height=4,
            font=("Segoe UI", 10),
            relief="solid",
            borderwidth=1
        )

        self.notes_text.grid(
            row=2,
            column=3,
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

        button_frame.pack(
            pady=15
        )

        tk.Button(
            button_frame,
            text="Add Medical Record",
            command=self.add_record,
            bg=self.PRIMARY,
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=18,
            pady=8
        ).grid(
            row=0,
            column=0,
            padx=8
        )

        tk.Button(
            button_frame,
            text="Clear Form",
            command=self.clear_form,
            bg=self.GRAY,
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=18,
            pady=8
        ).grid(
            row=0,
            column=1,
            padx=8
        )

        tk.Button(
            button_frame,
            text="Refresh History",
            command=self.load_medical_history,
            bg=self.SUCCESS,
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=18,
            pady=8
        ).grid(
            row=0,
            column=2,
            padx=8
        )

        tk.Button(
            button_frame,
            text="View Record",
            command=self.view_record,
            bg=self.SUCCESS,
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=18,
            pady=8
        ).grid(
            row=0,
            column=3,
            padx=8
        )
        tk.Button(
            button_frame,
            text="Edit Record",
            command=self.edit_record,
            bg="#EF6C00",
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=18,
            pady=8
        ).grid(
            row=0,
            column=4,
            padx=8
        )

        # ==================================================
        # MEDICAL HISTORY TABLE
        # ==================================================

        history_frame = tk.LabelFrame(
            main_frame,
            text="  Medical History  ",
            bg=self.WHITE,
            fg=self.DARK,
            font=("Segoe UI", 11, "bold")
        )

        history_frame.pack(
            fill="both",
            expand=True
        )

        columns = (
            "record_id",
            "date",
            "symptoms",
            "diagnosis",
            "treatment",
            "doctor",
            "notes"
        )

        self.records_table = ttk.Treeview(
            history_frame,
            columns=columns,
            show="headings"
        )

        # ==================================================
        # HEADINGS
        # ==================================================

        self.records_table.heading(
            "record_id",
            text="Record ID"
        )

        self.records_table.heading(
            "date",
            text="Visit Date"
        )

        self.records_table.heading(
            "symptoms",
            text="Symptoms"
        )

        self.records_table.heading(
            "diagnosis",
            text="Diagnosis"
        )

        self.records_table.heading(
            "treatment",
            text="Treatment"
        )

        self.records_table.heading(
            "doctor",
            text="Doctor"
        )

        self.records_table.heading(
            "notes",
            text="Notes"
        )

        # ==================================================
        # COLUMN WIDTHS
        # ==================================================

        self.records_table.column(
            "record_id",
            width=100
        )

        self.records_table.column(
            "date",
            width=100
        )

        self.records_table.column(
            "symptoms",
            width=180
        )

        self.records_table.column(
            "diagnosis",
            width=180
        )

        self.records_table.column(
            "treatment",
            width=180
        )

        self.records_table.column(
            "doctor",
            width=140
        )

        self.records_table.column(
            "notes",
            width=180
        )

        # ==================================================
        # SCROLLBARS
        # ==================================================

        vertical_scrollbar = ttk.Scrollbar(
            history_frame,
            orient="vertical",
            command=self.records_table.yview
        )

        horizontal_scrollbar = ttk.Scrollbar(
            history_frame,
            orient="horizontal",
            command=self.records_table.xview
        )

        self.records_table.configure(
            yscrollcommand=vertical_scrollbar.set,
            xscrollcommand=horizontal_scrollbar.set
        )

        self.records_table.pack(
            side="top",
            fill="both",
            expand=True
        )

        horizontal_scrollbar.pack(
            side="bottom",
            fill="x"
        )

        vertical_scrollbar.pack(
            side="right",
            fill="y"
        )

    # ======================================================
    # LOAD PATIENTS
    # ======================================================

    def load_patients(self):

        patients = self.db.get_all_patients()

        self.patient_lookup = {}

        patient_options = []

        for patient in patients:

            patient_id = patient[0]
            patient_name = patient[1]

            display_text = (
                f"{patient_id} - {patient_name}"
            )

            patient_options.append(
                display_text
            )

            self.patient_lookup[
                display_text
            ] = patient_id

        self.patient_combo["values"] = patient_options

    # ======================================================
    # PATIENT SELECTED
    # ======================================================

    def patient_selected(self, event=None):

        selected = self.patient_combo.get()

        if not selected:
            return

        patient_id = self.patient_lookup.get(
            selected
        )

        if not patient_id:
            return

        patient = self.db.get_patient(
            patient_id
        )

        if patient:

            self.patient_info_label.config(
                text=(
                    f"Patient ID: {patient[0]}    |    "
                    f"Gender: {patient[2]}    |    "
                    f"Blood Group: {patient[6]}"
                )
            )

        self.load_medical_history()

    # ======================================================
    # ADD MEDICAL RECORD
    # ======================================================

    def add_record(self):

        selected = self.patient_combo.get()

        if not selected:

            messagebox.showwarning(
                "No Patient Selected",
                "Please select a patient first."
            )

            return

        patient_id = self.patient_lookup.get(
            selected
        )

        visit_date = (
            self.visit_date_entry
            .get()
            .strip()
        )

        symptoms = (
            self.symptoms_text
            .get("1.0", tk.END)
            .strip()
        )

        diagnosis = (
            self.diagnosis_text
            .get("1.0", tk.END)
            .strip()
        )

        treatment = (
            self.treatment_text
            .get("1.0", tk.END)
            .strip()
        )

        doctor = (
            self.doctor_entry
            .get()
            .strip()
        )

        notes = (
            self.notes_text
            .get("1.0", tk.END)
            .strip()
        )

        # ==================================================
        # VALIDATION
        # ==================================================

        if not all([
            visit_date,
            symptoms,
            diagnosis,
            treatment,
            doctor
        ]):

            messagebox.showerror(
                "Missing Information",
                "Please complete the required medical record fields."
            )

            return

        # ==================================================
        # GENERATE RECORD ID
        # ==================================================

        existing_records = (
            self.db.get_patient_medical_records(
                patient_id
            )
        )

        record_number = len(
            existing_records
        ) + 1

        record_id = (
            f"REC-{patient_id.replace('PAT-', '')}"
            f"-{record_number:03d}"
        )

        # ==================================================
        # SAVE RECORD
        # ==================================================

        saved = self.db.add_medical_record(
            record_id,
            patient_id,
            visit_date,
            symptoms,
            diagnosis,
            treatment,
            doctor,
            notes
        )

        if not saved:

            messagebox.showerror(
                "Save Error",
                "The medical record could not be saved."
            )

            return

        messagebox.showinfo(
            "Record Saved",
            f"Medical record saved successfully.\n\n"
            f"Record ID: {record_id}"
        )

        self.clear_form()

        self.load_medical_history()

    # ======================================================
    # LOAD MEDICAL HISTORY
    # ======================================================

    def load_medical_history(self):

        for item in self.records_table.get_children():

            self.records_table.delete(
                item
            )

        selected = self.patient_combo.get()

        if not selected:
            return

        patient_id = self.patient_lookup.get(
            selected
        )

        if not patient_id:
            return

        records = (
            self.db.get_patient_medical_records(
                patient_id
            )
        )

        for record in records:

            self.records_table.insert(
                "",
                "end",
                values=(
                    record[0],
                    record[2],
                    record[3],
                    record[4],
                    record[5],
                    record[6],
                    record[7]
                )
            )

    # ======================================================
    # CLEAR FORM
    # ======================================================

    def clear_form(self):

        self.visit_date_entry.delete(
            0,
            tk.END
        )

        self.symptoms_text.delete(
            "1.0",
            tk.END
        )

        self.diagnosis_text.delete(
            "1.0",
            tk.END
        )

        self.treatment_text.delete(
            "1.0",
            tk.END
        )

        self.doctor_entry.delete(
            0,
            tk.END
        )

        self.notes_text.delete(
            "1.0",
            tk.END
        )
        # ======================================================
    # VIEW MEDICAL RECORD
    # ======================================================

    def view_record(self):

        selected = self.records_table.selection()

        if not selected:

            messagebox.showwarning(
                "No Record Selected",
                "Please select a medical record from the table first."
            )

            return

        # --------------------------------------------------
        # Get selected record
        # --------------------------------------------------

        values = self.records_table.item(
            selected[0],
            "values"
        )

        record_id = values[0]

        # --------------------------------------------------
        # Get patient
        # --------------------------------------------------

        patient_selection = self.patient_combo.get()

        if not patient_selection:
            return

        patient_id = self.patient_lookup.get(
            patient_selection
        )

        if not patient_id:
            return

        # --------------------------------------------------
        # Find complete record
        # --------------------------------------------------

        records = self.db.get_patient_medical_records(
            patient_id
        )

        record = None

        for item in records:

            if item[0] == record_id:

                record = item

                break

        if record is None:

            messagebox.showerror(
                "Record Not Found",
                "The selected medical record could not be found."
            )

            return

        # ==================================================
        # RECORD PROFILE WINDOW
        # ==================================================

        profile_window = tk.Toplevel(
            self.window
        )

        profile_window.title(
            f"Medical Record - {record_id}"
        )

        profile_window.geometry(
            "700x650"
        )

        profile_window.configure(
            bg=self.BACKGROUND
        )

        profile_window.resizable(
            False,
            False
        )

        # ==================================================
        # HEADER
        # ==================================================

        header = tk.Frame(
            profile_window,
            bg=self.PRIMARY,
            height=95
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        tk.Label(
            header,
            text="Medical Record",
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
            text=f"Record ID: {record_id}",
            font=("Segoe UI", 10),
            bg=self.PRIMARY,
            fg=self.WHITE
        ).pack(
            anchor="w",
            padx=27
        )

        # ==================================================
        # INFORMATION FRAME
        # ==================================================

        info_frame = tk.Frame(
            profile_window,
            bg=self.WHITE,
            padx=30,
            pady=25
        )

        info_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # ==================================================
        # RECORD INFORMATION
        # ==================================================

        information = [
            ("Record ID", record[0]),
            ("Patient ID", record[1]),
            ("Visit Date", record[2]),
            ("Symptoms", record[3]),
            ("Diagnosis", record[4]),
            ("Treatment", record[5]),
            ("Doctor", record[6]),
            ("Notes", record[7])
        ]

        for row, (label, value) in enumerate(information):

            tk.Label(
                info_frame,
                text=f"{label}:",
                font=("Segoe UI", 10, "bold"),
                bg=self.WHITE,
                fg=self.DARK
            ).grid(
                row=row,
                column=0,
                sticky="nw",
                padx=10,
                pady=8
            )

            tk.Label(
                info_frame,
                text=value if value else "N/A",
                font=("Segoe UI", 10),
                bg=self.WHITE,
                fg=self.DARK,
                wraplength=450,
                justify="left"
            ).grid(
                row=row,
                column=1,
                sticky="nw",
                padx=20,
                pady=8
            )

        # ==================================================
        # CLOSE BUTTON
        # ==================================================

        tk.Button(
            info_frame,
            text="Close",
            command=profile_window.destroy,
            bg=self.GRAY,
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=25,
            pady=8
        ).grid(
            row=len(information),
            column=0,
            columnspan=2,
            pady=20
        )
            # ======================================================
    # EDIT MEDICAL RECORD
    # ======================================================

    def edit_record(self):

        selected = self.records_table.selection()

        if not selected:

            messagebox.showwarning(
                "No Record Selected",
                "Please select a medical record from the table first."
            )

            return

        # --------------------------------------------------
        # Get selected record ID
        # --------------------------------------------------

        values = self.records_table.item(
            selected[0],
            "values"
        )

        record_id = values[0]

        # --------------------------------------------------
        # Get selected patient
        # --------------------------------------------------

        patient_selection = self.patient_combo.get()

        if not patient_selection:

            messagebox.showwarning(
                "No Patient Selected",
                "Please select a patient first."
            )

            return

        patient_id = self.patient_lookup.get(
            patient_selection
        )

        if not patient_id:
            return

        # --------------------------------------------------
        # Find complete record
        # --------------------------------------------------

        records = self.db.get_patient_medical_records(
            patient_id
        )

        record = None

        for item in records:

            if item[0] == record_id:

                record = item
                break

        if record is None:

            messagebox.showerror(
                "Record Not Found",
                "The selected medical record could not be found."
            )

            return

        # ==================================================
        # EDIT WINDOW
        # ==================================================

        edit_window = tk.Toplevel(
            self.window
        )

        edit_window.title(
            f"Edit Medical Record - {record_id}"
        )

        edit_window.geometry(
            "700x700"
        )

        edit_window.configure(
            bg=self.BACKGROUND
        )

        edit_window.resizable(
            False,
            False
        )

        # ==================================================
        # HEADER
        # ==================================================

        header = tk.Frame(
            edit_window,
            bg=self.PRIMARY,
            height=95
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        tk.Label(
            header,
            text="Edit Medical Record",
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
            text=f"Record ID: {record_id}",
            font=("Segoe UI", 10),
            bg=self.PRIMARY,
            fg=self.WHITE
        ).pack(
            anchor="w",
            padx=27
        )

        # ==================================================
        # FORM
        # ==================================================

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

        # ==================================================
        # VISIT DATE
        # ==================================================

        tk.Label(
            form,
            text="Visit Date",
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

        visit_date_entry = ttk.Entry(
            form,
            width=40
        )

        visit_date_entry.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        visit_date_entry.insert(
            0,
            record[2]
        )

        # ==================================================
        # DOCTOR
        # ==================================================

        tk.Label(
            form,
            text="Doctor",
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

        doctor_entry = ttk.Entry(
            form,
            width=40
        )

        doctor_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        doctor_entry.insert(
            0,
            record[6]
        )

        # ==================================================
        # SYMPTOMS
        # ==================================================

        tk.Label(
            form,
            text="Symptoms",
            bg=self.WHITE,
            fg=self.DARK,
            font=("Segoe UI", 10, "bold")
        ).grid(
            row=2,
            column=0,
            sticky="nw",
            padx=10,
            pady=10
        )

        symptoms_text = tk.Text(
            form,
            width=40,
            height=5,
            font=("Segoe UI", 10),
            relief="solid",
            borderwidth=1
        )

        symptoms_text.grid(
            row=2,
            column=1,
            padx=10,
            pady=10
        )

        symptoms_text.insert(
            "1.0",
            record[3]
        )

        # ==================================================
        # DIAGNOSIS
        # ==================================================

        tk.Label(
            form,
            text="Diagnosis",
            bg=self.WHITE,
            fg=self.DARK,
            font=("Segoe UI", 10, "bold")
        ).grid(
            row=3,
            column=0,
            sticky="nw",
            padx=10,
            pady=10
        )

        diagnosis_text = tk.Text(
            form,
            width=40,
            height=5,
            font=("Segoe UI", 10),
            relief="solid",
            borderwidth=1
        )

        diagnosis_text.grid(
            row=3,
            column=1,
            padx=10,
            pady=10
        )

        diagnosis_text.insert(
            "1.0",
            record[4]
        )

        # ==================================================
        # TREATMENT
        # ==================================================

        tk.Label(
            form,
            text="Treatment",
            bg=self.WHITE,
            fg=self.DARK,
            font=("Segoe UI", 10, "bold")
        ).grid(
            row=4,
            column=0,
            sticky="nw",
            padx=10,
            pady=10
        )

        treatment_text = tk.Text(
            form,
            width=40,
            height=5,
            font=("Segoe UI", 10),
            relief="solid",
            borderwidth=1
        )

        treatment_text.grid(
            row=4,
            column=1,
            padx=10,
            pady=10
        )

        treatment_text.insert(
            "1.0",
            record[5]
        )

        # ==================================================
        # NOTES
        # ==================================================

        tk.Label(
            form,
            text="Notes",
            bg=self.WHITE,
            fg=self.DARK,
            font=("Segoe UI", 10, "bold")
        ).grid(
            row=5,
            column=0,
            sticky="nw",
            padx=10,
            pady=10
        )

        notes_text = tk.Text(
            form,
            width=40,
            height=5,
            font=("Segoe UI", 10),
            relief="solid",
            borderwidth=1
        )

        notes_text.grid(
            row=5,
            column=1,
            padx=10,
            pady=10
        )

        notes_text.insert(
            "1.0",
            record[7]
        )

        # ==================================================
        # UPDATE FUNCTION
        # ==================================================

        def update_record():

            visit_date = (
                visit_date_entry
                .get()
                .strip()
            )

            doctor = (
                doctor_entry
                .get()
                .strip()
            )

            symptoms = (
                symptoms_text
                .get("1.0", tk.END)
                .strip()
            )

            diagnosis = (
                diagnosis_text
                .get("1.0", tk.END)
                .strip()
            )

            treatment = (
                treatment_text
                .get("1.0", tk.END)
                .strip()
            )

            notes = (
                notes_text
                .get("1.0", tk.END)
                .strip()
            )

            # ----------------------------------------------
            # Validation
            # ----------------------------------------------

            if not all([
                visit_date,
                doctor,
                symptoms,
                diagnosis,
                treatment
            ]):

                messagebox.showerror(
                    "Missing Information",
                    "Please complete all required fields.",
                    parent=edit_window
                )

                return

            # ----------------------------------------------
            # Update database
            # ----------------------------------------------

            updated = self.db.update_medical_record(
                record_id,
                visit_date,
                symptoms,
                diagnosis,
                treatment,
                doctor,
                notes
            )

            if not updated:

                messagebox.showerror(
                    "Update Error",
                    "The medical record could not be updated.",
                    parent=edit_window
                )

                return

            # ----------------------------------------------
            # Success
            # ----------------------------------------------

            messagebox.showinfo(
                "Record Updated",
                f"Medical record {record_id} "
                f"was updated successfully.",
                parent=edit_window
            )

            edit_window.destroy()

            self.load_medical_history()

        # ==================================================
        # BUTTONS
        # ==================================================

        tk.Button(
            form,
            text="Update Record",
            command=update_record,
            bg=self.PRIMARY,
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=8
        ).grid(
            row=6,
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
            row=6,
            column=1,
            padx=10,
            pady=20
        )

# ============================================================
# CONSULTATION / CLINICAL ENTRY WINDOW
# ============================================================

class ConsultationWindow:

    def __init__(
    self,
    parent,
    appointment_id,
    patient_id,
    doctor_id,
    visit_date,
    appointments_window=None
):

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
        # CONSULTATION CONTEXT
        # ==================================================

        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.visit_date = visit_date
        self.appointments_window = appointments_window

        # ==================================================
        # GET PATIENT INFORMATION
        # ==================================================

        patient = self.db.get_patient(
            patient_id
        )

        if patient:
            self.patient_name = patient[1]
            self.patient_gender = patient[2]
            self.patient_blood_group = patient[6]
        else:
            self.patient_name = "Unknown Patient"
            self.patient_gender = ""
            self.patient_blood_group = ""

        # ==================================================
        # GET DOCTOR INFORMATION
        # ==================================================

        doctor = self.db.get_doctor(
            doctor_id
        )

        if doctor:
            self.doctor_name = doctor[1]
            self.doctor_specialization = doctor[4]
        else:
            self.doctor_name = "Unknown Doctor"
            self.doctor_specialization = ""

        # ==================================================
        # WINDOW
        # ==================================================

        self.window = tk.Toplevel(
            parent
        )

        self.window.title(
            "MedCare HMS - Clinical Consultation"
        )

        self.window.geometry(
            "1000x700"
        )

        self.window.minsize(
            900,
            650
        )

        self.window.configure(
            bg=self.BACKGROUND
        )

        # ==================================================
        # CREATE INTERFACE
        # ==================================================

        self.create_interface()

    # ======================================================
    # CREATE INTERFACE
    # ======================================================

    def create_interface(self):

        # ==================================================
        # HEADER
        # ==================================================

        header = tk.Frame(
            self.window,
            bg=self.PRIMARY,
            height=90
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(
            False
        )

        tk.Label(
            header,
            text="Clinical Consultation",
            font=("Segoe UI", 22, "bold"),
            bg=self.PRIMARY,
            fg=self.WHITE
        ).pack(
            side="left",
            padx=30,
            pady=20
        )

        tk.Label(
            header,
            text="Clinical assessment and consultation entry",
            font=("Segoe UI", 10),
            bg=self.PRIMARY,
            fg=self.WHITE
        ).pack(
            side="right",
            padx=30
        )

        # ==================================================
        # MAIN CONTAINER
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
        # APPOINTMENT INFORMATION
        # ==================================================

        appointment_frame = tk.LabelFrame(
            main_frame,
            text="  Consultation Information  ",
            bg=self.WHITE,
            fg=self.DARK,
            font=("Segoe UI", 11, "bold"),
            padx=20,
            pady=15
        )

        appointment_frame.pack(
            fill="x"
        )

        # --------------------------------------------------
        # APPOINTMENT ID
        # --------------------------------------------------

        tk.Label(
            appointment_frame,
            text="Appointment ID",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=10,
            pady=8
        )

        self.appointment_id_entry = ttk.Entry(
            appointment_frame,
            width=30
        )

        self.appointment_id_entry.grid(
            row=0,
            column=1,
            padx=10,
            pady=8
        )

        self.appointment_id_entry.insert(
            0,
            self.appointment_id
        )

        self.appointment_id_entry.config(
            state="readonly"
        )

        # --------------------------------------------------
        # VISIT DATE
        # --------------------------------------------------

        tk.Label(
            appointment_frame,
            text="Visit Date",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).grid(
            row=0,
            column=2,
            sticky="w",
            padx=10,
            pady=8
        )

        self.visit_date_entry = ttk.Entry(
            appointment_frame,
            width=25
        )

        self.visit_date_entry.grid(
            row=0,
            column=3,
            padx=10,
            pady=8
        )

        self.visit_date_entry.insert(
            0,
            self.visit_date
        )

        self.visit_date_entry.config(
            state="readonly"
        )

        # --------------------------------------------------
        # PATIENT
        # --------------------------------------------------

        tk.Label(
            appointment_frame,
            text="Patient",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=10,
            pady=8
        )

        self.patient_entry = ttk.Entry(
            appointment_frame,
            width=30
        )

        self.patient_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=8
        )

        self.patient_entry.insert(
            0,
            f"{self.patient_id} - {self.patient_name}"
        )

        self.patient_entry.config(
            state="readonly"
        )

        # --------------------------------------------------
        # DOCTOR
        # --------------------------------------------------

        tk.Label(
            appointment_frame,
            text="Doctor",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).grid(
            row=1,
            column=2,
            sticky="w",
            padx=10,
            pady=8
        )

        self.doctor_entry = ttk.Entry(
            appointment_frame,
            width=30
        )

        self.doctor_entry.grid(
            row=1,
            column=3,
            padx=10,
            pady=8
        )

        self.doctor_entry.insert(
            0,
            f"{self.doctor_id} - {self.doctor_name}"
        )

        self.doctor_entry.config(
            state="readonly"
        )

        # ==================================================
        # CLINICAL ENTRY FORM
        # ==================================================

        form_frame = tk.LabelFrame(
            main_frame,
            text="  Clinical Assessment  ",
            bg=self.WHITE,
            fg=self.DARK,
            font=("Segoe UI", 11, "bold"),
            padx=20,
            pady=15
        )

        form_frame.pack(
            fill="both",
            expand=True,
            pady=(15, 0)
        )

        # ==================================================
        # SYMPTOMS
        # ==================================================

        tk.Label(
            form_frame,
            text="Symptoms",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).grid(
            row=0,
            column=0,
            sticky="nw",
            padx=10,
            pady=8
        )

        self.symptoms_text = tk.Text(
            form_frame,
            width=38,
            height=5,
            font=("Segoe UI", 10),
            relief="solid",
            borderwidth=1
        )

        self.symptoms_text.grid(
            row=0,
            column=1,
            padx=10,
            pady=8
        )

        # ==================================================
        # DIAGNOSIS
        # ==================================================

        tk.Label(
            form_frame,
            text="Diagnosis",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).grid(
            row=0,
            column=2,
            sticky="nw",
            padx=10,
            pady=8
        )

        self.diagnosis_text = tk.Text(
            form_frame,
            width=38,
            height=5,
            font=("Segoe UI", 10),
            relief="solid",
            borderwidth=1
        )

        self.diagnosis_text.grid(
            row=0,
            column=3,
            padx=10,
            pady=8
        )

        # ==================================================
        # TREATMENT
        # ==================================================

        tk.Label(
            form_frame,
            text="Treatment",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).grid(
            row=1,
            column=0,
            sticky="nw",
            padx=10,
            pady=8
        )

        self.treatment_text = tk.Text(
            form_frame,
            width=38,
            height=5,
            font=("Segoe UI", 10),
            relief="solid",
            borderwidth=1
        )

        self.treatment_text.grid(
            row=1,
            column=1,
            padx=10,
            pady=8
        )

        # ==================================================
        # NOTES
        # ==================================================

        tk.Label(
            form_frame,
            text="Notes",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).grid(
            row=1,
            column=2,
            sticky="nw",
            padx=10,
            pady=8
        )

        self.notes_text = tk.Text(
            form_frame,
            width=38,
            height=5,
            font=("Segoe UI", 10),
            relief="solid",
            borderwidth=1
        )

        self.notes_text.grid(
            row=1,
            column=3,
            padx=10,
            pady=8
        )

        # ==================================================
        # PATIENT SUMMARY
        # ==================================================

        summary_text = (
            f"Patient ID: {self.patient_id}    |    "
            f"Gender: {self.patient_gender}    |    "
            f"Blood Group: {self.patient_blood_group}"
        )

        tk.Label(
            form_frame,
            text=summary_text,
            font=("Segoe UI", 9),
            bg=self.WHITE,
            fg=self.GRAY
        ).grid(
            row=2,
            column=0,
            columnspan=4,
            pady=10
        )

        # ==================================================
        # BUTTONS
        # ==================================================

        button_frame = tk.Frame(
            main_frame,
            bg=self.BACKGROUND
        )

        button_frame.pack(
            pady=15
        )

        # ==================================================
        # SAVE CONSULTATION
        # ==================================================

        tk.Button(
            button_frame,
            text="Save Consultation",
            command=self.save_consultation,
            bg=self.PRIMARY,
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=9
        ).pack(
            side="left",
            padx=8
        )

        tk.Button(
            button_frame,
            text="Close Consultation",
            command=self.window.destroy,
            bg=self.GRAY,
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=9
        ).pack(
            side="left",
            padx=8
        )

    # ======================================================
    # GET CONSULTATION DATA
    # ======================================================

    def get_consultation_data(self):

        return {
            "appointment_id": self.appointment_id,
            "patient_id": self.patient_id,
            "doctor_id": self.doctor_id,
            "visit_date": self.visit_date,
            "symptoms": self.symptoms_text.get(
                "1.0",
                tk.END
            ).strip(),
            "diagnosis": self.diagnosis_text.get(
                "1.0",
                tk.END
            ).strip(),
            "treatment": self.treatment_text.get(
                "1.0",
                tk.END
            ).strip(),
            "notes": self.notes_text.get(
                "1.0",
                tk.END
            ).strip()
        }
        # ======================================================
    # SAVE CONSULTATION
    # ======================================================

    def save_consultation(self):

        # --------------------------------------------------
        # Get clinical information
        # --------------------------------------------------

        symptoms = self.symptoms_text.get(
            "1.0",
            tk.END
        ).strip()

        diagnosis = self.diagnosis_text.get(
            "1.0",
            tk.END
        ).strip()

        treatment = self.treatment_text.get(
            "1.0",
            tk.END
        ).strip()

        notes = self.notes_text.get(
            "1.0",
            tk.END
        ).strip()

        # --------------------------------------------------
        # Validate required clinical information
        # --------------------------------------------------

        if not symptoms:

            messagebox.showwarning(
                "Missing Information",
                "Please enter the patient's symptoms."
            )

            return

        if not diagnosis:

            messagebox.showwarning(
                "Missing Information",
                "Please enter the diagnosis."
            )

            return

        if not treatment:

            messagebox.showwarning(
                "Missing Information",
                "Please enter the treatment."
            )

            return

        # --------------------------------------------------
        # Confirm saving
        # --------------------------------------------------

        confirm = messagebox.askyesno(
            "Save Consultation",
            "Are you sure you want to save this consultation?\n\n"
            f"Patient: {self.patient_name}\n"
            f"Doctor: {self.doctor_name}\n"
            f"Appointment: {self.appointment_id}"
        )

        if not confirm:
            return

        # --------------------------------------------------
        # Generate Medical Record ID
        # --------------------------------------------------

        existing_records = (
            self.db.get_patient_medical_records(
                self.patient_id
            )
        )

        record_number = (
            len(existing_records) + 1
        )

        record_id = (
            f"REC-{self.patient_id.replace('PAT-', '')}"
            f"-{record_number:03d}"
        )

        # --------------------------------------------------
        # Save Medical Record
        # --------------------------------------------------

        saved = self.db.add_medical_record(
            record_id,
            self.patient_id,
            self.visit_date,
            symptoms,
            diagnosis,
            treatment,
            self.doctor_name,
            notes
        )

        # --------------------------------------------------
        # Check save result
        # --------------------------------------------------

        if not saved:

            messagebox.showerror(
                "Save Error",
                "The consultation could not be saved.\n\n"
                "The appointment has not been completed."
            )

            return

        # --------------------------------------------------
        # Mark appointment as completed
        # --------------------------------------------------

        completed = self.db.complete_appointment(
            self.appointment_id
        )

        if not completed:

            messagebox.showerror(
                "Completion Error",
                "The consultation was saved, but the appointment "
                "could not be marked as completed."
            )

            return

        

        # --------------------------------------------------
        # REFRESH APPOINTMENTS
        # --------------------------------------------------

        if self.appointments_window:

            self.appointments_window.load_appointments()

        # --------------------------------------------------
        # REFRESH DASHBOARD
        # --------------------------------------------------

        if (
            self.appointments_window
            and self.appointments_window.dashboard
        ):

            self.appointments_window.dashboard.refresh_dashboard()
            
        # --------------------------------------------------
        # SUCCESS
        # --------------------------------------------------

        messagebox.showinfo(
            "Consultation Saved",
            "Consultation saved successfully.\n\n"
            "The appointment has been marked as completed."
        )

        self.window.destroy()