import math

while True:
    print("\nChoose the math operation.\n\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raising to a power\n6"
          " - Square root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n")

    question = input("\nYour Option From The Menu: ")

    if question == "0":
        sus1 = float(input("\nFirst Value: "))
        sus2 = float(input("\nSecond Value: "))