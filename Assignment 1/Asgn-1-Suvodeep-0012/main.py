def calculator(a,b,operation):
    if(operation == "" or operation == "add"):
        return a+b
    else:
        if(operation == "subtract"):
            return a-b
        elif(operation == "multiply"):
            return a*b
        elif(operation == "divide"):
            if(b==0):
                return "divide by zero is not allowed"
            else:
                return a/b
        else:
            return "wrong intput!!!"
        
'''a=int(input("Enter the first element: "))
b=int(input("Enter the second element: "))
operation=input("Enter the operation do you like: ")
print(calculator(a,b,operation))'''

print(calculator(3,4,""))
print(calculator(4,5,"subtract"))
print(calculator(4,5,"multiply"))
print(calculator(20,5,"divide"))
print(calculator(20,0,"divide"))
print(calculator(20,5,"abc"))
