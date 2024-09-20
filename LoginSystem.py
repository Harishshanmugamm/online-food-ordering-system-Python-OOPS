import re
from Models.User import User

class LoginSystem:
    def Login(self):
        pass
    def Register(self):
        name=input("Name : ")
        checkno_true=True
        while checkno_true:
            mobile = input("Mobile No: ")
            checkregex=re.fullmatch('[6-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]',mobile)
            if checkregex!=None:
                checkno_true=False
            else:
                print("Please Enter the valid Mobile Number")
        mobile=int(mobile)
        check_email=True
        while check_email:
            mail_id = input("Email Id: ")
            checkregex = re.fullmatch('[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[A-Z|a-z]{2,7}',mail_id)
            if checkregex!=None:
                check_email=False
            else:
                print("Please Enter the valid Email Address")
        mail_id = mail_id
        check_password=True
        while check_password:
            print("Note :8-16 Character with Special Characters and Symbols")
            password = input("Password: ")
            checkregex=re.fullmatch(r'[A-Za-z0-9!@#$%^&*()]{8,16}', password)
            if checkregex!=None:
                check_password=False
            else:
                print("Please Enter the valid Password with 8-16 Character with Special Characters and Symbols")
        password = password
        user = User(name,mobile,mail_id,password)
        pass
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