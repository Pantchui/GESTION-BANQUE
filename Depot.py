from datetime import datetime
import pymysql

# importations des classes
import Configuration as config
import ConnexionBDD as bd


class Depot:
    def __init__(self, interface, code_compte_depot, montant_depot, motif_depot):
        self.interface = interface
        self.code_compte_depot = code_compte_depot
        self.montant_depot = montant_depot
        self.motif_depot = motif_depot

    def verification(self):
        if not (self.code_compte_depot and self.montant_depot and self.motif_depot) == "":
            # verification du solde intitiale
            try:
                self.montant_depot = float(self.montant_depot)
            except ValueError:
                config.msg("Attention", "Le montant n'est pas valide", "warning")
                return 0

            # si aucune exception n'est declanche
            else:
                return 1
        else:
            config.msg("Attention", "Veuillez completer tous les champs", "warning")
            return 0

    def depot(self):

        # requet
        sql = "SELECT type_compte, solde FROM compte WHERE code_compte = %s"
        try:
            bd.donnees_fetche.execute(sql, (self.code_compte_depot,))
            results = bd.donnees_fetche.fetchone()
        except pymysql.Error:
            config.msg("Erreur", "Nous avons rencontré un probleme de la transaction\n"
                                 "Merci de ressayer!", "cancel")
        else:
            if results is not None:
                if not len(results) == 0:
                    if results[0] == "Courant":
                        nouveau_solde = results[1] + self.montant_depot
                    else:
                        nouveau_solde = ((results[1] + self.montant_depot) * 5) / 100 + results[1] + self.montant_depot

                    # mise a jour du solde
                    sql1 = "UPDATE compte SET solde = %s WHERE code_compte = %s"
                    # enregistrement de la transaction
                    sql2 = "INSERT INTO transactions VALUES(%s, %s, %s, %s, %s)"
                    try:
                        # debut des transactions
                        bd.bd_connexion.begin()
                        # modification du solde
                        bd.donnees_fetche.execute(sql1, (nouveau_solde, self.code_compte_depot))

                        # enregistrement de la transaction
                        bd.donnees_fetche.execute(sql2, (config.numero(), self.code_compte_depot,
                                                         datetime.now(), "R", self.motif_depot))
                        # validation des transactions
                        bd.bd_connexion.commit()
                    except pymysql.Error:
                        config.msg("Erreur", "Nous avons rencontré un probleme de la transaction\n"
                                             "Merci de ressayer!", "cancel")
                        return False
                    else:
                        config.msg("Success", f"Votre depot sur le compte {self.code_compte_depot}\n "
                                              f"a bien été éffectué avec succès!!", "check")

                        # affichage du main
                        self.interface.deiconify()

                        return True
                else:
                    config.msg("Information", "Aucun compte n'existe avec ce numero\n"
                                              "Merci de ressayer!", "check")
