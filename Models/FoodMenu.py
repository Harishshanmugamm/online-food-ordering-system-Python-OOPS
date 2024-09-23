from Models.AbstractItem import AbstractItem
from Models.FoodItem import FoodItem
class FoodMenu(AbstractItem):

    def __init__(self,name):
        super().__init__(name)
        self.__FoodItems=[]

    @property
    def FoodItem(self):
        return self.__FoodItems

    @FoodItem.setter
    def FoodItem(self,items):
        for item in items:
            if not isinstance(item,FoodItem):
                print("Invalid FoodItem..")
                return
            self.__FoodItems = items

    def DisplayItem(self):
        return  f"Menu: {self.Name}"

