# 2022Nov01
Unfortunately, PyPDF2 does not have good support in terms of splitting
a PDF document - The non-example document I was splitting (300MB) resulted
in multiple 300MB pages. This would balloon the document into well over 10GB.
Since this library is not a good fit, I am archiving this work and using 
pymupdf instead.

In addition, PyPDF2 was taking ~1 minute per page of PDF processed - And the
document was well over 2,000 pages. This simply was not sustainable.

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


