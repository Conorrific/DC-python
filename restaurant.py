class Restaurant:
    def __init__(self,restaurant_type,food_type):
        self.restaurant_type = "casual"
        self.food_type = "mexican"
    def describe_restaurant(self,restaurant_type,food_type):
        print(f"The type of food is {food_type}, and the restaurant is {restaurant_type}")

    def open_restaurant(self):
        print("the restaurant is open")

restaurant = Restaurant("casual","Mexican")
restaurant.open_restaurant()
restaurant.describe_restaurant("Mexican","tasty")

print(restaurant.food_type)
print(restaurant.restaurant_type)


