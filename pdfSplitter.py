import PyPDF2
import os

input_pdf = open('02meetingminutes2.pdf', 'rb')
read_input_pdf = PyPDF2.PdfFileReader(input_pdf);
print(read_input_pdf.numPages)
page = read_input_pdf.getPage(0)
print(page.extractText())