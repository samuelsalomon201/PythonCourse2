class MyRouter(object):
    "Do You Know Da Wae"
    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.seralno = serialno
        self.ios = ios

    def print_router(self, manuf_date):
        print("The router name is: ", self.routername)
        print("The router model is: ", self.model)
        print("The serial number of: ", self.serialno)
        print("The IOS version is: ", self.ios)
        print("The model and date combined: ", self.model + manuf_date)
          #Router
    router1 = ('R1', '2600', '123456', '12.4')
    print(router1)