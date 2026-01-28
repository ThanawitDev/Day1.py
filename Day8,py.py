my_bike = {
    "model" : "ducati v4s",
    "fuel" : 20
}

def refuel(bike):
    bike["fuel"] += 80

def start_journey(bike):
    if bike["fuel"] >= 50:
        print (f"Your fuel is {my_bike['fuel']} Vrooom!! Ready to go for ride huh?")
    else:
        print (f"Your fuel is {my_bike['fuel']} Hell nah...")

start_journey(my_bike)
print ("You need to find Gas Station")
refuel(my_bike)
start_journey(my_bike)