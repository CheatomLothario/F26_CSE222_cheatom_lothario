import tkinter as tk
from tkinter import scrolledtext

class DataDisplayGUI:

    def __init__(self, parent):

        # Creates Data Display Window
        self.display_window = tk.Toplevel(parent)
        self.display_window.title("Weather Data Project")

        # Sets Window Dimensions
        window_width = 750
        window_height = 450

        # Centers Data Display Window
        screen_width = self.display_window.winfo_screenwidth()
        screen_height = self.display_window.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.display_window.geometry(
            f"{window_width}x{window_height}+{x}+{y}"
        )

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

        # Creates Scrollable Text Display
        self.data_text = scrolledtext.ScrolledText(
            self.display_frame,
            width=85,
            height=18,
            font=("Courier New", 10),
            wrap="none",
            state="disabled"
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

    def close_window(self):

        # Closes Data Display Window
        self.display_window.destroy()


if __name__ == "__main__":

    # Creates Temporary Root Window for Testing
    root = tk.Tk()
    root.withdraw()

    # Opens Data Display Window
    app = DataDisplayGUI(root)

    # Closes Test Application When Display Window Closes
    app.display_window.protocol(
        "WM_DELETE_WINDOW",
        root.destroy
    )

    root.mainloop()
