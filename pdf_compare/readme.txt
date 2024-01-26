Instead of using OCR to extract text, we are using a docx created from a pdf in google drive.
OCR was having too many errors and the docx is much more accurate.

Current files:
pdf_extract.py - not using as too may OCR issues
docx-to-txt.py - converts a docx file (created using google drive) to a txt file.
pdf-ai.py - submits text to openai to create a summary of an insurance policy.