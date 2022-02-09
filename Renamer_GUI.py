from tkinter import *
from tkinter import filedialog
import Renamer_Functions

Renamer_main_window = Tk()
Renamer_main_window.geometry('500x200')
Renamer_main_window.title('Renamer')

folder_path = ""
empty_dic = {}


def browse_folder_function():
    folder_path = filedialog.askdirectory()
    if folder_path != "":
        selected_folder_label['text'] = folder_path
        browse_button['text'] = "Selected"
        

def rename_now():
    empty_dic = Renamer_Functions.access(selected_folder_label['text'])
    Renamer_Functions.renamer(empty_dic)


browse_button = Button(Renamer_main_window, text='Select Folder', command=browse_folder_function, height=1, width=18)
browse_button.place(relx=0.7, rely=0.05, anchor=N)

rename_button = Button(Renamer_main_window, text='Rename', command=rename_now, height=1, width=18)
rename_button.place(relx=0.7, rely=0.4, anchor=N)

selected_folder_label = Label(text="You need to select a folder")
selected_folder_label.place(relx=0.3, rely=0.07, anchor=N)

Renamer_main_window.mainloop()
