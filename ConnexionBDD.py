import pymysql
from CTkMessagebox import CTkMessagebox

# importations des classes
import Configuration as config

try:
    bd_connexion = pymysql.connect(
        host="localhost",
        user="root",
        password="mysql2023",
        database="BANQUES")

    donnees_fetche = bd_connexion.cursor()

except:
    CTkMessagebox(title="Erreur", message="Nous avons rencontré un problème lors de la connexion à la base de données",
                  icon="cancel", button_color=config.titre_color, button_text_color="black",
                  text_color="white", button_hover_color=config.titre_color, icon_size=(32, 32))
