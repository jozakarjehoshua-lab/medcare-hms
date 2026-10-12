import tkinter as tk
from tkinter import ttk, messagebox
from database import Database
from datetime import datetime

class BillingWindow:

    def __init__(self, parent):

        self.db = Database()

        self.current_bill_id = None

        
        self.window = tk.Toplevel(parent)

        self.window.title("MedCare HMS - Billing & Payments")

        self.window.geometry("1150x700")

        self.window.minsize(1000, 650)

        self.window.configure(bg="#F4F7FA")

        self.create_interface()

        self.load_patients()


# ======================================================
# NEW BILL
# ======================================================

    def new_bill(self):

        self.current_bill_id = None

        self.patient_combo.set("")

        self.appointment_combo.set("")

        self.appointment_combo["values"] = ()

        self.bill_date_entry.delete(
            0,
            tk.END
       )

        self.bill_date_entry.insert(
            0,
            datetime.now().strftime("%d/%m/%Y")
       )

        self.description_entry.delete(
            0,
            tk.END
       )

        self.quantity_entry.delete(
            0,
            tk.END
       )

        self.quantity_entry.insert(
            0,
            "1"
       )

        self.price_entry.delete(
            0,
            tk.END
       )

        self.total_label.config(
            text="0.00"
       )

        for item in self.items_tree.get_children():

            self.items_tree.delete(item)

        self.create_bill_button.config(
        state="normal"
    )
    # ======================================================
    # CREATE INTERFACE
    # ======================================================

    def create_interface(self):

        # --------------------------------------------------
        # HEADER
        # --------------------------------------------------

        header = tk.Frame(
            self.window,
            bg="#1565C0",
            height=80
        )

        header.pack(
            fill="x"
        )

        title_label = tk.Label(
            header,
            text="Billing & Payments",
            font=("Segoe UI", 22, "bold"),
            bg="#1565C0",
            fg="white"
        )

        title_label.pack(
            anchor="w",
            padx=25,
            pady=(15, 0)
        )

        subtitle_label = tk.Label(
            header,
            text="Create bills and manage patient payments",
            font=("Segoe UI", 10),
            bg="#1565C0",
            fg="white"
        )

        subtitle_label.pack(
            anchor="w",
            padx=27,
            pady=(0, 10)
        )


        # --------------------------------------------------
        # MAIN CONTAINER
        # --------------------------------------------------

        main_frame = tk.Frame(
            self.window,
            bg="#F4F7FA"
        )

        main_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )


        # --------------------------------------------------
        # LEFT PANEL - BILL INFORMATION
        # --------------------------------------------------

        bill_frame = tk.LabelFrame(
            main_frame,
            text="Bill Information",
            font=("Segoe UI", 11, "bold"),
            bg="white",
            fg="#263238",
            padx=15,
            pady=15
        )

        bill_frame.pack(
            side="left",
            fill="y",
            padx=(0, 10)
        )


        # Patient
        tk.Label(
            bill_frame,
            text="Patient:",
            bg="white",
            font=("Segoe UI", 10)
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=8
        )

        self.patient_combo = ttk.Combobox(
            bill_frame,
            width=28,
            state="readonly"
        )

        self.patient_combo.grid(
            row=0,
            column=1,
            pady=8,
            padx=10
        )


        # Appointment
        tk.Label(
            bill_frame,
            text="Appointment:",
            bg="white",
            font=("Segoe UI", 10)
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=8
        )

        self.appointment_combo = ttk.Combobox(
            bill_frame,
            width=28,
            state="readonly"
        )

        self.appointment_combo.grid(
            row=1,
            column=1,
            pady=8,
            padx=10
        )


        # Bill Date
        tk.Label(
            bill_frame,
            text="Bill Date:",
            bg="white",
            font=("Segoe UI", 10)
        ).grid(
            row=2,
            column=0,
            sticky="w",
            pady=8
        )

        self.bill_date_entry = tk.Entry(
            bill_frame,
            width=31,
            font=("Segoe UI", 10)
        )

        self.bill_date_entry.grid(
            row=2,
            column=1,
            pady=8,
            padx=10
        )

        self.bill_date_entry.insert(
            0,
            datetime.now().strftime("%d/%m/%Y")
        )


        # Create Bill Button
        self.create_bill_button = tk.Button(
            bill_frame,
            text="Create Bill",
            command=self.create_bill,
            bg="#1565C0",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2"
        )

        self.create_bill_button.grid(
            row=3,
            column=0,
            columnspan=2,
            pady=20
        )
        # New Bill Button
        self.new_bill_button = tk.Button(
            bill_frame,
            text="New Bill",
            command=self.new_bill,
            bg="#607D8B",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2"
        )

        self.new_bill_button.grid(
            row=4,
            column=0,
            columnspan=2,
            pady=(0, 10)
        )

        # --------------------------------------------------
        # RIGHT PANEL
        # --------------------------------------------------

        right_frame = tk.Frame(
            main_frame,
            bg="#F4F7FA"
        )

        right_frame.pack(
            side="left",
            fill="both",
            expand=True
        )


        # --------------------------------------------------
        # BILL ITEMS
        # --------------------------------------------------

        items_frame = tk.LabelFrame(
            right_frame,
            text="Bill Items",
            font=("Segoe UI", 11, "bold"),
            bg="white",
            fg="#263238",
            padx=15,
            pady=15
        )

        items_frame.pack(
            fill="both",
            expand=True
        )


        # Description

        tk.Label(
            items_frame,
            text="Description",
            bg="white"
        ).grid(
            row=0,
            column=0,
            sticky="w"
        )

        self.description_entry = tk.Entry(
            items_frame,
            width=25
        )

        self.description_entry.grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )


        # Quantity

        tk.Label(
            items_frame,
            text="Quantity",
            bg="white"
        ).grid(
            row=0,
            column=1,
            sticky="w"
        )

        self.quantity_entry = tk.Entry(
            items_frame,
            width=10
        )

        self.quantity_entry.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        self.quantity_entry.insert(
            0,
            "1"
        )


        # Unit Price

        tk.Label(
            items_frame,
            text="Unit Price",
            bg="white"
        ).grid(
            row=0,
            column=2,
            sticky="w"
        )

        self.price_entry = tk.Entry(
            items_frame,
            width=12
        )

        self.price_entry.grid(
            row=1,
            column=2,
            padx=5,
            pady=5
        )


        # Add Item

        tk.Button(
            items_frame,
            text="Add Item",
            command=self.add_item,
            bg="#2E7D32",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            padx=12,
            pady=5
        ).grid(
            row=1,
            column=3,
            padx=10
        )

        # --------------------------------------------------
        # ITEMS TABLE
        # --------------------------------------------------

        table_frame = tk.Frame(
            items_frame,
            bg="white"
        )

        table_frame.grid(
            row=2,
            column=0,
            columnspan=4,
            sticky="nsew",
            pady=20
        )

        columns = (
            "item_id",
            "description",
            "quantity",
            "unit_price",
            "total"
        )

        self.items_tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=12
        )

        self.items_tree.heading(
            "item_id",
            text="Item ID"
        )

        self.items_tree.heading(
            "description",
            text="Description"
        )

        self.items_tree.heading(
            "quantity",
            text="Quantity"
        )

        self.items_tree.heading(
            "unit_price",
            text="Unit Price"
        )

        self.items_tree.heading(
            "total",
            text="Total"
        )


        self.items_tree.column(
            "item_id",
            width=100,
            anchor="center"
        )

        self.items_tree.column(
            "description",
            width=250,
            anchor="center"
      )

        self.items_tree.column(
            "quantity",
            width=100,
            anchor="center"
        )

        self.items_tree.column(
            "unit_price",
            width=120,
            anchor="center"
       )

        self.items_tree.column(
            "total",
            width=120,
            anchor="center"
        )


        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.items_tree.yview
        )

        self.items_tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.items_tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )


        # --------------------------------------------------
        # BILL SUMMARY
        # --------------------------------------------------

        summary_frame = tk.Frame(
            items_frame,
            bg="white"
        )

        summary_frame.grid(
            row=3,
            column=0,
            columnspan=4,
            sticky="e",
            pady=10
        )

        tk.Label(
            summary_frame,
            text="Total:",
            font=("Segoe UI", 12, "bold"),
            bg="white"
        ).pack(
            side="left",
            padx=10
        )

        self.total_label = tk.Label(
            summary_frame,
            text="0.00",
            font=("Segoe UI", 14, "bold"),
            bg="white",
            fg="#1565C0"
        )

        self.total_label.pack(
            side="left"
        )

    # ======================================================
    # LOAD PATIENTS
    # ======================================================

    def load_patients(self):

        patients = self.db.get_active_patients()

        self.patient_combo["values"] = [
            f"{patient[0]} - {patient[1]}"
            for patient in patients
        ]

        self.patient_combo.bind(
            "<<ComboboxSelected>>",
            self.load_patient_appointments
        )


