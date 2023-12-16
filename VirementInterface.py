import customtkinter as ctk
import tkinter as tk

# importations des classes
import Configuration as config


class VirementInterface(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configuration de la page
        self.title("BANQUES - Virement banquaire")
        self.resizable(False, False)
        self.iconbitmap(bitmap="./res/logo.ico")

        # titre de la page
        self.titre = ctk.CTkLabel(self, text="Virement", text_color=config.titre_color,
                                  font=config.font_body)
        self.titre.pack(pady=(10, 30), padx=20)

        self.frame = ctk.CTkFrame(self, fg_color="transparent")
        self.frame.pack(fill=tk.BOTH)

        # code du compte
        self.code_compte_envoi = ctk.CTkEntry(self.frame, placeholder_text="N. du compte d'envoi",
                                              width=200, height=35, font=config.font_button)
        self.code_compte_envoi.pack(pady=10, padx=20, fill=tk.BOTH, side=tk.LEFT)

        # code du compte
        self.code_compte_recoit = ctk.CTkEntry(self.frame, placeholder_text="N. du compte beneficaire",
                                               width=200, height=35, font=config.font_button)
        self.code_compte_recoit.pack(pady=10, padx=20, fill=tk.BOTH, side=tk.RIGHT)

        # momtant
        self.montant = ctk.CTkEntry(self, placeholder_text="Montant a deposer", width=250, height=35,
                                    font=config.font_button)
        self.montant.pack(pady=10, padx=20, fill=tk.BOTH)

        self.mdp_compte = ctk.CTkEntry(self, placeholder_text="Mot de passe du compte", width=250, height=35,
                                       font=config.font_button, show="*")
        self.mdp_compte.pack(pady=10, padx=20, fill=tk.BOTH)

        self.label = ctk.CTkLabel(self, text="Motif du virement", font=config.font_petit)
        self.label.pack(padx=20, pady=(10, 5))

        # motif
        self.libelle = ctk.CTkTextbox(self, font=config.font_button, height=100)
        self.libelle.pack(pady=(0, 20), padx=20, fill=tk.BOTH)

        # button depot
        self.depot = ctk.CTkButton(self, font=config.font_button, fg_color=config.titre_color, hover=False,
                                   border_color=config.titre_color, text_color="black", text="Envoyer")
        self.depot.pack(pady=(30, 15), side=tk.RIGHT, padx=20)

        # button generation compte
        self.btn = ctk.CTkButton(self, font=config.font_button, fg_color="transparent", hover=False,
                                 border_color=config.titre_color, text_color=config.titre_color,
                                 text="Generez mon numero", command=self.code_generation)
        self.btn.pack(pady=(30, 15), side=tk.LEFT, padx=20)

    # generation de numero
    def code_generation(self):
        self.withdraw()

        # fenetre de generation
        dialog = ctk.CTkInputDialog(text="Entrer votre numero de telephone", button_hover_color=config.titre_color,
                                    button_fg_color=config.titre_color, button_text_color="black",
                                    title="Generation de numero", font=config.font_button)
        print(dialog.get_input())

        # self.deiconify()
