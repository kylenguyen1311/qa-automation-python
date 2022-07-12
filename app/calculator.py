from pickle import FALSE


class Calculator:
    
    def is_even(number):
        if(isinstance(number,int)):
            if (number%2==1):
              return False
            else:
                return True
        else:
            raise Exception("number is not interger")
