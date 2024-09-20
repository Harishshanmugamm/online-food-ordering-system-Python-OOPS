import re
def Mobile_No_Val():
    checkno_true = True
    while checkno_true:
        mobile = input("Mobile No: ")
        checkregex = re.fullmatch('[6-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', mobile)
        if checkregex != None:
            checkno_true = False
        else:
            print("Please Enter the valid Mobile Number")
def email_check():
    check_email = True
    while check_email:
        mail_id = input("Email Id: ")
        checkregex = re.fullmatch('[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[A-Z|a-z]{2,7}', mail_id)
        if checkregex != None:
            check_email = False
        else:
            print("Please Enter the valid Email Address")
def Password_Validator():
    check_password = True
    while check_password:
        print("Note :8-16 Character with Special Characters and Symbols")
        password = input("Password: ")
        checkregex = re.fullmatch(r'[A-Za-z0-9!@#$%^&*()]{8,16}', password)
        if checkregex != None:
            check_password = False
        else:
            print("Please Enter the valid Password with 8-16 Character with Special Characters and Symbols")