# ======================================================
# LOAD PATIENT APPOINTMENTS
# ======================================================

    def load_patient_appointments(self, event=None):

        self.appointment_combo.set("")

        patient_value = self.patient_combo.get()

        if not patient_value:
            return

        patient_id = patient_value.split(" - ")[0]

        appointments = self.db.get_patient_appointments(
            patient_id
        )

        self.appointment_combo["values"] = [
            f"{appointment[0]} - {appointment[3]} {appointment[4]}"
            for appointment in appointments
        ]

    # ======================================================
    # CREATE BILL
    # ======================================================

    def create_bill(self):

        patient_value = self.patient_combo.get()

        if not patient_value:

            messagebox.showwarning(
                "Missing Patient",
                "Please select a patient."
            )

            return

        bill_date = self.bill_date_entry.get().strip()

        if not bill_date:

            messagebox.showwarning(
                "Missing Date",
                "Please enter the bill date."
            )

            return

        patient_id = patient_value.split(" - ")[0]

        bill_id = f"BILL-{datetime.now().strftime('%Y%m%d%H%M%S')}"

        appointment_id = None

        appointment_value = self.appointment_combo.get()

        if appointment_value:

            appointment_id = appointment_value.split(" - ")[0]

        try:

            self.db.add_bill(
                bill_id,
                patient_id,
                appointment_id,
                bill_date
            )

            self.current_bill_id = bill_id

            messagebox.showinfo(
                "Success",
                f"Bill {bill_id} created successfully."
            )

            self.create_bill_button.config(
                state="disabled"
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"Could not create bill:\n{error}"
            )

        # ======================================================
    # ADD BILL ITEM
    # ======================================================

    def add_item(self):

        if self.current_bill_id is None:

            messagebox.showwarning(
                "No Bill",
                "Please create a bill first."
            )

            return

        description = self.description_entry.get().strip()

        if not description:

            messagebox.showwarning(
                "Missing Description",
                "Please enter a description."
            )

            return

        try:

            quantity = int(
                self.quantity_entry.get()
            )

            unit_price = float(
                self.price_entry.get()
            )

        except ValueError:

            messagebox.showwarning(
                "Invalid Amount",
                "Quantity must be a whole number and unit price must be numeric."
            )

            return

        if quantity <= 0 or unit_price < 0:

            messagebox.showwarning(
                "Invalid Values",
                "Quantity must be greater than zero and price cannot be negative."
            )

            return

        item_id = (
            f"ITEM-{datetime.now().strftime('%Y%m%d%H%M%S%f')}"
        )

        try:

            self.db.add_bill_item(
                item_id,
                self.current_bill_id,
                description,
                quantity,
                unit_price
            )

            self.db.update_bill_total(
                self.current_bill_id
            )

            total_price = quantity * unit_price

            self.items_tree.insert(
                "",
                "end",
                values=(
                    item_id,
                    description,
                    quantity,
                    f"{unit_price:.2f}",
                    f"{total_price:.2f}"
                )
            )

            bill = self.db.get_bill(
                self.current_bill_id
            )

            self.total_label.config(
                text=f"{bill[4]:.2f}"
            )

            self.description_entry.delete(
                0,
                tk.END
            )

            self.quantity_entry.delete(
                0,
                tk.END
            )

            self.quantity_entry.insert(
                0,
                "1"
            )

            self.price_entry.delete(
                0,
                tk.END
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"Could not add billing item:\n{error}"
            )
if __name__ == "__main__":

    root = tk.Tk()

    root.withdraw()

    BillingWindow(root)

    root.mainloop()                    