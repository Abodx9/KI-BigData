import PyPDF2
import csv

# I have created this script to extract and save any pdf file into a csv
  # Cause for some partei, it is so hard to scrap them locally

def extractor(pdf, out):
    with open(pdf, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        with open(out, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            
            for nr in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[nr]
                text = page.extract_text()
                
                # Split text with comma to match the csv, but it does not work and I do not have time to fix it
                lines = text.split(',')
                for line in lines:
                    csv_writer.writerow([line])

    print(f"Done saved to {out}")

pdf_in = input("Paste your pdf file path here: ")
csv_out = input("Enter a name for the output file: ")
extractor(pdf_in, f"{csv_out}.csv")