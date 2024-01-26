import sys
import os
from docx import Document

def docx_to_text(docx_file):
    # Open the docx file
    doc = Document(docx_file)

    # Initialize an empty string to hold the extracted text
    text = ''

    # Loop through each paragraph in the document
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'

    # Determine the base name of the docx file (without the extension)
    base_name = os.path.splitext(docx_file)[0]

    # Append '.txt' to the base name to create the txt file name
    txt_file = base_name + '.txt'

    # Write the extracted text to a txt file
    with open(txt_file, 'w') as file:
        file.write(text)

# Use the function with command-line arguments
if len(sys.argv) != 2:
    print("Usage: python script.py [input.docx]")
else:
    docx_to_text(sys.argv[1])
