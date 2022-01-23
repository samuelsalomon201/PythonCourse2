import math

while True:
    print("\nChoose the math operation.\n\n0 - Addition\n1 - Subtraction\n2 - Multyplication\n3 - Division\n4 - Modulo\n5 - Raising to a power\n6 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n")
    oper = input("\nYour option from the menu: ")

    if oper == "0":
        val1 = float(input("\nFirst Value: "))
        val2 = float(input("\nSecond Value: "))

        print("\nThe result is: " + str(val1 + val2) + "\n")

        back = input('\nGo back to the main menu? (y/n)ඞ ')