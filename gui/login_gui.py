import tkinter as tk
from tkinter import messagebox

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
            width = 30
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
            show = "*"
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

        # Collects User Information
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Checks for Information
        if username == "" or password == "":
            messagebox.showerror(
                "Login Error",
                "Please enter a username and password."
            )
        else:
            messagebox.showinfo(
                "Login",
                "Login information is valid."
            )

    def submit_login(self, event):
        self.check_login()
