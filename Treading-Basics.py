import threading

import time

print("Chumi-mimi")


# Arigato Gyro Beatdown.
def oraoraora():
    print("ora ora ora ora ora ora ora ora ora ora")
    time.sleep(0.001)
    print("ora ora ora ora ora ora ora ora ora ora")


oras = []

for i in range(70):
    th = threading.Thread(target=oraoraora())
    th.start()
    oras.append(th)

for th in oras:
    th.join()

print("ORA\nඞ")
