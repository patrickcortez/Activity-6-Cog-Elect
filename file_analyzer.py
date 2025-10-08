def file_analyze(filename):
    try:
        with open(filename,'r') as file:
        
            lines = file.readlines()
        
        linec = len(lines)
        words = sum(len(line.split()) for line in lines)
        characs = sum(len(line) for line in lines)
        
        print(f" Line Count: {linec} \nWord count: {words} \nCharacter count: {characs}")
    
        return 0
    except FileNotFoundError:
        print("File not found!")
        return 1
        
if __name__ == "__main__":
    file = input("Enter File Name: ")
        
    success = file_analyze(file)
    
    if success == 0:
        print("Program Ran Successfully!")    
    else:
        print("Something Went Wrong!")  
      
        
        