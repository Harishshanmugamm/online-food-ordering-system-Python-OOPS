from Models.User import User
class UserManager:
    __Users = []

    @classmethod
    def AddUser(cls,userobj):
        if isinstance(userobj,User):
            cls.__Users.append(userobj)
            print("You have been Successfully registered")



    @classmethod
    def FindUser(cls,mailid,pwd):
        for user in cls.__Users:
            if user.Email_Id == mailid and user.Password == pwd:
                return user