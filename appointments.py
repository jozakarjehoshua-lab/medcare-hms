import tkinter as tk
from tkinter import ttk, messagebox

from database import Database
from medical_records import ConsultationWindow
from datetime import datetime


class AppointmentsWindow:

    # ======================================================
    # INITIALIZATION
    # ======================================================

    def __init__(self, parent, dashboard=None):

        self.db = Database()
        self.dashboard = dashboard
        self.editing_appointment_id = None
        

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
        # WINDOW
        # ==================================================

        self.window = tk.Toplevel(parent)

        self.window.title(
            "MedCare HMS - Appointments"
        )

        self.window.geometry(
            "1250x780"
        )

        self.window.minsize(
            1100,
            680
        )

        self.window.configure(
            bg=self.BACKGROUND
        )

        # ==================================================
        # CREATE INTERFACE
        # ==================================================

        self.create_interface()

        self.load_appointments()
        # ======================================================
    # DATE VALIDATION
    # ======================================================

    def validate_date(self, date_text):
        """
        Validates appointment date using DD/MM/YYYY format.
        """

        try:
            datetime.strptime(date_text, "%d/%m/%Y")
            return True

        except ValueError:
            return False
        # ======================================================
    # TIME VALIDATION
    # ======================================================

    def validate_time(self, time_text):
        """
        Validates appointment time using HH:MM format.
        """

        try:
            datetime.strptime(time_text, "%H:%M")
            return True

        except ValueError:
            return False 
        # ======================================================
    # VALIDATE APPOINTMENT DATE AND TIME
    # ======================================================

    def validate_appointment_datetime(
        self,
        appointment_date,
        appointment_time
    ):
        """
        Checks whether the appointment date and time
        are valid and are not in the past.
        """

        try:

            appointment_datetime = datetime.strptime(
                f"{appointment_date} {appointment_time}",
                "%d/%m/%Y %H:%M"
            )

        except ValueError:

            return False

        current_datetime = datetime.now()

        if appointment_datetime < current_datetime:

            return False

        return True           

    # ======================================================
    # MAIN INTERFACE
    # ======================================================

    def create_interface(self):

        # ==================================================
        # HEADER
        # ==================================================

        header = tk.Frame(
            self.window,
            bg=self.WHITE,
            height=85
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="Appointment Management",
            font=("Segoe UI", 22, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        )

        title.pack(
            side="left",
            padx=30,
            pady=22
        )

        # ==================================================
        # MAIN CONTAINER
        # ==================================================

        main_container = tk.Frame(
            self.window,
            bg=self.BACKGROUND
        )

        main_container.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=20
        )

        # ==================================================
        # FORM
        # ==================================================

        form_frame = tk.LabelFrame(
            main_container,
            text=" Schedule Appointment ",
            font=("Segoe UI", 11, "bold"),
            bg=self.WHITE,
            fg=self.DARK,
            padx=20,
            pady=15
        )

        form_frame.pack(
            fill="x"
        )

        # ==================================================
        # PATIENT
        # ==================================================

        tk.Label(
            form_frame,
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
            form_frame,
            width=28,
            state="readonly"
        )

        self.patient_combo.grid(
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

        self.doctor_combo = ttk.Combobox(
            form_frame,
            width=28,
            state="readonly"
        )

        self.doctor_combo.grid(
            row=0,
            column=3,
            padx=10,
            pady=8
        )

        # ==================================================
        # DATE
        # ==================================================

        tk.Label(
            form_frame,
            text="Appointment Date",
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

        self.date_entry = tk.Entry(
            form_frame,
            width=30,
            font=("Segoe UI", 10)
        )

        self.date_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=8
        )

        self.date_entry.insert(
            0,
            "DD/MM/YYYY"
        )

        # ==================================================
        # TIME
        # ==================================================

        tk.Label(
            form_frame,
            text="Appointment Time",
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

        self.time_entry = tk.Entry(
            form_frame,
            width=30,
            font=("Segoe UI", 10)
        )

        self.time_entry.grid(
            row=1,
            column=3,
            padx=10,
            pady=8
        )

        self.time_entry.insert(
            0,
            "HH:MM"
        )

        # ==================================================
        # REASON
        # ==================================================

        tk.Label(
            form_frame,
            text="Reason for Visit",
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

        self.reason_entry = tk.Entry(
            form_frame,
            width=30,
            font=("Segoe UI", 10)
        )

        self.reason_entry.grid(
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
            sticky="w",
            padx=10,
            pady=8
        )

        self.notes_entry = tk.Entry(
            form_frame,
            width=30,
            font=("Segoe UI", 10)
        )

        self.notes_entry.grid(
            row=2,
            column=3,
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
            column=0,
            columnspan=4,
            pady=(15, 5)
        )

        self.register_button = tk.Button(
            button_frame,
            text="Register Appointment",
            command=self.register_appointment,
            bg=self.PRIMARY,
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=9
        )

        self.register_button.pack(
            side="left",
            padx=5
        )

        self.update_button = tk.Button(
    button_frame,
    text="Edit Selected",
    command=self.load_selected_appointment,
            bg=self.WARNING,
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=9
        )

        self.update_button.pack(
            side="left",
            padx=5
        )

        self.save_button = tk.Button(
            button_frame,
            text="Update Appointment",
            command=self.update_selected_appointment,
            bg="#1565C0",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=5
        )

        self.save_button.pack(
            side="left",
            padx=5
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
            padx=20,
            pady=9
        )

        clear_button.pack(
            side="left",
            padx=5
        )

        # ==================================================
        # LOAD PATIENTS / DOCTORS
        # ==================================================

        self.load_patients()

        self.load_doctors()

        # ==================================================
        # SEARCH
        # ==================================================

        search_frame = tk.Frame(
            main_container,
            bg=self.WHITE,
            padx=15,
            pady=12
        )

        search_frame.pack(
            fill="x",
            pady=20
        )

        tk.Label(
            search_frame,
            text="Search Appointment:",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).pack(
            side="left",
            padx=5
        )

        self.search_entry = tk.Entry(
            search_frame,
            width=35,
            font=("Segoe UI", 10)
        )

        self.search_entry.pack(
            side="left",
            padx=10
        )

        search_button = tk.Button(
            search_frame,
            text="Search",
            command=self.search_appointments,
            bg=self.PRIMARY,
            fg=self.WHITE,
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=6
        )

        search_button.pack(
            side="left",
            padx=5
        )

        show_all_button = tk.Button(
            search_frame,
            text="Show All",
            command=self.load_appointments,
            bg=self.GRAY,
            fg=self.WHITE,
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=6
        )

        show_all_button.pack(
            side="left",
            padx=5
        )

        todays_button = tk.Button(
            search_frame,
            text="Today's Appointments",
            command=self.load_todays_appointments,
            bg=self.SUCCESS,
            fg=self.WHITE,
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=6
        )

        todays_button.pack(
            side="left",
            padx=5
        )

        upcoming_button = tk.Button(
            search_frame,
            text="Upcoming Appointments",
            command=self.load_upcoming_appointments,
            bg=self.PRIMARY,
            fg=self.WHITE,
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=6
        )

        upcoming_button.pack(
            side="left",
            padx=5
        )
                # ==================================================
        # FILTERS
        # ==================================================

        filter_frame = tk.Frame(
            main_container,
            bg=self.WHITE,
            padx=15,
            pady=10
        )

        filter_frame.pack(
            fill="x",
            pady=(0, 10)
        )

        tk.Label(
            filter_frame,
            text="Filter:",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).pack(
            side="left",
            padx=5
        )

        # --------------------------------------------------
        # STATUS FILTER
        # --------------------------------------------------

        tk.Label(
            filter_frame,
            text="Status",
            font=("Segoe UI", 9, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).pack(
            side="left",
            padx=(15, 5)
        )

        self.status_filter = ttk.Combobox(
            filter_frame,
            width=15,
            state="readonly",
            values=(
                "All",
                "Scheduled",
                "Completed",
                "Cancelled"
            )
        )

        self.status_filter.pack(
            side="left",
            padx=5
        )

        self.status_filter.current(0)

        # --------------------------------------------------
        # DOCTOR FILTER
        # --------------------------------------------------

        tk.Label(
            filter_frame,
            text="Doctor",
            font=("Segoe UI", 9, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).pack(
            side="left",
            padx=(15, 5)
        )

        self.doctor_filter = ttk.Combobox(
            filter_frame,
            width=25,
            state="readonly"
        )

        self.doctor_filter.pack(
            side="left",
            padx=5
        )

        self.doctor_filter["values"] = (
            ["All"] +
            list(self.doctor_combo["values"])
        )

        self.doctor_filter.current(0)

        # --------------------------------------------------
        # DATE FILTER
        # --------------------------------------------------

        tk.Label(
            filter_frame,
            text="Date",
            font=("Segoe UI", 9, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).pack(
            side="left",
            padx=(15, 5)
        )

        self.date_filter = tk.Entry(
            filter_frame,
            width=15,
            font=("Segoe UI", 9)
        )

        self.date_filter.pack(
            side="left",
            padx=5
        )

        self.date_filter.insert(
            0,
            "DD/MM/YYYY"
        )

        # --------------------------------------------------
        # APPLY FILTER BUTTON
        # --------------------------------------------------

        apply_filter_button = tk.Button(
            filter_frame,
            text="Apply Filters",
            command=self.apply_appointment_filters,
            bg=self.PRIMARY,
            fg=self.WHITE,
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=6
        )

        apply_filter_button.pack(
            side="left",
            padx=5
        )

        # --------------------------------------------------
        # CLEAR FILTER BUTTON
        # --------------------------------------------------

        clear_filter_button = tk.Button(
            filter_frame,
            text="Clear Filters",
            command=self.clear_appointment_filters,
            bg=self.GRAY,
            fg=self.WHITE,
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=6
        )

        clear_filter_button.pack(
            side="left",
            padx=5
        )

        # ======================================================
        # APPOINTMENT TABLE
        # ======================================================

        table_frame = tk.Frame(
            self.window,
            bg=self.BACKGROUND
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.appointment_table = ttk.Treeview(
            table_frame,
            columns=(
                "appointment_id",
                "patient_id",
                "doctor_id",
                "date",
                "time",
                "reason",
                "status"
            ),
            show="headings"
        )
        self.appointment_table.heading(
            "appointment_id",
            text="Appointment ID"
        )

        self.appointment_table.heading(
            "patient_id",
            text="Patient ID"
        )

        self.appointment_table.heading(
            "doctor_id",
            text="Doctor ID"
        )

        self.appointment_table.heading(
            "date",
            text="Date"
        )

        self.appointment_table.heading(
            "time",
            text="Time"
        )

        self.appointment_table.heading(
            "reason",
            text="Reason"
        )

        self.appointment_table.heading(
            "status",
            text="Status"
        )

        self.appointment_table.column(
    "appointment_id",
    width=120
)

        self.appointment_table.column(
    "patient_id",
    width=100
)

        self.appointment_table.column(
    "doctor_id",
    width=100
)

        self.appointment_table.column(
    "date",
    width=100
)

        self.appointment_table.column(
    "time",
    width=80
)

        self.appointment_table.column(
    "reason",
    width=180
)

        self.appointment_table.column(
            "status",
            width=100
        )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.appointment_table.yview
        )

        self.appointment_table.configure(
            yscrollcommand=scrollbar.set
        )

        self.appointment_table.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.appointment_table.bind(
            "<Double-1>",
            lambda event: self.view_selected_appointment()
        )

        # ==================================================
        # ACTION BUTTONS
        # ==================================================

        action_frame = tk.Frame(
            main_container,
            bg=self.BACKGROUND
        )

        action_frame.pack(
            fill="x",
            pady=(15, 0)
        )

        view_button = tk.Button(
            action_frame,
            text="View Details",
            command=self.view_selected_appointment,
            bg=self.PRIMARY,
            fg=self.WHITE,
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=8
        )

        view_button.pack(
            side="left",
            padx=5
        )

        # ==================================================
        # START CONSULTATION BUTTON
        # ==================================================

        start_consultation_button = tk.Button(
            action_frame,
            text="Start Consultation",
            command=self.start_consultation,
            bg=self.SUCCESS,
            fg=self.WHITE,
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=8
        )

        start_consultation_button.pack(
            side="left",
            padx=5
        )

        cancel_button = tk.Button(
            action_frame,
            text="Cancel Appointment",
            command=self.cancel_selected_appointment,
            bg=self.DANGER,
            fg=self.WHITE,
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=8
        )

        cancel_button.pack(
            side="left",
            padx=5
        )

        complete_button = tk.Button(
            action_frame,
            text="Mark Completed",
            command=self.complete_selected_appointment,
            bg=self.SUCCESS,
            fg=self.WHITE,
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=8
        )

        complete_button.pack(
            side="left",
            padx=5
        )

        restore_button = tk.Button(
            action_frame,
            text="Restore",
            command=self.restore_selected_appointment,
            bg=self.WARNING,
            fg=self.WHITE,
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=8
        )

        restore_button.pack(
            side="left",
            padx=5
        )

        # ==================================================
        # DOUBLE CLICK
        # ==================================================

        self.appointment_table.bind(
            "<Double-1>",
            lambda event: self.view_selected_appointment()
        )

    # ======================================================
    # LOAD PATIENTS
    # ======================================================

    def load_patients(self):

        patients = self.db.get_active_patients()

        patient_values = []

        for patient in patients:

            patient_values.append(
                f"{patient[0]} - {patient[1]}"
            )

        self.patient_combo["values"] = patient_values

        if patient_values:

            self.patient_combo.current(0)

    # ======================================================
    # LOAD DOCTORS
    # ======================================================

    def load_doctors(self):

        doctors = self.db.get_active_doctors()

        doctor_values = []

        for doctor in doctors:

            doctor_values.append(
                f"{doctor[0]} - {doctor[1]} ({doctor[3]})"
            )

        self.doctor_combo["values"] = doctor_values

        if doctor_values:

            self.doctor_combo.current(0)

    # ======================================================
    # REFRESH DASHBOARD
    # ======================================================

    def refresh_dashboard(self):

        if self.dashboard is not None:

            self.dashboard.refresh_dashboard()    

    # ======================================================
    # REGISTER APPOINTMENT
    # ======================================================

    def register_appointment(self):

        patient = self.patient_combo.get().strip()
        doctor = self.doctor_combo.get().strip()

        appointment_date = self.date_entry.get().strip()
        appointment_time = self.time_entry.get().strip()
        reason = self.reason_entry.get().strip()
        notes = self.notes_entry.get().strip()

        if not patient:

            messagebox.showwarning(
                "Missing Patient",
                "Please select a patient."
            )

            return

        if not doctor:

            messagebox.showwarning(
                "Missing Doctor",
                "Please select a doctor."
            )

            return

        if not appointment_date or appointment_date == "DD/MM/YYYY":

            messagebox.showwarning(
                "Invalid Date",
                "Please enter the appointment date."
            )

            return

        if not appointment_time or appointment_time == "HH:MM":

            messagebox.showwarning(
                "Invalid Time",
                "Please enter the appointment time."
            )

            return
                # --------------------------------------------------
        # Validate date format and calendar validity
        # --------------------------------------------------

        if not self.validate_date(appointment_date):
            messagebox.showwarning(
                "Invalid Date",
                "Please enter a valid date using DD/MM/YYYY format."
            )
            return

        # --------------------------------------------------
        # Validate time format and range
        # --------------------------------------------------

        if not self.validate_time(appointment_time):
            messagebox.showwarning(
                "Invalid Time",
                "Please enter a valid time using HH:MM format."
            )
            return
                # --------------------------------------------------
        # Prevent past appointments
        # --------------------------------------------------

        if not self.validate_appointment_datetime(
            appointment_date,
            appointment_time
        ):

            messagebox.showwarning(
                "Past Appointment",
                "The appointment date and time cannot be in the past."
            )

            return

        if not reason:

            messagebox.showwarning(
                "Missing Reason",
                "Please enter the reason for the visit."
            )

            return

        patient_id = patient.split(" - ")[0]
        doctor_id = doctor.split(" - ")[0]

        appointments = self.db.get_all_appointments()

        appointment_number = len(appointments) + 1

        appointment_id = (
            f"APT-{appointment_number:04d}"
        )

        # ======================================================
        # CHECK FOR APPOINTMENT CONFLICT
        # ======================================================

        conflict = self.db.check_appointment_conflict(
            doctor_id,
            appointment_date,
            appointment_time
        )

        if conflict:
            messagebox.showwarning(
                "Appointment Conflict",
                f"The selected doctor already has a scheduled appointment "
                f"at {appointment_time} on {appointment_date}."
            )
            return

        saved = self.db.add_appointment(
            appointment_id,
            patient_id,
            doctor_id,
            appointment_date,
            appointment_time,
            reason,
            notes
        )

        if not saved:

            messagebox.showerror(
                "Error",
                "Failed to register appointment."
            )

            return

        messagebox.showinfo(
            "Success",
            f"Appointment {appointment_id} "
            "registered successfully."
        )

        self.clear_form()

        self.load_appointments()
        self.refresh_dashboard()

    # ======================================================
    # GET SELECTED APPOINTMENT ID
    # ======================================================

    def get_selected_appointment_id(self):

        selected = (
            self.appointment_table.selection()
        )

        if not selected:

            messagebox.showwarning(
                "No Selection",
                "Please select an appointment first."
            )

            return None

        values = (
            self.appointment_table.item(
                selected[0],
                "values"
            )
        )

        return values[0]

    # ======================================================
    # VIEW APPOINTMENT
    # ======================================================

    def view_selected_appointment(self):

        appointment_id = (
            self.get_selected_appointment_id()
        )

        if not appointment_id:

            return

        appointment = (
            self.db.get_appointment(
                appointment_id
            )
        )

        if not appointment:

            messagebox.showerror(
                "Error",
                "Appointment could not be found."
            )

            return

        (
            apt_id,
            patient_id,
            doctor_id,
            appointment_date,
            appointment_time,
            reason,
            status,
            notes,
            created_at
        ) = appointment

        details = (
            f"Appointment ID: {apt_id}\n\n"
            f"Patient ID: {patient_id}\n"
            f"Doctor ID: {doctor_id}\n\n"
            f"Date: {appointment_date}\n"
            f"Time: {appointment_time}\n\n"
            f"Reason: {reason}\n"
            f"Status: {status}\n\n"
            f"Notes: {notes or 'None'}\n\n"
            f"Created: {created_at}"
        )

        messagebox.showinfo(
            "Appointment Details",
            details
        )

        # ======================================================
    # LOAD SELECTED APPOINTMENT FOR EDITING
    # ======================================================

    def load_selected_appointment(self):

        appointment_id = self.get_selected_appointment_id()

        if not appointment_id:
            return

        appointment = self.db.get_appointment(
            appointment_id
        )

        if not appointment:

            messagebox.showerror(
                "Error",
                "The selected appointment could not be found."
            )

            return

        # --------------------------------------------------
        # Extract appointment information
        # --------------------------------------------------

        patient_id = appointment[1]
        doctor_id = appointment[2]
        appointment_date = appointment[3]
        appointment_time = appointment[4]
        reason = appointment[5]
        notes = appointment[7]

        # --------------------------------------------------
        # Load patient
        # --------------------------------------------------

        for value in self.patient_combo["values"]:

            if value.startswith(patient_id):

                self.patient_combo.set(value)
                break

        # --------------------------------------------------
        # Load doctor
        # --------------------------------------------------

        for value in self.doctor_combo["values"]:

            if value.startswith(doctor_id):

                self.doctor_combo.set(value)
                break

        # --------------------------------------------------
        # Load date
        # --------------------------------------------------

        self.date_entry.delete(
            0,
            tk.END
        )

        self.date_entry.insert(
            0,
            appointment_date
        )

        # --------------------------------------------------
        # Load time
        # --------------------------------------------------

        self.time_entry.delete(
            0,
            tk.END
        )

        self.time_entry.insert(
            0,
            appointment_time
        )

        # --------------------------------------------------
        # Load reason
        # --------------------------------------------------

        self.reason_entry.delete(
            0,
            tk.END
        )

        self.reason_entry.insert(
            0,
            reason
        )

        # --------------------------------------------------
        # Load notes
        # --------------------------------------------------

        self.notes_entry.delete(
            0,
            tk.END
        )

        self.notes_entry.insert(
            0,
            notes if notes else ""
        )

        # --------------------------------------------------
        # Remember appointment being edited
        # --------------------------------------------------

        self.editing_appointment_id = appointment_id

        messagebox.showinfo(
            "Edit Appointment",
            f"Appointment {appointment_id} loaded for editing."
        )
    # ======================================================
    # UPDATE SELECTED APPOINTMENT
    # ======================================================

        # ======================================================
    # SAVE APPOINTMENT CHANGES
    # ======================================================

    def update_selected_appointment(self):

        appointment_id = self.editing_appointment_id

        if not appointment_id:
            messagebox.showwarning(
                "No Appointment Loaded",
                "Please select an appointment and click "
                "'Edit Selected' first."
            )

            return

        # --------------------------------------------------
        # Get values from the form
        # --------------------------------------------------

        patient_value = self.patient_combo.get().strip()
        doctor_value = self.doctor_combo.get().strip()
        appointment_date = self.date_entry.get().strip()
        appointment_time = self.time_entry.get().strip()
        reason = self.reason_entry.get().strip()
        notes = self.notes_entry.get().strip()

        # --------------------------------------------------
        # Basic validation
        # --------------------------------------------------

        if not patient_value:
            messagebox.showwarning(
                "Missing Information",
                "Please select a patient."
            )
            return

        if not doctor_value:
            messagebox.showwarning(
                "Missing Information",
                "Please select a doctor."
            )
            return

        if not appointment_date:
            messagebox.showwarning(
                "Missing Information",
                "Please enter the appointment date."
            )
            return

        if not appointment_time:
            messagebox.showwarning(
                "Missing Information",
                "Please enter the appointment time."
            )
            return
                # --------------------------------------------------
        # Validate date format and calendar validity
        # --------------------------------------------------

        if not self.validate_date(appointment_date):
            messagebox.showwarning(
                "Invalid Date",
                "Please enter a valid date using DD/MM/YYYY format."
            )
            return

        # --------------------------------------------------
        # Validate time format and range
        # --------------------------------------------------

        if not self.validate_time(appointment_time):
            messagebox.showwarning(
                "Invalid Time",
                "Please enter a valid time using HH:MM format."
            )
            return
                # --------------------------------------------------
        # Prevent past appointments
        # --------------------------------------------------

        if not self.validate_appointment_datetime(
            appointment_date,
            appointment_time
        ):

            messagebox.showwarning(
                "Past Appointment",
                "The appointment date and time cannot be in the past."
            )

            return

        if not reason:
            messagebox.showwarning(
                "Missing Information",
                "Please enter the appointment reason."
            )
            return

        # --------------------------------------------------
        # Extract IDs from combobox values
        # --------------------------------------------------

        patient_id = patient_value.split(" - ")[0]
        doctor_id = doctor_value.split(" - ")[0]

        # --------------------------------------------------
        # Check for appointment conflicts
        #
        # The current appointment is excluded from the check.
        # --------------------------------------------------

        conflict = self.db.check_appointment_conflict(
            doctor_id,
            appointment_date,
            appointment_time,
            exclude_appointment_id=appointment_id
        )

        if conflict:
            messagebox.showwarning(
                "Appointment Conflict",
                f"The selected doctor already has a scheduled "
                f"appointment at {appointment_time} on "
                f"{appointment_date}."
            )
            return

        # --------------------------------------------------
        # Confirm update
        # --------------------------------------------------

        confirm = messagebox.askyesno(
            "Confirm Update",
            "Are you sure you want to save these appointment changes?"
        )

        if not confirm:
            return

        # --------------------------------------------------
        # Update appointment
        # --------------------------------------------------

        updated = self.db.update_appointment(
            appointment_id,
            patient_id,
            doctor_id,
            appointment_date,
            appointment_time,
            reason,
            notes
        )

        if updated:
            messagebox.showinfo(
                "Success",
                "Appointment updated successfully."
            )

            self.clear_form()
            self.load_appointments()

        else:
            messagebox.showerror(
                "Update Failed",
                "The appointment could not be updated."
            )
    # ======================================================
    # CANCEL SELECTED APPOINTMENT
    # ======================================================

        # ======================================================
    # CANCEL APPOINTMENT
    # ======================================================

    def cancel_selected_appointment(self):

        appointment_id = self.get_selected_appointment_id()

        if not appointment_id:
            messagebox.showwarning(
                "No Selection",
                "Please select an appointment first."
            )
            return

        appointment = self.db.get_appointment(appointment_id)

        if not appointment:
            messagebox.showerror(
                "Error",
                "The selected appointment could not be found."
            )
            return

        status = appointment[6]

        # --------------------------------------------------
        # Only scheduled appointments can be cancelled.
        # --------------------------------------------------

        if status != "Scheduled":
            messagebox.showwarning(
                "Action Not Allowed",
                f"This appointment is already {status.lower()}.\n\n"
                "Only scheduled appointments can be cancelled."
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Cancellation",
            "Are you sure you want to cancel this appointment?"
        )

        if not confirm:
            return

        cancelled = self.db.cancel_appointment(appointment_id)

        if cancelled:
            messagebox.showinfo(
                "Success",
                "Appointment cancelled successfully."
            )

            self.load_appointments()
            self.refresh_dashboard()

        else:
            messagebox.showerror(
                "Error",
                "The appointment could not be cancelled."
            )

    # ======================================================
    # COMPLETE SELECTED APPOINTMENT
    # ======================================================

       # ======================================================
    # COMPLETE APPOINTMENT
    # ======================================================

    def complete_selected_appointment(self):

        appointment_id = self.get_selected_appointment_id()

        if not appointment_id:
            messagebox.showwarning(
                "No Selection",
                "Please select an appointment first."
            )
            return

        appointment = self.db.get_appointment(appointment_id)

        if not appointment:
            messagebox.showerror(
                "Error",
                "The selected appointment could not be found."
            )
            return

        status = appointment[6]

        # --------------------------------------------------
        # Only scheduled appointments can be completed.
        # --------------------------------------------------

        if status != "Scheduled":
            messagebox.showwarning(
                "Action Not Allowed",
                f"This appointment is already {status.lower()}.\n\n"
                "Only scheduled appointments can be completed."
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Completion",
            "Mark this appointment as completed?"
        )

        if not confirm:
            return

        completed = self.db.complete_appointment(appointment_id)

        if completed:
            messagebox.showinfo(
                "Success",
                "Appointment marked as completed."
            )

            self.load_appointments()
            self.refresh_dashboard()

        else:
            messagebox.showerror(
                "Error",
                "The appointment could not be completed."
            )

    # ======================================================
    # RESTORE SELECTED APPOINTMENT
    # ======================================================

        # ======================================================
    # RESTORE APPOINTMENT
    # ======================================================

    def restore_selected_appointment(self):

        appointment_id = self.get_selected_appointment_id()

        if not appointment_id:
            messagebox.showwarning(
                "No Selection",
                "Please select an appointment first."
            )
            return

        appointment = self.db.get_appointment(appointment_id)

        if not appointment:
            messagebox.showerror(
                "Error",
                "The selected appointment could not be found."
            )
            return

        status = appointment[6]

        # --------------------------------------------------
        # Only cancelled appointments can be restored.
        # --------------------------------------------------

        if status != "Cancelled":
            messagebox.showwarning(
                "Action Not Allowed",
                f"This appointment is currently {status.lower()}.\n\n"
                "Only cancelled appointments can be restored."
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Restoration",
            "Restore this appointment to Scheduled status?"
        )

        if not confirm:
            return

        restored = self.db.restore_appointment(appointment_id)

        if restored:
            messagebox.showinfo(
                "Success",
                "Appointment restored successfully."
            )

            self.load_appointments()
            self.refresh_dashboard()
        else:
            messagebox.showerror(
                "Error",
                "The appointment could not be restored."
            )
        # ======================================================
    # LOAD APPOINTMENTS
    # ======================================================

    def load_appointments(self):

        # --------------------------------------------------
        # Clear existing table contents
        # --------------------------------------------------

        for item in self.appointment_table.get_children():

            self.appointment_table.delete(item)

        # --------------------------------------------------
        # Retrieve appointments from database
        # --------------------------------------------------

        appointments = self.db.get_all_appointments()

        # --------------------------------------------------
        # Display appointments in the table
        # --------------------------------------------------

        for appointment in appointments:

            self.appointment_table.insert(
                "",
                "end",
                values=(
                    appointment[0],  # Appointment ID
                    appointment[1],  # Patient ID
                    appointment[2],  # Doctor ID
                    appointment[3],  # Date
                    appointment[4],  # Time
                    appointment[5],  # Reason
                    appointment[6]   # Status
                )
            )        
    # ======================================================
    # SEARCH APPOINTMENTS
    # ======================================================
        # ======================================================
    # LOAD TODAY'S APPOINTMENTS
    # ======================================================

    def load_todays_appointments(self):

        # --------------------------------------------------
        # Clear existing table
        # --------------------------------------------------

        for item in self.appointment_table.get_children():

            self.appointment_table.delete(item)

        # --------------------------------------------------
        # Get today's date
        # --------------------------------------------------

        today = datetime.now().strftime("%d/%m/%Y")

        # --------------------------------------------------
        # Retrieve all appointments
        # --------------------------------------------------

        appointments = self.db.get_all_appointments()

        todays_appointments = []

        # --------------------------------------------------
        # Filter appointments for today
        # --------------------------------------------------

        for appointment in appointments:

            appointment_date = appointment[3]

            if appointment_date == today:

                todays_appointments.append(appointment)

        # --------------------------------------------------
        # Display today's appointments
        # --------------------------------------------------

        for appointment in todays_appointments:

            self.appointment_table.insert(
                "",
                "end",
                values=(
                    appointment[0],
                    appointment[1],
                    appointment[2],
                    appointment[3],
                    appointment[4],
                    appointment[5],
                    appointment[6]
                )
            )

        # --------------------------------------------------
        # Inform user if there are no appointments today
        # --------------------------------------------------

        if not todays_appointments:

            messagebox.showinfo(
                "Today's Appointments",
                "There are no appointments scheduled for today."
            )
        # ======================================================
    # LOAD UPCOMING APPOINTMENTS
    # ======================================================

    def load_upcoming_appointments(self):

        # --------------------------------------------------
        # Clear the current table
        # --------------------------------------------------

        for item in self.appointment_table.get_children():

            self.appointment_table.delete(item)

        # --------------------------------------------------
        # Get current date and time
        # --------------------------------------------------

        current_datetime = datetime.now()

        # --------------------------------------------------
        # Retrieve all appointments
        # --------------------------------------------------

        appointments = self.db.get_all_appointments()

        upcoming_appointments = []

        # --------------------------------------------------
        # Filter upcoming scheduled appointments
        # --------------------------------------------------

        for appointment in appointments:

            appointment_date = appointment[3]
            appointment_time = appointment[4]
            status = appointment[6]

            try:

                appointment_datetime = datetime.strptime(
                    f"{appointment_date} {appointment_time}",
                    "%d/%m/%Y %H:%M"
                )

            except ValueError:

                continue

            if (
                appointment_datetime >= current_datetime
                and status == "Scheduled"
            ):

                upcoming_appointments.append(
                    appointment
                )

        # --------------------------------------------------
        # Sort by date and time
        # --------------------------------------------------

        upcoming_appointments.sort(
            key=lambda appointment: datetime.strptime(
                f"{appointment[3]} {appointment[4]}",
                "%d/%m/%Y %H:%M"
            )
        )

        # --------------------------------------------------
        # Display upcoming appointments
        # --------------------------------------------------

        for appointment in upcoming_appointments:

            self.appointment_table.insert(
                "",
                "end",
                values=(
                    appointment[0],
                    appointment[1],
                    appointment[2],
                    appointment[3],
                    appointment[4],
                    appointment[5],
                    appointment[6]
                )
            )

        # --------------------------------------------------
        # Inform user if none exist
        # --------------------------------------------------

        if not upcoming_appointments:

            messagebox.showinfo(
                "Upcoming Appointments",
                "There are no upcoming scheduled appointments."
            )

    def search_appointments(self):

        search_term = (
            self.search_entry.get().strip()
        )

        if not search_term:

            self.load_appointments()

            return

        appointments = (
            self.db.search_appointments(
                search_term
            )
        )

        for item in (
            self.appointment_table.get_children()
        ):

            self.appointment_table.delete(item)

        for appointment in appointments:

            self.appointment_table.insert(
                "",
                "end",
                values=(
                    appointment[0],
                    appointment[1],
                    appointment[2],
                    appointment[3],
                    appointment[4],
                    appointment[5],
                    appointment[6]
                )
            )

        if not appointments:

            messagebox.showinfo(
                "No Results",
                "No matching appointments found."
            )
        # ======================================================
    # APPLY APPOINTMENT FILTERS
    # ======================================================

    def apply_appointment_filters(self):

        status_filter = self.status_filter.get().strip()
        doctor_filter = self.doctor_filter.get().strip()
        date_filter = self.date_filter.get().strip()

        # --------------------------------------------------
        # Validate date if one was entered
        # --------------------------------------------------

        if date_filter and date_filter != "DD/MM/YYYY":

            if not self.validate_date(date_filter):

                messagebox.showwarning(
                    "Invalid Date",
                    "Please enter a valid date using DD/MM/YYYY format."
                )

                return

        appointments = self.db.get_all_appointments()

        filtered_appointments = []

        # --------------------------------------------------
        # Apply filters
        # --------------------------------------------------

        for appointment in appointments:

            appointment_doctor_id = appointment[2]
            appointment_date = appointment[3]
            appointment_status = appointment[6]

            # --------------------------------------------------
            # Status filter
            # --------------------------------------------------

            if (
                status_filter != "All"
                and appointment_status != status_filter
            ):

                continue

            # --------------------------------------------------
            # Doctor filter
            # --------------------------------------------------

            if doctor_filter != "All":

                selected_doctor_id = doctor_filter.split(" - ")[0]

                if appointment_doctor_id != selected_doctor_id:

                    continue

            # --------------------------------------------------
            # Date filter
            # --------------------------------------------------

            if (
                date_filter
                and date_filter != "DD/MM/YYYY"
                and appointment_date != date_filter
            ):

                continue

            filtered_appointments.append(
                appointment
            )

        # --------------------------------------------------
        # Clear current table
        # --------------------------------------------------

        for item in self.appointment_table.get_children():

            self.appointment_table.delete(item)

        # --------------------------------------------------
        # Display filtered appointments
        # --------------------------------------------------

        for appointment in filtered_appointments:

            self.appointment_table.insert(
                "",
                "end",
                values=(
                    appointment[0],
                    appointment[1],
                    appointment[2],
                    appointment[3],
                    appointment[4],
                    appointment[5],
                    appointment[6]
                )
            )

        # --------------------------------------------------
        # No results
        # --------------------------------------------------

        if not filtered_appointments:

            messagebox.showinfo(
                "No Results",
                "No appointments match the selected filters."
            ) 
        # ======================================================
    # CLEAR APPOINTMENT FILTERS
    # ======================================================

    def clear_appointment_filters(self):

        # Reset status
        self.status_filter.current(0)

        # Reset doctor
        self.doctor_filter.current(0)

        # Reset date
        self.date_filter.delete(
            0,
            tk.END
        )

        self.date_filter.insert(
            0,
            "DD/MM/YYYY"
        )

        # Restore all appointments
        self.load_appointments()               

    # ======================================================
    # CLEAR FORM
    # ======================================================

    def clear_form(self):

        if self.patient_combo["values"]:

            self.patient_combo.current(0)

        if self.doctor_combo["values"]:

            self.doctor_combo.current(0)

        self.date_entry.delete(
            0,
            tk.END
        )

        self.date_entry.insert(
            0,
            "DD/MM/YYYY"
        )

        self.time_entry.delete(
            0,
            tk.END
        )

        self.time_entry.insert(
            0,
            "HH:MM"
        )

        self.reason_entry.delete(
            0,
            tk.END
        )

        self.notes_entry.delete(
            0,
            tk.END
        )
        # ======================================================
    # START CONSULTATION
    # ======================================================

    def start_consultation(self):

        appointment_id = self.get_selected_appointment_id()

        if not appointment_id:
            return

        appointment = self.db.get_appointment(
            appointment_id
        )

        if not appointment:

            messagebox.showerror(
                "Error",
                "The selected appointment could not be found."
            )

            return

        # --------------------------------------------------
        # Get appointment information
        # --------------------------------------------------

        patient_id = appointment[1]
        doctor_id = appointment[2]
        appointment_date = appointment[3]
        status = appointment[6]

        # --------------------------------------------------
        # Only scheduled appointments can start consultation
        # --------------------------------------------------

        if status != "Scheduled":

            messagebox.showwarning(
                "Action Not Allowed",
                f"This appointment is currently {status.lower()}.\n\n"
                "Only scheduled appointments can start a consultation."
            )

            return

        # --------------------------------------------------
        # Confirm consultation start
        # --------------------------------------------------

        confirm = messagebox.askyesno(
            "Start Consultation",
            f"Start consultation for appointment "
            f"{appointment_id}?\n\n"
            f"Patient: {patient_id}\n"
            f"Doctor: {doctor_id}"
        )

        if not confirm:
            return

        # --------------------------------------------------
        # Store consultation context
        # --------------------------------------------------

        self.consultation_context = {
            "appointment_id": appointment_id,
            "patient_id": patient_id,
            "doctor_id": doctor_id
        }

        # --------------------------------------------------
        # Open Consultation Window
        # --------------------------------------------------

        ConsultationWindow(
            self.window,
            appointment_id=appointment_id,
            patient_id=patient_id,
            doctor_id=doctor_id,
            visit_date=appointment_date,
            appointments_window=self

        )