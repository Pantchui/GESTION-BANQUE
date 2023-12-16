import customtkinter as ctk
import tkinter as tk

# importations des classes
import Configuration as config


class CreationCompteInterface(ctk.CTk):

    def __init__(self):
        super().__init__()

        # configuration de la page
        self.title("BANQUES - Creation compte")
        self.geometry("620x620")
        self.resizable(False, False)
        self.iconbitmap(bitmap="./res/logo.ico")

        self.frame = ctk.CTkScrollableFrame(self, width=600, height=600)
        self.frame.pack(fill=tk.BOTH, padx=10, pady=10)

        self.frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # titre de la page
        self.titre = ctk.CTkLabel(self.frame, text="Creation d'un compte", text_color=config.titre_color,
                                  font=config.font_body)
        self.titre.grid(row=0, column=0, columnspan=4, pady=(30, 50), padx=20)

        # separation section
        self.label = ctk.CTkLabel(self.frame, text="Informations globales sur le proprietaire", font=config.font_petit,
                                  text_color=config.titre_color)
        self.label.grid(row=1, column=0, pady=(0, 20))

        # nom du compte
        self.nom_utilisateur = ctk.CTkEntry(self.frame, placeholder_text="Votre nom", width=250, height=35,
                                            font=config.font_button)
        self.nom_utilisateur.grid(row=2, column=0, columnspan=2, pady=20, padx=20)

        # prenom
        self.nom_utilisateur = ctk.CTkEntry(self.frame, placeholder_text="Votre prenom", width=250, height=35,
                                            font=config.font_button)
        self.nom_utilisateur.grid(row=2, column=2, columnspan=4, pady=20, padx=20)

        # adresse mail
        self.email = ctk.CTkEntry(self.frame, placeholder_text="Votre adresse mail", width=250, height=35,
                                  font=config.font_button)
        self.email.grid(row=3, column=0, columnspan=2, pady=20, padx=20)

        # numero de telephone
        self.numero_tel = ctk.CTkEntry(self.frame, placeholder_text="Votre numero de telephone", width=250, height=35,
                                       font=config.font_button)
        self.numero_tel.grid(row=3, column=2, columnspan=4, pady=20, padx=20)

        # mot de passe
        self.mdp1 = ctk.CTkEntry(self.frame, placeholder_text="Votre mot de passe", width=250, height=35,
                                 font=config.font_button)
        self.mdp1.grid(row=4, column=0, columnspan=2, pady=20, padx=20)

        # numero de telephone
        self.mdp2 = ctk.CTkEntry(self.frame, placeholder_text="Confirmation du mot de passe", width=250, height=35,
                                 font=config.font_button)
        self.mdp2.grid(row=4, column=2, columnspan=4, pady=20, padx=20)

        # separation section
        self.label1 = ctk.CTkLabel(self.frame, text="Informations sur la residence",
                                   font=config.font_petit, text_color=config.titre_color)
        self.label1.grid(row=5, column=0, pady=(20, 20))

        # pays
        self.pays = ctk.CTkEntry(self.frame, placeholder_text="Votre pays", width=250, height=35,
                                 font=config.font_button)
        self.pays.grid(row=6, column=0, columnspan=2, pady=20, padx=20)

        # ville
        self.ville = ctk.CTkEntry(self.frame, placeholder_text="Votre ville", width=250, height=35,
                                  font=config.font_button)
        self.ville.grid(row=6, column=2, columnspan=4, pady=20, padx=20)

        # pays
        self.quartier = ctk.CTkEntry(self.frame, placeholder_text="Votre quartier", width=250, height=35,
                                     font=config.font_button)
        self.quartier.grid(row=7, column=0, columnspan=2, pady=20, padx=20)

        # residence
        self.residence = ctk.CTkEntry(self.frame, placeholder_text="Votre residence", width=250, height=35,
                                      font=config.font_button)
        self.residence.grid(row=7, column=2, columnspan=4, pady=20, padx=20)

        # separation section
        self.label2 = ctk.CTkLabel(self.frame, text="Autres informations sur le compte", font=config.font_petit,
                                   text_color=config.titre_color)
        self.label2.grid(row=8, column=0, pady=(20, 20))

        # proffesion
        self.label3 = ctk.CTkLabel(self.frame, text="Proffesion", font=config.font_button)
        self.label3.grid(row=9, column=0, columnspan=2, sticky="se", pady=20, padx=(0, 10))

        # entry proffession
        self.proffesion = ctk.CTkEntry(self.frame, width=250, height=35,
                                       font=config.font_button)
        self.proffesion.grid(row=9, column=2, columnspan=4, pady=20, sticky="nw", padx=(10, 0))

        # proffesion
        self.label3 = ctk.CTkLabel(self.frame, text="Type de compte: ", font=config.font_button)
        self.label3.grid(row=10, column=0, columnspan=2, sticky="se", pady=(20, 50), padx=(0, 10))

        # entry proffession
        self.proffesion = ctk.CTkComboBox(self.frame, width=250, height=35,
                                          font=config.font_button, values=["Courant", "Epargne"],
                                          button_color=config.titre_color,
                                          button_hover_color=config.titre_color,
                                          dropdown_hover_color=config.titre_color,
                                          border_color=config.titre_color, dropdown_fg_color="white",
                                          dropdown_text_color="black")
        self.proffesion.grid(row=10, column=2, columnspan=4, pady=(20, 50), sticky="nw", padx=(10, 0))

        # button
        self.creation_compte = ctk.CTkButton(self.frame, text="Creer mon compte", hover=False,
                                             fg_color=config.titre_color, corner_radius=8, font=config.font_button,
                                             text_color="black")
        self.creation_compte.grid(row=11, column=3, pady=(0, 20), ipady=5)
