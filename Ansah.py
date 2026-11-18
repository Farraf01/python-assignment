# PIZZA
# for pizza in pizzas:
#  message = f'You all know that I like {pizza.title()} pizza.'
#  print(message)
# # print('\n I am a big fan of tasty pizzas.\t')
# # # print('I really like those!')
# # squares=[ value**3 for value in range(1,11)]
# # print(squares)
# # for num in range(1,21):
# #  print(num)
# # squares = []
# # for value in range(1,5):
# #     square = value / 2
# #     squares.append(square)
# # print(squares)
# # print('The first three items in the lists are:',pizzas[1:4])
# # print("The first three items in the meaning of the list are:",pizzas[2:])
# # pizzas = ['pork','sausage pizza','chicken pizza','cheese pizza']
# # pizzas.append("kelewele")
# # print(pizzas)
# # frinds_pizza = pizzas[ :]
# # print(frinds_pizza)
# # basic_foods = ('jollof','waakye','gob3','Kenkey','Ampesie')
# # print('\tOriginal food:')
# # for food in basic_foods:
# #     print(food)

# # restructured_foods = ('banku','akpele',"kelewele")
# # print('restructured_foods:')
# # for food in restructured_foods:
# #     print(food)
# # def railways( good morning):
# #     print('hello',railways)
# # car = 'Picanto'
# # car.lower() == 'picanto'
# # print(car == 'Picanto')
# # alien_color = ['green','yellow','red']
# # for color in alien_color :
# #  if color == 'blue':
# #    print('You just earned 5 points for shooting an alien')
# # else:
# #      print('You just earned 10 points')
# # stages in life
# age = 17
# if age< 2:
#     print('You are a baby')
# elif  age < 4:
#     print('You are a toddler')
# elif age < 13:
#     print('You are a kid')
# elif age < 20:
#     print('You are a teenager')
# elif age < 65:
#     print('You are an adult')
# else :
#     print('You an an elderly person')

# favourite_fruits = ['strawberry','mango','watermelon']

# if 'strawberry' in favourite_fruits:
#     print('You really like strawberries!')
# if 'mango' in favourite_fruits:
#     print('You really like mangoes!')
# if 'watermelon' in favourite_fruits:
#     print('You really like watermelons!')
#  Hello admin 5 to 8
# users = ['admin','Karl','Nolan','Raf','Tisha']

# for user in users:
#     if user == 'admin':
#         print('Hello admin,would you like to see a status report?')
#     else :
#         print(f'Hello {user},thank you for logging in again')
# 5 to 9 No Users
#  5 to 11 ordinal numbers
# ordinal = [1,2,3,4,5,6,7,8,9]

# for num in ordinal:
#     if num == 1:
#         print('1st')
#     elif num == 2:
#         print('2nd')
#     elif num == 3:
#         print('3rd')
#     else:
#         print(f'{num}th')
# glossary = {
#     "append": "add",
#     "del": "delete",
#     "elif": "condition",
#     "get": "replacement",
#     "formatted strings" : "used for editing by inputting"}

# # Glossary 2 ,6 to 4
# for key,value in glossary.items():
#     print(f'for {key}, the meaning is {value}')
# favourite_languages = {
#     'Janice':'python',
#     'Patrick' :'c++',
#     'Richmond' :'java',
#     'Anthony':'javascript',
#     'Raymond': 'scratch',
# }
# print('The list of all those who have taken the poll:')
# for key,vals in favourite_languages.items():
#     print(key)
#rental 
# car = input('Which rental car do you want?')
# print(f'Let me see if i can get you are {car}.')


# people= input('How many people are at the table?')
# people = int(people)

# if people > 8:
#     print('Your table is ready')
# else :
#     print('You  will have to wait for a table')
# DELI
# food = ['burger','shawarma','pizza','indomie']
# foods = []
# while food:
#     foo = food.pop()

#     print(f'Checking food: {foo.title()}')
#     foods.append(foo)
# def display_message():
#     """What I am learning in this chapter"""
#     print("I am learning functions")


# display_message()
#T Shirt
# def make_shirt(size,something):
#     """Using functions"""
#     print(f'\nThe size of my T-Shirt is {size.title()}')
#     print(f'This is the text that should be on it,{something}')

# make_shirt('Extra Large','The gods are not to be blamed')
# def city_country(city,country):
#     cittry = f'{city.title()},{country.title()}'
#     print(cittry)


# city_country('Accra','Ghana')
# short_texts = ['rice','salad','shito','okro','ginger']

# def shorties():
#     for texts in short_texts:
#      print(texts)
# shorties()
#Sandwiches 
# def wanted_items(*items):
#      print(items)

# wanted_items('Rice','Koko')
# def build_profile(first,last,**user_profile):
#     user_profile['first_name'] = first
#     user_profile['last_name'] = last
#     print(user_profile)

# build_profile('albert','Rover',location= 'Dome',hometown='Osu')
#cars
# def cars(name,manufacturer,**others):
#     others['car_name']= name
#     others['manu']= manufacturer
#     return others

# car = cars('BMW','M5',colour = 'ash',)
# print(car)
# def printings_items(*toppings):
#     """I am printing the items that i want"""
#     print(f'These are all the toppings:')
#     print(f'{toppings}')

# class Restaurant:

#     def __init__(rest,restaurant_name,cuisine_type):
#         rest.restaurant_name = restaurant_name
#         rest.cuisine_type = cuisine_type
#         rest.number_served = 0

#     def describe_restaurant(rest):
#         print(f'This is the name of the restaurant {restaurant.restaurant_name} and the cuisine type is {restaurant.cuisine_type}')
#         print(f'This is the name of the Restaurant {restaurants.restaurant_name} and the cuisine is {restaurant.cuisine_type}')
#         print(f'The name of customers the restaurant has served is {rest.number_served}')
        

#     def update_number_served(rest,topps):
#             rest.number_served = topps

#     def increment_number_served(rest,topppps):
#         rest.number_served += topppps

# restaurant = Restaurant("Abena Chop Bar","Fufu")
# restaurants = Restaurant('Chef Abyys Kitchen','Banku')

# restaurant.update_number_served(45)
# restaurant.describe_restaurant()

# restaurant.increment_number_served(25)
# restaurant.describe_restaurant()



class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Vanilla", "Chocolate", "Strawberry", "Mango"]

    def show_flavors(self):
        print("Available ice cream flavors:")
        for flavor in self.flavors:
            print(flavor)



