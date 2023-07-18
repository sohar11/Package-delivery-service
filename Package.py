#Creates package class
class Package:

    def __init__(self, ID, address, city, state, zip, weight, Deadline, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.weight = weight
        self.status = status
        self.Deadline = Deadline
        self.departure_time = None
        self.arrival_time = None




    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip, self.weight, self.Deadline, self.status, self.arrival_time)


# updates delivery status of package to DELIVERED, EN-ROUTE, OR AT-HUB
    def delivery_status(self,time_update):
        if self.arrival_time < time_update:
            self.status = "DELIVERED"

        elif self.departure_time > time_update:
            self.status = "EN-ROUTE"
        else:
            self.status = "AT-HUB"