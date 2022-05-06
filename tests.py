"""while into while"""

a = 1
while a <= 10:
    b = 1
    while b <= 10:
        print(f"{a} + {b} = {a + b}")
        b += 1
    a += 1
print("end")


"""Getting better in condictons"""
#What should I do after waking up?
get_up = True
coffee = "warm"
if get_up == True:
    print("Get up, and make some coffee!")
    if coffee == "warm":
        print("it's a good coffe, indeed!")
    else:
        print(coffee)
else:
    print('Sleep a little longer...')

#cableway
students = 5
monitors = 1
if (students + monitors) > 10:
    print("Sorry, the cableway have reached it's full capacity")
else:
    print("everybody aboard!!")