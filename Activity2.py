def math(x,y,z):
    match(z):
        case '+':
            return x+y
        case '-':
            return x-y
        case '*':
            return x*y
        case '/':
            return x/y
        

if __name__ == "__main__":
    
    num1 = int(input("Enter 1st Number: "))
    
    num2 = int(input("Enter 2nd Number: "))
    
    operator = input("Enter any operator (+,-,*,/): ")
    
    answer = math(num1,num2,operator)
    
    print(f"Answer: {answer}")