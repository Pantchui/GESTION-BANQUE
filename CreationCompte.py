import pymysql
from random import randint
from datetime import datetime

# importations des classes
import Configuration as config
import ConnexionBDD as bd


class CreationCompte:
    def __init__(self, interface, nom_utilisateur, prenom_utilisateur, email, numero_tel, mdp1, mdp2, pays, ville,
                 quartier, residence, proffesion, type_compte, solde_intiale):

        self.interface = interface
        self.nom_utilisateur = nom_utilisateur
        self.prenom_utilisateur = prenom_utilisateur
        self.email = email
        self.numero_tel = numero_tel
        self.mdp1 = mdp1
        self.mdp2 = mdp2
        self.pays = pays
        self.ville = ville
        self.quartier = quartier
        self.residence = residence
        self.proffession = proffesion
        self.type_compte = type_compte
        self.solde_intiale = solde_intiale

    def verification(self):
        # verification des entrees vide
        if not (self.nom_utilisateur and self.prenom_utilisateur and self.email and
                self.numero_tel and self.mdp1 and self.mdp2 and self.pays and self.ville and
                self.quartier and self.proffession and self.residence and self.solde_intiale) == "":

            # verification de l'adresse mail
            if '.' in self.email and '@' in self.email:

                # verification des mots de passe
                if self.mdp1 == self.mdp2:

                    # verification longeurs du mot de passe
                    if len(self.mdp1) >= 8:
                        # verification du solde intitiale
                        try:
                            self.solde_intiale = float(self.solde_intiale)
                        except ValueError:
                            config.msg("Attention", "Les solde initial n'est pas valide", "warning")
                            return 0

                        # si aucune exception n'est declanche
                        else:
                            return 1
                    else:
                        config.msg("Attention", "Les mots doivent avoir au moins 8 caracteres!", "warning")
                        return 0

                else:
                    config.msg("Attention", "Les mots de passe ne correspondent pas!", "warning")
                    return 0
            else:
                config.msg("Attention", "L'adresse mail n'est pas correct!", "warning")
                return 0
        else:
            config.msg("Attention", "Veuillez completer tous les champs", "warning")
            return 0

    def creation(self):

        # generation automatiques de code
        code = str(randint(1000000000000000000000000, 9999999999999999999999999))
        # sql
        sql1 = ("INSERT INTO compte(code_compte, type_compte, nom, prenom, email, num_tel, mdp, pays, "
                "ville, quartier, residence, proffesion, date_creation, solde_initial, solde) "
                "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        sql2 = "INSERT INTO transactions VALUES(%s, %s, %s, %s, %s)"

        try:
            if self.type_compte == "Courant":
                solde = self.solde_intiale
            else:
                solde = (self.solde_intiale * 5) / 100 + self.solde_intiale

            # debut de la transaction
            bd.bd_connexion.begin()

            bd.donnees_fetche.execute(sql1, (code, self.type_compte, self.nom_utilisateur, self.prenom_utilisateur,
                                             self.email, self.numero_tel, self.mdp1, self.pays, self.ville,
                                             self.quartier, self.residence, self.proffession,
                                             datetime.now(), self.solde_intiale, solde))

            bd.donnees_fetche.execute(sql2, (config.numero(), code, datetime.now(), "D",
                                             "Solde initiale. Ouverture du compte"))
            # valider la transaction
            bd.bd_connexion.commit()
        except pymysql.Error:
            config.msg("Erreur", "Nous avons rencontré un probleme lors de la création du compte\n"
                                 "Merci de ressayer!", "cancel")
        else:
            config.msg("Terminé", "Votre compte a bien été créé!", "check")

            # import de la classe main
            self.interface.deiconify()
