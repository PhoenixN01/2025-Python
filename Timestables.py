x = ""
y = ""
cycle = 0

def timestables():
    while True:
        x = input("Enter a times tables number: ")
        if x.isdigit():
            x = int(x)
            break
        else:
            print("Number must be an integer with no spaces")


    while True:
        y = input(f"Enter a number of multiples of {x}: ")
        if y.isdigit():
            y = int(y)
            break

    n = 0
    for n in range(n + 1, y + 1):
        print(x, " x ", n, " = ", x * n)
    
    global cycle
    cycle = cycle + 1

while True:
    if cycle == 0:
        timestables()
    else:
        restart = input("Would you like another times table?(y/n): ")
        yes_answer = ["y", "Y", "yes", "Yes"]
        if restart in yes_answer:
            timestables()
        else:
            break