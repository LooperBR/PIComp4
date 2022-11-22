from loginModel import LoginModel

class LoginController:
    def login(login,senha):
        usuario = LoginModel.getUsuarioByLogin(login,senha)

        if ((len(usuario)>0) and (usuario[0][12]==1)):
            print("foi porra")
            print(usuario[0][11]==1)
            return True,usuario[0][1],usuario[0][11]
        else:
            print("nao foi porra")
            return False,""