from Validation.Login import Mobile_No_Val, email_check,Password_Validator
from Models.User import User
from Models.UserManager import UserManager
from Controllers.MainMenu import MainMenu

class LoginSystem:
    def Login(self):
        mail_id = email_check()
        password = Password_Validator()
        user = UserManager.FindUser(mail_id,password)
        if user is not None:
            print("Login Successful......")
            menu =MainMenu()
        else:
            print("Invalid Email_id / Password...... Please Retry!!")


    def Register(self):
        name=input("Name : ")
        mobile=Mobile_No_Val()
        mail_id = email_check()
        password=Password_Validator()
        user = User(name,mobile,mail_id,password)
        UserManager.AddUser(user)


    def Guest(self):
        pass

    def Exit(self):
        print("Thank you for using our Food App")
        exit()


    def ValidateOption(self,option):
        # match option:
        #     case 1:
        #         self.Login()
        #     case 2:
        #         self.Register()
        #     case 3:
        #         self.Guest()
        #     case 4:
        #        self.Exit()
        #     case _ :
        #         print("Enter Options 1 to 4 ")
        getattr(self,option)()
        pass