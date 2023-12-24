import os
import shutil
from tkinter import filedialog as fd 
from tkinter import messagebox as mb
from tkinter import *

def copyFile():  
   fileToCopy = fd.askopenfilename(  title = "Select a file to copy",  filetypes=[("All files", "*.*")])  
   directoryToPaste = "D:\Python\Final Proposal\playlist"
   try:  
      shutil.copy(fileToCopy, directoryToPaste)  
      mb.showinfo(  
         title = "File copied!",  
         message = "The selected file has been copied to the selected location.")  
   except:  
      mb.showerror(  title = "Error!",  message = "Selected file is unable to copy to the selected location. Please try again!")  

if __name__ == "__main__":  
   # creating an object of the Tk() class  
   win_root = Tk()  
   # setting the title of the main window  
   win_root.title("File Explorer - JAVATPOINT")  
   # set the size and position of the window  
   win_root.geometry("300x500+650+250")  
   # disabling the resizable option  
   win_root.resizable(0, 0)  
   # setting the background color to #D8E9E6  
   win_root.configure(bg = "#D8E9E6")  

   c = Button(win_root, text = "copy file", command = copyFile).pack()

   win_root.mainloop()