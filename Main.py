import customtkinter as ctk
import tkinter as tk

from PIL import Image, ImageTk

# importation des classes
from CreationCompteInterface import CreationCompteInterface
from DepotInterface import DepotInterface
from RetraitInterface import RetraitInterface
from VirementInterface import VirementInterface

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

        # effectuer un virement
        self.historique_image = Image.open("./res/historiques.png")
        self.historique_image_tk = ctk.CTkImage(self.historique_image)
        self.button_historique = ctk.CTkButton(self.frame, fg_color="transparent", bg_color="transparent",
                                               text="Consulter l'historique", font=config.font_button,
                                               image=self.historique_image_tk, hover_color=config.hover_color_button)
        self.button_historique.pack(pady=(0, 30), ipady=5)

    # fonction de creation compte
    def creation_compte(self):
        self.destroy()
        creation_compte = CreationCompteInterface()
        creation_compte.mainloop()

    # fonction de depot
    def effectuer_depot(self):
        self.destroy()
        effectuer_depot = DepotInterface()
        effectuer_depot.mainloop()

    # fonction de retrait
    def effectuer_retrait(self):
        self.destroy()
        effectuer_retrait = RetraitInterface()
        effectuer_retrait.mainloop()

    def effectuer_virement(self):
        self.destroy()
        effectuer_virement = VirementInterface()
        effectuer_virement.mainloop()


if __name__ == "__main__":
    app = Main()
    app.mainloop()
