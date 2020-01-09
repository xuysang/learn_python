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
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)
        text = retstr.getvalue()

        break
    strs = text.replace(" ", "").split()
    fp.close()
    device.close()
    retstr.close()
    try:
        title = strs[0] + strs[1] + strs[2]
    except IndexError:
        print("此为图片")
        return "此为图片"
    if '公告' in str(strs[0]) or '说明书' in str(strs[0]) or '协议' in str(strs[0]) or ':' in str(strs[1]) or '：' in str(strs[1]):
        title = strs[0]
    else:
        if '公告' in str(strs[1]) or '说明书' in str(strs[1]) or '协议' in str(strs[1]) or ':' in str(strs[2]) or '：' in str(strs[2]):
            title = strs[0] + strs[1]
        else:
            if '公告' in str(strs[2]) or '说明书' in str(strs[2]) or '协议' in str(strs[2]) or ':' in str(strs[3]) or '：' in str(strs[3]):
                title = strs[0] + strs[1] + strs[2]


    return title
'''

def file_name(path):
    p = Path(path)
    list_name = [x.name for x in list(p.glob('**/*.pdf'))]
    # print(list_name)
    return list_name


list_name = file_name(r'D:\Pycharm\pdf解析')
for each in list_name:
    # print(each)
    convert_pdf_to_txt(each)
    # import pdb
    # pdb.set_trace()
'''