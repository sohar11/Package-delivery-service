#creates Truck Class
class Truck:

    def __init__(self, maxload, package, speed,mileage, address, departure_time):
        self.maxload = maxload
        self.package = package
        self.speed = speed
        self.mileage = mileage
        self.address = address
        self.departure_time = departure_time
        self.time = departure_time


    def __str__(self):
        return "%s, %s, %s, %s, %s, %s" % (self.maxload, self.package, self.speed, self.mileage, self.address, self.departure_time)

# checks whether a truck still has room for more packages. Returns false if truck still has room, Returns true if truck is full.
    def at_capacity(self):
        if int(self.maxload) > len(self.package):
            return False
        else:
            return True