# Start Of Code
import math

while True:
    print(
        "\nChoose the math operation.\n\n0 - Addition\n1 - Subtraction\n2 - Multyplication\n3 - Division\n4 - Modulo\n5 - Raising to a power\n6 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n")
    oper = input("\nYour option from the menu: ")

    # Addition
    if oper == "0":
        val1 = float(input("\nFirst Value: "))
        val2 = float(input("\nSecond Value: "))

        print("\nThe result is: " + str(val1 + val2) + "\n")

        back = input('\nGo back to the main menu? (y/n)ඞ ')

        if back == 'y':
            continue
        else:
            break

    # Subtraction
    elif oper == "1":
        val1 = float(input("\nFirst Value: "))
        val2 = float(input("\nSecond Value: "))

        print("\nThe result is: " + str(val1 - val2) + "\n")

        back = input('\nGo back to the main menu? (y/n)ඞ ')

        if back == 'y':
            continue
        else:
            break

    # Multyplication
    elif oper == "2":
        val1 = float(input("\nFirst Value: "))
        val2 = float(input("\nSecond Value: "))

        print("\nThe result is: " + str(val1 * val2) + "\n")

        back = input('\nGo back to the main menu? (y/n)ඞ ')

        if back == 'y':
            continue
        else:
            break

    # Division
    elif oper == "3":
        val1 = float(input("\nFirst Value: "))
        val2 = float(input("\nSecond Value: "))

        print("\nThe result is: " + str(val1 / val2) + "\n")

        back = input('\nGo back to the main menu? (y/n)ඞ ')

        if back == 'y':
            continue
        else:
            break

    # Modulo
    elif oper == "4":
        val1 = float(input("\nFirst Value: "))
        val2 = float(input("\nSecond Value: "))

        print("\nThe result is: " + str(val1 % val2) + "\n")

        back = input('\nGo back to the main menu? (y/n)ඞ ')

        if back == 'y':
            continue
        else:
            break

    # Raising to a power
    elif oper == "5":
        val1 = float(input("\nFirst Value: "))
        val2 = float(input("\nSecond Value: "))

        print("\nThe result is: " + str(math.pow(val1, val2)) + "\n")

        back = input('\nGo back to the main menu? (y/n)ඞ ')

        if back == 'y':
            continue
        else:
            break

    # Square root
    elif oper == "6":
        val1 = float(input("\nEnter value for extracting the square root: "))

        print("\nThe result is: " + str(math.sqrt(val1)) + "\n")

        back = input('\nGo back to the main menu? (y/n)ඞ ')

        if back == 'y':
            continue
        else:
            break

    # Logaithm
    elif oper == "7":
        val1 = float(input("\nEnter value for calculating the logarith to base: "))

        print("\nThe result is: " + str(math.log(val1)) + "\n")

        back = input('\nGo back to the main menu? (y/n)ඞ ')

        if back == 'y':
            continue
        else:
            break

    # Sine
    elif oper == "8":
        val1 = float(input("\nEnter value (in degrees) for calculatin the sine: "))

        print("\nThe result is: " + str(math.sin(math.radians(val1))) + "\n")

        back = input('\nGo back to the main menu? (y/n)ඞ ')

        if back == 'y':
            continue
        else:
            break

    # Cosine
    elif oper == "9":
        val1 = float(input("\nEnter value (in degrees) for calculatin the cosine: "))

        print("\nThe result is: " + str(math.cos(math.radians(val1))) + "\n")

        back = input('\nGo back to the main menu? (y/n)ඞ ')

        if back == 'y':
            continue
        else:
            break

    # Tangent
    elif oper == "9":
        val1 = float(input("\nEnter value (in degrees) for calculatin the tangent: "))

        print("\nThe result is: " + str(math.tan(math.radians(val1))) + "\n")

        back = input('\nGo back to the main menu? (y/n)ඞ ')

        if back == 'y':
            continue
        else:
            break

    # Handling invalid options
    else:
        print("\nInvalid option!\n")
        continue

# End Of Code ඞ
