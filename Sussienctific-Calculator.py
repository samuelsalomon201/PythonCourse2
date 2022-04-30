import math

while True:
    print(
        "\nChoose the math operation.\n\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5" \
        " - Raising to a power\n6 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n11 - None\n")
    operation = input("\nYour option from the menu ඞ: ")

    if operation == "0":
        val1 = float(input("\nFirst Value: "))
        val2 = float(input("\nSecond Value: "))

        print("\nThe result is: " + str(val1 + val2) + "\n")

        back = input('\nGo back to the main menu? (y/n)ඞ ')

        if back == 'y':
            continue
        else:
            break

    elif operation == "1":
        val1 = float(input("\nFirst Value: "))
        val2 = float(input("\nSecond Value: "))

        print("\nThe result is: " + str(val1 - val2) + "\n")

        back = input('\nGo back to the main menu? (y/n)ඞ ')

        if back == 'y':
            continue
        else:
            break

    elif operation == "2":
        val1 = float(input("\nFirst Value: "))
        val2 = float(input("\nSecond Value: "))

        print("\nThe result is: " + str(val1 * val2) + "\n")

        back = input('\nGo back to the main menu? (y/n)ඞ ')

        if back == 'y':
            continue
        else:
            break

    elif operation == "3":
        val1 = float(input("\nFirst Value: "))
        val2 = float(input("\nSecond Value: "))

        print("\nThe result is: " + str(val1 / val2) + "\n")

        back = input('\nGo back to the main menu? (y/n)ඞ ')

        if back == 'y':
            continue
        else:
            break

    elif operation == "4":
        val1 = float(input("\nFirst Value: "))
        val2 = float(input("\nSecond Value: "))

        print("\nThe result is: " + str(val1 % val2) + "\n")

        back = input('\nGo back to the main menu? (y/n)ඞ ')

        if back == 'y':
            continue
        else:
            break

    elif operation == "5":
        val1 = float(input("\nFirst Value: "))
        val2 = float(input("\nSecond Value: "))

        print("\nThe result is: " + str(math.pow(val1, val2)) + "\n")

        back = input('\nGo back to the main menu? (y/n)ඞ ')

        if back == 'y':
            continue
        else:
            break

    elif operation == "6":
        val1 = float(input("\nEnter value for extracting the square root: "))

        print("\nThe result is: " + str(math.sqrt(val1)) + "\n")

        back = input('\nGo back to the main menu? (y/n)ඞ ')

        if back == 'y':
            continue
        else:
            break

    elif operation == "7":
        val1 = float(input("\nEnter value for calculating the logarithm to base: "))

        print("\nThe result is: " + str(math.log(val1)) + "\n")

        back = input('\nGo back to the main menu? (y/n)ඞ ')

        if back == 'y':
            continue
        else:
            break

    elif operation == "8":
        val1 = float(input("\nEnter value (in degrees) for calculating the sine: "))

        print("\nThe result is: " + str(math.sin(math.radians(val1))) + "\n")

        back = input('\nGo back to the main menu? (y/n)ඞ ')

        if back == 'y':
            continue
        else:
            break

    elif operation == "9":
        val1 = float(input("\nEnter value (in degrees) for calculating the cosine: "))

        print("\nThe result is: " + str(math.cos(math.radians(val1))) + "\n")

        back = input('\nGo back to the main menu? (y/n)ඞ ')

        if back == 'y':
            continue
        else:
            break

    elif operation == "9":
        val1 = float(input("\nEnter value (in degrees) for calculating the tangent: "))

        print("\nThe result is: " + str(math.tan(math.radians(val1))) + "\n")

        back = input('\nGo back to the main menu? (y/n)ඞ ')

        if back == 'y':
            continue
        else:
            break

    elif operation == "11":
        break
    else:
        print("Invalid Option")
        continue
