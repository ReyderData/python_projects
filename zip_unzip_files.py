import tkinter as tk
from tkinter import filedialog, messagebox
import os
import zipfile

# Function show main menu
def show_menu():
    clean_window()
    tk.Button(window, text="Zip files", command=show_zip).pack(pady=20)
    tk.Button(window, text="Unzip files", command=show_unzip).pack(pady=20)

# Function clean window
def clean_window():
    for widget in window.winfo_children():
        widget.destroy()

# Interface functions
def show_zip():
    clean_window()
    tk.Label(window, text="Files selected:").pack(anchor="w", padx=10, pady=5)
    tk.Label(window, textvariable=files_list, justify="left", wraplength=580, bg="white", relief="sunken", height=5).pack(fill="x", padx=10, pady=5)
    tk.Button(window, text="Select files", command=select_files).pack(pady=5)
    tk.Label(window, text="Output directory:").pack(anchor="w", padx=10, pady=5)
    tk.Entry(window, textvariable=output_directory, width=50).pack(side="left", padx=10)
    tk.Button(window, text="Select directory", command=select_directory).pack(side="left", padx=5)
    tk.Label(window, text="ZIP file name:").pack(anchor="w", padx=10, pady=5)
    tk.Entry(window, textvariable=zip_file_name, width=50).pack(fill="x", padx=10, pady=5)
    tk.Button(window, text="Create ZIP", command=create_zip).pack(pady=20)
    tk.Button(window, text="Back to the menu", command=show_menu).pack(pady=10)

def show_unzip():
    clean_window()
    tk.Label(window, text="Select file to unzip:").pack(anchor="w", padx=10, pady=5)
    tk.Button(window, text="Select ZIP", command=select_zip).pack(pady=5)
    tk.Label(window, text="Output directory:").pack(anchor="w", padx=10, pady=5)
    tk.Entry(window, textvariable=output_directory, width=50).pack(side="left", padx=10)
    tk.Button(window, text="Select directory", command=select_directory).pack(side="left", padx=5)
    tk.Button(window, text="Unzip file", command=unzip_files).pack(pady=20)
    tk.Button(window, text="Back to the menu", command=show_menu).pack(pady=10)


# Zip functions
def select_files():
    files = filedialog.askopenfilenames(title="Select files")
    if files:
        files_list.set("\n".join(files))
    else:
        files_list.set("No files selected.")

def select_directory():
    directory = filedialog.askdirectory(title="Select an output directory")
    if directory:
        output_directory.set(directory)
    else:
        messagebox.showinfo("Info", "No directory selected.")

def create_zip():
    files = files_list.get().split("\n")
    if not files or files[0] == "No files selected.":
        messagebox.showerror("Error", "Must select at least one file.")
        return

    destination = output_directory.get()
    if not destination:
        destination = os.path.dirname(files[0])  # Use directory of the first file if none is selected.

    zip_name = zip_file_name.get().strip()
    if not zip_name:
        messagebox.showerror("Error", "ZIP file name cannot be empty.")
        return

    # Ensure the file name ends with .zip
    if not zip_name.endswith(".zip"):
        zip_name += ".zip"

    zip_path = os.path.join(destination, zip_name)
    try:
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for archivo in files:
                zipf.write(archivo, os.path.basename(archivo))  # Add to ZIP with base name
        messagebox.showinfo("Success", f"ZIP file created at: {zip_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Error creating the ZIP file: {e}")

# Unzip functions
def select_zip():
    zip_file = filedialog.askopenfilename(title="Select ZIP File", filetypes=[("ZIP files", "*.zip")])
    if zip_file:
        selected_file.set(zip_file)
    else:
        selected_file.set("No ZIP file selected.")

def unzip_files():
    zip_file = selected_file.get()
    if not zip_file or zip_file == "No ZIP file selected.":
        messagebox.showerror("Error", "You must select a ZIP file.")
        return

    destination = output_directory.get()
    if not destination:
        messagebox.showerror("Error", "You must select an output directory.")
        return

    try:
        with zipfile.ZipFile(zip_file, 'r') as zipf:
            zipf.extractall(destination)
        messagebox.showinfo("Success", f"ZIP file extracted to: {destination}")
    except Exception as e:
        messagebox.showerror("Error", f"Error extracting the ZIP file: {e}")

# Main window config
window = tk.Tk()
window.title("ZIP File Manager")
window.geometry("600x400")

# Vars to storage data selected
files_list = tk.StringVar(value="No files selected.")
output_directory = tk.StringVar(value="")
zip_file_name = tk.StringVar(value="files_compressed.zip")  # Default ZIP file name
selected_file = tk.StringVar(value="No ZIP file selected.")

# Show the menu at the beginning
show_menu()

window.mainloop()
