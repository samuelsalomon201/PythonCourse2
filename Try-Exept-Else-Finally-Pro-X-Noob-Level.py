for pp in range(5):
    try:
        print(pp / 0)
    except ZeroDivisionError:
        print("--> MEEP MEEP MEEP ERROR *Python Dying Noises*")
    except NameError:
        print("YOU MISS SPELLED SOMETHING FIX IT NOW")
    except ValueError:
        print("WRONG WRONG WRONG VALUE >:(")
    finally:
        print("I DON'T CARE, I'M GETTING PRINTED EITHER WAY!!!")
