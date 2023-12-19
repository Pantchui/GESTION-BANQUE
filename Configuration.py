from random import randint
from CTkMessagebox import CTkMessagebox

# les polices
font_titre = ("Ubuntu", 60)
font_body = ("Ubuntu", 40)
font_label = ("Ubuntu", 25)
font_moyen = ("Ubuntu", 17)
font_button = ("Ubuntu", 15)
font_petit = ("Ubuntu", 12)


# les couleur
hover_color_button = "#4f514f"
titre_color = "#00ff00"


def msg(titre, message, type_icon):
    CTkMessagebox(title=titre, message=message,
                  icon=type_icon, button_color=titre_color, button_text_color="black",
                  text_color="white", button_hover_color=titre_color, icon_size=(32, 32))


def numero():
    generation_numero = str(randint(100000000000000000000000000000, 999999999999999999999999999999))
    return generation_numero
