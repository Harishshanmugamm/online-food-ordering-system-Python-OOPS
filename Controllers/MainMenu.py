from traceback import print_tb

from Controllers.FoodManager import FoodManager
# from Models.Restaurant import Restaurant


class MainMenu:
    __Options = {1:"ShowRestaurants", 2:"ShowFoodItems",3:"SearchRestaurants",4:"SearchFoodItem",5:"Logout"}

    def __init__(self):
        self.__FoodManager = FoodManager()

    def ShowRestaurants(self):
        print("-" * 50)
        i=1
        for res in self.__FoodManager.Restaurants:
            print(f"{i}. {res.Name} => Rating : {res.Rating}")
            i+=1
        print("-"*50)
        choice = int(input("Please Select the Restaurant: "))
        restaurants = self.__FoodManager.Restaurants
        if 1 <= choice <= len(restaurants):
            selected_res = restaurants[choice - 1]
            self.ShowFoodMenus(selected_res.FoodMenus)
        else:
            print("Invalid selection. Please choose a valid Restaurant....")
        # res = self.__FoodManager.Restaurants[choice-1]
        # self.ShowFoodMenus(res.FoodMenus)

    def ShowFoodItems(self,foodItems = None):

        if foodItems is not None:
            print("-" * 100)
            i=1
            for item in foodItems:
                print(f"{i}. {item.Name},  Rating: {item.Rating}, Price: {item.Price}, Description: {item.Description}")
                i+=1
            print("-" * 100)
        else:
            print("-"*100)
            for res in self.__FoodManager.Restaurants:
                print(f"{res.Name} => Rating: {res.Rating} | Location: {res.Location}")
                for menus in res.FoodMenus:
                    print(f"  Menu: {menus.Name}")
                    for item in menus.FoodItems:
                        print(
                            f"    - {item.Name}: Rating: {item.Rating}, Price: {item.Price}, Description: {item.Description}")
                print("-"*100)
            # print(f"{res.Name} => Rating : {res.Rating}")
        pass

    def SearchRestaurants(self):
        resName = input("Enter Restaurant Name: ")
        res = self.__FoodManager.FindRestaurant(resName)
        if res is not None:
            print('-'*50)
            print("Restaurant Found....")
            print('-' * 50)
            print(f"Name : {res.Name}, Rating : {res.Rating} | Location : {res.Location}")
            self.ShowFoodMenus(res.FoodMenus)
        else:
            print(f"No Restaurant found on the name {resName}")

    def SearchFoodItem(self):
        itemName = input ("Enter a Item Name ")

    def ShowFoodMenus(self,menus):
        print("\n\nList of Menus Available")
        print("-" * 50)
        i=1
        for menu in menus:
            print(f"{i}  Menu: {menu.Name}")
            i+=1
        print("-" * 50)
        choice = int(input("Please Select the Menu Type: "))
        if 1 <= choice <= len(menus):
            selected_menu = menus[choice - 1]
            self.ShowFoodItems(selected_menu.FoodItems)
        else:
            print("Invalid selection. Please choose a valid menu.")


    def Logout(self):
        pass


    def Start(self):
        while True:
            for option in MainMenu.__Options:
                print(f"{option}.{MainMenu.__Options[option]}",end=" ")
            print()
            try:
                choice = int(input("Enter your Choice: " ))
                value =MainMenu.__Options[choice]
                getattr(self,value)()
            except (ValueError,KeyError):
                print("Invalid input.. Please Enter the Valid Choice")