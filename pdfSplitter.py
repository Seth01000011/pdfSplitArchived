from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path
import os, sys

if len(sys.argv) < 2:
  raise ValueError("Usage: Type filename.pdf for the pdf you want to split")
if len(sys.argv) < 3:
  raise ValueError("Please enter the keyword you are searching for")

keyword = sys.argv[2]
in_pdf = PdfReader(sys.argv[1])
out_pdf = PdfWriter()
page_breaks = []

if not Path("./split_pdfs/"):
  os.makedirs("./split_pdfs/")

def writeFile(page_number):
  out_pdf_name = "./split_pdfs/section" + str(page_number) + ".pdf"
  with open(out_pdf_name, 'wb') as file:
    out_pdf.write(file)


for x in range(len(in_pdf.pages)):
  page = in_pdf.pages[x]
  out_pdf.add_page(page)
  print("Page " + str(x))
  text = page.extract_text()
  if keyword in text:
    print("Found on page " + str(x))
    page_breaks.append(x)
    # write out buffer as pdf
    writeFile(x)
    out_pdf = PdfWriter()
print(page_breaks)
writeFile("end")
