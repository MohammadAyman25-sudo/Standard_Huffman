from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Compression import HuffmanCompression

root = Tk()
root.title("Huffman Compression")
root.resizable(False, False)

style = ttk.Style()
style.configure('TRadiobutton', font=("Arial", 14, "bold"))
style.configure('TButton', font=("Arial", 14, "bold"))

input_ = ttk.Label(root, text="Enter text: ")

output_ = ttk.Label(root, text="Compressed Data: ")

input_.grid(row=0, column=0, padx=10, pady=10)
input_.config(font=("Arial", 14, "bold"))

output_.grid(row=1, column=0, padx=10, pady=10)
output_.config(font=("Arial", 14, "bold"))

input_text = ttk.Entry(root, width=55)
input_text.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
input_text.config(font=("Arial", 14, "bold"))

output_text = ttk.Entry(root, width=55)
output_text.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
output_text.config(font=("Arial", 14, "bold"), state='disabled')

frame = ttk.Frame(root, width=30, height=40)
frame.grid(row=0, column=3, padx=10, pady=10)

inputMethod = StringVar()

file = ttk.Radiobutton(frame, text='File', variable=inputMethod, value='File')
file.pack()
text_input = ttk.Radiobutton(frame, text='Text', variable=inputMethod, value='Text')
text_input.pack()

compress_btn = ttk.Button(root, text='Compress', width=30)
compress_btn.grid(row=2, column=1, padx=10, pady=10)


def change_text():
    if inputMethod.get() == 'File':
        input_['text'] = "Enter File Name:"
    elif inputMethod.get() == 'Text':
        input_['text'] = "Enter text:"


def compress_GUI():
    if inputMethod.get() == 'File':
        huffman = HuffmanCompression(input_text.get())
    else:
        huffman = HuffmanCompression('Input.txt', input_text.get())
    file_found = huffman.compress()
    if file_found is None:
        msg = 'File Not Found!!'
        messagebox.showerror(title='File does not exist', message=msg)
    else:
        msg = 'Compression is Done Successfully'
        messagebox.showinfo(title="Compression Finished Successfully", message=msg)
        output_text.config(state='normal')
        output_text.insert(0, file_found)
        output_text.config(state='disabled')


file.config(command=change_text)
text_input.config(command=change_text)
compress_btn.config(command=compress_GUI)
root.mainloop()
