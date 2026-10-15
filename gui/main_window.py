import tkinter as tk
from account_gui import AccountGUI
from login_gui import LoginGUI

class MainWindow:
    def __init__(self):
        # Creates Program Window
        self.root = tk.Tk()
        self.root.title("Weather Data Project")

        # Center Main Window
        window_width = 450
        window_height = 350

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Title of the Program
        title_label = tk.Label(
            self.root,
            text = "Weather Data Project",
            font = ("Arial", 18, "bold")
        )
        title_label.pack(pady=10)

        instructions = tk.Label(
            self.root,
            text = "Create an account or login to continue."
        )
        instructions.pack(pady=10)

        # Account Button
        self.create_account_button = tk.Button(
            self.root,
            text = "Create Account",
            width = 20,
            command = self.open_account_window
        )
        self.create_account_button.pack(pady=5)

        # Login Button
        self.login_button = tk.Button(
            self.root,
            text = "Login",
            width = 20,
            command = self.open_login_window
        )
        self.login_button.pack(pady=5)

        # Cancel Button
        self.cancel_button = tk.Button(
            self.root,
            text = "Cancel",
            width = 20,
            command = self.root.destroy
        )
        self.cancel_button.pack(pady=5)


    def open_account_window(self):

        # Checks if Account Window Already Exists
        if hasattr(self, "account_gui"):
            if self.account_gui.account_window.winfo_exists():
                self.account_gui.account_window.lift()
                self.account_gui.account_window.focus_force()
                return
        # Creates Account Window
        self.account_gui = AccountGUI(self.root)
        
    def open_login_window(self):
        # Checks if Login Window Already Exists
        if hasattr(self, "login_gui"):
            if self.login_gui.login_window.winfo_exists():
                self.login_gui.login_window.lift()
                self.login_gui.login_window.focus_force()
                return
            
        # Creates Login Window
        self.login_gui = LoginGUI(self.root)
        
        
if __name__ == "__main__":
    app = MainWindow()
    app.root.mainloop()
