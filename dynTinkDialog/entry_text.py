from dynTinkDialog.entry import Entry
import tkinter as tk

class TextEntry(Entry):
    def custom_init(self, master: tk.Widget) -> None:
        self.entry = tk.Entry(master)
        self.entry.pack()
        # default
        if self.default is not None:
            self.entry.insert(0, self.default)
        
    def get(self) -> str:
        return self.entry.get()