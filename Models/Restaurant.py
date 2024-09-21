from AbstractItem import AbstractItem
class Restaurant(AbstractItem):

    def __init__(self,name,rating,location,offer):
        super().__init__(name,rating)
        self.Location=location
        self.Offer=offer
        self.FoodMenu=None