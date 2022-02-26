for pp in range(5):
    try:
        print(pp / 0)
    except ZeroDivisionError as BRUH:
        print(BRUH, "--> MEEP MEEP MEEP ERROR ERROR")
