from reportlab.pdfgen import canvas

# new PDF file

pdf_file: canvas = canvas.Canvas("exemple.pdf")

# text to the pdf
pdf_file.drawString(72, 720, "Hello, world!")
pdf_file.drawString(72, 700, "Nuevo documento PDF")
pdf_file.drawString(72, 680, "Te gusta | No te gusta")
pdf_file.drawString(72, 660, "Muchas gracias")

# save pdf file
pdf_file.save()
