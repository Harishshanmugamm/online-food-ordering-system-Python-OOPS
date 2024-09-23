from Models.AbstractItem import AbstractItem
class FoodItem(AbstractItem):

    def __init__(self,name,rating,price,description):
        super().__init__(name,rating)
        self.Price = price
        self.Description = description

    def DisplayItem(self):
        return f" {self.Name},  Rating: {self.Rating}, Price: {self.Price}, Description: {self.Description}"

