# for i in range(5):
#     try:
#         print(i / 0)
#     except ZeroDivisionError as e:
#         print(e, "--> Division BY 0 Is Not Allowed, Sorry Noob!!!")

# for i in range(5):
#     try:
#         print(i / 1)
#     except ZeroDivisiwonError:
#         print("Division By 0 Is Just Right ;)")
#     print("The Rest Of The Code")

for i in range(5):
    try:
        print(i / 1)
    except ZeroDivisionError:
        print("NOOB Division By 0 Is For NOOBS")
    except NameError:
        print("NOOB Name Error Detected!")
    except ValueError:
        print("SUPER NOOB Wrong Value")