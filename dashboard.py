from patients import PatientsWindow
from doctors import DoctorsWindow
from medical_records import MedicalRecordsWindow
from appointments import AppointmentsWindow
from database import Database
from billing import BillingWindow 
import tkinter as tk


class Dashboard:

    def __init__(self, username="Administrator"):

        # ==================================================
        # COLORS
        # ==================================================

        self.BACKGROUND = "#F4F7FA"
        self.PRIMARY = "#1565C0"
        self.DARK = "#263238"
        self.WHITE = "#FFFFFF"
        self.GRAY = "#607D8B"
        self.LIGHT_BLUE = "#E3F2FD"
        self.DANGER = "#C62828"
        self.SUCCESS = "#2E7D32"
        self.DANGER = "#C62828"

        self.username = username
        self.db = Database()

        # ==================================================
        # MAIN WINDOW
        # ==================================================

        self.window = tk.Toplevel()

        self.window.title("MedCare HMS - Dashboard")
        self.window.geometry("1100x700")
        self.window.minsize(950, 600)

        self.window.configure(
            bg=self.BACKGROUND
        )

        # ==================================================
        # CREATE INTERFACE
        # ==================================================

        self.create_sidebar()
        self.create_main_area()

    # ======================================================
    # SIDEBAR
    # ======================================================

    def create_sidebar(self):

        self.sidebar = tk.Frame(
            self.window,
            bg=self.DARK,
            width=230
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(False)

        # --------------------------------------------------
        # Logo / Hospital Name
        # --------------------------------------------------

        logo_frame = tk.Frame(
            self.sidebar,
            bg=self.PRIMARY,
            height=100
        )

        logo_frame.pack(
            fill="x"
        )

        logo_frame.pack_propagate(False)

        logo = tk.Label(
            logo_frame,
            text="MedCare HMS",
            font=("Segoe UI", 18, "bold"),
            bg=self.PRIMARY,
            fg=self.WHITE
        )

        logo.pack(
            pady=(20, 2)
        )

        logo_subtitle = tk.Label(
            logo_frame,
            text="Hospital Management",
            font=("Segoe UI", 9),
            bg=self.PRIMARY,
            fg=self.DARK
        )

        logo_subtitle.pack()

        # --------------------------------------------------
        # Navigation
        # --------------------------------------------------

        nav_frame = tk.Frame(
            self.sidebar,
            bg=self.DARK
        )

        nav_frame.pack(
            fill="both",
            expand=True,
            pady=20
        )

        self.create_nav_button(
            nav_frame,
            "Dashboard",
            self.show_dashboard
        )

        self.create_nav_button(
            nav_frame,
            "Patients",
            self.open_patients
        )

        self.create_nav_button(
            nav_frame,
            "Doctors",
            self.open_doctors
        )

        self.create_nav_button(
            nav_frame,
            "Appointments",
            self.open_appointments
        )

        self.create_nav_button(
            nav_frame,
            "Medical Records",
            self.open_records
        )

        self.create_nav_button(
            nav_frame,
            "Billing",
            self.open_billing
        )

        self.create_nav_button(
            nav_frame,
            "Users & Roles",
            self.open_users
        )

        # --------------------------------------------------
        # Logout
        # --------------------------------------------------

        logout_button = tk.Button(
            self.sidebar,
            text="Logout",
            command=self.logout,
            bg=self.DANGER,
            fg=self.WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=10
        )

        logout_button.pack(
            fill="x",
            padx=20,
            pady=20
        )

    # ======================================================
    # NAVIGATION BUTTON
    # ======================================================

    def create_nav_button(self, parent, text, command):

        button = tk.Button(
            parent,
            text=text,
            command=command,
            anchor="w",
            bg=self.DARK,
            fg=self.WHITE,
            activebackground=self.PRIMARY,
            activeforeground=self.WHITE,
            font=("Segoe UI", 10),
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=25,
            pady=12
        )

        button.pack(
            fill="x",
            pady=2
        )

    # ======================================================
    # MAIN AREA
    # ======================================================

    def create_main_area(self):

        self.main_area = tk.Frame(
            self.window,
            bg=self.BACKGROUND
        )

        self.main_area.pack(
            side="right",
            fill="both",
            expand=True
        )

        self.show_dashboard()

    # ======================================================
    # CLEAR MAIN AREA
    # ======================================================

    def clear_main_area(self):

        for widget in self.main_area.winfo_children():
            widget.destroy()

    # ======================================================
    # DASHBOARD
    # ======================================================

    def show_dashboard(self):

        self.clear_main_area()

        # --------------------------------------------------
        # Header
        # --------------------------------------------------

        header = tk.Frame(
            self.main_area,
            bg=self.WHITE,
            height=90
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="Dashboard",
            font=("Segoe UI", 24, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        )

        title.pack(
            side="left",
            padx=30,
            pady=25
        )

        welcome = tk.Label(
            header,
            text=f"Welcome, {self.username}",
            font=("Segoe UI", 10),
            bg=self.WHITE,
            fg=self.GRAY
        )

        welcome.pack(
            side="right",
            padx=30
        )

        # --------------------------------------------------
        # Dashboard Content
        # --------------------------------------------------

        content = tk.Frame(
            self.main_area,
            bg=self.BACKGROUND
        )

        content.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=30
        )

        intro = tk.Label(
            content,
            text="Hospital Overview",
            font=("Segoe UI", 16, "bold"),
            bg=self.BACKGROUND,
            fg=self.DARK
        )

        intro.pack(
            anchor="w",
            pady=(0, 15)
        )

        # --------------------------------------------------
        # Summary Cards
        # --------------------------------------------------

        cards_frame = tk.Frame(
            content,
            bg=self.BACKGROUND
        )

        cards_frame.pack(
            fill="x"
        )

        self.create_card(
            cards_frame,
            "Active Patients",
            str(self.db.get_patient_count()),
            0
        )

        self.create_card(
            cards_frame,
            "Doctors",
            str(self.db.get_doctor_count()),
            1
        )

        self.create_card(
    cards_frame,
    "Appointments",
    str(self.db.get_appointment_count()),
    2
    )
        

        self.create_card(
            cards_frame,
            "Medical Records",
            str(self.db.get_medical_record_count()),
            3
        )
        # ==================================================
        # APPOINTMENT SUMMARY
        # ==================================================

        appointment_summary = tk.LabelFrame(
            content,
            text=" Appointment Summary ",
            font=("Segoe UI", 11, "bold"),
            bg=self.WHITE,
            fg=self.DARK,
            padx=15,
            pady=15
        )

        appointment_summary.pack(
            fill="x",
            padx=25,
            pady=(10, 20)
        )
        # Configure four equal columns
        for i in range(4):
            appointment_summary.grid_columnconfigure(
                i,
                weight=1
            )

        # ==================================================
        # TODAY'S APPOINTMENTS
        # ==================================================

        today_count = self.db.get_todays_appointment_count()

        today_frame = tk.Frame(
            appointment_summary,
            bg=self.WHITE
        )

        today_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=10
        )

        tk.Label(
            today_frame,
            text="Today's Appointments",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).pack(
            pady=(5, 3)
        )

        tk.Label(
            today_frame,
            text=str(today_count),
            font=("Segoe UI", 24, "bold"),
            bg=self.WHITE,
            fg=self.PRIMARY
        ).pack()

        # ==================================================
        # UPCOMING APPOINTMENTS
        # ==================================================

        upcoming_count = self.db.get_upcoming_appointment_count()

        upcoming_frame = tk.Frame(
            appointment_summary,
            bg=self.WHITE
        )

        upcoming_frame.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=10
        )

        tk.Label(
            upcoming_frame,
            text="Upcoming Appointments",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).pack(
            pady=(5, 3)
        )

        tk.Label(
            upcoming_frame,
            text=str(upcoming_count),
            font=("Segoe UI", 24, "bold"),
            bg=self.WHITE,
            fg=self.SUCCESS
        ).pack()

        # ==================================================
        # COMPLETED APPOINTMENTS
        # ==================================================

        completed_count = self.db.get_appointment_status_count(
            "Completed"
        )

        completed_frame = tk.Frame(
            appointment_summary,
            bg=self.WHITE
        )

        completed_frame.grid(
            row=0,
            column=2,
            sticky="nsew",
            padx=10
    )

        tk.Label(
            completed_frame,
            text="Completed",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).pack(
            pady=(5, 3)
        )

        tk.Label(
            completed_frame,
            text=str(completed_count),
            font=("Segoe UI", 24, "bold"),
            bg=self.WHITE,
            fg=self.PRIMARY
        ).pack()

        # ==================================================
        # CANCELLED APPOINTMENTS
        # ==================================================

        cancelled_count = self.db.get_appointment_status_count(
            "Cancelled"
        )

        cancelled_frame = tk.Frame(
            appointment_summary,
            bg=self.WHITE
        )

        cancelled_frame.grid(
            row=0,
            column=3,
            sticky="nsew",
            padx=10
        )

        tk.Label(
            cancelled_frame,
            text="Cancelled",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).pack(
            pady=(5, 3)
        )

        tk.Label(
            cancelled_frame,
            text=str(cancelled_count),
            font=("Segoe UI", 24, "bold"),
            bg=self.WHITE,
            fg=self.DANGER
        ).pack()

        # --------------------------------------------------
        # System Information
        # --------------------------------------------------

        info_frame = tk.Frame(
            content,
            bg=self.WHITE,
            padx=25,
            pady=20
        )

        info_frame.pack(
            fill="x",
            pady=30
        )

        info_title = tk.Label(
            info_frame,
            text="System Information",
            font=("Segoe UI", 13, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        )

        info_title.pack(
            anchor="w"
        )

        info_text = tk.Label(
            info_frame,
            text=(
                "Welcome to MedCare Hospital Management System.\n"
                "Use the navigation menu to manage hospital operations."
            ),
            font=("Segoe UI", 10),
            bg=self.WHITE,
            fg=self.GRAY,
            justify="left"
        )

        info_text.pack(
            anchor="w",
            pady=(10, 0)
        )

    # ======================================================
    # REFRESH DASHBOARD
    # ======================================================

    def refresh_dashboard(self):

        self.show_dashboard()    

    # ======================================================
    # DASHBOARD CARD
    # ======================================================

    def create_card(self, parent, title, value, column):

        card = tk.Frame(
            parent,
            bg=self.WHITE,
            width=180,
            height=120
        )

        card.grid(
            row=0,
            column=column,
            padx=8,
            sticky="nsew"
        )

        card.grid_propagate(False)

        value_label = tk.Label(
            card,
            text=value,
            font=("Segoe UI", 25, "bold"),
            bg=self.WHITE,
            fg=self.PRIMARY
        )

        value_label.pack(
            pady=(20, 2)
        )

        title_label = tk.Label(
            card,
            text=title,
            font=("Segoe UI", 10),
            bg=self.WHITE,
            fg=self.GRAY
        )

        title_label.pack()

    # ======================================================
    # MODULE PLACEHOLDERS
    # ======================================================

    def show_module_message(self, module):

        self.clear_main_area()

        label = tk.Label(
            self.main_area,
            text=f"{module} Module",
            font=("Segoe UI", 24, "bold"),
            bg=self.BACKGROUND,
            fg=self.DARK
        )

        label.pack(
            pady=100
        )

        message = tk.Label(
            self.main_area,
            text="This module will be developed in the next stages.",
            font=("Segoe UI", 11),
            bg=self.BACKGROUND,
            fg=self.GRAY
        )

        message.pack()

    def open_patients(self):
        PatientsWindow(self.window)

    def open_doctors(self):
        DoctorsWindow(self.window)

    def open_appointments(self):
        AppointmentsWindow(
        self.window,
        dashboard=self
    )   

    def open_records(self):
        MedicalRecordsWindow(self.window)
     

    def open_billing(self):
        BillingWindow(self.window)

    def open_users(self):
        self.show_module_message("Users & Roles")

    # ======================================================
    # LOGOUT
    # ======================================================

    def logout(self):

        self.window.destroy()

    # ======================================================
    # RUN
    # ======================================================

    def run(self):

        self.window.mainloop()