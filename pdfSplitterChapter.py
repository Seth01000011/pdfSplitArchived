from PyPDF2 import PdfReader, PdfWriter
import PyPDF2
from pathlib import Path
import os, sys 
from multiprocessing import Process

if len(sys.argv) < 2:
  raise ValueError("Usage: Type filename.pdf for the pdf you want to split")
# if len(sys.argv) < 3:
  # raise ValueError("Please enter the keyword you are searching for")

# keyword = sys.argv[2]
print("Loading pdf...")
in_pdf = PdfReader(sys.argv[1])
out_pdf = PdfWriter()
page_breaks = []

if not Path("./split_pdfs/").exists(): # create split_pdf subdir in cwd if it doesn't exist
  os.makedirs("./split_pdfs/")

def writeFile(path_and_name):
  with open(path_and_name, 'wb') as file:
    out_pdf.write(file)

def remove_whitespace(string):
  string.replace("/","_AND_") # replace slash used as an "and" in some destination titles
  return string.replace(" ", "_")

def prepend_zero_to_nine(iterable): # prepends a "0" to numbers less than 2 digits
  if iterable < 10:
    return (str(0) + str(iterable))
  else:
    return str(iterable)

sections = in_pdf.outline
subdir = "" # create subdir as a global variable to carry between functions
sub_obj_destination_page_nums = [] # global array to hold destination page numbers
sub_obj_path_filename = "" # global array to hold name of each section, matching the 
                           # global array of destination page numbers
y = 0  # iterator for working through arrays of page numbers and destination names 
last_page_number_written = 0

for obj in sections: # sections is of type list, contains DESTINATIONS and LISTS
  # 'obj' refer to 'chapters' encoded in the PDF file
  print("Looking for chapters...")
  if isinstance(obj, PyPDF2.generic.Destination): # is a destination (good titles)
    subdir = "./split_pdfs/" + prepend_zero_to_nine(y) + "_" + remove_whitespace(obj.title)
    y = y + 1 # increment iterator one to move along subsection stuff
    if not Path(subdir).exists():
      os.makedirs(subdir)
    print("Making subdir " + subdir)
  print("Looking for sections...")
  for sub_obj in obj: # sub_obj refers to subsections within chapters, encoded in PDF
    if isinstance(sub_obj, PyPDF2.generic.Destination):
      # page_num = in_pdf.get_destination_page_number(sub_obj) # get page num of subsection
      # sub_obj_destination_page_nums.append(page_num) # save page num to compare
                                                     # when splitting pdf
                          
      # print("Added page number " + str(sub_obj.page))
      title_of_sub_obj = remove_whitespace(sub_obj.title)
      # print("Found page_num in sub_obj_destination page nums, creating pdf...")
      # out_pdf.add_metadata(in_pdf.metadata)
      current_page = in_pdf.get_destination_page_number(sub_obj)
      if sub_obj_path_filename == "":

        sub_obj_path_filename = (subdir + "/TABLE_OF_CONTENTS.pdf")
      print("Compressing and adding pages to buffer...")
      for x in range(last_page_number_written, current_page):
        compressed_page = in_pdf.pages[x]
        compressed_page.compress_content_streams()
        out_pdf.add_page(compressed_page)


      # get page number of page subobj


      last_page_number_written = current_page
      out_pdf.remove_links() # supposed to reduce size of output PDFs
      if not Path(sub_obj_path_filename).exists():# check if program has already 
                                                     # written file
        print("Writing file " + sub_obj_path_filename)                                                     
        writeFile(sub_obj_path_filename)
      # print("Creating filename " + subdir + "/" + title_of_sub_obj + ".pdf")
      sub_obj_path_filename = (subdir + "/" + title_of_sub_obj + ".pdf")
      # sub_obj_path_filename.append(subdir + "/" + title_of_sub_obj + ".pdf")
      print("Clearing out_pdf buffer")
      out_pdf = PdfWriter()
# sub_obj_path_filename.append(subdir + "/" + "end.pdf")
# sub_obj_destination_page_nums.append(len(in_pdf.pages)) # last in array is total # pages
writeFile(subdir + "/" + "end.pdf")
    

# print(sub_obj_destination_page_num)
# print(sub_obj_path_filename)
# print(len(sub_obj_destination_page_num))
# print(len(sub_obj_path_filename))

k = 0 # iterator for sub_obj_path_filename and sub_obj... lists

# for x in range(len(in_pdf.pages)):
#   page = in_pdf.pages[x]
#   page_num = in_pdf.getPageNumber(page)
#   print("Looping through page " + str(page_num))
#   if page_num in sub_obj_destination_page_nums:
#     print("Found page_num in sub_obj_destination page nums, creating pdf...")
#     # out_pdf.add_metadata(in_pdf.metadata)
#     out_pdf.remove_links() # supposed to reduce size of output PDFs
#     if not Path(sub_obj_path_filename[k]).exists():# check if program has already 
#                                                    # written file
#       writeFile(sub_obj_path_filename[k])
#     else:
#       print("Already exists! Skipping...")
#     k = k + 1
#     print("Clearing out_pdf buffer")
#     out_pdf = PdfWriter()
#     print("Writing file...")
#   out_pdf.add_page(page)
# writeFile(sub_obj_path_filename[k]) # prints out the remaining pages in buffer (if any)
