def power(num1,power):
    temp = num1
    for x in range(1,power):
        temp *= num1
        print(temp)
        
    return temp

if __name__ == "__main__":
    
    num1 = int(input("Enter a number: "))
    pow = int(input("Enter Exponent: "))
    
    answer = power(num1,pow)
    
    print(f"{num1} raised to {pow} is {answer}")