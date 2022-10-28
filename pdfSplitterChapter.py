from PyPDF2 import PdfReader, PdfWriter
import PyPDF2
from pathlib import Path
import os, sys

if len(sys.argv) < 2:
  raise ValueError("Usage: Type filename.pdf for the pdf you want to split")
# if len(sys.argv) < 3:
  # raise ValueError("Please enter the keyword you are searching for")

# keyword = sys.argv[2]
in_pdf = PdfReader(sys.argv[1])
out_pdf = PdfWriter()
page_breaks = []

if not Path("./split_pdfs/"):
  os.makedirs("./split_pdfs/")

def writeFile(path_and_name):
  with open(path_and_name, 'wb') as file:
    out_pdf.write(file)

def remove_whitespace(string):
  return string.replace(" ", "_")

def prepend_zero_to_nine(iterable):
  if iterable < 10:
    return (str(0) + str(iterable))
  else:
    return str(iterable)

sections = in_pdf.outline
subdir = ""
sub_obj_destination_page_nums = []
sub_obj_path_filename = []
y = 0

for obj in sections: # sections is of type list, contains DESTINATIONS and LISTS
  if isinstance(obj, PyPDF2.generic.Destination): # is a destination (good titles)
    subdir = "./split_pdfs/" + prepend_zero_to_nine(y) + "_" + remove_whitespace(obj.title)
    y = y + 1
    os.makedirs(subdir)
    print("Making subdir " + subdir)
  for sub_obj in obj:
    if isinstance(sub_obj, PyPDF2.generic.Destination):
      page_num = in_pdf.get_destination_page_number(sub_obj)
      sub_obj_destination_page_nums.append(page_num)
      print("Added page number " + str(sub_obj.page))
      title_of_sub_obj = remove_whitespace(sub_obj.title)
      print("Creating filename " + subdir + "/" + title_of_sub_obj + ".pdf")
      sub_obj_path_filename.append(subdir + "/" + title_of_sub_obj + ".pdf")
    

# print(sub_obj_destination_page_num)
# print(sub_obj_path_filename)
# print(len(sub_obj_destination_page_num))
# print(len(sub_obj_path_filename))


for x in range(len(in_pdf.pages)):
  page = in_pdf.pages[x]
  page_num = in_pdf.getPageNumber(page)
  print("Looping through page " + str(page_num))
  if page_num in sub_obj_destination_page_nums:
    writeFile(sub_obj_path_filename[0])
    sub_obj_path_filename.pop(0)
    sub_obj_destination_page_nums.pop(0)
  out_pdf.add_page(page)

# begin at page zero
# is this page number inside sub_obj_destination_page_num?
  # write out with name sub_obj_path_filename
    # AND pop() that bad boy out of sub_obj_path_filename
  # remove first position in list sub_obj_destination_page_num
# add each page to buffer

# sections = in_pdf.outline
# named = in_pdf.named_destinations
# while 
# for each in named:
  # print(each + "\n")
# print(named)


# for x in range(len(in_pdf.pages)):
#   page = in_pdf.pages[x]
#   out_pdf.add_page(page)
#   print("Page " + str(x))
#   text = page.extract_text()
#   if keyword in text:
#     print("Found on page " + str(x))
#     page_breaks.append(x)
#     # write out buffer as pdf
#     writeFile(x)
#     out_pdf = PdfWriter()
# print(page_breaks)
# writeFile("end")
