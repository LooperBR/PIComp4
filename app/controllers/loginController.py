from loginModel import LoginModel

class LoginController:
    def login(login,senha):
        usuario = LoginModel.getUsuarioByLogin(login,senha)
        if len(usuario)>0:
            return "<p>Ola "+usuario[0][3]+"!</p>",usuario[0][1]
        else:
            return "<p>usuario nao encontrado!</p>",""