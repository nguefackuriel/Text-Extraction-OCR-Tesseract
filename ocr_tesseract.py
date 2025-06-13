import sys
import os
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

def ocr_pdf_file(pdf_path, output_file, language='fra'):
    try:
        # We first convert PDF pages to images
        pages = convert_from_path(pdf_path)

        # Text extraction
        full_text = ""
        for i, img in enumerate(pages):
            text = pytesseract.image_to_string(img, lang=language)
            full_text += f"\n\n=== Page {i+1} ===\n{text}"

        # Write to output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_text)

        print(f"Bingoo!! OCR complete. The output is saved to: {output_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python ocr_tesseract.py <input.pdf> <output.txt>")
    else:
        pdf_path = sys.argv[1]
        output_file = sys.argv[2]
        ocr_pdf_file(pdf_path, output_file)
