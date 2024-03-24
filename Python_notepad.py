from tkinter import*
from tkinter import filedialog

root=Tk()
root.geometry("600x600")
root.title("Python Notepad")
root.config(bg='lightgrey') 
root.resizable(False, False)
root.iconbitmap('python_notepad.ico')

def save_file():
    global open_file
    open_file=filedialog.asksaveasfile (mode='w', defaultextension='.txt')
    if open_file is None:
        return
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()

def open_file():
    file=filedialog.askopenfile(mode='r', filetype=[('text files','*.txt')])
    if file is not None:
        global content
        content=file.read()
    entry.insert(INSERT, content)

b1=Button(root, width='5', height='1',bg='darkgrey',text='Save',command=save_file).place(x=10,y=5) 
b2=Button(root, width='5', height='1',bg='darkgrey',text='Open',command=open_file).place(x=60,y=5)
entry=Text (root, height="33", width="70", wrap=WORD) 
entry.place(x=10,y=35)
root.mainloop()