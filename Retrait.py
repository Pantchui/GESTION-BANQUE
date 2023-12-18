from datetime import datetime
import pymysql

# importations des classes
import Configuration as config
import ConnexionBDD as bd


class Retrait:
    def __init__(self, interface, code_compte_retrait, montant_retrait, mdp_compte_retrait, libelle_retrait):
        self.interface = interface
        self.code_compte_retrait = code_compte_retrait
        self.montant_retrait = montant_retrait
        self.mdp_compte_retrait = mdp_compte_retrait
        self.libelle_retrait = libelle_retrait

    def verification(self):
        if not (self.code_compte_retrait and self.montant_retrait and self.libelle_retrait
                and self.code_compte_retrait) == "":
            # verification du solde intitiale
            try:
                self.montant_retrait = float(self.montant_retrait)
            except ValueError:
                config.msg("Attention", "Le montant n'est pas valide", "warning")
                return 0

            # si aucune exception n'est declanche
            else:
                return 1
        else:
            config.msg("Attention", "Veuillez completer tous les champs", "warning")
            return 0

    def retrait(self):

        # requet
        sql = "SELECT type_compte, solde, solde_initial, mdp FROM compte WHERE code_compte = %s"
        try:
            bd.donnees_fetche.execute(sql, (self.code_compte_retrait,))
            results = bd.donnees_fetche.fetchone()
        except pymysql.Error:
            config.msg("Erreur", "Nous avons rencontré un probleme de la transaction\n"
                                 "Merci de ressayer!", "cancel")
        else:
            if results is not None:
                if not len(results) == 0:

                    # verification du mot de pase
                    if results[3] == self.mdp_compte_retrait:
                        nouveau_solde = results[1] - self.montant_retrait
                        __retrait__ = False

                        # verification du type de compte
                        if results[0] == "Courant":
                            # condition de retrait compte courant
                            if nouveau_solde > results[2]:
                                __retrait__ = True
                            else:
                                config.msg("Attention", "Vous ne pouvez pas éffectuer cette transaction\n"
                                                        "car après l'opération le solde finale sera inférieur au "
                                                        "solde intitiale\nAlors que vous possédez un compte courant!",
                                           "warning")
                        else:
                            # condition de retrait compte epargne
                            if results[1] > self.montant_retrait:
                                __retrait__ = True
                            else:
                                config.msg("Attention", "Vous ne pouvez pas éffectuer cette transaction\n"
                                                        "car le montant a rétirer est supérieur au solde totale de "
                                                        "votre compte\nEt vous possédez un compte epargne!",
                                           "warning")
                        if __retrait__:
                            # mise a jour du solde
                            sql1 = "UPDATE compte SET solde = %s WHERE code_compte = %s"
                            # enregistrement de la transaction
                            sql2 = "INSERT INTO transactions VALUES(%s, %s, %s, %s, %s)"
                            try:
                                # debut des transactions
                                bd.bd_connexion.begin()
                                # modification du solde
                                bd.donnees_fetche.execute(sql1, (nouveau_solde, self.code_compte_retrait))

                                # enregistrement de la transaction
                                bd.donnees_fetche.execute(sql2, (config.numero(), self.code_compte_retrait,
                                                                 datetime.now(), "R", self.libelle_retrait))
                                # validation des transactions
                                bd.bd_connexion.commit()
                            except pymysql.Error:
                                config.msg("Erreur", "Nous avons rencontré un probleme de la transaction\n"
                                                     "Merci de ressayer!", "cancel")
                                return False
                            else:
                                config.msg("Succèss", f"Votre retrait sur le compte {self.code_compte_retrait}\n"
                                                      f" a bien été éffectué avec succès!", "check")

                                # affichage du main
                                self.interface.deiconify()
                                return True
                    else:
                        config.msg("Attention", "Le mot de passe est incorrect\n"
                                                "Merci de ressayer!", "warning")

                else:
                    config.msg("Information", "Aucun compte n'existe avec ce numero\n"
                                              "Merci de ressayer!", "check")
