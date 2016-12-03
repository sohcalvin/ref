from nameko.rpc import rpc, RpcProxy
import base64

class Pdf2Text(object):
    name = "pdf2text"

    @rpc
    def convert(self, pdf_bytes_encoded_as_base64_str):
        t = type(pdf_bytes_encoded_as_base64_str)
        print("Begin conversion for input type = ", t )
        if(type(pdf_bytes_encoded_as_base64_str) == bytes) :
            decoded = pdf_bytes_encoded_as_base64_str
        else :
            decoded = base64.b64decode(pdf_bytes_encoded_as_base64_str)

        binStream = io.BytesIO(decoded)
        return readTextFromPDF(binStream)
        # return "pdf converted text"


import pdfminer.pdftypes
import io
import pdfminer.settings
import pdfminer.high_level
import pdfminer.layout

from os import listdir, path, mkdir,rmdir
import pickle
import json
import datetime
import shutil
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

TRANSFORM_SUB ="transformation"
UPLOADED_SUBDIR ="uploaded"
PROCESSED_SUBDIR = "processed"
ARCHIVED_SUBDIR = "archived"
TRANSFORMATION_SEQ_FILE = "transformation_seq.txt"

def readTextFromPDFPath(path_to_pdf):
    # result = ''
    # pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # for i in range(pdfReader.numPages):
    #     pageObj = pdfReader.getPage(i)
    #     result+=pageObj.extractText()
    #     print(result)
    # return result

    pdfFileObj=open(path_to_pdf, "rb")
    result= readTextFromPDF(pdfFileObj)
    pdfFileObj.close()
    return result

def readTextFromPDF(pdfFileObj):

    # outfp = io.StringIO()
    # codec = 'utf-8'
    # laparams = pdfminer.layout.LAParams()
    # for param in ("all_texts", "detect_vertical", "word_margin", "char_margin", "line_margin", "boxes_flow"):
    #     paramv = locals().get(param, None)
    #     if paramv is not None:
    #         setattr(laparams, param, paramv)
    #
    # pdfminer.high_level.extract_text_to_fp(pdfFileObj,**locals())
    # return outfp.getvalue()

    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = pdfFileObj
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()
    fp.close()
    device.close()
    retstr.close()
    return text

if __name__ == "__main__":
    pdfFile = open("sample.pdf", "rb")
    pdfbytes = pdfFile.read()
    pdf2Text= Pdf2Text()
    converted = pdf2Text.convert(pdfbytes)
    print("--------\n", converted)