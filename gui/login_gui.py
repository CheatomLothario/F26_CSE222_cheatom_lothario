import tkinter as tk
from tkinter import messagebox
from account_storage import verify_account

class LoginGUI:
    def __init__(self, parent):

        # Creates Login Window
        self.login_window = tk.Toplevel(parent)
        self.login_window.title("Login")

        # Center Login Window
        window_width = 450
        window_height = 350

        screen_width = self.login_window.winfo_screenwidth()
        screen_height = self.login_window.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.login_window.geometry(
            f"{window_width}x{window_height}+{x}+{y}"
        )


        # Title of the Window
        title_label = tk.Label(
            self.login_window,
            text = "Login",
            font = ("Arial", 18, "bold")
        )
        title_label.pack(pady=10)

        # Instructions for the User
        instructions = tk.Label(
            self.login_window,
            text = "Enter your username and password below to login.\n"
                   "When done, click Login to continue.",
            justify = "center"
        )
        instructions.pack(pady=10)

        # Username
        username_label = tk.Label(
            self.login_window,
            text = "Username:"
        )
        username_label.pack()

        self.username_entry = tk.Entry(
            self.login_window,
            width = 30,
            justify = "right"
        )
        self.username_entry.pack(pady=5)
        self.username_entry.focus_set()

        # Password
        password_label = tk.Label(
            self.login_window,
            text = "Password"
        )
        password_label.pack()

        self.password_entry = tk.Entry(
            self.login_window,
            width = 30,
            show = "*",
            justify = "right"
        )
        self.password_entry.pack(pady=5)

        # Login Button
        self.login_button = tk.Button(
            self.login_window,
            text = "Login",
            width = 20,
            command = self.check_login
        )
        self.login_button.pack(pady=10)

        # Cancel Button
        self.cancel_button = tk.Button(
            self.login_window,
            text = "Cancel",
            width = 20,
            command = self.login_window.destroy
        )
        self.cancel_button.pack(pady=5)

        # Lets "Enter" work the same as clicking
        self.login_window.bind("<Return>", self.submit_login)

    def check_login(self):
        # Retrieves Username and Password
        username = self.username_entry.get().strip()
        password = self.password_entry.get()

        # Checks for Empty Fields
        if username == "" or password == "":
            messagebox.showerror(
                "Login Error",
                "Please Enter a username and password.",
                parent = self.login_window
            )
            return

        # Attempts to Verify Account
        try:
            account_verified = verify_account(username, password)

        except (OSError, ValueError, KeyError, TypeError) as error:
            messagebox.showerror(
                "Login Error",
                f"Unable to verify account information: {error}",
                parent = self.login_window
            )
            return

        # Checks Whether Credentials Match
        if not account_verified:
            messagebox.showerror(
                "Login Failed",
                "Invalid username or password.",
                parent = self.login_window
            )

            # Clears Login Entry Fields
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)

            # Returns Cursor to Username Field
            self.username_entry.focus_set()
            return

        # Confirms Successful Login
        messagebox.showinfo(
            "Login Successful",
            f"Welcome, {username}!",
            parent = self.login_window
        )

        # Closes Login Window
        self.login_window.destroy()

    def submit_login(self, event):
        self.check_login()
