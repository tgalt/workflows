import sys
import os
import pytesseract
from PIL import Image
from pdf2image import convert_from_path

def pdf_to_text(pdf_file):
    # Convert PDF to images
    images = convert_from_path(pdf_file)

    # Initialize an empty string to hold the extracted text
    text = ''

    # Loop through each image and perform OCR
    for i in range(len(images)):
        text += pytesseract.image_to_string(images[i], lang='eng')

    # Determine the base name of the pdf file (without the extension)
    base_name = os.path.splitext(pdf_file)[0]

    # Append '.txt' to the base name to create the txt file name
    txt_file = base_name + '.txt'

    # Write the extracted text to a txt file
    with open(txt_file, 'w') as file:
        file.write(text)

# Use the function with command-line arguments
if len(sys.argv) != 2:
    print("Usage: python script.py [input.pdf]")
else:
    pdf_to_text(sys.argv[1])
