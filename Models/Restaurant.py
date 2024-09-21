from Models.AbstractItem import AbstractItem
from Models.FoodMenu import FoodMenu
class Restaurant(AbstractItem):

    def __init__(self,name,rating,location,offer):
        super().__init__(name,rating)
        self.Location=location
        self.Offer=offer
        self.__FoodMenu=[]

        @property
        def FoodMenu(self):
            return self.__FoodMenu

        @FoodMenu.setter
        def FoodMenu(self, items):
            for item in items:
                if not isinstance(item, FoodMenu):
                    print("Invalid FoodMenu..")
                    return
                self.__FoodMenu = items