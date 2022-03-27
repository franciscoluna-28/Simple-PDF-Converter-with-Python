from tkinter import messagebox
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
import functions


#Main window
window = Tk()
window.title("Image to PDF Converter")
window.resizable(height=0, width=0)


#Button Images
exitBtnImg = PhotoImage(file=r"Exit2.png")
convertBtnImg = PhotoImage(file=r"ConvertPDF.png")
selectBtnImg = PhotoImage(file=r"Select2.png")


#Destroy function
def exitFunction():
    warningBox = messagebox.askquestion("Exit application", "Are you sure you want to exit?")
    if warningBox == "yes":
        window.destroy()
        print("Proccess finished")
    

#Select file button
selectBtn = Button(window, command=functions.getFile, border=0, image=selectBtnImg)
selectBtn.grid(columnspan=1, column=1, row=1)


#Convert to PDF button
convertBtn = Button(window, image=convertBtnImg, command=functions.savePDF, border=0)
convertBtn.grid(columnspan=1, column=1, row=2)


#Exit button
exitBtn = Button(window, command=exitFunction, image=exitBtnImg, border=0)
exitBtn.grid(columnspan=1, column=1, row=3)


#Main Canvas
canvas = Canvas(window, width=300, height=100)
canvas.grid(columnspan=3)  
 

#Logo
logo = Image.open("ConverterLogo.png")
logo = ImageTk.PhotoImage(logo)

logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)




""" #Text
mainText = Label(window, text="Insert your images into a PDF document. It's completely easy!", font="Railway")
mainText.grid(columnspan=3) """


window.mainloop() 









