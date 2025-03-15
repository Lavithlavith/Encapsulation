class Phone:
    def __init__(self, brand , RAM , ROM, colour, AndroidVersion, Password):
        self.brand = brand
        self.RAM=RAM
        self.ROM = ROM
        self.colour= colour
        self.AndroidVersion = AndroidVersion
        self.__Password= Password #put '--' before the name to hide it
    
    def printInfo(self):
        print("Brand: ", self.brand)
        print("ROM : ", self.ROM )
        print("RAM: ",self.RAM)
        print("AndroidVersion: ",self.AndroidVersion)


Samsung = Phone("Samsung","16gb","128gb", "Black", "OneUi-7","something")
print(Samsung.AndroidVersion)
print(Samsung.RAM)
print(Samsung.ROM)
#print(Samsung.__Password)#this will throw a error as it will not be able to find it!