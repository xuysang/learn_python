from pathlib import Path
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
        text = retstr.getvalue()

        break
    strs = text.replace(" ", "").split()
    fp.close()
    device.close()
    retstr.close()
    if '公告' in str(strs[0]):
        title = strs[0]
    else:
        title = strs[0]+strs[1]
    print(title)
    return title

def file_name(path):
    p = Path(path)
    list_name = [x.name for x in list(p.glob('**/*.pdf'))]
    print(list_name)
    return list_name

list_name = file_name(r'\\10.3.2.15\数据二部共享\基金组\四大报数据源下载\证监会公告\2019-12-25')
for each in list_name:
    convert_pdf_to_txt(each)

