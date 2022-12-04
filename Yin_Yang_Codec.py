import tkinter as tk
from tkinter import filedialog, messagebox
import os
from main import encoding, decoding

def encode():
    window = tk.Tk()
    window.title("Encoder") 
    savedPath = tk.Entry(window, width=20)
    savedPath.pack()
    def browseFiles():

        if os.path.isdir(savedPath.get()) == False:
            messagebox.showinfo("Wrong diectory", "Please select correct directory")
            return
        inputFile = filedialog.askopenfilename(initialdir = "/", title = "Select a File",
                                                filetypes = (('All Files',"*"),))
        print(inputFile)
        print(savedPath.get())
        encoding(inputFile,savedPath.get())
        # use filename and savedPath
    
    
    tk.Button(window, text="Browse Files", command=browseFiles).pack()
    window.mainloop()
    

def decode():
    window = tk.Tk()
    window.title("Decoder") 
    savedPath = tk.Entry(window, width=20)
    savedPath.pack()
    def browseFiles():

        if os.path.isdir(savedPath.get()) == False:
            messagebox.showinfo("Wrong diectory", "Please select correct directory")
            return
        inputFilePath = filedialog.askopenfilename(initialdir = "/", title = "Select a File",
                                                filetypes = (("Text files", "*.dna*"),))
        print(inputFilePath)
        print(savedPath.get())
        decoding(inputFilePath, savedPath.get())
        # use filename and savedPath
    
    
    tk.Button(window, text="Browse Files", command=browseFiles).pack()
    window.mainloop()


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Yin-Yang Codec")
    tk.Button(window, text="Encode", command=encode).pack()
    tk.Button(window, text="Decode", command=decode).pack()
    window.mainloop()
