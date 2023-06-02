from dynTinkDialog.entry import Entry
import tkinter as tk

class IntEntry(Entry):
    def custom_init(self, master: tk.Widget) -> None:

        self.entry = tk.Entry(
            master,
            validate="key", 
            validatecommand=(master.register(self.validate), "%P")
        )
        self.entry.pack()
        # default
        if self.default is not None and isinstance(self.default, int):
            self.entry.insert(0, self.default)
        
    def get(self) -> str:
        return int(self.entry.get())

    def validate(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False
        
    def default_check(self):
        if self.default is None:
            return
        if not isinstance(self.default, int):
            raise TypeError("Default value must be an integer")
        
    