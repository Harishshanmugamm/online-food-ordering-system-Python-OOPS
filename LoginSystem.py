from Validation.Login import Mobile_No_Val, email_check,Password_Validator
from Models.User import User
from Models.UserManager import UserManager

class LoginSystem:
    def Login(self):
        mail_id = email_check()
        password = Password_Validator()
        pass




    def Register(self):
        name=input("Name : ")
        mobile=Mobile_No_Val()
        mail_id = email_check()
        password=Password_Validator()
        user = User(name,mobile,mail_id,password)
        UserManager.AddUser(user)




    def Guest(self):
        pass




    def ValidateOption(self,option):
        match option:
            case 1:
                self.Login()
            case 2:
                self.Register()
            case 3:
                self.Guest()
            case 4:
                print("Thankyou for using our Food App")
                exit()
            case _ :
                print("Enter Options 1 to 4 ")
        pass