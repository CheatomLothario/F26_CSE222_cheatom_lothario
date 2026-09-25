import tkinter as tk
from account_gui import AccountGUI

class MainWindow:
    def __init__(self):
        # Creates Program Window
        self.root = tk.Tk()
        self.root.title("Weather Data Project")
        self.root.geometry("450x350")

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
            width = 20
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

        # Start Loop
        self.root.mainloop()

    def open_account_window(self):
        AccountGUI(self.root)
        
        
if __name__ == "__main__":
    MainWindow()
