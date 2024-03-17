first_name = input( "Enter your name ? " )
age =input( "what is your age ? ")

print ( "hello"  + first_name + "\n" +"you are "+ age+ "years old" )

friends=['frank','francis','franklin','franka','fredrick','fredy','freda']
friends.insert(1,'derrick')
print(friends)


first_number= int(input("your first number  "))
second_number =int(input("your second number   "))

if first_number> second_number:
    print("first pick was greater than second ")
else:
    print ("second number was greater ")