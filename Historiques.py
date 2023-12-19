import pymysql

import ConnexionBDD as bd
import Configuration as config


class Historiques:

    def __init__(self, interface, code_compte, mdp_compte):
        self.interface = interface
        self.code_compte = code_compte
        self.mdp_compte = mdp_compte

    def verification(self):
        # reauet
        sql = "SELECT COUNT(*) FROM compte WHERE code_compte = %s AND mdp = %s"
        try:
            bd.donnees_fetche.execute(sql, (self.code_compte, self.mdp_compte))
            result = bd.donnees_fetche.fetchone()
        except pymysql.Error:
            config.msg("Erreur", "Nous avons rencontré un probleme de la transaction\n"
                                 "Merci de ressayer!", "cancel")
            return False
        else:
            if result[0] > 0:
                return True
            else:
                config.msg("Attention", "Le mot de passe est incorrect!\n"
                                        "Merci de reessayer!", "warning")
                return False

    def affichages_transaction(self):
        sql = "SELECT * FROM transactions WHERE code_compte = %s ORDER BY date_transaction DESC"
        try:
            bd.donnees_fetche.execute(sql, (self.code_compte, ))
            results = bd.donnees_fetche.fetchall()
        except pymysql.Error:
            config.msg("Erreur", "Nous avons rencontré un probleme de la transaction\n"
                                 "Merci de ressayer!", "cancel")
            return False
        else:
            return results

    def affichages_information(self):
        sql = "SELECT * FROM compte WHERE code_compte = %s"
        try:
            bd.donnees_fetche.execute(sql, (self.code_compte,))
            results = bd.donnees_fetche.fetchone()
        except pymysql.Error:
            config.msg("Erreur", "Nous avons rencontré un probleme de la transaction\n"
                                 "Merci de ressayer!", "cancel")
            return False
        else:
            return results
