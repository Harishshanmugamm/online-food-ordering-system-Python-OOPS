class Cart:

    def __init__(self, items, choices):
        self.Choices = choices
        self.FoodItems = self.__AddToCart(items)

    def __AddToCart(self, items):
        foodDictionary = {}
        for choice in self.Choices:
            if choice > len(items):
                raise KeyError(f"Invalid food item selection: {choice}")
            if choice in foodDictionary:
                foodDictionary[choice] += 1
            else:
                foodDictionary[choice] = 1
        return foodDictionary

    def ProcessOrder(self, foodItems):
        self.ShowCart(foodItems)
        while True:
            print("\nOptions: ")
            print("1. Proceed to payment")
            print("2. Remove an item from the cart")
            option = int(input("Enter option: "))

            if option == 1:
                self.__ProcessPayment(foodItems)
                break
            elif option == 2:
                self.RemoveItemFromCart(foodItems)
            else:
                print("Invalid option. Please choose again.")

    def ShowCart(self, foodItems):
        print("-" * 50)
        Total = 0
        for item in self.FoodItems:
            price = self.FoodItems[item] * foodItems[item - 1].Price
            Total += price
            print(f"{foodItems[item - 1].Name} x {self.FoodItems[item]} = {price}")
        print(f"Total: {Total}")
        print("-" * 50)

    def RemoveItemFromCart(self, foodItems):
        print("Current Cart:")
        self.ShowCart(foodItems)
        try:
            item_to_remove = int(input("Enter the number of the food item to remove: "))
            if item_to_remove in self.FoodItems:
                self.FoodItems[item_to_remove] -= 1
                if self.FoodItems[item_to_remove] == 0:
                    del self.FoodItems[item_to_remove]
                print(f"Item {foodItems[item_to_remove - 1].Name} removed.")
            else:
                print("Item not found in cart.")
        except (ValueError, KeyError):
            print("Invalid input.")

    def __ProcessPayment(self, foodItems):
        Total = 0
        for item in self.FoodItems:
            price = self.FoodItems[item] * foodItems[item - 1].Price
            Total += price
        print(f"Total Amount: {Total}")

        # Payment Options
        print("\nChoose Payment Method:")
        print("1. Credit/Debit Card")
        print("2. UPI")
        print("3. Net Banking")
        payment_option = int(input("Enter Payment Method: "))

        if payment_option == 1:
            self.__ProcessCardPayment(Total)
        elif payment_option == 2:
            self.__ProcessUPIPayment(Total)
        elif payment_option == 3:
            self.__ProcessNetBankingPayment(Total)
        else:
            print("Invalid Payment Method.")

    def __ProcessCardPayment(self, amount):
        card_number = input("Enter Card Number: ")
        expiry_date = input("Enter Expiry Date (MM/YY): ")
        cvv = input("Enter CVV: ")

        # Simple validation
        if len(card_number) == 16 and len(expiry_date) == 5 and len(cvv) == 3:
            print(f"Payment of {amount} successful via Card!")
        else:
            print("Invalid Card details. Please try again.")

    def __ProcessUPIPayment(self, amount):
        upi_id = input("Enter UPI ID: ")

        if '@' in upi_id:
            print(f"Payment of {amount} successful via UPI!")
        else:
            print("Invalid UPI ID. Please try again.")

    def __ProcessNetBankingPayment(self, amount):
        bank_name = input("Enter Bank Name: ")
        account_number = input("Enter Account Number: ")
        password = input("Enter Password: ")

        # Simple validation
        if len(account_number) >= 8 and len(password) >= 6:
            print(f"Payment of {amount} successful via Net Banking!")
        else:
            print("Invalid Account details. Please try again.")
