from AbstractItem import AbstractItem
class FoodMenu(AbstractItem):

    def __init__(self,name):
        super().__init__(name)
        self.FoodItems=[]
