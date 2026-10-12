from dashboard import Dashboard

import tkinter as tk
from tkinter import messagebox


class LoginWindow:

    def __init__(self):

        # ==================================================
        # COLORS
        # ==================================================

        self.BACKGROUND = "#F4F7FA"
        self.PRIMARY = "#1565C0"
        self.DARK = "#263238"
        self.WHITE = "#FFFFFF"
        self.GRAY = "#607D8B"

        # ==================================================
        # MAIN WINDOW
        # ==================================================

        self.window = tk.Tk()

        self.window.title("MedCare HMS - Login")
        self.window.geometry("450x500")
        self.window.resizable(False, False)

        self.window.configure(
            bg=self.BACKGROUND
        )

        # Create interface
        self.create_interface()

    # ======================================================
    # CREATE LOGIN INTERFACE
    # ======================================================

    def create_interface(self):

        # ==================================================
        # HEADER
        # ==================================================

        header = tk.Frame(
            self.window,
            bg=self.PRIMARY,
            height=110
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="MedCare HMS",
            font=("Segoe UI", 24, "bold"),
            bg=self.PRIMARY,
            fg=self.WHITE
        )

        title.pack(
            pady=(20, 3)
        )

        subtitle = tk.Label(
            header,
            text="Hospital Management System",
            font=("Segoe UI", 10),
            bg=self.PRIMARY,
            fg=self.WHITE
        )

        subtitle.pack()

        # ==================================================
        # LOGIN AREA
        # ==================================================

        login_frame = tk.Frame(
            self.window,
            bg=self.WHITE,
            padx=35,
            pady=25
        )

        login_frame.pack(
            padx=40,
            pady=35,
            fill="both",
            expand=True
        )

        # Login title

        login_title = tk.Label(
            login_frame,
            text="User Login",
            font=("Segoe UI", 18, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        )

        login_title.pack(
            pady=(5, 20)
        )

        # ==================================================
        # USERNAME
        # ==================================================

        username_label = tk.Label(
            login_frame,
            text="Username",
            font=("Segoe UI", 11),
            bg=self.WHITE,
            fg=self.DARK
        )

        username_label.pack(
            anchor="w",
            pady=(0, 5)
        )

        self.username_entry = tk.Entry(
            login_frame,
            font=("Segoe UI", 12),
            width=30,
            relief="solid",
            bd=1
        )

        self.username_entry.pack(
            fill="x",
            pady=(0, 15),
            ipady=6
        )

        # ==================================================
        # PASSWORD
        # ==================================================

        password_label = tk.Label(
            login_frame,
            text="Password",
            font=("Segoe UI", 11),
            bg=self.WHITE,
            fg=self.DARK
        )

        password_label.pack(
            anchor="w",
            pady=(0, 5)
        )

        self.password_entry = tk.Entry(
            login_frame,
            font=("Segoe UI", 12),
            width=30,
            show="*",
            relief="solid",
            bd=1
        )

        self.password_entry.pack(
            fill="x",
            pady=(0, 20),
            ipady=6
        )

        # ==================================================
        # LOGIN BUTTON
        # ==================================================

        login_button = tk.Button(
            login_frame,
            text="Login",
            command=self.login,
            bg=self.PRIMARY,
            fg=self.WHITE,
            font=("Segoe UI", 12, "bold"),
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=8
        )

        login_button.pack(
            fill="x",
            pady=10
        )

        # ==================================================
        # FOOTER
        # ==================================================

        footer = tk.Label(
            self.window,
            text="MedCare HMS © 2026",
            font=("Segoe UI", 9),
            bg=self.BACKGROUND,
            fg=self.GRAY
        )

        footer.pack(
            pady=10
        )

        # Allow ENTER key to login

        self.window.bind(
            "<Return>",
            lambda event: self.login()
        )

    # ======================================================
    # LOGIN FUNCTION
    # ======================================================

    def login(self):

        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        # Check empty fields

        if username == "" or password == "":
            messagebox.showerror(
                "Login Error",
                "Please enter your username and password."
            )
            return

        # Temporary login credentials
        # We will replace this with the database
        # authentication system later.

        if username == "admin" and password == "admin123":
            messagebox.showinfo(
                "Login Successful",
                "Welcome to MedCare HMS."
            )

            self.window.withdraw()

            dashboard = Dashboard(
                username=username
            )

            dashboard.run()
            self.window.destroy()

        else:
            messagebox.showerror(
                "Login Failed",
                "Invalid username or password."
            )

    # ======================================================
    # RUN APPLICATION
    # ======================================================

    def run(self):

        self.window.mainloop()