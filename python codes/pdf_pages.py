import PyPDF2

def print_pages(pdfFile):
    pdfObj=open(pdfFile,'rb')
    pdfReader=PyPDF2.PdfReader(pdfObj)
    print("The pdf contains",len(pdfReader.pages),"pages")
    pdfObj.close()

pdfFile=input("enter pdf name: ")
if not pdfFile.endswith(".pdf"):
    raise Exception("File is not of the type .pdf")
print_pages(pdfFile=pdfFile)
