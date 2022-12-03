import tkinter as tk

def encode():
    window = tk.Tk()
    window.title("Encoder") 
    binary = tk.Entry(window, width=20)
    binary.pack()
    def onclick():
        encoded = binary.get() # import encoder function here
        tk.Label(window, text="Encoded output is "+ str(encoded), font=("Times New Roman", 15)).pack(side="bottom")
    tk.Button(window, text="Enter", command=onclick).pack()
    window.mainloop()

def decode():
    window = tk.Tk()
    window.title("Decoder")
    dna_sequence = tk.Entry(window, width=20)
    dna_sequence.pack()
    def onclick():
        decoded = dna_sequence.get()  # import decoder sequence here
        tk.Label(window, text="Decoded output is "+ str(decoded), font=("Times New Roman", 15)).pack(side="bottom")
    tk.Button(window, text="Enter", command=onclick).pack()
    window.mainloop()


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Yin-Yang Codec")
    tk.Button(window, text="Encode", command=encode).pack()
    tk.Button(window, text="Decode", command=decode).pack()
    window.mainloop()
