import customtkinter as ctk
import tkinter as tk

from PIL import Image, ImageTk


# importation des classes
from CreationCompteInterface import CreationCompteInterface
from DepotInterface import DepotInterface
from Historiques import Historiques
from RetraitInterface import RetraitInterface
from VirementInterface import VirementInterface
from GenerationCode import GenerationCode
from HistoriquesInterface import HistoriquesInterface
from InformationsInterface import InformationsInterface

import Configuration as config

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class Main(ctk.CTk):

    def __init__(self):
        super().__init__()

        # configuration de la page
        self.title("BANQUES")
        self.geometry("500x570")
        self.resizable(False, False)
        self.iconbitmap(bitmap="./res/logo.ico")

        # ajout element
        self.frame = ctk.CTkFrame(self, corner_radius=5, width=500, height=500, fg_color="transparent")
        self.frame.pack(padx=10, pady=10)

        # text intoduction
        self.image_titre = Image.open("./res/logo.png")
        self.image_titre_tk = ImageTk.PhotoImage(self.image_titre.resize((70, 70)))
        self.titre = ctk.CTkLabel(self.frame, text="BANQUES", font=config.font_titre, text_color=config.titre_color,
                                  image=self.image_titre_tk, compound=tk.LEFT)
        self.titre.pack(pady=(20, 40))

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

        # consultation historique
        self.historique_image = Image.open("./res/historiques.png")
        self.historique_image_tk = ctk.CTkImage(self.historique_image)
        self.button_historique = ctk.CTkButton(self.frame, fg_color="transparent", bg_color="transparent",
                                               text="Consulter l'historique", font=config.font_button,
                                               image=self.historique_image_tk, hover_color=config.hover_color_button,
                                               command=lambda: self.verifications_informations("historique",
                                                                                               Historiques,
                                                                                               HistoriquesInterface))
        self.button_historique.pack(pady=(0, 30), ipady=5)

        # info compte
        self.historique_image = Image.open("./res/info.png")
        self.historique_image_tk = ctk.CTkImage(self.historique_image)
        self.button_historique = ctk.CTkButton(self.frame, fg_color="transparent", bg_color="transparent",
                                               text="Informations du compte", font=config.font_button,
                                               image=self.historique_image_tk, hover_color=config.hover_color_button,
                                               command=lambda: self.verifications_informations("information",
                                                                                               Historiques,
                                                                                               InformationsInterface))
        self.button_historique.pack(pady=(0, 10), ipady=5)

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
    def verifications_informations(self, type_appelation, __class__, __class__interface__):

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
                                              f"compte que vous souhaitez voir les historiques de transactions",
                               "check")
            else:
                config.msg("Erreur", "Desole le numero est incorrect!", "cancel")

        def afficher_historiques():
            infos = __class__(self, code_compte.get(), mdp_compte.get())
            if infos.verification():
                affichage = False

                # si la methode est appele pour consulter l'historique
                if type_appelation == "historique":
                    results = infos.affichages_transaction()
                    if len(results) > 0:
                        affichage = True
                        toplevel.destroy()
                        infos_interface = __class__interface__(self, results[0][1], results)
                        infos_interface.mainloop()

                # si la methode est appele pour consulter les informations
                else:
                    results = infos.affichages_information()
                    if len(results) > 0:
                        affichage = True
                        toplevel.destroy()
                        infos_interface = __class__interface__(interface=self, resultats=results)
                        infos_interface.mainloop()

                # dans le cas ou on ne trouve pas d'informations
                if not affichage:
                    config.msg("Information", f"Aucune transaction pour se compte \n"
                                              f"(Numero: {code_compte.get()})", "check")
                    toplevel.destroy()
                    self.deiconify()

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
                                  font=config.font_button, width=400, show="*")
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
