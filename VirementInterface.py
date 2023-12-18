import customtkinter as ctk
import tkinter as tk

# importations des classes
import Configuration as config
from Depot import Depot
from GenerationCode import GenerationCode
from Retrait import Retrait
from Virement import Virement


class VirementInterface(ctk.CTk):
    def __init__(self, interface):
        super().__init__()
        self.interface = interface

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

        self.mdp_compte_envoi = ctk.CTkEntry(self, placeholder_text="Mot de passe du compte d'envoi", width=250,
                                             height=35,
                                             font=config.font_button, show="*")
        self.mdp_compte_envoi.pack(pady=10, padx=20, fill=tk.BOTH)

        self.label = ctk.CTkLabel(self, text="Motif du virement", font=config.font_petit)
        self.label.pack(padx=20, pady=(10, 5))

        # motif
        self.libelle = ctk.CTkTextbox(self, font=config.font_button, height=100)
        self.libelle.pack(pady=(0, 20), padx=20, fill=tk.BOTH)

        # button depot
        self.virement = ctk.CTkButton(self, font=config.font_button, fg_color=config.titre_color, hover=False,
                                      border_color=config.titre_color, text_color="black", text="Envoyer",
                                      command=self.virement)
        self.virement.pack(pady=(30, 15), side=tk.RIGHT, padx=20)

        # button generation compte
        self.btn = ctk.CTkButton(self, font=config.font_button, fg_color="transparent", hover=False,
                                 border_color=config.titre_color, text_color=config.titre_color,
                                 text="Generez mon numero", command=self.code_generation)
        self.btn.pack(pady=(30, 15), side=tk.LEFT, padx=20)

        # fermeture
        self.protocol("WM_DELETE_WINDOW", self.close_root)

    def close_root(self):
        self.destroy()
        self.interface.deiconify()

    # generation de numero
    def code_generation(self):
        self.withdraw()

        # fenetre de generation
        dialog = ctk.CTkInputDialog(text="Entrer votre numero de telephone", button_hover_color=config.titre_color,
                                    button_fg_color=config.titre_color, button_text_color="black",
                                    title="Generation de numero", font=config.font_button)

        generation_numero = GenerationCode(dialog.get_input())
        results = generation_numero.generation_code()

        if not len(results) == 0:
            numero = ""
            if len(results) == 1:
                numero = str(results[0][0])
            else:
                for result in results:
                    numero = numero + str(result[0][0]) + "\n\n"
            config.msg("Information", f"Voici vos numeros de compte:\n\n{numero}\n\nEntrer le numero du "
                                      f"compte que vous souhaitez!", "check")
        else:
            config.msg("Erreur", "Desole le numero est incorrect!", "cancel")
        self.deiconify()

    def virement(self):
        virement = Virement(self.code_compte_envoi.get(), self.code_compte_recoit.get(),
                            self.montant.get(), self.mdp_compte_envoi.get(), self.libelle.get(1.0, tk.END))
        result = virement.verification()
        if result == 1:
            # retrait au solde d'enoi
            retrait = Retrait(self.interface, self.code_compte_envoi.get(), float(self.montant.get()),
                              self.mdp_compte_envoi.get(), self.libelle.get(1.0, tk.END))
            type_retrait = retrait.retrait()

            # depot au compte beneficiaire
            depot = Depot(self.interface, self.code_compte_recoit.get(), float(self.montant.get()),
                          self.libelle.get(1.0, tk.END))
            type_depot = depot.depot()

            if type_depot and type_retrait:
                self.destroy()

