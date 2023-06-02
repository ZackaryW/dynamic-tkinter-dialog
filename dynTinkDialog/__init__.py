"""
take json as args and dynamically create a tkinter dialog box
"""
import json
import os
import tkinter as tk
import sys
import click
import typing
from dynTinkDialog.entry import Entry
from dynTinkDialog.entry_file import FileEntry

from dynTinkDialog.entry_folder import FolderEntry
from dynTinkDialog.entry_int import IntEntry
from dynTinkDialog.entry_text import TextEntry

MATCHING_MAP :  typing.Dict[str, Entry] = {
    "text" : TextEntry,
    "file" : FileEntry,
    "folder" : FolderEntry,
    "int"  : IntEntry
}

def create_entries(master : tk.Frame, data : dict) -> typing.Dict[str, Entry]:
    entries = {}
    for key, type in data.items():
        default = None
        if isinstance(type, list):
            type, default = type
        
        if type not in MATCHING_MAP:
            raise ValueError(f"Type {type} not supported")
    
        entries[key] = MATCHING_MAP[type](key, default)
    
    for entry in entries.values():
        entry : Entry
        tk.Label(master, text="").pack()
        entry.create_widgets(master)
        
        
    return entries


class DialogBox(tk.Frame):
    def __init__(self, master=None, data=None):
        super().__init__(master)
        self.master : tk.Frame = master
        self.json : dict = data
        # bigger window, font and center
        self.master.geometry("500x500")
        self.master.option_add("*Font", "arial 15")
        self.master.option_add("*justify", "left")
        
        # space between widgets
        self.master.option_add("*padx", 10)

        
        self.pack()
        self.widgets = create_entries(self, self.json)
        
        self.confirm = tk.Button(self, text="Confirm", command=self.final)
        self.confirm.pack()
        
    def final(self) -> None:
        # print value 
        output = {}
        for key, widget in self.widgets.items():
            output[key] = widget.get()
        print(output)
        return super().quit()
 
def create_window(data=None):
    # create a root window
    root = tk.Tk()
    
    if os.path.isfile(data):
        with open(data, "r") as f:
            data = json.load(f)
    
    if isinstance(data, str):
        data = json.loads(data)
    
    if data is None:
        print("No data provided")
        sys.exit(1)
        
    # create a dialog box with the json data
    app = DialogBox(master=root, data=data)
    # run the dialog box
    app.mainloop()

 
@click.command()
@click.option("--data", default=None, help="json data to be used in the dialog box")    
def main(data=None):
    create_window(data)

if __name__ == "__main__":
    main()
    