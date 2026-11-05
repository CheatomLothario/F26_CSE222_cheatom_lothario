import math
import tkinter as tk
from tkinter import messagebox
from account_gui import AccountGUI
from login_gui import LoginGUI
from weather_calculations import calculate_wind_chill, calculate_cloud_base

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

        # Frame for Initial Menu
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack(expand = True)

        # Title of the Program
        title_label = tk.Label(
            self.menu_frame,
            text = "Weather Data Project",
            font = ("Arial", 18, "bold")
        )
        title_label.pack(pady=10)

        instructions = tk.Label(
            self.menu_frame,
            text = "Create an account or login to continue."
        )
        instructions.pack(pady=10)

        # Account Button
        self.create_account_button = tk.Button(
            self.menu_frame,
            text = "Create Account",
            width = 20,
            command = self.open_account_window
        )
        self.create_account_button.pack(pady=5)

        # Login Button
        self.login_button = tk.Button(
            self.menu_frame,
            text = "Login",
            width = 20,
            command = self.open_login_window
        )
        self.login_button.pack(pady=5)

        # Cancel Button
        self.cancel_button = tk.Button(
            self.menu_frame,
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
        self.login_gui = LoginGUI(
            self.root,
            self.show_weather_interface
        )

    def show_weather_interface(self, username):

        # Closes Account Creation Window if Open
        if hasattr(self, "account_gui"):
            if self.account_gui.account_window.winfo_exists():
                self.account_gui.account_window.destroy()

        # Removes Initial Menu
        self.menu_frame.destroy()

        # Updates Program Window
        self.root.title("Weather Data Program")

        # Centers Weather Interface
        window_width = 650
        window_height = 500

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - window_width) //2
        y = (screen_height - window_height) // 2

        self.root.geometry(
            f"{window_width}x{window_height}+{x}+{y}"
        )
        
        # Creates Weather Interface Frame
        self.weather_frame = tk.Frame(
            self.root,
            padx = 20,
            pady = 20
        )
        self.weather_frame.pack(fill = "both", expand = True)

        # Welcome Message
        welcome_label = tk.Label(
            self.weather_frame,
            text = f"Welcome, {username}!",
            font = ("Arial", 12)
        )
        welcome_label.pack(pady = 10)

        # Weather Interface Instructions
        instructions = tk.Label(
            self.weather_frame,
            text = "Enter the weather measurements below. \n"
                   "Click Compute to calculate the results.",
            justify = "center",
            font = ("Arial", 10)
        )
        instructions.pack(pady = (0, 15))

        # Meteorlogical Calculations Frame
        calculation_frame = tk.LabelFrame(
            self.weather_frame,
            text = "Meteorological Calculations",
            font = ("Arial", 12, "bold"),
            padx = 20,
            pady = 15
        )
        calculation_frame.pack(fill = "both", expand = True)

        # Temperature Label
        temperature_label = tk.Label(
            calculation_frame,
            text = "Temperature (°F):"
        )
        temperature_label.grid(
            row = 0,
            column = 0,
            sticky = "e",
            padx = 10,
            pady = 10
        )

        # Temperature Entry
        self.temperature_entry = tk.Entry(
            calculation_frame,
            width = 20,
            justify = "right"
        )
        self.temperature_entry.grid(
            row = 0,
            column = 1,
            padx = 10,
            pady = 10
        )

        # Wind Speed Label
        wind_speed_label = tk.Label(
            calculation_frame,
            text = "Wind Speed (mph):"
        )
        wind_speed_label.grid(
            row = 1,
            column = 0,
            sticky = "e",
            padx = 10,
            pady = 10
        )

        # Wind Speed Entry
        self.wind_speed_entry = tk.Entry(
            calculation_frame,
            width = 20,
            justify = "right"
        )
        self.wind_speed_entry.grid(
            row = 1,
            column = 1,
            padx = 10,
            pady = 10
        )

        # Dew Point Label
        dew_point_label = tk.Label(
            calculation_frame,
            text = "Dew Point (°F):"
        )
        dew_point_label.grid(
            row = 2,
            column = 0,
            sticky = "e",
            padx = 10,
            pady = 10
        )

        # Dew Point Entry
        self.dew_point_entry = tk.Entry(
            calculation_frame,
            width = 20,
            justify ="right"
        )
        self.dew_point_entry.grid(
            row = 2,
            column = 1,
            padx = 10,
            pady = 10
        )

        # Wind Chill Label
        wind_chill_label = tk.Label(
            calculation_frame,
            text = "Wind Chill Factor (°F):"
        )
        wind_chill_label.grid(
            row = 3,
            column = 0,
            sticky = "e",
            padx = 10,
            pady = 10
        )

        # Wind Chill Result
        self.wind_chill_result = tk.Label(
            calculation_frame,
            text = "-",
            width = 20,
            anchor = "e",
            relief = "sunken"
        )
        self.wind_chill_result.grid(
            row = 3,
            column = 1,
            padx = 10,
            pady = 10
        )

        # Cloud Base Label
        cloud_base_label = tk.Label(
            calculation_frame,
            text = "Cloud Base Altitude (feet):"
        )
        cloud_base_label.grid(
            row = 4,
            column = 0,
            sticky = "e",
            padx = 10,
            pady = 10
        )

        # Cloud Base Result
        self.cloud_base_result = tk.Label(
            calculation_frame,
            text = "-",
            width = 20,
            anchor = "e",
            relief = "sunken"
        )
        self.cloud_base_result.grid(
            row = 4,
            column = 1,
            padx = 10,
            pady = 10
        )

        # Frame for Buttons
        button_frame = tk.Frame(calculation_frame)
        button_frame.grid(
            row = 5,
            column = 0,
            columnspan = 2,
            pady = 15
        )

        # Show File Data Button
        self.show_file_button = tk.Button(
            button_frame,
            text = "Show File Data",
            width = 15
        )
        self.show_file_button.pack(side = "left", padx = 10)

        # Compute Button
        self.compute_button = tk.Button(
            button_frame,
            text = "Compute",
            width = 15,
            command = self.process_weather_data
        )
        self.compute_button.pack(side = "left", padx = 10)

        # Exit Button
        self.exit_button = tk.Button(
            button_frame,
            text = "Exit",
            width = 15,
            command = self.root.destroy
        )
        self.exit_button.pack(side = "left", padx = 10)

        # Centers Weather Components
        calculation_frame.grid_columnconfigure(0, weight = 1)
        calculation_frame.grid_columnconfigure(1, weight = 1)

        # Status Message
        self.status_label = tk.Label(
            self.weather_frame,
            text = "Enter Weather measurements and click Compute",
            font = ("Arial", 10),
            fg = "blue"
        )
        self.status_label.pack(pady = 5)
        
        # Clears Results When Weather Inputs Change
        self.temperature_entry.bind(
            "<KeyRelease>",
            self.clear_weather_results
        )

        self.wind_speed_entry.bind(
            "<KeyRelease>",
            self.clear_weather_results
        )

        self.dew_point_entry.bind(
            "<KeyRelease>",
            self.clear_weather_results
        )

        # Places Cursor in Temperature Entry
        self.temperature_entry.focus_set()

    def clear_weather_results(self, event=None):

        # Clears Previous Calculation Results
        self.wind_chill_result.config(text="-")
        self.cloud_base_result.config(text="-")

        # Updates Status Message
        self.status_label.config(
            text = "Weather measurements changed. Click Compute.",
            fg = "blue"
        )
        
    def process_weather_data(self):

        # Retrieves Keyboard Input
        temperature_input = self.temperature_entry.get().strip()
        wind_speed_input = self.wind_speed_entry.get().strip()
        dew_point_input = self.dew_point_entry.get().strip()

        # Clears Previous Results
        self.wind_chill_result.config(text = "-")
        self.cloud_base_result.config(text = "-")

        # Resets Status Message
        self.status_label.config(
            text = "Validating weather measurements...",
            fg = "blue"
        )

        # Checks for Empty Fields
        if not temperature_input or not wind_speed_input or not dew_point_input:

            # Updates Status for Missing Input
            self.status_label.config(
                text = "Error: All weather measurements are required.",
                fg = "red"
            )

            messagebox.showerror(
                "Input Error",
                "All weather measurements are required.",
                parent = self.root
            )
            return

        # Converts Input to Numbers
        try:
            temperature = float(temperature_input)
            wind_speed = float(wind_speed_input)
            dew_point = float(dew_point_input)

        except ValueError:

            # Updates Status for Invalid Numbers
            self.status_label.config(
                text = "Error: Please enter numeric values only.",
                fg = "red"
            )
            
            messagebox.showerror(
                "Input Error",
                "Please enter numeric values only.",
                parent = self.root
            )
            return

        # Checks for Non-finite Numbers
        if not all(math.isfinite(value) for value in
                   (temperature, wind_speed, dew_point)):

            # Updates Status for Non-finite Numbers
            self.status_label.config(
                text = "Error: Please enter finite numeric values.",
                fg = "red"
            )
            
            messagebox.showerror(
                "Input Error",
                "Please enter finite numeric values.",
                parent = self.root
            )
            return

        # Checks for Invalid Wind Speed
        if wind_speed < 0:

            # Updates Status for Invalid Wind Speed
            self.status_label.config(
                text = "Error: Wind Speed cannot be negative.",
                fg = "red"
            )
            
            messagebox.showerror(
                "Input Error",
                "Wind speed cannot be negative.",
                parent = self.root
            )
            return
        
        # Checks for Invalid Dew Point
        if dew_point > temperature:

            # Updates Status for Invalid Dew Point
            self.status_label.config(
                text = "Error: Dew Point cannot exceed temperature.",
                fg = "red"
            )
            
            messagebox.showerror(
                "Input Error",
                "Dew point cannot exceed the air temperature.",
                parent = self.root
            )
            return

        # Calculates Wind Chill Factor
        wind_chill = calculate_wind_chill(
            temperature,
            wind_speed
        )

        # Displays Wind Chill Result
        if wind_chill is not None:
            self.wind_chill_result.config(
                text = f"{wind_chill:.2f} °F"
            )

        else:
            self.wind_chill_result.config(
                text = "Not Applicable"
            )

            # Updates Status for Invalid Wind Chill Conditions
            self.status_label.config(
                text = "Wind chill not applicable under these conditions.",
                fg = "orange"
            )

            messagebox.showwarning(
                "Wind Chill Not Applicable",
                "Wind chill is only defined when the "
                "temperature is 50°F or lower and the "
                "wind speed is greater than 3 mph.",
                parent = self.root

            )

        # Calculates Cloud Base Altitude
        cloud_base = calculate_cloud_base(
            temperature,
            dew_point
        )

        # Displays Cloud Base Result
        self.cloud_base_result.config(
            text = f"{cloud_base:.2f} feet"
        )

        # Displays Success Status
        if wind_chill is not None:
            self.status_label.config(
                text = "Weather Calculations completed successfully.",
                fg = "green"
            )
        
if __name__ == "__main__":
    app = MainWindow()
    app.root.mainloop()
