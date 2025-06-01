# -*- coding: utf-8 -*-
"""
Merge_All_Files_in_Folder_into_one_PDF

Identifies all the PDFs in a folder and merges them into one PDF file.

Instructions-
1. Paste the folder path in the "folder_path" variable below.
2. Run the script
3. Change the file name of "merged_pdf.pdf" which while be saved 
    to the same
    folder.
"""
# Import Packages ------------------------------------------------------
import fitz
import os

# Define Variables -----------------------------------------------------

# Name of the folder containing the screenshots
folder_path = r"PATH/TO/FOLDER"

# Name of the output file that will be placed in the folder_path above
output_name = 'NAME_OF_OUTPUT_PDF.pdf'

# DEFINITIONS ----------------------------------------------------------
# Definitions are custom functions you create
# This definition takes in the input file list and the output folder
def merge_pdfs(input_files, output_folder, output_name):
    file_name = output_name
    output_file = os.path.join(output_folder, file_name)
    output_doc = fitz.open()
    for pdf in input_files:
        source_doc = fitz.open(pdf)
        output_doc.insert_pdf(source_doc)
        source_doc.close()
    output_doc.save(output_file)
    output_doc.close()
    

folder_path = r"C:\Users\test_user\Documents\output\screenshots"
folder_files = os.listdir(folder_path)

input_files = []

for f in folder_files:
    if f[-4:] == '.pdf' or f[-4:] == '.PDF':
        fp = os.path.join(folder_path, f)
        input_files.append(fp)
        
merge_pdfs(input_files, folder_path, output_name)