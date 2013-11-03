from PyPDF2 import PdfFileMerger
from sys import argv

script, pdf1, pdf2, pdf = argv

merged_pdf = PdfFileMerger()

file1 = open(pdf1,'rb')
file2 = open(pdf2,'rb')

merged_pdf.append(file1)
merged_pdf.append(file2)

output = open(pdf,'wb')
merged_pdf.write(output)