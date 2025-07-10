import PyPDF2
from tkinter import *
from tkinter import filedialog
import os

def split_pdf(original_file, splits):
    new_file_folder = filedialog.askdirectory(title="Select Folder to Save")
    if not new_file_folder:
        return  # User canceled saving

    org_file_obj = open(original_file, 'rb')
    org_reader_obj = PyPDF2.PdfReader(org_file_obj)
    splits.append(len(org_reader_obj.pages))
    new_file_name = (original_file.split('/')[-1]).split('.')[0]
    x = 0
    lst = []
    for i in range(0, len(splits)):
        writer_obj = PyPDF2.PdfWriter()
        for j in range(x, splits[i]):
            page_obj = org_reader_obj.pages[j]
            writer_obj.add_page(page_obj)
            x = splits[i]
        # Construct the full path for the new PDF file
        new_file_path = os.path.join(new_file_folder, f"{new_file_name}_split_{i+1}.pdf")
        with open(new_file_path, 'wb') as f:
            writer_obj.write(f)
            lst.append(new_file_path)
        writer_obj.close()
    org_file_obj.close()
    print("PDF splitted successfully")
    print("Your PDFs are :")
    for pdf in lst:
        print(pdf)


def browse_file():
    filename = filedialog.askopenfilename(title="Select a PDF File", filetypes=(("PDF files", "*.pdf*"), ("All files", "*.*")))
    entry_file.delete(0, END)
    entry_file.insert(0, filename)

def split():
    original_file = entry_file.get()
    if not original_file:
        print("Please select a PDF file.")
        return
    splits = []
    try:
        no_of_splits = int(entry_splits.get())
    except ValueError:
        print("Please enter a valid number of splits.")
        return
    for i in range(no_of_splits):
        try:
            split_page = int(entry_page.get())
        except ValueError:
            print(f"Please enter a valid page number for split {i+1}.")
            return
        splits.append(split_page)
    split_pdf(original_file, splits)

root = Tk()
root.title("Split PDF")
root.geometry("600x200")

frame = Frame(root)
frame.pack(pady=20)

label_file = Label(frame, text="Select PDF File:")
label_file.grid(row=0, column=0, padx=10)

entry_file = Entry(frame, width=40)
entry_file.grid(row=0, column=1, padx=10)

button_browse = Button(frame, text="Browse", command=browse_file)
button_browse.grid(row=0, column=2, padx=10)

label_splits = Label(frame, text="Number of Splits:")
label_splits.grid(row=1, column=0, padx=10)

entry_splits = Entry(frame, width=10)
entry_splits.grid(row=1, column=1, padx=10)

label_pages = Label(frame, text="Enter split page numbers:")
label_pages.grid(row=2, column=0, padx=10)

entry_page = Entry(frame, width=10)
entry_page.grid(row=2, column=1, padx=5)

button_split = Button(frame, text="Split PDF", command=split)
button_split.grid(row=3, column=1, pady=10)

root.mainloop()
