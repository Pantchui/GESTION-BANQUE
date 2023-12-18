# importations des classes
import Configuration as config


class Virement:
    def __init__(self, code_compte_envoi, code_compte_recoit, montant, mdp_compte_envoi, libelle):
        self.code_compte_envoi = code_compte_envoi
        self.code_compte_recoit = code_compte_recoit
        self.montant = montant
        self.mdp_compte_envoi = mdp_compte_envoi
        self.libelle = libelle

    def verification(self):
        if not (self.code_compte_envoi and self.code_compte_recoit and self.montant
                and self.mdp_compte_envoi and self.libelle) == "":
            # verification du solde intitiale
            try:
                self.montant = float(self.montant)
            except ValueError:
                config.msg("Attention", "Le montant n'est pas valide", "warning")
                return 0

            # si aucune exception n'est declanche
            else:
                return 1
        else:
            config.msg("Attention", "Veuillez completer tous les champs", "warning")
            return 0
