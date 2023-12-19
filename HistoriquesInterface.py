import customtkinter as ctk
import tkinter as tk

import Configuration as config


class HistoriquesInterface(ctk.CTk):

    # constructeur
    def __init__(self, interface, code_compte, resultats):
        super().__init__()
        self.interface = interface
        self.resultats = resultats
        self.code_compte = code_compte

        # configuration de la page
        self.title("BANQUES - Historiques de transactions")
        self.geometry("500x620")
        self.resizable(False, False)
        self.iconbitmap(bitmap="./res/logo.ico")

        # titre de la page
        ctk.CTkLabel(self, text="Historiques des transctions", text_color=config.titre_color,
                     font=config.font_label).pack(pady=30, padx=20)

        ctk.CTkLabel(self, text=f"Numero du compte {self.code_compte}\n",
                     font=config.font_button).pack(pady=20, padx=10)

        self.frame = ctk.CTkScrollableFrame(self, height=620)
        self.frame.pack(padx=10, pady=10, fill=tk.BOTH)

        self.frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        libelles = ["Numero transaction: ", "Numero du compte: ", "Date de la transaction: ",
                    "Type de la transaction: ", "Motif de la transaction: "]
        # separator
        for resultat in self.resultats:
            informations = ""
            for i in range(len(resultat)):
                if i == 1:
                    continue
                informations = informations + " - " + libelles[i] + str(resultat[i]) + "\n"

            if resultat[3] == 'R':
                ctk.CTkLabel(self.frame, text=informations, text_color="red", font=config.font_button,
                             justify=tk.LEFT).grid(padx=20, pady=5, column=0, columnspan=2)
            else:
                ctk.CTkLabel(self.frame, text=informations, text_color=config.titre_color, font=config.font_button,
                             justify=tk.LEFT).grid(padx=20, pady=5, column=0, columnspan=2)

        self.protocol("WM_DELETE_WINDOW", self.close_panel)

    def close_panel(self):
        self.destroy()
        self.interface.deiconify()
