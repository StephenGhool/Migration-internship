import PyPDF2
import PIL as Image
FILE_PATH = 'C:/Users/SG610854/Desktop/migration/Data/123_plan_pdf.pdf'

with open(FILE_PATH, mode='rb') as f:

    # reader = PyPDF2.PdfFileReader(f)
    reader = PyPDF2.PdfReader(f)
    page = reader.getPage(0)

    print(page.extractText())


# from PyPDF2 import PdfReader

# FILE_PATH = 'C:/Users/SG610854/Desktop/migration/Data/plan_pdf.pdf'

# reader = PdfReader(FILE_PATH)
# number_of_pages = len(reader.pages)
# page = reader.pages[0]
# text = page.extract_text()
# print(text)

# from pdf2docx import Converter

# pdf_file = 'C:/Users/SG610854/Desktop/migration/Data/test.pdf'
# docx_file = 'C:/Users/SG610854/Desktop/migration/Data/test.docx'
# 
# # convert pdf to docx
# cv = Converter(pdf_file)
# cv.convert(docx_file) 
# cv.close()

# with open(FILE_PATH, 'rb') as pdf_file:
#     pdf_reader = PyPDF2.PdfReader(pdf_file)
#     print(f'Number of Pages in PDF File is {pdf_reader.getNumPages()}')
#     print(f'PDF Metadata is {pdf_reader.documentInfo}')
#     print(f'PDF File Author is {pdf_reader.documentInfo["/Author"]}')
    
#     # printing first page contents
#     pdf_page = pdf_reader.getPage(0)
#     print(pdf_page.extractText())

#     # extracting images from the 1st page
#     page0 = pdf_reader.getPage(0)

#     if '/XObject' in page0['/Resources']:
#         xObject = page0['/Resources']['/XObject'].getObject()

#         for obj in xObject:
#             if xObject[obj]['/Subtype'] == '/Image':
#                 size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
#                 data = xObject[obj].getData()
#                 if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
#                     mode = "RGB"
#                 else:
#                     mode = "P"

#                 if '/Filter' in xObject[obj]:
#                     if xObject[obj]['/Filter'] == '/FlateDecode':
#                         img = Image.frombytes(mode, size, data)
#                         img.save(obj[1:] + ".png")
#                     elif xObject[obj]['/Filter'] == '/DCTDecode':
#                         img = open(obj[1:] + ".jpg", "wb")
#                         img.write(data)
#                         img.close()
#                     elif xObject[obj]['/Filter'] == '/JPXDecode':
#                         img = open(obj[1:] + ".jp2", "wb")
#                         img.write(data)
#                         img.close()
#                     elif xObject[obj]['/Filter'] == '/CCITTFaxDecode':
#                         img = open(obj[1:] + ".tiff", "wb")
#                         img.write(data)
#                         img.close()
#                 else:
#                     img = Image.frombytes(mode, size, data)
#                     img.save(obj[1:] + ".png")
#     else:
#         print("No image found.")

#     # reading all the pages content one by one
#     for page_num in range(pdf_reader.numPages):
#         pdf_page = pdf_reader.getPage(page_num)
#         print(pdf_page.extractText())