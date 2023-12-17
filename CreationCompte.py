import pymysql
from CTkMessagebox import CTkMessagebox
from random import randint
from datetime import datetime

# importations des classes
import Configuration as config
import ConnexionBDD as bd


class CreationCompte:
    def __init__(self, nom_utilisateur, prenom_utilisateur, email, numero_tel, mdp1, mdp2, pays, ville, quartier,
                 residence, proffesion, type_compte, solde_intiale):

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

                    # verification du solde intitiale
                    try:
                        self.solde_intiale = float(self.solde_intiale)
                    except ValueError:
                        CTkMessagebox(title="Attention", message="Les solde initial n'est pas valide",
                                      icon="warning", button_color=config.titre_color, button_text_color="black",
                                      text_color="white", button_hover_color=config.titre_color, icon_size=(32, 32))
                        return 0

                    # si aucune exception n'est declanche
                    else:
                        return 1

                else:
                    CTkMessagebox(title="Attention", message="Les mots de passe ne correspondent pas!",
                                  icon="warning", button_color=config.titre_color, button_text_color="black",
                                  text_color="white", button_hover_color=config.titre_color, icon_size=(32, 32))
                    return 0
            else:
                CTkMessagebox(title="Attention", message="L'adresse mail n'est pas correct!",
                              icon="warning", button_color=config.titre_color, button_text_color="black",
                              text_color="white", button_hover_color=config.titre_color, icon_size=(32, 32))
                return 0
        else:
            CTkMessagebox(title="Attention", message="Veuillez completer tous les champs",
                          icon="warning", button_color=config.titre_color, button_text_color="black",
                          text_color="white", button_hover_color=config.titre_color, icon_size=(32, 32))
            return 0

    def insertion(self):

        # generation automatiques de code
        code = (str(randint(1000000000000, 9999999999999)) + "." + str(datetime.now().year) + "." +
                str(randint(100000000000000, 99999999999999999)) + "_BANQUES" + "." + str(randint(10000, 99999)))
        # sql
        sql = ("INSERT INTO compte(code_compte, type_compte, nom, prenom, email, num_tel, mdp, pays, "
               "ville, quartier, residence, proffesion, date_creation, solde_initial, solde) "
               "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

        try:
            bd.donnees_fetche.execute(sql, (code, self.type_compte, self.nom_utilisateur, self.prenom_utilisateur,
                                            self.email, self.numero_tel, self.mdp1, self.pays, self.ville,
                                            self.quartier, self.residence, self.proffession,
                                            datetime.now(), self.solde_intiale, self.solde_intiale))
            # valider la transaction
            bd.bd_connexion.commit()
        except pymysql.Error:
            CTkMessagebox(title="Erreur", message="Nous avons rencontré un probleme lors de la création du compte\n"
                                                  "Merci de ressayer!", icon="cancel", button_color=config.titre_color,
                          button_text_color="black", text_color="white",
                          button_hover_color=config.titre_color, icon_size=(32, 32))
        else:
            CTkMessagebox(title="Succes", message="Votre compte a bien été créé!", icon="cancel",
                          button_color=config.titre_color, button_text_color="black", text_color="white",
                          button_hover_color=config.titre_color, icon_size=(32, 32))

            # import de la classe menu
            from Main import Main
            app = Main()
            app.mainloop()
        finally:
            bd.donnees_fetche.close()
            bd.bd_connexion.close()
