from asyncio.proactor_events import _ProactorDuplexPipeTransport
from itertools import chain
from operator import truediv
from re import A


class Check_password:
    SpecialSym = ["$", "@", "#", "%", "*"]
    val = True   
    def isSymbol(char):
        val1 = []
        SpecialSym = ["$", "@", "#", "%", "*"]
        if not any(char in SpecialSym):
            val1.append(False)
            return val1
        else:
            val1.append[True]
            return val1

    # def check_password(password):
    #     if len(password) < 8:
    #         print("Password length should be at least 8")
    #         val = False
    #     if not any(char.isdigit() for char in password):
    #         print("Password should have at least one numeral")
    #         val = False
    #     if not any(char.isupper() for char in password):
    #         print("Password should have at least one uppercase letter")
    #         val = False
    #     if not any(char.islower() for char in password):
    #         print("Password should have at least one lowercase letter")
    #         val = False
    #     if (Check_password.isSymbol(char) for char in password) == False:
    #         print("Password should have at least one symbol")
    #         val = (Check_password.isSymbol(char) for char in password)
    #     else:
    #         print("Password correct")
    #         return val

str = "a"
# Check_password.check_password(str)
Check_password.isSymbol(str)