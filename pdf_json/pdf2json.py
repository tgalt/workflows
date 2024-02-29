import fitz  # PyMuPDF
import json

# Function to read PDF and store its text into a JSON file
def pdf_to_json(pdf_path, json_path):
    # Open the provided PDF file
    pdf_document = fitz.open(pdf_path)
    pdf_data = {}

    # Iterate through each page of the PDF
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        # Extract text from the current page
        text = page.get_text()
        # Store the extracted text using the page number as key
        pdf_data[f"page_{page_num + 1}"] = text

    # Close the PDF after reading
    pdf_document.close()

    # Save our extracted data to a JSON file
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(pdf_data, json_file, ensure_ascii=False, indent=4)

    print(f"PDF text has been successfully extracted to {json_path}")

# Replace 'your_pdf_path.pdf' with the path to the PDF file you want to convert
# and 'output.json' with the desired output JSON file name.