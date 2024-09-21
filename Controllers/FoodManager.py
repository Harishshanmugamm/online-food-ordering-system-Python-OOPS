from Models.FoodItem import FoodItem
from Models.FoodMenu import FoodMenu
from Models.Restaurant import  Restaurant


class FoodManager:

    def __init__(self):
        self.Restaurants = self.__PrepareRestaurants()

    def __PrepareFoodItems(self):
        item1 = FoodItem("Chicken Briyani", 4, 200, "Authentic Chettinad-style biryani with rich spices")
        item2 = FoodItem("Infused Chicken", 4.5, 500, "Succulent chicken infused with bold flavors and aromatic spices")
        item3 = FoodItem("Paneer Butter Masala", 5, 250, "Creamy and rich with paneer cubes")
        item4 = FoodItem("Chicken 65", 4.5, 180, "Spicy deep-fried chicken appetizer")
        item5 = FoodItem("Mutton Rogan Josh", 5, 350, "Tender mutton cooked in aromatic spices")
        item6 = FoodItem("Fish Fry", 4, 220, "Crispy fried fish with South Indian spices")
        item7 = FoodItem("Vegetable Pulao", 3.5, 150, "Fragrant rice cooked with mixed vegetables")
        item8 = FoodItem("Tandoori Chicken", 4.7, 300, "Marinated chicken cooked in a clay oven")
        item9 = FoodItem("Butter Naan", 4, 40, "Soft flatbread topped with butter")
        item10 = FoodItem("Gulab Jamun", 4.2, 90, "Soft milk-solid dumplings soaked in sugar syrup")
        return [item1,item2,item3,item4,item5,item6,item7,item8,item9,item10]

    def __PrepareFoodMenus(self):
        FoodItems= self.__PrepareFoodItems()
        menu1=FoodMenu("Veg")
        menu1.FoodItems=[FoodItems[2],FoodItems[6],FoodItems[8]]
        menu2=FoodMenu("Non-Veg")
        menu2.FoodItems=[FoodItems[0],FoodItems[3],FoodItems[4],FoodItems[5],FoodItems[7]]
        menu3=FoodMenu("Desserts")
        menu3.FoodItems=[FoodItems[9]]
        menu4=FoodMenu("Special")
        menu4.FoodItems=[FoodItems[1]]
        return [menu1,menu2,menu3,menu4]

    def __PrepareRestaurants(self):
        FoodMenus = self.__PrepareFoodMenus()
        res1 = Restaurant("A2B", 5,"Chennai",15)
        res1.FoodMenus=[FoodMenus[2],FoodMenus[6],FoodMenus[8],FoodMenus[9]]
        res2 = Restaurant("Rameshwaram Cafe",4.9, "Bangalore", 20)
        res2.FoodMenus = [FoodMenus[2],FoodMenus[6],FoodMenus[8],FoodMenus[9]]
        res3 = Restaurant("Annapoona",3.9,"Coimbatore",25)
        res3.FoodMenus = [FoodMenus[2], FoodMenus[6], FoodMenus[8], FoodMenus[9]]
        res4 = Restaurant("Tovo",4.7,"Coimbatore",16)
        res4.FoodMenus = [FoodMenus[1],FoodMenus[0],FoodMenus[3],FoodMenus[4],FoodMenus[5],FoodMenus[7],FoodMenus[9]]
        res5 = Restaurant("Dindugal Thalapakatti", 4.8,"Dindugal",25)
        res5.FoodMenus = [FoodMenus[0],FoodMenus[3],FoodMenus[4],FoodMenus[5],FoodMenus[7],FoodMenus[9]]
        return [res1,res2,res3,res4,res5]
