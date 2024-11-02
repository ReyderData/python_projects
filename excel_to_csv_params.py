import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog, ttk

def select_folder():
    root = tk.Tk()
    root.withdraw()
    chosen_folder = filedialog.askdirectory(title="Select the root folder:")
    return chosen_folder

def convert_excel_to_csv(sep, encoding):
    root_folder = select_folder()
    
    if not root_folder:
        print("No folder selected.")
        return
    
    for actual_folder, subfolders, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".xlsx"):
                excel_path = os.path.join(actual_folder, file)
                file_name = os.path.splitext(file)[0]
                csv_path = os.path.join(actual_folder, f"{file_name}.csv")
                
                if os.path.exists(csv_path):
                    print(f"The file {csv_path} already exists. Skipping...")
                    continue
                
                df = pd.read_excel(excel_path)
                df.to_csv(csv_path, index=False, sep=sep, encoding=encoding)
                
                print(f"File converted: {csv_path}")

def show_options_window():
    # Window config
    root = tk.Tk()
    root.title("CSV Converter")
    root.geometry("350x350")
    root.configure(bg="#f0f0f0")
    root.resizable(False, False)  # avoid resizing the window

    # Frame: center the objects
    frame = tk.Frame(root, bg="#f0f0f0")
    frame.pack(pady=20, padx=20)

    # INFO
    tk.Label(frame, text="Select conversion parameters:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=(0, 10))

    # Dropdown for choosing the separator
    tk.Label(frame, text="Separator:", font=("Arial", 10), bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=(0, 10))
    sep_var = tk.StringVar()
    sep_options = {", (comma)": ",", "; (semicolon)": ";", "/ (slash)": "/", "\t (tab)": "\t"}
    sep_dropdown = ttk.Combobox(frame, textvariable=sep_var, values=list(sep_options.keys()), state="readonly", width=15)
    sep_dropdown.grid(row=1, column=1, sticky="w")
    sep_dropdown.current(0)

    # Dropdown for choosing the encoding
    tk.Label(frame, text="Encoding:", font=("Arial", 10), bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=(0, 10), pady=(10, 0))
    encoding_var = tk.StringVar()
    encoding_options = ["utf-8", "latin_1", "utf-16", "ascii"]
    encoding_dropdown = ttk.Combobox(frame, textvariable=encoding_var, values=encoding_options, state="readonly", width=15)
    encoding_dropdown.grid(row=2, column=1, sticky="w", pady=(10, 0))
    encoding_dropdown.current(0)

    # Conversion button
    def start_conversion():
        sep = sep_options[sep_var.get()]
        encoding = encoding_var.get()
        root.destroy()
        convert_excel_to_csv(sep, encoding)

    # Close window button
    def cancel():
        print("Action cancelled.")
        root.destroy()

    # Add buttons
    tk.Button(frame, text="Select Folder", command=start_conversion, bg="#4CAF50", fg="white", font=("Arial", 10)).grid(row=3, column=0, pady=20, padx=(0, 5))
    tk.Button(frame, text="Cancel", command=cancel, bg="#f44336", fg="white", font=("Arial", 10)).grid(row=3, column=1, pady=20, padx=(5, 0))

    root.mainloop()

if __name__ == "__main__":
    show_options_window()
