from Models.product import Product
from PySide2.QtCore import QObject, Signal, Property
from Models.userfactorModel import userFactorModel


class Productmodel():

    def __int__(self):
        self.product_data = [Product]
        self.factor = [userFactorModel]

    changed = Signal()

    def getTotalCount(self):
        counter: int = 0
        for item in self.factor:
            counter = counter + item.getCount()
        return counter

    totalCountProperty = Property(int, getTotalCount, notify=changed)

    def getTotalFinalPrice(self):
        total_final_price: float = 0
        for item in self.factor:
            total_final_price += (item.getFinalPrice() * item.getCount())
        return total_final_price

    totalFinalPriceProperty = Property(int, getTotalFinalPrice, notify=changed)

    def getTotalPrice(self):
        total_price: float = 0
        for item in self.factor:
            total_price += (item.getPrice() * item.getCount())
        return total_price

    totalPriceProperty = Property(float, getTotalPrice, notify=changed)

    def getProfitForEachProduct(self):
        Price_without_discount: int = 0
        Price_with_discount: int = 0
        Profit = []
        for item in self.factor:
            Price_without_discount += item.getPrice() * item.getCount()
            Price_with_discount += item.getFinalPrice() * item.getCount()
            Profit.append(Price_without_discount - Price_with_discount)
        return Profit

    ProfitForEachProductProperty = Property(int, getProfitForEachProduct, notify=changed)


    def getSummationOfProfits(self):
        All_Profits: int = 0
        for item in self.getProfitForEachProduct():
            All_Profits += item
        return All_Profits






