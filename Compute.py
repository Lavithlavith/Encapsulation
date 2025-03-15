class Computer:
    def __init__(self,brand, seller, age, maxPrice,ProductId):
        self.brand=brand
        self.seller= seller
        self.age = age
        self.__maxprice = maxPrice
        self.__ProductId=ProductId

    def Sales(self): 
        print("Brand: ",self.brand)
        print("Seller: ", self.seller)
        print("Age of Computer: ", self.age)
        
    def getMaxPrice(self):
        return self.__maxprice
    def setMaxPrice(self,newprice):
        self.__maxprice = newprice
    
    def getProductId(self):
        return self.__ProductId
    def setProductId (self, UpdatedProductId):
        self.__ProductId = UpdatedProductId
        

Amazon= Computer("Windows", "Amazon", "1 year", "£1300","WIN_0912345")
print(Amazon.getMaxPrice())
Amazon.setMaxPrice("£1800") 
print(Amazon.getMaxPrice())

print(Amazon.getProductId())
Amazon.setProductId("WIN_9991204")
print(Amazon.getProductId())