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
                config.msg("Information", "Le mot de passe est incorrect!", "check")
                return False
