from loginModel import LoginModel

class LoginController:
    def login(login,senha):
        usuario = LoginModel.getUsuarioByLogin(login,senha)
        print(usuario)
        print(usuario[0][12])
        print(usuario[0][12]==1)

        if ((len(usuario)>0) and (usuario[0][12]==1)):
            print("foi porra")
            return True,usuario[0][1]
        else:
            print("nao foi porra")
            return False,""