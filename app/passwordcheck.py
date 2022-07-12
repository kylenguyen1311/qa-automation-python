class Passwordcheck:
         
    def is_acceptable_password(string):
        list1 = list(string)
        isNumber = False
        isUpper = False
        isLower = False
        isSymbol = False
        noInvalidChar = True
        if len(list1)>=8:
            for i in range(len(list1)):
                
                if list1[i].isdigit() == True:
                    isNumber = True
                    print("is this a number? ", isNumber)

                elif list1[i].islower() == True:
                    isLower = True
                    print("is this a lowercase? ", isLower)

                elif list1[i].isupper() == True:
                    isUpper = True
                    print("is this an uppercase? ", isUpper)

                elif list1[i] in ["!","@", "#", "$","%","^", "&","*","(",")"]:
                    isSymbol = True
                    print("is this a symbol? ", isSymbol)
                
                else:
                    noInvalidChar = False
                    print("character is invalid")

                print(list1[i])
            if (isNumber & isLower & isUpper & isSymbol & noInvalidChar == True):
                print("Your Password is acceptable")
                return True
            else: print("Your Password is unacceptable")
            return False

        else:
            print('Password length is not valid')
            return False

str2 = "abcD8877"
Passwordcheck.is_acceptable_password(str2)