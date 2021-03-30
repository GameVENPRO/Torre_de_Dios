from app.utils.game_logic import get_xp


def user_text(user, username):
    return (f"🌟Felicidades! Nuevo nivel!🌟 \n Presiona /level_up \n\n"
            f"La batalla de los 7 castillos comienza en \n\n"
            f"{user.heroflag} {username} Maestro del Castillo de {user.castlename}\n"
            f"🏅Level:{user.lvl} \n"
            f"⚔️ Ataque: {user.ataque}"
            f"🛡️ Defensa: <b>{user.defensa}</b>\n"
            f"🔥Exp: {user.xp}/{get_xp(user.lvl)}\n"
            f"♥ Vida: <b>{user.vida}</b>/{user.max_vida}\n"            
            f"🔋Resistencia:{user.stamina}/{user.stamina}"
            f"{'' if user.max_mana == 0 else  '💧Mana: ' + str(user.mana) + '/' + str(user.max_mana)}\n"
            f"💰{user.oro}"
            f"{'' if user.bolsa_de_oro == 0 else '👝' + str(user.bolsa_de_oro)}"
            f"{'' if user.gemas == 0 else '💎' + str(user.gemas)}\n\n"
            f"🎽Equipamiento +15⚔️+64🛡\n"
            f"🎒Bolso: {user.bolso}/{user.bolso} /inv \n\n"
            f"Mascota: \n"
            f"🐭 giant mouse Mousekt3 (24 lvl) 😁 /pet \n\n"
            f"Estado:\n"
            f"{user.estado}\n\n"
            f"More: /heroe")
    
def heroe_text(user, username):
    return (f"{user.heroflag} {username} \n"
            f"🏅Level:{user.lvl} \n"
            f"⚔️ Ataque: {user.ataque}"
            f"🛡️ Defensa: <b>{user.defensa}</b>\n"
            f"🔥Exp: {user.xp}/{get_xp(user.lvl)}\n"
            f"♥ Vida: <b>{user.vida}</b>/{user.max_vida}\n"            
            f"🔋Resistencia:{user.stamina}/{user.stamina}"
            f"{'' if user.max_mana == 0 else  '💧Mana: ' + str(user.mana) + '/' + str(user.max_mana)}\n"
            f"💰{user.oro}"
            f"{'' if user.bolsa_de_oro == 0 else '👝' + str(user.bolsa_de_oro)}"
            f"{'' if user.gemas == 0 else '💎' + str(user.gemas)}\n"
            f"📚Pergaminos:\n"
            f"🎉Logros:\n"
            f"🏛Información de clase: \n"
            f"🚹Male \n\n"
            f"✨Efectos: 🛡↑/efectos \n\n"
            f"🎽Equipamiento +15⚔️+64🛡\n"
            f"Casco:\n"
            f"Grantes:\n"
            f"Armadura:\n"
            f"Botas:\n"
            f"Arma Principal: ⚔️+\n"
            f"Arman Segundaria: ⚔️+\n"
            f"Especial\n"
            f"Anillo\n"
            f"Collar\n\n"
            f"🎒Bolso: {user.bolso}/{user.bolso} /inv \n"
            f"📦Almacén: {user.stock} /alm")
    
    def inv_user():
        return(f"🎽Equipamiento +15⚔️+64🛡\n 🎒Bag(0/15):")

    def stock_user():
        return(f"📦Almacen (0/5000):\n\n")

    def misc_user():
        return(f"🗃Varios \n\n")

    def alchemy_user():
        return(f"⚗️Alquimia \n\n")
    
    def crafting_user():
        return(f"⚒Elaboración \n\n")
    
    def equipment_user():
        return(f"🏷Equipamiento \n\n")
    

