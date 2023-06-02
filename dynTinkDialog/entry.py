import tkinter as tk

from dynTinkDialog import config

class Entry:
    def __init__(self, name : str, default: str =None) -> None:
        self.name = name
        self.default = default
        if config.REQUIRE_INIT_VALIDATE:
            self.default_check()
    
    def default_check(self):
        pass
    
    def custom_init(self, master: tk.Widget) -> None:
        pass
    
    def create_widgets(self, master: tk.Frame) -> None:
        # create widget with border 
        self.widget = tk.Frame(master, borderwidth=1, relief="solid")
        
        # frame size as big as master
        self.widget.setvar(name="width", value=master.winfo_width())
        
        
        self.label = tk.Label(self.widget, text=self.name)
        # pack
        self.label.pack()

        self.custom_init(self.widget)

        self.widget.pack()
    
    def get(self) -> str:
        pass