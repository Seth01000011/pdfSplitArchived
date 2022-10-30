# pdfSplitter

Splits PDFs according to key words using PyPDF2 library

## Current set up

- set up virtual environment in current working directory with $ python3 -m venv ./
  - execute virtual environment with $ source ./bin/activate
    - when done splitting pdfs, exit venv with $ deactivate
- install PyPDF2 with
  $ pip install PyPDF2

# Usage

- Place pdfSplitter in directory with pdf to be split
- Use in the terminal with:
  $ python3 pdfSplitter.py [filename.pdf] [string to end section on]

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


