# Import Module
from tkinter import *
import img2pdf
from tkinter.filedialog import askopenfilenames
from tkinter import messagebox

# Create Object 
root = Tk()
# set Geometry
root.geometry('400x200')

def select_file():
 global file_names
 file_names = askopenfilenames(initialdir = "/",title = "Select File")

# IMAGE TO PDF
def image_to_pdf():
 for index, file_name in enumerate(file_names):
  with open(f"file {index}.pdf", "wb") as f:
   f.write(img2pdf.convert(file_name))
   messagebox.showinfo("Success!!","The file has been successfully converted")

# IMAGES TO PDF
def images_to_pdf():
 with open(f"file.pdf","wb") as f:
  f.write(img2pdf.convert(file_names))
  messagebox.showinfo("Success!!","The files have been successfully converted")



# Add Labels and Buttons
Label(root, text = "IMAGE CONVERSION",
 font = "Raleway", background="pink").pack(pady = 10)

Button(root, text = "Select Images",command=select_file, font = "Raleway",bg='purple').pack(pady = 10)

frame = Frame()
frame.pack(pady = 20)

Button(frame, text = "Image to PDF",command=image_to_pdf, relief = "solid",
    bg = "white", font = "Raleway").pack(side = LEFT,padx = 10)



Button(frame, text = "Images to PDF",command=images_to_pdf, relief = "solid",
    bg = "white",font = "Raleway").pack()

# Execute Tkinter
root.mainloop()