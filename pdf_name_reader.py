import os
from openpyxl import Workbook

def save_pdf_names_to_excel(folder_path, output_excel="pdf_names.xlsx"):
    # Get list of all files in the folder
    files = os.listdir(folder_path)
    
    # Filter only PDF files
    pdf_files = [f for f in files if f.lower().endswith(".pdf")]

    # Remove .pdf extension
    pdf_names = [os.path.splitext(f)[0] for f in pdf_files]

    # Create a new Excel workbook and sheet
    wb = Workbook()
    ws = wb.active
    ws.title = "PDF Files"

    # Write header
    ws.append(["PDF File Name"])

    # Write PDF filenames (without .pdf extension)
    for name in pdf_names:
        ws.append([name])

    # Save the workbook
    wb.save(output_excel)

    print(f"Saved {len(pdf_names)} PDF names to '{output_excel}' without file extensions.")

# Example usage
folder_path = "evs_pdfs"  # Replace this with your actual folder path
save_pdf_names_to_excel(folder_path)
