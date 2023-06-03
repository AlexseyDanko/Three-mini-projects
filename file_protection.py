from PyPDF2 import PdfReader, PdfWriter


writer = PdfWriter()
reader = PdfReader("kolobok.pdf")

# Add all pages to the writer
for page in reader.pages:
    writer.add_page(page)

writer.encrypt(user_password=input('Enter The Password: '))

with open("encrypted-pdf.pdf", "wb") as f:
    writer.write(f)
