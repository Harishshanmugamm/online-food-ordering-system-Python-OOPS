# **🍔 Online Food Ordering System (OOP-based)**
## Overview
This Online Food Ordering System is built using Python and follows an Object-Oriented Programming (OOP) paradigm. The project allows users to browse through different restaurants, view their food items, and place orders. It also supports user authentication and has a guest mode where users can browse but cannot place orders.

![image](https://github.com/user-attachments/assets/59e236b5-f3ad-4998-a7d9-07f1837756ef)
![image](https://github.com/user-attachments/assets/6f35af2d-b6bf-4ace-8dd4-f742aad32c33)
![image](https://github.com/user-attachments/assets/b53c0be7-6ee8-4584-b4e2-c57c97fd93a1)
![image](https://github.com/user-attachments/assets/ad1619dd-12b2-45ef-8278-d9592220de6a)
![image](https://github.com/user-attachments/assets/51d9b5b2-8e2c-41f8-a348-6bd6cf4ce39e)
![image](https://github.com/user-attachments/assets/a0dc1ad6-fe4a-4b16-99cd-238fc9ab668f)
![image](https://github.com/user-attachments/assets/7b7d7231-bcf8-4f89-b27b-15f35b58f524)



## **Features**
1. User Authentication:

    * Users can register and log in to place orders.
    * Guest users can browse food items but cannot place orders.

2. Restaurants & Menus:

    *Restaurants are listed with ratings and location.
    *Each restaurant has multiple menus with a variety of food items.

3. Order Placement:

    * Registered users can add food items to their cart and proceed to checkout.
    * Cart management includes the ability to remove items and see the total price.
    * Multiple payment methods: Cards, UPI, and Netbanking.

4. Sorting & Searching:

    * Restaurants can be sorted by rating or average price.
    * Search functionality to find restaurants or specific food items.

## **Key Components**

1. ` LoginSystem.py `
#### Handles user authentication:

  * Login: Validates email and password.
  * Register: Allows users to register by providing their name, email, mobile, and password.
  * Guest: Enables guest access with browsing-only capabilities.

2. ` MainMenu.py `
#### Provides access to the main functionalities:

  *  ShowRestaurants: Displays available restaurants.
  * ShowFoodItems: Displays available food items in a selected menu.
  * SearchRestaurants: Allows users to search for restaurants by name.
  * SearchFoodItem: Allows users to search for food items.
  * ShowTopRestaurants: Lists top restaurants by rating or price.

3. ` Cart.py `
#### Manages the cart functionality:

  * **Add to Cart**: Users can add selected food items to their cart.
  * **Remove Items**: Users can remove items from their cart.
  * **ProcessOrder**: Finalizes the order and displays the total price.

4. ` FoodManager.py `
#### Responsible for managing restaurants, menus, and food items:

  * **Restaurants**: List of available restaurants.
  * **FindRestaurant**: Search for a specific restaurant by name.
  * **FindFoodItem**: Search for food items across all restaurants.

5. ` UserManager.py `
#### Handles user registration and authentication:

  * **FindUser**: Validates user credentials.
  * **AddUser**: Registers a new user into the system.

# How to Run

### Clone the Repository:

```
git clone https://github.com/yourusername/online-food-ordering-system-oop.git
```
### Navigate to the Project Directory:

```
cd online-food-ordering-system-oop
```

### Run the Application:
```
python main.py
```

# Usage
  * Login or Register: Start by logging in or registering as a user. Alternatively, you can continue as a guest.
  *  Browse Restaurants: View available restaurants, sort them by rating or price, and browse their menus.
  * Search: Use the search feature to find a restaurant or a specific food item.
  * Place Orders: If you’re logged in, add food items to your cart, and proceed to checkout with your preferred payment method.
  * Guest Mode: If using guest mode, you can only browse menus and restaurants without placing any orders.

# Project Structure
```


|-- Controllers
|   |-- FoodManager.py     # Manages food items and restaurants
|   |-- MainMenu.py        # Main menu logic
|
|-- Models
|   |-- AbstractItem.py     # Base class for items
|   |-- Cart.py             # Cart functionalities
|   |-- FoodItem.py         # Food item class
|   |-- FoodMenu.py         # Menu class
|   |-- Restaurant.py       # Restaurant class
|   |-- User.py             # User class
|   |-- UserManager.py      # Manages user registration and login
|
|-- Validation
|   |-- FoodApp.py          # Application-level validations
|   |-- LoginSystem.py      # Validates user inputs (email, password, etc.)
|
|-- main.py                # Entry point of the application

```
# Future Enhancements
  1. Add more payment options.
  2. Implement delivery tracking.
  3. Integrate with a database to persist user data and order history.
# Contributing
#### Feel free to fork this repository and submit pull requests. Any contributions to improve the functionality or design of the system are welcome.

# License
This project is licensed under the MIT License.
