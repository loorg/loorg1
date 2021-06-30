# Сложность O(N)
def authorizat1 (user, user_log, user_password):
    for key, value in user.items():
        if key == user_log:
            if value ['password'] == user_password and value ['Activ']:
                return "  Здравствуй путник, вход разрешон"
            elif value ['password'] == user_password \
                    and not value ['Activ']:
                return " Тебя нет в списке"
            elif value ['password'] != user_password:
                return "Не раслышал, может другой пароль?"
    return "Увы, схватить чужестранца"


#Cложность O(1)

def authorizat2 (user, user_log, user_password):
    if user.get(user_log):
        if user[user_log]['password'] == user_password \
               and user[user_log]['ACTIV']:
            return "  Здравствуй путник, вход разрешон"
        elif user[user_log]['password'] == user_password \
                and not user[user_log]['ACTIV']:
              return " Тебя нет в списке"
        elif user[user_log]['password'] != user_password \
                and user[user_log]['ACTIV']:

             return "Не раслышал, может другой пароль?"
    else:
        return "Увы, схватить чужестранца"
