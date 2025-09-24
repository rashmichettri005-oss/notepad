'''
simple note pad
'''

import tkinter as tk
from pydoc import text
from tkinter import filedialog, messagebox

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file,read())

def save_file():
    file_path=filedialogue.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))
            mesagebox.showinfo("Info", "File saved")

root = tk.Tk()
root.title("simple text editor")
root.geometry("800x600")

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="EXIT", command=root.quit)

text = tk.Text(root, wrap=tk.WORD, font=("Arial", 20), fg="blue")
text.pack(expand=tk.YES, fill=tk.BOTH)

root.mainloop()