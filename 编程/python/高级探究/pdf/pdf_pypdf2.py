from PyPDF2 import PdfFileReader
def extract_info(pdf_path):
	with open(pdf_path,'rb') as f:
		pdf = PdfFileReader(f)
		information = pdf.getDocumentInfo()
	title = information.title
	print(information)

extract_info("大成基金大成优势企业混合关于大成优势企业混合型证券投资基金基金合同生效公告.pdf")