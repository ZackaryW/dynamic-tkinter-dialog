from tkinter import filedialog
from dynTinkDialog.entry import Entry
import tkinter as tk
import os

class FileEntry(Entry):
    def custom_init(self, master: tk.Widget) -> None:
        self.button = tk.Button(master, text="Browse", command=self.browse_file)
        self.button.pack()
        # label
        self.default = self.default if self.default is not None else "No file selected"
        self.file_label = tk.Label(master, text=self.default)
        self.file_label.pack()
        
    def browse_file(self) -> None:
        # open a file dialog
        filename = filedialog.askopenfilename(initialdir="/", title="Select file")
        # set the value of the entry to the file path
        self.file_label["text"] = filename
        
    def get(self) -> str:
        return self.file_label["text"]
    
    def default_check(self):
        if self.default is None:
            return
        if not isinstance(self.default, str):
            raise TypeError("Default value must be a string")
        if not os.path.isdir(self.default):
            raise ValueError("Default value must be a valid folder path")
