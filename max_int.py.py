num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
list = []

while num_int >=0:
    list.append(num_int)
    num_int = int(input("Input a number: "))
    
max_int = max(list)


print("The maximum is", max_int) 
