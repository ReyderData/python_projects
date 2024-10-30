import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog

def select_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    chosen_folder = filedialog.askdirectory(title="Select the root folder")
    return chosen_folder

def convert_excel_to_csv():
    # Elect the root folder
    root_folder = select_folder()
    
    if not root_folder:
        print("No folder selected.")
        return
    
    # Iterate all subfolders and files inside the root folder
    for actual_folder, subfolders, files in os.walk(root_folder):
        # Process all the Excel files (.xlsx) in the actual folder
        for file in files:
            if file.endswith(".xlsx"):
                excel_path = os.path.join(actual_folder, file)
                
                # Get the file name w/out the extension
                file_name = os.path.splitext(file)[0]
                
                # Create the full path to create the csv file
                csv_path = os.path.join(actual_folder, f"{file_name}.csv")
                
                # Check if the .csv already exists
                if os.path.exists(csv_path):
                    print(f"El file {csv_path} ya existe. Saltando...")
                    continue  # Pass if this file already exists
                
                # Read the excel file
                df = pd.read_excel(excel_path)
                
                # Save the DataFrame as CSV with latin_1 encoding and comma separated
                df.to_csv(csv_path, index=False, sep=',', encoding='latin_1')
                
                print(f"file converted: {csv_path}")

if __name__ == "__main__":
    convert_excel_to_csv()
