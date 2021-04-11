import uuid


# Represents the customer of the car insurance company
class Customer:
    def __init__(self, name, address):
        self.ID = str(uuid.uuid1())
        self.name = name
        self.address = address
        self.cars = []  # List of cars
        self.claims = []

    def addCar(self, car):
        self.cars.append(car)

    # convert object o JSON
    def serialize(self):
        return {
            'id': self.ID,
            'name': self.name,
            'address': self.address,
        }


class Car:
    def __init__(self, model_name, number_plate, motor_power, year):
        self.name = model_name
        self.number_plate = number_plate
        self.motor_power = motor_power
        self.year = year

class Claims:
    def __init__(self, text, amount):
        self.ID = str(uuid.uuid1())
        self.text = str(text)
        self.status = 'Pending'
        self.amount = 0


    def updateStatus(self, value):    # depenging on the value given
        if value != 0:
            if value == self.amount:
                self.status = 'FULLY COVERED'
            elif value < self.amount:
                self.status = 'PARTLY COVERED'
        else:
            self.status = 'REJECTED'

class Payment:
    def __init__(self, date, amount, id):
        self.date = date
        self.amount = amount
        self.id = id

