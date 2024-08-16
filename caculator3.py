#user input 
a = input("enter here:")

#calculations
if '+' in a:
    num1,num2 = a.split("+")
    result = float(num1) + float(num2)
elif '-' in a:
    num1,num2 = a.split("-")
    result = float(num1) + float(num2)
elif '*' in a:
    num1,num2 = a.split("*")
    result = float(num1) * float(num2)
elif '/' in a:
    num1,num2 = a.split("/")
    result = float(num1) / float(num2)
elif '%' in a:
    num1,num2 = a.split("%")
    result = float(num1) % float(num2)
elif '**' in a:
    num1,num2 = a.split("**")
    result = float(num1) ** float(num2)

#printing output 
print(a,("="),{result})
