import tkinter as tk
from tkinter import messagebox
from account_storage import create_account

class AccountGUI:
    def __init__(self, parent):

        # Creates Account Creation
        self.account_window = tk.Toplevel(parent)
        self.account_window.title("Create Account")

        # Center Account Creation Window
        window_width = 450
        window_height = 400

        screen_width = self.account_window.winfo_screenwidth()
        screen_height = self.account_window.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.account_window.geometry(
            f"{window_width}x{window_height}+{x}+{y}"
        )

        # Brings Account Creation Window to Front
        self.account_window.lift()

        self.account_window.protocol(
            "WM_DELETE_WINDOW",
            self.account_window.destroy
        )


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
            text = "Creates username and password.\n"
                   "Password must be 9+ characters with uppercase,\n"
                   "lowercase, and a number.",
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
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        confirm_password = self.confirm_entry.get()

        # Checks for Information
        if username == "" or password == "" or confirm_password == "":
            messagebox.showerror(
                "Account Error",
                "Please fill out all fields.",
                parent = self.account_window
            )
            return

        # Checks for Matching Passwords
        if password != confirm_password:
            messagebox.showerror(
                "Account Error",
                "Passwords do not match.",
                parent = self.account_window
            )

            # Clears Password Field
            self.password_entry.delete(0, tk.END)
            self.confirm_entry.delete(0, tk.END)

            # Returns Cursor to Password Field
            self.password_entry.focus_set()
            return

        # Validates Password Requirements
        password_error = self.validate_password(password)

        if password_error is not None:
            messagebox.showerror(
                "Invalid Password",
                password_error,
                parent=self.account_window
            )

            # Clears Invalid Password
            self.password_entry.delete(0, tk.END)
            self.confirm_entry.delete(0, tk.END)

            # Returns Cursor to Password Field
            self.password_entry,focus_set()
            return

        # Attempts to Create Account
        try:
            account_created = create_account(username, password)

        except (OSError, ValueError) as error:
            messagebox.showerror(
                "Storage Error",
                f"Unable to save account: {error}",
                parent = self.account_window
            )
            return

        # Checks for Duplicate Username
        if not account_created:
            messagebox.showerror(
                "Account Error",
                "This username already exists. Please choose another.",
                parent = self.account_window
            )
            self.username_entry.focus_set()

            # Clears Username Field
            self.username_entry.delete(0, tk.END)
            
            # Returns Cursor to Username Field
            self.username_entry.focus_set()
            return

        # Confirms Successful Account Creation
        messagebox.showinfo(
            "Account Created",
            "Your account has been created successfully!\n"
            "You can now log in.",
            parent = self.account_window
        )

        # Closes Account Creation Window
        self.account_window.destroy()

    def submit_account(self, event):
        self.check_account()

    def validate_password(self, password):

        # Checks Password Length
        if len(password) < 9:
            return "Password must contain at least 9 characters."

        # Checks for Uppercase Letter
        if not any(char.isupper() for char in password):
            return "Password must contain an uppercase letter."

        # Checks for Lowercase Letter
        if not any (char.islower() for char in password):
            return "Password must contain a lowercase letter."

        # Checks for Digit
        if not any (char.isdigit() for char in password):
            return "Password must contain a digit."

        # Password meets ALL requirements
        return None
