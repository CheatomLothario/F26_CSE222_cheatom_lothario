import tkinter as tk
from tkinter import scrolledtext

class DataDisplayGUI:

    def __init__(self, parent):

        # Creates Data Display Window
        self.display_window = tk.Toplevel(parent)
        self.display_window.title("Weather Data Project")

        # Sets Window Dimensions
        window_width = 850
        window_height = 500

        # Centers Data Display Window
        screen_width = self.display_window.winfo_screenwidth()
        screen_height = self.display_window.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.display_window.geometry(
            f"{window_width}x{window_height}+{x}+{y}"
        )

        # Tracks Number of Weather Entries Displayed
        self.entry_count = 0

        # Creates Main Frame
        self.display_frame = tk.Frame(
            self.display_window,
            padx=15,
            pady=15
        )
        self.display_frame.pack(fill="both", expand=True)

        # Window Title
        title_label = tk.Label(
            self.display_frame,
            text="Weather Data Output",
            font=("Arial", 16, "bold")
        )
        title_label.pack(pady=(0, 10))

        # Instructions
        instructions = tk.Label(
            self.display_frame,
            text="Weather measurements and calculated results "
                 "will appear below.",
            font=("Arial", 10)
        )
        instructions.pack(pady=(0, 10))

        # Displays Number of Recorded Weather Entries
        self.entry_count_label = tk.Label(
            self.display_frame,
            text="Total Weather Entries: 0",
            font=("Arial", 10, "bold"),
            fg="blue"
        )
        self.entry_count_label.pack(pady=(0, 10))

        # Creates Scrollable Text Display
        self.data_text = scrolledtext.ScrolledText(
            self.display_frame,
            width=85,
            height=18,
            font=("Courier New", 11),
            wrap="none",
            state="disabled",
            bg="#F5F5F5",
            fg="black",
            padx=10,
            pady=10
        )
        self.data_text.pack(fill="both", expand=True)

        # Close Button
        close_button = tk.Button(
            self.display_frame,
            text="Close",
            width=15,
            command=self.close_window
        )
        close_button.pack(pady=(10, 0))

        # Brings Window to Front
        self.display_window.lift()

        # Handles Window Close Button
        self.display_window.protocol(
            "WM_DELETE_WINDOW",
            self.close_window
        )

        # Displays Table Headings
        self.display_headings()

    def display_headings(self):

        # Creates Column Headings
        headings = (
            f"{'Temp (F)':<12}"
            f"{'Wind (mph)':<12}"
            f"{'Dew Pt (F)':<12}"
            f"{'Wind Chill':<15}"
            f"{'Cloud Base':<15}\n"
        )

        # Creates Separator Line
        separator = "-" * 66 + "\n"

        # Enables Text Widget
        self.data_text.config(state="normal")

        # Inserts Headings and Separator
        self.data_text.insert(tk.END, headings)
        self.data_text.insert(tk.END, separator)

        # Disables Text Widget
        self.data_text.config(state="disabled")

    def append_weather_data(
        self,
        temperature,
        wind_speed,
        dew_point,
        wind_chill,
        cloud_base
    ):

        # Handles Wind Chill When Not Applicable
        if wind_chill is None:
            wind_chill_text = "N/A"
        else:
            wind_chill_text = f"{wind_chill:.2f}"

        # Formats Weather Data into Columns
        data_row = (
            f"{temperature:<12.2f}"
            f"{wind_speed:<12.2f}"
            f"{dew_point:<12.2f}"
            f"{wind_chill_text:<15}"
            f"{cloud_base:<15.2f}\n"
        )

        # Enables Text Widget
        self.data_text.config(state="normal")

        # Appends Weather Data
        self.data_text.insert(tk.END, data_row)

        # Scrolls to Most Recent Entry
        self.data_text.see(tk.END)

        # Disables Text Widget
        self.data_text.config(state="disabled")

        # Increased Weather Entry Count
        self.entry_count += 1

        # Updates Entry Count Label
        self.entry_count_label.config(
            text=f"Total Weather Entries: {self.entry_count}"
        )

    def close_window(self):

        # Closes Data Display Window
        self.display_window.destroy()


if __name__ == "__main__":

    # Creates Temporary Root Window
    root = tk.Tk()
    root.withdraw()

    # Creates Data Display Window
    app = DataDisplayGUI(root)

    # Adds Sample Weather Data
    app.append_weather_data(
        40,
        10,
        30,
        33.64,
        2272.73
    )

    app.append_weather_data(
        35,
        15,
        25,
        25.58,
        2272.73
    )

    app.append_weather_data(
        60,
        8,
        45,
        None,
        3409.09
    )

    # Ensures Both Close Methods Exit the Test
    app.display_window.protocol(
        "WM_DELETE_WINDOW",
        root.destroy
    )

    # Updates Close Button for Standalone Testing
    for widget in app.display_frame.winfo_children():
        if isinstance(widget, tk.Button):
            widget.config(command=root.destroy)

    root.mainloop()
