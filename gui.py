"""
This module is the GUI for discover directory.
"""

## Imports
import tkinter as tk
import discover_directory as dd
from tkinter.filedialog import askdirectory


# Create window
window = tk.Tk()
window.geometry("800x200")
status_text = "Ready to go. Please, select a directory in the field above.\n"


def browse_files():
    """Browses for directory names"""
    directory_name = askdirectory(master = window, title = "Select a directory")
    ent_directory_input.delete(0,tk.END)
    ent_directory_input.insert(0, directory_name)
    return directory_name
    

def create_csv():
    """Creates the CSV from discover directory"""
    dir_path = ent_directory_input.get()
    update_status(f"Working on CSV for {dir_path}...")
    dd.create_directory_list(dir_path)
    update_status("Finished.\n")


def update_status(update_text):
    """Updates the status text in the window."""
    current_text = lbl_status.cget("text")
    update_text = f"{current_text} {update_text}"
    lbl_status.config(text=update_text)


# Create frame for input
frm_directory_input = tk.Frame(master=window)
lbl_directory_input = tk.Label(master=frm_directory_input, text="Directory:")
lbl_directory_input.pack(side="left")
ent_directory_input = tk.Entry(master = frm_directory_input)
ent_directory_input.pack(fill=tk.X)

frm_set_button = tk.Frame(master=window)
btn_directory_input = tk.Button(master = frm_set_button, text = "Open", width=10, command=browse_files)
btn_directory_input.pack(side="right", padx=10)

frm_go_button = tk.Frame(master=window)
btn_go = tk.Button(master=frm_go_button, text="Create CSV",width=20, height=3, command=create_csv)
btn_go.pack()


frm_status = tk.Frame(master=window)
lbl_status = tk.Label(master=frm_status, text=status_text, background="white")
lbl_status.pack(fill=tk.BOTH)

# Add frames to grid
frm_directory_input.grid(row=0,column=0,sticky="ew",padx=5, pady=5)
frm_set_button.grid(row=0,column=1)
frm_go_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
frm_status.grid(row=2, column=0,columnspan=2, padx=5, pady=5, sticky="nsew")

window.columnconfigure(0, weight=1, minsize=50)
window.rowconfigure(2, weight=1,minsize=50)

window.mainloop()