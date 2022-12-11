import os
from tkinter import Tk, Button, Entry, filedialog, Label

def rename_files():
    folder_path = folder_entry.get()
    text_string = text_entry.get()
    starting_number = int(number_entry.get())

    # sort the files in the selected folder by date
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and not f.startswith('.')]
    files.sort(key=lambda f: os.path.getmtime(os.path.join(folder_path, f)))

    # rename the files
    for i, file in enumerate(files):
        file_name, file_ext = os.path.splitext(file)
        new_file_name = f"{text_string}{str(starting_number + i).zfill(2)}"
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path, f"{new_file_name}{file_ext}"))

# create the GUI
root = Tk()
root.geometry("600x200")

# create a button for selecting the folder
folder_label = Label(root, text="Folder path:")
folder_label.pack()
folder_entry = Entry(root, width=70, font=("Helvetica", 14))
folder_entry.pack()
folder_button = Button(root, text="Select Folder", command=lambda: folder_entry.insert(0, filedialog.askdirectory()))
folder_button.pack()

# create a text entry for the string
text_label = Label(root, text="Text string:")
text_label.pack()
text_entry = Entry(root, width=70, font=("Helvetica", 14))
text_entry.pack()

# create a number entry for the starting number
number_label = Label(root, text="Starting number:")
number_label.pack()
number_entry = Entry(root, width=70, font=("Helvetica", 14))
number_entry.pack()

# create a button for renaming the files
rename_button = Button(root, text="Rename Files", command=rename_files)
rename_button.pack()

root.mainloop()
