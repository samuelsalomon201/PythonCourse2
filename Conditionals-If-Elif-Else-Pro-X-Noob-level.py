# Sus = 10
#
# if Sus > 5:
#     print("Sus Is Sussier Than 5")
#     print(Sus * 2)
#
# elif Sus == 5:
#     print("Sus And 5 Have The Same Sussiness")
#
# else:
#     print("SNIFF SNIFF Sus Is Less Sussier Than 5")

Sus = 5

print("""
      C
     c
    c
 ._.
 /|\ 
 / \ """)

if Sus == 5 and type(Sus) is int:
    print("Sus Has The Same Sussines Level As 5. And Sus Is An Integer")
    print(Sus)

elif Sus == 10 and type(Sus) is int:
    print("Sus Is An Integer, But Is Sussier Than 5")

while True:
    hewo = input("Whats Da Password???")

    if hewo == "MUDA MUDA MUDA":
        print("ORA ORA ORA")

        back = input('\nGo back? (y/n) ')

        if back == 'YES YES YES':
            continue
        else:
            break

    if hewo == "ORA ORA ORA":
        print("MUDA MUDA MUDA")

        back = input('\nGo back? (y/n)')

        if back == "YES YES YES":
            continue
        else:
            break

    if hewo == "But I Refuse":
        print("NANI")

        back = input('\nGo back? (y/n)')

        if back == "YES YES YES":
            continue
        else:
            break
print(list(range(5, 15, 3)))