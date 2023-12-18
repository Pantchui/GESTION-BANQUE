import customtkinter as ctk
import tkinter as tk

from PIL import Image, ImageTk

# importation des classes
from CreationCompteInterface import CreationCompteInterface
from DepotInterface import DepotInterface
from RetraitInterface import RetraitInterface
from VirementInterface import VirementInterface
from GenerationCode import GenerationCode

import Configuration as config

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class Main(ctk.CTk):

    def __init__(self):
        super().__init__()

        # configuration de la page
        self.title("BANQUES")
        self.geometry("500x500")
        # self.resizable(False, False)
        self.iconbitmap(bitmap="./res/logo.ico")

        # ajout element
        self.frame = ctk.CTkFrame(self, corner_radius=5, width=500, height=500, fg_color="transparent")
        self.frame.pack(padx=10, pady=10)

        # text intoduction
        self.image_titre = Image.open("./res/logo.png")
        self.image_titre_tk = ImageTk.PhotoImage(self.image_titre.resize((70, 70)))
        self.titre = ctk.CTkLabel(self.frame, text="BANQUES", font=config.font_titre, text_color=config.titre_color,
                                  image=self.image_titre_tk, compound=tk.LEFT)
        self.titre.pack(pady=(20, 50))

        # creation compte
        self.creation_image = Image.open("./res/plus.png")
        self.creation_image_tk = ctk.CTkImage(self.creation_image)
        self.button_creation = ctk.CTkButton(self.frame, fg_color="transparent", bg_color="transparent",
                                             image=self.creation_image_tk, text="Creation de compte",
                                             font=config.font_button, hover_color=config.hover_color_button,
                                             command=self.creation_compte)
        self.button_creation.pack(pady=(0, 30), ipady=5)

        # faire un depot
        self.depot_image = Image.open("./res/depot.png")
        self.depot_image_tk = ctk.CTkImage(dark_image=self.depot_image)
        self.button_depot = ctk.CTkButton(self.frame, fg_color="transparent", bg_color="transparent",
                                          text="Effectuer un depot", font=config.font_button, image=self.depot_image_tk,
                                          hover_color=config.hover_color_button, command=self.effectuer_depot)
        self.button_depot.pack(pady=(0, 30), ipady=5)

        # effectuer un retrait
        self.retrait_image = Image.open("./res/retrait.png")
        self.retrait_image_tk = ctk.CTkImage(self.retrait_image)
        self.button_retrait = ctk.CTkButton(self.frame, fg_color="transparent", bg_color="transparent",
                                            text="Effectuer un retrait", font=config.font_button,
                                            image=self.retrait_image_tk, command=self.effectuer_retrait,
                                            hover_color=config.hover_color_button)
        self.button_retrait.pack(pady=(0, 30), ipady=5)

        # effectuer un virement
        self.virement_image = Image.open("./res/virement.png")
        self.virement_image_tk = ctk.CTkImage(self.virement_image)
        self.button_virement = ctk.CTkButton(self.frame, fg_color="transparent", bg_color="transparent",
                                             text="Effectuer un virement", font=config.font_button,
                                             image=self.virement_image_tk, hover_color=config.hover_color_button,
                                             command=self.effectuer_virement)
        self.button_virement.pack(pady=(0, 30), ipady=5)

        # consultation virement
        self.historique_image = Image.open("./res/historiques.png")
        self.historique_image_tk = ctk.CTkImage(self.historique_image)
        self.button_historique = ctk.CTkButton(self.frame, fg_color="transparent", bg_color="transparent",
                                               text="Consulter l'historique", font=config.font_button,
                                               image=self.historique_image_tk, hover_color=config.hover_color_button,
                                               command=self.historiques)
        self.button_historique.pack(pady=(0, 30), ipady=5)

    # fonction de creation compte
    def creation_compte(self):
        self.withdraw()
        creation_compte = CreationCompteInterface(self)
        creation_compte.mainloop()

    # fonction de depot
    def effectuer_depot(self):
        self.withdraw()
        effectuer_depot = DepotInterface(self)
        effectuer_depot.mainloop()

    # fonction de retrait
    def effectuer_retrait(self):
        self.withdraw()
        effectuer_retrait = RetraitInterface(self)
        effectuer_retrait.mainloop()

    def effectuer_virement(self):
        self.withdraw()
        effectuer_virement = VirementInterface(self)
        effectuer_virement.mainloop()

    # fonction historiques
    def historiques(self):

        def close_toplevel():
            toplevel.destroy()
            self.deiconify()

        def code_generation():
            # fenetre de generation
            dialog = ctk.CTkInputDialog(text="Entrer votre numero de telephone", button_hover_color=config.titre_color,
                                        button_fg_color=config.titre_color, button_text_color="black",
                                        title="Generation de numero", font=config.font_button)

            generation_numero = GenerationCode(dialog.get_input())
            results = generation_numero.generation_code()

            if not len(results) == 0:
                if len(results) == 1:
                    code_compte.insert(0, results[0])
                else:
                    numero = ""
                    for result in results:
                        numero = numero + str(result[0]) + "\n\n"
                    config.msg("Information", f"Voici vos numeros de compte:\n{numero}\nEntrer le numero du "
                                              f"compte que vous souhaitez faire le depot", "check")
            else:
                config.msg("Erreur", "Desole le numero est incorrect!", "cancel")

        def afficher_historiques():
            pass

        self.withdraw()
        toplevel = ctk.CTkToplevel(self)
        toplevel.iconbitmap(bitmap="./res/logo.ico")
        toplevel.title("Affichage historique")

        ctk.CTkLabel(toplevel, text="Informations du compte", font=config.font_label,
                     text_color=config.titre_color).pack(pady=20, padx=20)

        # champ
        code_compte = ctk.CTkEntry(toplevel, placeholder_text="Code du compte", height=35,
                                   font=config.font_button, width=400)
        code_compte.pack(padx=20, pady=20, fill=tk.BOTH)

        mdp_compte = ctk.CTkEntry(toplevel, placeholder_text="Mot de passe du compte", height=35,
                                  font=config.font_button, width=400)
        mdp_compte.pack(padx=20, pady=20, fill=tk.BOTH)

        # buttons
        btn1 = ctk.CTkButton(toplevel, text="Generez mon numero", font=config.font_button,
                             text_color=config.titre_color, hover=False, fg_color="transparent",
                             command=code_generation)
        btn1.pack(padx=20, pady=20, side=tk.LEFT)

        btn2 = ctk.CTkButton(toplevel, text="Mon historique", font=config.font_button,
                             text_color="black", hover=False, fg_color=config.titre_color,
                             command=afficher_historiques)
        btn2.pack(padx=20, pady=20, side=tk.RIGHT)

        toplevel.protocol("WM_DELETE_WINDOW", close_toplevel)


