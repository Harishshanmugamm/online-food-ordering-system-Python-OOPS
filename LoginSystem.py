from Validation.Login import Mobile_No_Val, email_check, Password_Validator
from Models.User import User
from Models.UserManager import UserManager
from Controllers.MainMenu import MainMenu


class LoginSystem:
    def Login(self):
        mail_id = email_check()
        password = Password_Validator()
        user = UserManager.FindUser(mail_id, password)
        if user is not None:
            print("Login Successful......")
            menu = MainMenu()
            menu.Start()
        else:
            print("Invalid Email_id / Password...... Please Retry!!")

    def Register(self):
        name = input("Name : ")
        mobile = Mobile_No_Val()
        mail_id = email_check()
        password = Password_Validator()
        user = User(name, mobile, mail_id, password)
        UserManager.AddUser(user)

    def Guest(self):
        print("You are now browsing as a guest.")
        print("Note: You won't be able to place orders as a guest.")

        menu = MainMenu(guest_mode=True)
        menu.Start()

    def Exit(self):
        print("Thank you for using our Food App")
        exit()

    def ValidateOption(self, option):
        getattr(self, option)()
