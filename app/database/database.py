fake_bd = []
def get_user(username: str):
    """
    Функция для поиска пользователя по имени пользователя. 
    В реальном проекте это должно быть запросом к базе данных.
    """
    for user in fake_bd:
        if user.get("username") == username:
            return user
    return None