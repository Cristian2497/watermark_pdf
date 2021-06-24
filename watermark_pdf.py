import PyPDF2

template = PyPDF2.PdfFileReader(open('dummy.pdf', 'rb')) # target pdf
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb')) # watermark file
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
	page = template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)

	with open('watermarked_output.pdf', 'wb') as file: # export pdf as a new file
		output.write(file)