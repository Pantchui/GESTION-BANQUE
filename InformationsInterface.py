import customtkinter as ctk
import tkinter as tk

import Configuration as config


class InformationsInterface(ctk.CTk):
    def __init__(self, interface, resultats):
        super().__init__()
        self.resultats = resultats
        self.interface = interface

        # configuration de la page
        self.title("BANQUES - Informations du compte")
        self.geometry("500x620")
        self.resizable(False, False)
        self.iconbitmap(bitmap="./res/logo.ico")

        # titre de la page
        ctk.CTkLabel(self, text="Informations sur le compte", text_color=config.titre_color,
                     font=config.font_label).pack(pady=30, padx=20)

        self.frame = ctk.CTkScrollableFrame(self, height=620)
        self.frame.pack(padx=10, pady=10, fill=tk.BOTH)

        self.frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        libelles = ["Code du compte: ", "Type de compte: ", "Votre nom: ",
                    "Votre prenom: ", "Votre adresse mail: ",
                    "Votre numero de telephone: ", "Mot de passe du compte: ",
                    "Votre pays: ", "Votre ville: ", "Votre quartier: ",
                    "Votre residence: ", "Votre proffession: ", "Date de creation du compte: ",
                    "Solde initial: ", "Solde du compte: "]

        # separator
        informations = ""
        for i in range(len(self.resultats)):
            if i == 13:
                continue
            informations = informations + str(i+1) + ". " + libelles[i] + str(self.resultats[i]) + "\n\n"

        ctk.CTkLabel(self.frame, text=informations, text_color="white", font=config.font_moyen,
                     justify=tk.LEFT).grid(padx=20, pady=10, column=0, columnspan=2)

        self.protocol("WM_DELETE_WINDOW", self.close_panel)

    def close_panel(self):
        self.destroy()
        self.interface.deiconify()
