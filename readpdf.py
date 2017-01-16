import PyPDF2
import os,re

pdf_file = os.path.join("C:\\","Users","manitbi","Desktop","InIntel","TechStuffs","Python","automate-the-boring-stuff-with-python-2015-.pdf")
#pdf_file = os.path.join("C:\\","Users","manitbi","Desktop","InIntel","TechStuffs","Python","Programming Python 3ed.pdf")
pdf_file_obj = open(pdf_file,'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
num_of_pages = pdf_reader.numPages

import_regx = re.compile(r"(import)\s(\w+)\s")
all_import_list = []

for page in range(num_of_pages):
    page_obj = pdf_reader.getPage(page)
    text = page_obj.extractText()
    lines = text.split('\n')

    for line in lines:
        matching_object =  import_regx.search(line)
        if matching_object:
            import_module = matching_object.group()
            module = matching_object.group(2)

            if module not in all_import_list:
                all_import_list.append(module)

with open("module.sh",'w') as fh:
    for im in all_import_list:
        pip_install = "pip install {} \n".format(im)
        fh.write(pip_install)
