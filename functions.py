from tkinter import filedialog
from PIL import Image
from tkinter import messagebox

#This only converts one type of file

imageList = []


def getFile():
    global img1
    acceptedTypes = [("JPG files", "*.jpg"),("JPEG files", "*.jpeg"), ("JPEG files", "*.jfif")]
    importFilePath = filedialog.askopenfilenames(filetypes=acceptedTypes)  
    
    for img in importFilePath:
        img1 = Image.open(img)
        img1.convert("RGB")
        
        if importFilePath != "":
            imageList.append(img1)
            
    
def savePDF():
    global img1
    exportFilePath = filedialog.asksaveasfilename(defaultextension=".pdf")
    
    try:
        if imageList != "":
            length = len(imageList)
            imageList.pop(length - 1)
            img1.save(exportFilePath, save_all=True, append_images=imageList)
            
            messagebox.showinfo("Warning", "Successfully converted to PDF!")
            
    except:
         messagebox.showerror("Warning", "You must have selected at least a valid image before!")
    

    
     