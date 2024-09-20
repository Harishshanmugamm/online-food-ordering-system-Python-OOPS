from Models.User import User
class UserManager:
    __Users = []

    @classmethod
    def AddUser(cls,userobj):
        if isinstance(userobj,User):
            cls.__Users.append(userobj)
            print("You have been Successfully registered")