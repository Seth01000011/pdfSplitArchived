from PyPDF2 import PdfReader
import os, sys

if len(sys.argv) < 2:
  raise ValueError("Usage: Type filename.pdf for the pdf you want to split")
if len(sys.argv) < 3:
  raise ValueError("Please enter the keyword you are searching for")

keyword = sys.argv[2]
input_pdf = PdfReader(sys.argv[1])
page_breaks = []
for x in range(len(input_pdf.pages)):
  page = input_pdf.pages[x]
  print("Page " + str(x))
  text = page.extract_text()
  if keyword in text:
    print("Found on page " + str(x))
    page_breaks.append(x)
print(page_breaks)