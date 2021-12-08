import os
import numpy as np
import docx

PATH_DATA_RAW = "./data-raw/"
PATH_DATA_OUTPUT = "./data-output/"

files = os.listdir(PATH_DATA_RAW)
output = docx.Document()

for file in files:
    with open(file) as f:
        text = f.read()
        output.add_paragraph(text)
        output.add_paragraph(" ")


output.save(str(PATH_DATA_OUTPUT) + "combined_file.docx")

print("Files combined. Please find result in 'data-output' folder")