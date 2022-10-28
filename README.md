# pdfSplitter

Splits PDFs according to keyword(s)

# Usage

- Place pdfSplitter in directory with pdf to be split
- Use in the terminal with:
  $ python3 pdfSplitter.py [filename.pdf] [string to end section on]
- pdfSplitter will create a subdirectory named "./split*pdfs/" and output
  the various sections as "section*[number].pdf"

# TODO's

- ~~take in keyword(s), pdf file name and path as arguments~~
- ~~save each section until keyword as its own pdf~~
- ~~save pdfs back to directory~~
- allow arg[3] to be used as output name if it exists, otherwise, use "section\_"
- output text summary of pages used as splits
- output first 20 words on each page used as a split? Last 20 words?
- pick up words on document... Header? to name each file distinctly
- or allow user to input list as names? (No)
- allow keyword to be a list of keywords, and split on finding any
  of them in the document

## Potential complications

- poor text encoding or OCR causing a failure to identify or misidentification

## Current set up

- set up virtual environment in cwd
  py -m venv ./
  - execute with source ./bin/activate
  - exit venv with deactivate
- install PyPDF2 with
  pip install PyPDF2
