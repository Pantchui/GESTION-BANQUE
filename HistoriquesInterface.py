import customtkinter as ctk
import tkinter as tk

import Configuration as config


class Historiques(ctk.CTk):

    # constructeur
    def __init__(self, interface):
        super().__init__()
        self.interface = interface

        # configuration de la page
        self.title("BANQUES - Historiques de transactions")
        self.geometry("500x620")
        self.resizable(False, False)
        self.iconbitmap(bitmap="./res/logo.ico")

        # titre de la page
        self.titre = ctk.CTkLabel(self, text="Historiques des transctions", text_color=config.titre_color,
                                  font=config.font_label)
        self.titre.pack(pady=30, padx=20)

        

app = Historiques("")
app.mainloop()