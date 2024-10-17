class Users:
    def __init__(self, nome, senha, admin = False):
         self.nome = nome
         self.senha = senha
         self.admin = admin

    def __repr__(self):
        return f"Users(nome={self.nome}, senha={self.senha}, admin={self.admin})"     

users = []

user_1 = Users("muborges", "12345")
users.append(user_1)
user_2 = Users("rafapi", "12345", True)
users.append(user_2)