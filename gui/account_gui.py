import tkinter as tk
from tkinter import messagebox

class AccountGUI:
    def __init__(self, parent):

        # Creates Account Creation
        self.account_window = tk.Toplevel(parent)
        self.account_window.title("Create Account")
        self.account_window.geometry("400x350")

        # Title of the Window
        title_label = tk.Label(
            self.account_window,
            text = "Create Account",
            font = ("Arial", 18, "bold")
        )
        title_label.pack(pady=10)

        # Instructions for the User
        instructions = tk.Label(
            self.account_window,
            text = "Enter a username and password to create an account."
        )
        instructions.pack(pady=10)

        # Username
        username_label = tk.Label(
            self.account_window,
            text = "Username:"
        )
        username_label.pack()

        self.username_entry = tk.Entry(
            self.account_window,
            width = 30
        )
        self.username_entry.pack(pady=5)

        # Password
        password_label = tk.Label(
            self.account_window,
            text = "Password:"
        )
        password_label.pack()

        self.password_entry = tk.Entry(
            self.account_window,
            width = 30,
            show = "*"
        )
        self.password_entry.pack(pady=5)

        # Password Confirmation
        confirm_label = tk.Label(
            self.account_window,
            text = "Confirm Password:"
        )
        confirm_label.pack()

        self.confirm_entry = tk.Entry(
            self.account_window,
            width = 30,
            show = "*"
        )
        self.confirm_entry.pack(pady=5)

        # Create Account Button
        self.create_button = tk.Button(
            self.account_window,
            text = "Create Account",
            width = 20,
            command = self.check_account
        )
        self.create_button.pack(pady=10)

        # Cancel Button
        self.cancel_button = tk.Button(
            self.account_window,
            text = "Cancel",
            width = 20,
            command = self.account_window.destroy
        )
        self.cancel_button.pack(pady=5)

    def check_account(self):

        # Collects User Information
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_entry.get()

        # Checks for Information
        if username == "" or password == "" or confirm_password == "":
            messagebox.showerror(
                "Account Error",
                "Please fill out all fields."
            )

        # Checks for Matching Passwords
        elif password != confirm_password:
            messagebox.showerror(
                "Account Error",
                "Passwprds do not match."
            )

        else:
            messagebox.showinfo(
                "Account",
                "Account information is valid."
            )
