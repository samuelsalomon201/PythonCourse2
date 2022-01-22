class MyRouter(object):
    "This is a class that describes the characteristics of a router."

    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios

    def print_router(self, manuf_date):
        print("The router name is: ", self.routername)
        print("The router model is: ", self.model)
        print("The serial number of: ", self.serialno)
        print("The IOS version is: ", self.ios)
        print("The model and date combined: ", self.model + manuf_date)


class MyNewRouter(MyRouter):
    def __init__(self, routername, model, serialno, ios, portsno):
        MyRouter.__init__(self, routername, model, serialno, ios)
        self.portsno = portsno

    def print_new_router(self, string):
        print(string + self.model)


new_router1 = MyNewRouter("newr1", "1800", "111111", "12.2", "10")

print(new_router1.portsno)
print(new_router1.model)
print(new_router1.ios)




print(new_router1.print_router("ahakhasjakls"))

print(new_router1.print_new_router("ahakhasjakls"))




print(issubclass(MyNewRouter, MyRouter))