# pdfSplitter

Splits PDFs according to key words

# TODO's

- take in keyword(s), pdf file name (and path as arguments)
- split pdf
- save pdfs back to directory

## Potential complications

- poor text encoding or OCR
- multiple references to same keyword on one page

## Current set up

- set up virtual environment in cwd
  py -m venv ./
  - execute with source ./bin/activate
- install PyPDF2 with
  pip install PyPDF2
