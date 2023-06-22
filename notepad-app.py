
import os
from tkinter import *
import webbrowser
try:
    # For Python 3+
    from tkinter import messagebox
except ImportError:
    # For Python 2
    from Tkinter import Message as messagebox
# Importing PySimpleGUI modules/widgets
import PySimpleGUI as sg
# Setting up window size and layout
sg.theme('DarkAmber')   # Add a touch of color
layout = [  [sg.Text("Note Title",size=(15,1)), sg.Input(key="-TITLE-")],
            [sg.Multiline(default_text="Your Note Goes here...", key='-NOTE-', size=(80,20))], 
            [sg.Button("Save"), sg.Cancel()]]
window = sg.Window("Notepad App", layout)
def save():
    title=values['-TITLE-']
    text=values["-NOTE-"]
    if len(title)==0 :
        messagebox.showerror("Error","Title cannot be empty!")
        return
    
    elif len(text)==0 :
         messagebox.showerror("Error","No Text Entered! ")
         return 
    else: 
        filename = title + ".txt"  
        f = open(filename,"w+")  
        f.write(f"{title}\n\n{text}")  
        f.close()    
        messagebox.showinfo("Success!",f'File saved successfully as {filename}')  
while True:             # Event Loop
    event, values = window.read()    
    print(event, values)  
    if event == 'Exit' or event is None:        
        break;         
    elif event=="Save":
        save()       
    
window.close()
