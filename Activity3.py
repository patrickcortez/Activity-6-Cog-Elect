def factorial(number):
    temp = 1
    for x in range(1,number+1):
        temp = temp * x
    
    return temp

if __name__ == "__main__":
    number = int(input("Enter any number"))
    
    answer = factorial(number)
    
    print(f"Answer: {answer}")