class ehiVcle:
    def__init__(self,)
class Passenger:



fareChart = {'Banani': 2, 'Mohakhali': 3, 'Mohammadpur':4, 'NewMarket':5, 'Others':6}
v1 = ehiVcle("Dhaka-123", "Bus", 3)
p1 = Passenger("Sam", "Banani")
print("1.===========================")
v1.addPassenger(p1) #Sam has taken the Bus.
print("2.===========================")
p1.calculateFare(v1)  #Calculating fare for Sam
print("3.===========================")
p2 = Passenger("John", "Mohakhali")
p3 = Passenger("Bran")
print("4.===========================")
p3.setDestination() #Destination cannot be empty!
print("5.===========================")
p3.setDestination("Kakrail")
print("6.===========================")
v1.addPassenger(p2)
print("7.===========================")
p2.calculateFare(v1)
print("8.===========================")
v1.addPassenger(p3)
print("9.===========================")
p3.calculateFare(v1)
p4 = Passenger("Mark", "Mohammadpur")
print("10.===========================")
p4.setDestination()
print("11.===========================")
v1.addPassenger(p4)
v1.addPassenger(Passenger("Jack", "New Market"))
print("12.===========================")
v1.details()
v2 = Vehicle("Chittagong-798", "Car", 0)
print("13.===========================")
v2.addPassenger(p1)
v2.addPassenger(p3)
print("14.===========================")
v2.details()
