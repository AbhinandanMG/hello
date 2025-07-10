import PyPDF2
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *


def pdfRotate(originalFile,newFile,rotation):
    pdfObj=open(originalFile,'rb') #open pdf as object in read binary mode
    pdfReaderObj=PyPDF2.PdfReader(pdfObj) #creating pdfReader object
    pdfWriterObj=PyPDF2.PdfWriter()    #creating pdfWriter object

    for page in pdfReaderObj.pages:
        pageObj=page #creating page object 
        pageObj.rotate(rotation)
        pdfWriterObj.add_page(pageObj) #adding page object to pdfWriter object

    newFileObj=open(newFile,'wb') #open new pdf object in write binary mode
    pdfWriterObj.write(newFileObj) #write new pdf Object in pdf writer object
    pdfObj.close() #close all objects
    newFileObj.close()
    print("PDF rotated successfully")

originalFile= filedialog.askopenfilename(initialdir="C:/Users/HP/Downloads",
                                            title="Select a File",
                                            filetypes=(("Pdf files", "*.pdf*"),
                                                       ("all files", "*.*")))
newFile=originalFile.replace('.pdf','rotated.pdf')
rotation=int(input("enter rotation angle(in multiples of 90): "))

if __name__ == "__main__":
    pdfRotate(originalFile,newFile,rotation)
