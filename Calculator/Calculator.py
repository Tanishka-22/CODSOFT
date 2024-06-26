
def add(num1, num2):
    return num1 + num2
 
def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("----------------CALCULATOR----------------")

print("Choose the key for desired operation :-\\n" 
        " 1. Add\\n 2. Subtract\\n 3. Multiply\\n 4. Divide\\nv5. exit")


key = int(input("Enter the key :"))

    
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))


if key == 1:
    print(num_1, "+", num_2, "=",
            add(num_1, num_2))

elif key == 2:
    print(num_1, "-", num_2, "=",
            subtract(num_1, num_2))
    
elif key == 3:
    print(num_1, "*", num_2, "=",
            multiply(num_1, num_2))
    
elif key == 4:
    print(num_1, "/", num_2, "=",
            divide(num_1, num_2))
      

else:
    print("Invalid input")
        

key = int(input("Enter the key :"))

