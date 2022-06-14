import pandas as pd
import openpyxl
from tkinter import Tk
from tkinter import filedialog
import os

root = Tk()
root.withdraw()
# get a file
import_file = filedialog.askopenfilename()
export_html_file = './files/table.html'
# check type of file
file_root, file_ext = os.path.splitext(import_file)
print(file_ext)

if file_ext == '.csv':
    imported_df = pd.read_csv(import_file)
elif file_ext == '.xlsx':
    imported_df = pd.read_excel(import_file)

# print(imported_df.columns)
imported_df.to_html(buf=export_html_file)

# parse the file
# build a table with the file

# file requirements
# assumptions

