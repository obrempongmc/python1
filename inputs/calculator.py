print( "Simple CALCULATOR ")

# function for checking operator
def operation(sign):
    if sign == '+':
        return first_number + second_number
    elif sign == '%':
        return first_number % second_number
    elif sign == '*':
        return first_number * second_number
    elif sign == '/':
         return first_number / second_number
    else: print("choose a sign")


first_number = float(input(" First number "))
your_sign =str(input("Enter your operator"))


# while your_sign != '+' or '-'or '/' or '*':
#     print ("chose + ,-,/,*")
#     your_sign =str(input("Enter your operator"))
#     break

second_number = float(input("Second number "))

print(operation(your_sign))





















