class CheckPassWord:

    def checkPassWord(password):
        isnumeric = False
        for i in password:
         if i.isnumeric():
            isnumeric = True
            break
        isupper = False
        for i in password:
         if i.isupper():
            isupper = True
            break
        islower = False
        for i in password:
         if i.islower():
            islower = True
            break
        if(isnumeric and isupper and islower and not password.isalnum() and len(password)>=8):
            return True
        else:
            return False


  




    




