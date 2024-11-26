# python_projects
          I will upload little projects in Python
------------------------------------------------------------

* excel_to_csv.py is a semi-automatic converter from .xlsx to .csv

You run the .py and the only thing you ned to do is select the root folder which 
contains all the excel files you want to convert to csv and It will iterate through all subfolders
in it and create the csv files, if one already exists, it wil be skipped

At the moment, the separator and encoding are a comma and latin as default, can update to pass them as 
arguments to the function.

* excel_to_csv_params.py

  Updated the previous version to further customization of the converter.
  Now it is possible to choose between a few separators and encodings, after that you select
  the desired folder as in the other program

* zip_unzip_files.py

  A graphic window that allows the user to find a zip file in the unit and unzip it, or viceversa.
  You can modify the .zip filename and the destination folder

* extract_PDF_pages.py

  A graphic window that allows to find a pdf file in your system and select which pages of that pdf do you want
  and it creates a pdf with only those pages, indicated with the numbers separated by commas
