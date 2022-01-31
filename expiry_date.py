
class Licence:
    #Today's date is a class property, shared by all instances.
    
    def __init__(self, expiry_date, todays_date):
        self.expiry_date = expiry_date
        self.todays_date = todays_date
        
    #simplified version of dates, need to figure out how to handle dates.
    def checkdate(self):
        if self.expiry_date > self.todays_date:
            print ("Renew driving licence now!")
        else:
            print ("Driving licence valid.")
        
class credit_card:
    def __init__(self, expiry_date):
        self.expiry_date = expiry_date

test1 = Licence(30, 10)
test1.checkdate()
