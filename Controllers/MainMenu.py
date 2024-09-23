from Controllers.FoodManager import FoodManager
from Models.Cart import Cart


class MainMenu:
    __Options = {
        1: "ShowRestaurants",
        2: "ShowFoodItems",
        3: "SearchRestaurants",
        4: "SearchFoodItem",
        5: "ShowTopRestaurants",
        6: "Logout"
    }

    def __init__(self):
        self.__FoodManager = FoodManager()
        self.__cart = None

    def ShowRestaurants(self):
        print("-" * 50)
        i = 1
        for res in self.__FoodManager.Restaurants:
            print(f"{i}. {res.DisplayItem()}")
            i += 1
        print("-" * 50)
        choice = int(input("Please Select the Restaurant: "))
        restaurants = self.__FoodManager.Restaurants
        if 1 <= choice <= len(restaurants):
            selected_res = restaurants[choice - 1]
            self.ShowFoodMenus(selected_res.FoodMenus)
        else:
            print("Invalid selection. Please choose a valid Restaurant....")

    def ShowTopRestaurants(self):
        print("Sort by: \n1. Rating \n2. Price")
        sort_choice = int(input("Enter your choice for sorting: "))

        if sort_choice == 1:
            # Sort restaurants by rating
            sorted_restaurants = sorted(self.__FoodManager.Restaurants, key=lambda x: x.Rating, reverse=True)
        elif sort_choice == 2:
            # Sort restaurants by average price
            sorted_restaurants = sorted(self.__FoodManager.Restaurants, key=lambda x: x.AvgPrice)
        else:
            print("Invalid choice. Showing restaurants by rating as default.")
            sorted_restaurants = sorted(self.__FoodManager.Restaurants, key=lambda x: x.Rating, reverse=True)

        print("\nTop Restaurants:")
        print("-" * 50)
        for i, res in enumerate(sorted_restaurants, 1):
            print(f"{i}. {res.DisplayItem()} (Rating: {res.Rating}, Avg Price: {res.AvgPrice})")
        print("-" * 50)

    def ShowFoodItems(self, foodItems=None):
        if foodItems is not None:
            print("-" * 100)
            i = 1
            for item in foodItems:
                print(f"{i}. {item.DisplayItem()}")
                i += 1
            print("-" * 100)

            choices = list(map(int, input("Please Choose your food items (comma separated): ").split(',')))
            self.__cart = Cart(foodItems, choices)
            self.__cart.ProcessOrder(foodItems)

        else:
            print("-" * 100)
            food_items = []
            for res in self.__FoodManager.Restaurants:
                print(res.DisplayItem())
                for menus in res.FoodMenus:
                    print(f"  {menus.DisplayItem()}")
                    for item in menus.FoodItems:
                        print(f"    - {item.DisplayItem()}")
                        food_items.append(item)  # Collect all food items from all menus
            print("-" * 100)

            # Allow user to add items to cart from the entire list
            if food_items:
                choices = list(
                    map(int, input("Please Choose your food items from the list (comma separated): ").split(',')))
                self.__cart = Cart(food_items, choices)
                self.__cart.ProcessOrder(food_items)
            else:
                print("No food items available.")

    def SearchRestaurants(self):
        resName = input("Enter Restaurant Name: ")
        res = self.__FoodManager.FindRestaurant(resName)
        if res is not None:
            print('-' * 50)
            print("Restaurant Found....")
            print('-' * 50)
            print(f"Name: {res.Name}, Rating: {res.Rating} | Location: {res.Location}")
            self.ShowFoodMenus(res.FoodMenus)
        else:
            print(f"No Restaurant found with the name {resName}")

    def SearchFoodItem(self):
        itemName = input("Enter an Item Name: ")
        result = self.__FoodManager.FindFoodItem(itemName)

        if result:
            print('-' * 50)
            print("Food Item Found....")
            print('-' * 50)

            food_items = []
            for res, menu, item in result:
                print(f"Restaurant: {res.DisplayItem()}")
                print(f"  Menu: {menu.DisplayItem()}")
                print(f"    - {item.DisplayItem()}")
                food_items.append(item)

            print('-' * 50)
            choices = list(
                map(int, input("Please Choose the items to add to your cart (comma separated): ").split(',')))
            self.__cart = Cart(food_items, choices)
            self.__cart.ProcessOrder(food_items)
        else:
            print("Food Item not found.")

    def ShowFoodMenus(self, menus):
        print("\n\nList of Menus Available")
        print("-" * 50)
        i = 1
        for menu in menus:
            print(f"{i}. {menu.DisplayItem()} ")
            i += 1
        print("-" * 50)
        choice = int(input("Please Select the Menu Type: "))
        if 1 <= choice <= len(menus):
            selected_menu = menus[choice - 1]
            self.ShowFoodItems(selected_menu.FoodItems)
        else:
            print("Invalid selection. Please choose a valid menu.")

    def Logout(self):
        print("Logging out... Goodbye!")
        exit()

    def Start(self):
        while True:
            print("\nMain Menu:")
            for option in MainMenu.__Options:
                print(f"{option}. {MainMenu.__Options[option]}")
            print()
            try:
                choice = int(input("Enter your Choice: "))
                value = MainMenu.__Options[choice]
                getattr(self, value)()
            except (ValueError, KeyError):
                print("Invalid input. Please Enter a Valid Choice")
