from LoginSystem import LoginSystem
class FoodApp:
    LoginOptions = {1:"Login",2:"Register",3:"Guest",4:"Exit"}
    @staticmethod
    def Init():
        print("<<Welcome to Online Food Ordering >>")

        loginsystem=LoginSystem()
        while True:
            for option in FoodApp.LoginOptions:
                print(f"{option}.{FoodApp.LoginOptions[option]}",end=" ")

            print()
            try:
                choice = int(input("Enter your Choice: " ))
                loginsystem.ValidateOption(FoodApp.LoginOptions[choice])
            except (ValueError,KeyError):
                print("Invalid input.. Please Enter the Valid Choice")
# FoodApp.Init()