""" Caspar's
_________        ___.                   ________ ____ ___.___ 
\_   ___ \___.__.\_ |__   ___________  /  _____/|    |   \   |
/    \  \<   |  | | __ \_/ __ \_  __ \/   \  ___|    |   /   |
\     \___\___  | | \_\ \  ___/|  | \/\    \_\  \    |  /|   |
 \______  / ____| |___  /\___  >__|    \______  /______/ |___|
        \/\/          \/     \/               \/              
"""

import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # -- WINDOW SETUP -- 
        self.title('CyberGUI')

        # window width, height
        wd = [600, 500]
        # get the screen width & height
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()

        self.geometry(f'{int(w/4)}x{int(h/4)}+{int(w/2 - wd[0]/2)}+{int(h/2 - wd[1]/2)}')
        self.resizable(False, False)

        # -- COLOR --
        #self.config(bg='Black')

        # -- WIDGETS --
        # mode menu
        self.modes = ('CESAR', 'VIGENERE', 'RSA')
        self.mode_var = tk.StringVar(self)
        
        # flip switch
        self.flips = ('ENCRYPT', 'DECRYPT')
        self.flip_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # padding
        paddings = {'padx': 5, 'pady': 5}

        # -- MENU FUNCTIONS --
        # label
        mode_label = ttk.Label(self,  text='SELECT MODE:')
        mode_label.grid(column=0, row=0, sticky=tk.W, **paddings)

        # menu
        option_menu = ttk.OptionMenu(
            self,
            self.mode_var,
            self.modes[0],
            *self.modes,
            command=self.mode_changed)

        option_menu.grid(column=1, row=0, sticky=tk.W, **paddings)

        # -- FLIP --
        # label
        flip_label = ttk.Label(self, text='ENCRYPT ELSE DECRYPT')
        flip_label.grid(column=0, row=1, sticky=tk.W, **paddings)

        # switch
        flip = ttk.Button(
            self, 
            text=self.flip_var[0]
        )
        flip.grid(column=0, row=2, sticky=tk.W, **paddings)


    def mode_changed(self, *args):
        print(self.mode_var.get())


    

if __name__ == "__main__":
    app = App()
    app.mainloop()