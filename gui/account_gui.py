import tkinter as tk
from tkinter import messagebox

class AccountGUI:
    def __init__(self, parent):

        # Creates Account Creation
        self.account_window = tk.Toplevel(parent)
        self.account_window.title("Create Account")

        # Center Account Creation Window
        window_width = 450
        window_height = 350

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")


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
            text = "Enter a username and password below to create an account.\n"
                   "Enter the password again to confirm.",
            justify = "center"
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
        self.username_entry.focus_set()

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

        # Lets "Enter" work the same as clicking
        self.account_window.bind("<Return>", self.submit_account)

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
                "Passwords do not match."
            )

        else:
            messagebox.showinfo(
                "Account",
                "Account information is valid."
            )

    def submit_account(self, event):
        self.check_account()
