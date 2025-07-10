import PyPDF2
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *

def split_pdf(originalFile,splits):
    orgFileObj=open(originalFile,'rb')
    orgReaderObj=PyPDF2.PdfReader(orgFileObj)
    splits.append(len(orgReaderObj.pages))
    newFileName=(originalFile.split('/')[-1]).split('.')[0]
    x=0
    lst=[]
    for i in range(0,len(splits)):
        writerObj=PyPDF2.PdfWriter()
        for j in range(x,splits[i]):
            pageObj=orgReaderObj.pages[j]
            writerObj.add_page(pageObj)
            x=splits[i]
        with open (f"{newFileName} split {i+1}.pdf",'wb') as f:
            writerObj.write(f)
            lst.append(f"{newFileName} split {i+1}.pdf")
        writerObj.close()
    orgFileObj.close()
    print("pdf splitted successfully")
    print("Your pdfs are :")
    for pdf in lst:
        print(pdf)

originalFile= filedialog.askopenfilename(initialdir="C:/Users/HP/Downloads",
                                            title="Select a File",
                                            filetypes=(("Pdf files", "*.pdf*"),
                                                       ("all files", "*.*")))
# originalFile=input("Enter the path (use '/') of the file to split: ")
# if not originalFile.endswith(".pdf"):
#     raise Exception("File is not of the type .pdf")
print(f"File selected is {originalFile}")
noOfSplits=int(input("Enter the number of splits to perform (NOTE:n split = n+1 pdfs): "))
splits=[]
for i in range(noOfSplits):
    print(f"Enter page no. of split {i+1}: ")
    i=int(input())
    splits.append(i)

if __name__ == "__main__":
    split_pdf(originalFile=originalFile,splits=splits)