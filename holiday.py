# Holiday exercise
# Task is to calculate a user's total holiday cost, including the plane cost, hotel cost and car rental
# Get user input: city_flight, num_nights, rental_days

city_flight = str(input("Enter your desired destination: "))

num_nights = int(input("Enter the number of nights you will be spending in a hotel: "))

rental_days = int(input("Enter the number of days you will be renting a car: "))

# Create 4 functions
# hotel_cost, plane_cost, car_rental, holiday_cost

print("Hello, you have chosen to fly to " + city_flight + "!")


def hotel_cost(num_nights):
    hotel_price = 120
    total_hotel = num_nights * hotel_price
    return total_hotel
print("Your total hotel cost is: ", hotel_cost(num_nights)) 


def plane_cost(city_flight):
    flight_prices = {     # Dictionary created to store flight prices
    "Rome": 300,
    "Paris": 400,
    "New York": 1000,
    "Shanghai": 1400,
    "Johannesburg": 1700
    }
    flight_cost = flight_prices.get(city_flight)
    return flight_cost
flight_cost = plane_cost(city_flight)
print("Your total flight cost is: ", flight_cost)

def car_rental(rental_days):
    rental_price = 70
    total_car = rental_days * rental_price
    return total_car
print("Your total car rental cost is: ", car_rental(rental_days))

def holiday_cost(city_flight, num_nights, rental_days):
    hotel_cost_total = hotel_cost(num_nights)
    plane_cost_total = plane_cost(city_flight)
    car_rental_total = car_rental(rental_days)
    total_cost = hotel_cost_total + plane_cost_total + car_rental_total 
    return total_cost
total_cost = holiday_cost(city_flight, num_nights, rental_days)

print("Your total holiday cost is: ", total_cost)
print("Enjoy your holiday!")

