import pymysql
import ConnexionBDD as bd

# importations des classes
import Configuration as config


class GenerationCode:
    def __init__(self, numero_tel):
        self.numero_tel = numero_tel

    def generation_code(self):

        # requet
        sql = "SELECT code_compte FROM compte WHERE num_tel = %s"
        try:
            bd.donnees_fetche.execute(sql, (self.numero_tel, ))
            result = bd.donnees_fetche.fetchall()
        except pymysql.Error:
            config.msg("Erreur", "Nous avons rencontre un probleme lors "
                                 "de la transaction\nMerci de ressayer", "cancel")
            return
        else:
            return result
