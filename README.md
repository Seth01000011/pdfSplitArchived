# pdfSplitter

Splits PDFs according to key words

# TODO's

- ~~take in keyword(s), pdf file name and path as arguments~~
- ~~save each section until keyword as its own pdf~~
- ~~save pdfs back to directory~~
- allow arg[3] to be used as output name if it exists, otherwise, use "section\_"
- output text summary of pages used as splits
- output first 20 words on each page used as a split? Last 20 words?
- pick up words on document... Header? to name each file distinctly
- or allow user to input list as names? (No)

## Potential complications

- poor text encoding or OCR
- multiple references to same keyword on one page

## Current set up

- set up virtual environment in cwd
  py -m venv ./
  - execute with source ./bin/activate
- install PyPDF2 with
  pip install PyPDF2
