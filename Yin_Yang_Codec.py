import tkinter as tk
from tkinter import filedialog, messagebox
import os
from main import encoding, decoding

def encode():
    window = tk.Tk()
    window.title("Encoder")
    window.geometry("500x100")
    window.resizable(0,0)
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)
    tk.Label(window, text="Specify path to save output: ").grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
    savedPath = tk.Entry(window, width=50)
    savedPath.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
    def browseFiles():

        if os.path.isdir(savedPath.get()) == False:
            messagebox.showinfo("Wrong diectory", "Please select correct directory")
            return
        inputFile = filedialog.askopenfilename(initialdir = "/", title = "Select a File",
                                                filetypes = (('Image Files',"*.jpeg"),
                                                             ('Image Files',"*.png"),
                                                             ('Text File',"*.txt"),))
        print(inputFile)
        print(savedPath.get())
        encoding(inputFile,savedPath.get())
        # use filename and savedPath
    
    tk.Label(window, text="Select file to be encoded: ").grid(column=0, row=1)
    tk.Button(window, text="Browse file", command=browseFiles).grid(column=1, row=1, sticky=tk.W, padx=100)
    window.mainloop()
    

def decode():
    window = tk.Tk()
    window.title("Decoder") 
    window.geometry("500x100")
    window.resizable(0,0)
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)
    tk.Label(window, text="Specify path to save output: ").grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
    savedPath = tk.Entry(window, width=50)
    savedPath.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
    tk.Label(window, text="Specify output file format: ").grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
    fileformat = tk.Entry(window, width=5)
    fileformat.grid(column=1, row=1, sticky=tk.W)
    def browseFiles():

        if os.path.isdir(savedPath.get()) == False:
            messagebox.showinfo("Wrong diectory", "Please select correct directory")
            return
        inputFilePath = filedialog.askopenfilename(initialdir = "/", title = "Select a File",
                                                filetypes = (("Text files", "*.dna*"),))
        print(inputFilePath)
        print(savedPath.get())
        print(fileformat.get())
        decoding(inputFilePath, savedPath.get())
        # use filename and savedPath
    
    
    tk.Label(window, text="Select file to be decoded: ").grid(column=0, row=2)
    tk.Button(window, text="Browse file", command=browseFiles).grid(column=1, row=2, sticky=tk.W, padx=100)


    window.mainloop()


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Yin-Yang Codec")
    window.geometry("280x100")
    window.resizable(0,0)
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)
    
    #tk.Label(window, text="DNA Encoding and Decoding Using Yin-Yang Rules", font=("Times New Roman", 15)).grid(column=0, row=0)

    tk.Label(window, text="Encode a file: ", font=("Times New Roman", 13)).grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
    tk.Button(window, text="Encode", command=encode).grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

    tk.Label(window, text="Decode a file: ", font=("Times New Roman", 13)).grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
    tk.Button(window, text="Decode", command=decode).grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
    window.mainloop()
