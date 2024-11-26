import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
import os

def select_file():
    file_path = filedialog.askopenfilename(
        title="Select your PDF file",
        filetypes=[("PDF files ", "*.pdf")]
    )
    input_origin_file.delete(0, tk.END)
    input_origin_file.insert(0, file_path)

def extract_pages_pdf():
    # get input values
    origin_pdf_file = input_origin_file.get()
    output_pdf_filename = entrada_output_file.get()
    pages_str = input_pages.get()
    
    # Cases validations
    if not origin_pdf_file:
        messagebox.showerror("Error", "Must select a PDF file.")
        return
    
    if not output_pdf_filename:
        messagebox.showerror("Error", "Must select an output filename.")
        return

    try:
        # get origin file directory
        origin_directory = os.path.dirname(origin_pdf_file)
        
        # add the .pdf extension to the selected name
        pdf_output_fullname = os.path.join(origin_directory, f"{output_pdf_filename}.pdf")
        
        # convert the designed pages to a integer list
        pages = [int(num.strip()) for num in pages_str.split(",") if num.strip().isdigit()]
        
        if not pages:
            messagebox.showerror("Error", "Must enter at least one valid page number.")
            return
        
        # Open the input pdf file in "read binary" mode
        with open(origin_pdf_file, 'rb') as pdf_file:
            read_pdf = PyPDF2.PdfReader(pdf_file)
            write_pdf = PyPDF2.PdfWriter()
            
            # get the selected pages
            for page_num in pages:
                # Rest 1 as list starts in index 0
                if 0 <= page_num - 1 < len(read_pdf.pages):
                    page = read_pdf.pages[page_num - 1]
                    write_pdf.add_page(page)
                else:
                    messagebox.showwarning("Warning", f"The page {page_num} does not exist.")
            
            # Save the output pdf file with just the selected pages
            with open(pdf_output_fullname, 'wb') as output_file:
                write_pdf.write(output_file)
            
            messagebox.showinfo("Success", f"PDF successfully created: {pdf_output_fullname}")
            window.quit()  # Close the window after operation
    
    except Exception as e:
        messagebox.showerror("Error", f"An error has occurred: {e}")

# Create the graphic interface
window = tk.Tk()
window.title("PDF files modifier")
window.geometry("500x300")

# Widgets to select the PDF file
tk.Label(window, text="PDF file: ").pack(pady=5)
input_origin_file = tk.Entry(window, width=50)
input_origin_file.pack(pady=5)
tk.Button(window, text="Select PDF file", command=select_file).pack(pady=5)

# Input field to enter the desired output filename
tk.Label(window, text="Enter an output file name:").pack(pady=5)
entrada_output_file = tk.Entry(window, width=50)
entrada_output_file.pack(pady=5)

# Input field to enter the desired pages from the pdf (comma separated)
tk.Label(window, text="Pages to extract (comma separated):").pack(pady=5)
input_pages = tk.Entry(window, width=50)
input_pages.pack(pady=5)

# Execute button
tk.Button(window, text="Get your new PDF!", command=extract_pages_pdf, bg="green", fg="white").pack(pady=20)

# Launch interface
window.mainloop()
