from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import PyPDF2

def browseFiles1():
    filenames = filedialog.askopenfilenames(initialdir="C:/Users/HP/Downloads",
                                            title="Select a File",
                                            filetypes=(("Pdf files", "*.pdf*"),
                                                       ("all files", "*.*")))
    for filename in filenames:
        paths.append(filename)
    update_label2()

def update_label2():
    label2.configure(text="\n".join(paths))

def merge_pdf():
    new_file = filedialog.asksaveasfilename(defaultextension=".pdf",
                                             filetypes=(("PDF files", "*.pdf"), ("All Files", "*.*")),
                                             title="Save merged PDF as")
    if not new_file:
        return  # User canceled saving

    pdfMergerObj = PyPDF2.PdfMerger()
    for pdf in paths:
        try:
            pdfMergerObj.append(pdf)
        except Exception as e:
            print(f"Error reading {pdf}: {e}")

    try:
        with open(new_file, 'wb') as new_file_obj:
            pdfMergerObj.write(new_file_obj)
        print(f"Pdfs {paths} are merged into {new_file} successfully")
        label4.configure(text="Files merged successfully")
    except Exception as e:
        print(f"Error saving merged PDF: {e}")

root = Tk()
root.title("Merge PDFs")
root.geometry('300x300')
root.columnconfigure([0, 1, 2], weight=1)

label1 = Label(root, text="Select files to merge")
label1.grid(column=0, row=0, columnspan=3, pady=10)

label2 = Label(root, text="Selected files")
label2.grid(column=0, row=1, columnspan=3, pady=5)

label4 = Label(root, text="Click below to merge")
label4.grid(column=0, row=5, columnspan=3, pady=5)

btn1 = Button(root, text="Choose Files", command=browseFiles1)
btn1.grid(column=1, row=2, pady=5)

btn3 = Button(root, text="Merge", command=merge_pdf)
btn3.grid(column=1, row=6, pady=5)

paths = []

root.mainloop()
