class LoginSystem:
    pass


class foodApp:
    LoginOptions = {1:"Login",2:"Register",3:"Guest",4:"Exit"}
    @staticmethod
    def Init():
        print("<<Welcome to Online Food Ordering >>")

        for option in foodApp.LoginOptions:
            print(f"{option}.{foodApp.LoginOptions[option]}",end=" ")
# foodApp.Init()