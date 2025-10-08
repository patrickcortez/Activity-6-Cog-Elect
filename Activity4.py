if __name__ == "__main__":
    it = 1
    results = []
    while it <= 5:
        
        num = int(input(f"Enter number {it}:"))
        
        
        if num%2 == 0:
            print(f"Number:{num} is Even")
            results.append("Even")
            it = it + 1
        else:
            print(f"Number:{num} is Odd")
            results.append("Odd")
            it = it + 1
    
    for x in results:
        print(f"{x}")
        
        