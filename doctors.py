import tkinter as tk
from tkinter import ttk, messagebox

from database import Database


class DoctorsWindow:

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
        self.WARNING = "#EF6C00"
        self.LIGHT_BLUE = "#E3F2FD"

        # ==================================================
        # DATABASE
        # ==================================================

        self.db = Database()

        # ==================================================
        # WINDOW
        # ==================================================

        self.window = tk.Toplevel(parent)

        self.window.title(
            "MedCare HMS - Doctors"
        )

        self.window.geometry(
            "1200x750"
        )

        self.window.minsize(
            1050,
            650
        )

        self.window.configure(
            bg=self.BACKGROUND
        )

        # ==================================================
        # CREATE INTERFACE
        # ==================================================

        self.create_interface()

        # Load doctors
        self.load_doctors()

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
            text="Doctors Management",
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
            text="Register and manage medical staff",
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
        # DOCTOR FORM
        # ==================================================

        form_frame = tk.LabelFrame(
            main_frame,
            text="  Doctor Information  ",
            bg=self.WHITE,
            fg=self.DARK,
            font=("Segoe UI", 11, "bold"),
            padx=20,
            pady=15
        )

        form_frame.pack(
            fill="x"
        )

        # ==================================================
        # FULL NAME
        # ==================================================

        tk.Label(
            form_frame,
            text="Full Name *",
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

        tk.Label(
            form_frame,
            text="Gender *",
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

        self.gender_combo = ttk.Combobox(
            form_frame,
            values=[
                "Male",
                "Female"
            ],
            state="readonly",
            width=27
        )

        self.gender_combo.grid(
            row=0,
            column=3,
            padx=10,
            pady=8
        )

        # ==================================================
        # SPECIALIZATION
        # ==================================================

        tk.Label(
            form_frame,
            text="Specialization *",
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

        self.specialization_combo = ttk.Combobox(
            form_frame,
            values=[
                "General Practitioner",
                "Cardiologist",
                "Dermatologist",
                "Pediatrician",
                "Gynecologist",
                "Neurologist",
                "Orthopedic",
                "Psychiatrist",
                "Surgeon",
                "Dentist",
                "Radiologist",
                "Oncologist",
                "Ophthalmologist",
                "Urologist",
                "ENT Specialist",
                "Other"
            ],
            state="readonly",
            width=27
        )

        self.specialization_combo.grid(
            row=1,
            column=1,
            padx=10,
            pady=8
        )

        # ==================================================
        # PHONE
        # ==================================================

        tk.Label(
            form_frame,
            text="Phone *",
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

        self.phone_entry = ttk.Entry(
            form_frame,
            width=30
        )

        self.phone_entry.grid(
            row=1,
            column=3,
            padx=10,
            pady=8
        )

        # ==================================================
        # EMAIL
        # ==================================================

        tk.Label(
            form_frame,
            text="Email",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=10,
            pady=8
        )

        self.email_entry = ttk.Entry(
            form_frame,
            width=30
        )

        self.email_entry.grid(
            row=2,
            column=1,
            padx=10,
            pady=8
        )

        # ==================================================
        # ADDRESS
        # ==================================================

        tk.Label(
            form_frame,
            text="Address *",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).grid(
            row=2,
            column=2,
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
            column=3,
            padx=10,
            pady=8
        )

        # ==================================================
        # LICENSE NUMBER
        # ==================================================

        tk.Label(
            form_frame,
            text="License Number *",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).grid(
            row=3,
            column=0,
            sticky="w",
            padx=10,
            pady=8
        )

        self.license_entry = ttk.Entry(
            form_frame,
            width=30
        )

        self.license_entry.grid(
            row=3,
            column=1,
            padx=10,
            pady=8
        )

        # ==================================================
        # BUTTONS
        # ==================================================

        button_frame = tk.Frame(
            form_frame,
            bg=self.WHITE
        )

        button_frame.grid(
            row=3,
            column=2,
            columnspan=2,
            padx=10,
            pady=8,
            sticky="e"
        )

        self.add_button = tk.Button(
            button_frame,
            text="Register Doctor",
            command=self.add_doctor,
            bg=self.PRIMARY,
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=8
        )

        self.add_button.pack(
            side="left",
            padx=5
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
            padx=15,
            pady=8
        ).pack(
            side="left",
            padx=5
        )

        # ==================================================
        # SEARCH / FILTER AREA
        # ==================================================

        search_frame = tk.Frame(
            main_frame,
            bg=self.WHITE,
            padx=15,
            pady=12
        )

        search_frame.pack(
            fill="x",
            pady=(15, 10)
        )

        tk.Label(
            search_frame,
            text="Search Doctor:",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).pack(
            side="left",
            padx=(5, 10)
        )

        self.search_entry = ttk.Entry(
            search_frame,
            width=40
        )

        self.search_entry.pack(
            side="left",
            padx=5
        )

        self.search_entry.bind(
            "<Return>",
            lambda event: self.search_doctors()
        )

        tk.Button(
            search_frame,
            text="Search",
            command=self.search_doctors,
            bg=self.PRIMARY,
            fg=self.WHITE,
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=6
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            search_frame,
            text="Show All",
            command=self.load_doctors,
            bg=self.GRAY,
            fg=self.WHITE,
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=6
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            search_frame,
            text="Active Only",
            command=self.load_active_doctors,
            bg=self.SUCCESS,
            fg=self.WHITE,
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=6
        ).pack(
            side="left",
            padx=5
        )

        # ==================================================
        # DOCTORS TABLE
        # ==================================================

        table_frame = tk.LabelFrame(
            main_frame,
            text="  Registered Doctors  ",
            bg=self.WHITE,
            fg=self.DARK,
            font=("Segoe UI", 11, "bold")
        )

        table_frame.pack(
            fill="both",
            expand=True
        )

        columns = (
            "doctor_id",
            "name",
            "gender",
            "specialization",
            "phone",
            "email",
            "license",
            "status"
        )

        self.doctors_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            selectmode="browse"
        )

        # ==================================================
        # HEADINGS
        # ==================================================

        self.doctors_table.heading(
            "doctor_id",
            text="Doctor ID"
        )

        self.doctors_table.heading(
            "name",
            text="Full Name"
        )

        self.doctors_table.heading(
            "gender",
            text="Gender"
        )

        self.doctors_table.heading(
            "specialization",
            text="Specialization"
        )

        self.doctors_table.heading(
            "phone",
            text="Phone"
        )

        self.doctors_table.heading(
            "email",
            text="Email"
        )

        self.doctors_table.heading(
            "license",
            text="License No."
        )

        self.doctors_table.heading(
            "status",
            text="Status"
        )

        # ==================================================
        # COLUMN WIDTHS
        # ==================================================

        self.doctors_table.column(
            "doctor_id",
            width=110,
            anchor="center"
        )

        self.doctors_table.column(
            "name",
            width=180
        )

        self.doctors_table.column(
            "gender",
            width=80,
            anchor="center"
        )

        self.doctors_table.column(
            "specialization",
            width=170
        )

        self.doctors_table.column(
            "phone",
            width=130
        )

        self.doctors_table.column(
            "email",
            width=190
        )

        self.doctors_table.column(
            "license",
            width=130
        )

        self.doctors_table.column(
            "status",
            width=90,
            anchor="center"
        )

        # ==================================================
        # SCROLLBARS
        # ==================================================

        vertical_scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.doctors_table.yview
        )

        horizontal_scrollbar = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=self.doctors_table.xview
        )

        self.doctors_table.configure(
            yscrollcommand=vertical_scrollbar.set,
            xscrollcommand=horizontal_scrollbar.set
        )

        self.doctors_table.pack(
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

        # ==================================================
        # TABLE DOUBLE CLICK
        # ==================================================

        self.doctors_table.bind(
            "<Double-1>",
            self.load_selected_doctor
        )

        # ==================================================
        # ACTION BUTTONS
        # ==================================================

        action_frame = tk.Frame(
            main_frame,
            bg=self.BACKGROUND
        )

        action_frame.pack(
            pady=12
        )

        tk.Button(
            action_frame,
            text="Edit Selected Doctor",
            command=self.edit_selected_doctor,
            bg=self.WARNING,
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=8
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            action_frame,
            text="Deactivate Doctor",
            command=self.deactivate_selected_doctor,
            bg=self.DANGER,
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=8
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            action_frame,
            text="Activate Doctor",
            command=self.activate_selected_doctor,
            bg=self.SUCCESS,
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=8
        ).pack(
            side="left",
            padx=5
        )

    # ======================================================
    # LOAD ALL DOCTORS
    # ======================================================

    def load_doctors(self):

        self.clear_table()

        doctors = self.db.get_all_doctors()

        for doctor in doctors:

            self.doctors_table.insert(
                "",
                "end",
                values=(
                    doctor[0],
                    doctor[1],
                    doctor[2],
                    doctor[3],
                    doctor[4],
                    doctor[5],
                    doctor[7],
                    doctor[8]
                )
            )

    # ======================================================
    # LOAD ACTIVE DOCTORS
    # ======================================================

    def load_active_doctors(self):

        self.clear_table()

        doctors = self.db.get_active_doctors()

        for doctor in doctors:

            self.doctors_table.insert(
                "",
                "end",
                values=(
                    doctor[0],
                    doctor[1],
                    doctor[2],
                    doctor[3],
                    doctor[4],
                    doctor[5],
                    doctor[7],
                    doctor[8]
                )
            )

    # ======================================================
    # SEARCH DOCTORS
    # ======================================================

    def search_doctors(self):

        search_term = (
            self.search_entry
            .get()
            .strip()
        )

        if not search_term:

            self.load_doctors()

            return

        self.clear_table()

        doctors = self.db.search_doctors(
            search_term
        )

        for doctor in doctors:

            self.doctors_table.insert(
                "",
                "end",
                values=(
                    doctor[0],
                    doctor[1],
                    doctor[2],
                    doctor[3],
                    doctor[4],
                    doctor[5],
                    doctor[7],
                    doctor[8]
                )
            )

        if not doctors:

            messagebox.showinfo(
                "Search Results",
                "No doctors matching your search were found."
            )

    # ======================================================
    # CLEAR TABLE
    # ======================================================

    def clear_table(self):

        for item in self.doctors_table.get_children():

            self.doctors_table.delete(
                item
            )

    # ======================================================
    # ADD DOCTOR
    # ======================================================

    def add_doctor(self):

        full_name = (
            self.name_entry
            .get()
            .strip()
        )

        gender = (
            self.gender_combo
            .get()
            .strip()
        )

        specialization = (
            self.specialization_combo
            .get()
            .strip()
        )

        phone = (
            self.phone_entry
            .get()
            .strip()
        )

        email = (
            self.email_entry
            .get()
            .strip()
        )

        address = (
            self.address_entry
            .get()
            .strip()
        )

        license_number = (
            self.license_entry
            .get()
            .strip()
        )

        # ==================================================
        # VALIDATION
        # ==================================================

        if not all([
            full_name,
            gender,
            specialization,
            phone,
            address,
            license_number
        ]):

            messagebox.showerror(
                "Missing Information",
                "Please complete all required fields."
            )

            return

        # ==================================================
        # CHECK LICENSE NUMBER
        # ==================================================

        existing_doctors = (
            self.db.search_doctors(
                license_number
            )
        )

        for doctor in existing_doctors:

            if doctor[7].lower() == license_number.lower():

                messagebox.showerror(
                    "Duplicate License",
                    "A doctor with this license number already exists."
                )

                return

        # ==================================================
        # GENERATE DOCTOR ID
        # ==================================================

        doctors = self.db.get_all_doctors()

        doctor_number = len(doctors) + 1

        doctor_id = (
            f"DOC-{doctor_number:04d}"
        )

        # ==================================================
        # SAVE DOCTOR
        # ==================================================

        saved = self.db.add_doctor(
            doctor_id,
            full_name,
            gender,
            specialization,
            phone,
            email,
            address,
            license_number
        )

        if not saved:
            messagebox.showerror(
                "Save Error",
                "The doctor could not be registered.\n\n"
                "The Doctor ID or License Number may already exist."
            )

            return

        # ==================================================
        # DATABASE DIAGNOSTIC
        # ==================================================

        print("DOCTOR SAVED:", saved)

        saved_doctors = self.db.get_all_doctors()

        print(
            "TOTAL DOCTORS IN DATABASE:",
            len(saved_doctors)
        )

        for doctor in saved_doctors:
            print(
                "DOCTOR RECORD:",
                doctor
            )

        messagebox.showinfo(
            "Doctor Registered",
            f"Doctor registered successfully.\n\n"
            f"Doctor ID: {doctor_id}"
        )

        self.clear_form()

        self.load_doctors()
    # ======================================================
    # GET SELECTED DOCTOR
    # ======================================================

    def get_selected_doctor_id(self):

        selected = (
            self.doctors_table.selection()
        )

        if not selected:

            messagebox.showwarning(
                "No Selection",
                "Please select a doctor from the table."
            )

            return None

        item = selected[0]

        values = (
            self.doctors_table.item(
                item,
                "values"
            )
        )

        return values[0]

    # ======================================================
    # LOAD SELECTED DOCTOR
    # ======================================================

    def load_selected_doctor(self, event=None):

        doctor_id = self.get_selected_doctor_id()

        if not doctor_id:
            return

        doctor = self.db.get_doctor(
            doctor_id
        )

        if not doctor:
            return

        self.name_entry.delete(
            0,
            tk.END
        )

        self.name_entry.insert(
            0,
            doctor[1]
        )

        self.gender_combo.set(
            doctor[2]
        )

        self.specialization_combo.set(
            doctor[3]
        )

        self.phone_entry.delete(
            0,
            tk.END
        )

        self.phone_entry.insert(
            0,
            doctor[4]
        )

        self.email_entry.delete(
            0,
            tk.END
        )

        self.email_entry.insert(
            0,
            doctor[5]
        )

        self.address_entry.delete(
            0,
            tk.END
        )

        self.address_entry.insert(
            0,
            doctor[6]
        )

        self.license_entry.delete(
            0,
            tk.END
        )

        self.license_entry.insert(
            0,
            doctor[7]
        )

    # ======================================================
    # EDIT SELECTED DOCTOR
    # ======================================================

    def edit_selected_doctor(self):

        doctor_id = self.get_selected_doctor_id()

        if not doctor_id:
            return

        full_name = (
            self.name_entry
            .get()
            .strip()
        )

        gender = (
            self.gender_combo
            .get()
            .strip()
        )

        specialization = (
            self.specialization_combo
            .get()
            .strip()
        )

        phone = (
            self.phone_entry
            .get()
            .strip()
        )

        email = (
            self.email_entry
            .get()
            .strip()
        )

        address = (
            self.address_entry
            .get()
            .strip()
        )

        license_number = (
            self.license_entry
            .get()
            .strip()
        )

        if not all([
            full_name,
            gender,
            specialization,
            phone,
            address,
            license_number
        ]):

            messagebox.showerror(
                "Missing Information",
                "Please complete all required fields."
            )

            return

        confirmation = messagebox.askyesno(
            "Confirm Update",
            f"Update information for Doctor {doctor_id}?"
        )

        if not confirmation:
            return

        updated = self.db.update_doctor(
            doctor_id,
            full_name,
            gender,
            specialization,
            phone,
            email,
            address,
            license_number
        )

        if not updated:

            messagebox.showerror(
                "Update Error",
                "Doctor information could not be updated."
            )

            return

        messagebox.showinfo(
            "Doctor Updated",
            "Doctor information updated successfully."
        )

        self.clear_form()

        self.load_doctors()

    # ======================================================
    # DEACTIVATE DOCTOR
    # ======================================================

    def deactivate_selected_doctor(self):

        doctor_id = self.get_selected_doctor_id()

        if not doctor_id:
            return

        doctor = self.db.get_doctor(
            doctor_id
        )

        if not doctor:
            return

        if doctor[8] == "Inactive":

            messagebox.showinfo(
                "Already Inactive",
                "This doctor is already inactive."
            )

            return

        confirmation = messagebox.askyesno(
            "Confirm Deactivation",
            f"Deactivate Doctor {doctor_id}?\n\n"
            f"Doctor: {doctor[1]}"
        )

        if not confirmation:
            return

        deactivated = (
            self.db.deactivate_doctor(
                doctor_id
            )
        )

        if deactivated:

            messagebox.showinfo(
                "Doctor Deactivated",
                "The doctor has been successfully deactivated."
            )

            self.load_doctors()

        else:

            messagebox.showerror(
                "Error",
                "The doctor could not be deactivated."
            )

    # ======================================================
    # ACTIVATE DOCTOR
    # ======================================================

    def activate_selected_doctor(self):

        doctor_id = self.get_selected_doctor_id()

        if not doctor_id:
            return

        doctor = self.db.get_doctor(
            doctor_id
        )

        if not doctor:
            return

        if doctor[8] == "Active":

            messagebox.showinfo(
                "Already Active",
                "This doctor is already active."
            )

            return

        confirmation = messagebox.askyesno(
            "Confirm Activation",
            f"Activate Doctor {doctor_id}?\n\n"
            f"Doctor: {doctor[1]}"
        )

        if not confirmation:
            return

        activated = (
            self.db.activate_doctor(
                doctor_id
            )
        )

        if activated:

            messagebox.showinfo(
                "Doctor Activated",
                "The doctor has been successfully activated."
            )

            self.load_doctors()

        else:

            messagebox.showerror(
                "Error",
                "The doctor could not be activated."
            )

    # ======================================================
    # CLEAR FORM
    # ======================================================

    def clear_form(self):

        self.name_entry.delete(
            0,
            tk.END
        )

        self.gender_combo.set("")

        self.specialization_combo.set("")

        self.phone_entry.delete(
            0,
            tk.END
        )

        self.email_entry.delete(
            0,
            tk.END
        )

        self.address_entry.delete(
            0,
            tk.END
        )

        self.license_entry.delete(
            0,
            tk.END
        )