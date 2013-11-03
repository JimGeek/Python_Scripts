from PyPDF2 import PdfFileReader
from sys import argv

script, pdf_file = argv

pdf_read = PdfFileReader(open(pdf_file,'rb'))
page1 = pdf_read.getPage(0)

pdf_text = page1.extractText()
print pdf_text