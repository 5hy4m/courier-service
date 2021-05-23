import operator
import functools

from offer import Offer

class Package(Offer):
    package_instances = []

    def __init__(self,details):
        try:
            self.name = details[0] #Package Name
            self.weight = int(details[1]) # Package weight
            self.distance = float(details[2]) # distance of the package
            self.offer = self.getOfferObject(details[3]) # Offer mapped with the package
            self.delivery_time = 0.0 # Time it takes to deliver the package
            self.discounted_price = 0.0 # Discounted Price of the package
            self.package_instances.append(self) # appending all instances
        except ValueError as e:
            raise ValueError(e)

    @staticmethod
    def summationOfTheArray(array):
        return functools.reduce(operator.add,array)

    @staticmethod
    def truncate(n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier
    
    @classmethod
    def getPackages(cls):
        return cls.package_instances

    def checkOffer(self):
        if self.offer:
            if not self.offer.ll_distance <= self.distance <= self.offer.ul_distance:
                # print('Offer code not valid due to distance limitation')
                return False
            if not self.offer.ll_weight <= self.weight <= self.offer.ul_weight:
                # print('Offer code not valid due to weight limitation')
                return False
            return True
        else:
            # print('Offer code does not exist')
            return False

    def calculateDeliveryCost(self,base_delivery_cost):
        delivery_cost = base_delivery_cost + (self.weight * 10) + (self.distance * 5)
        
        # Checking if the offer is applicable to this package
        if self.checkOffer():
            discount = round(delivery_cost * (self.offer.discount/100),2)
            delivery_cost -= discount 
        else:
            discount = 0.0

        #modifying delivery and discount cost to match with the sample output
        delivery_cost = int(delivery_cost) if delivery_cost.is_integer() else delivery_cost
        discount = int(discount) if discount.is_integer() else discount

        #Asigning the cost and discount to the package object
        self.delivery_cost = delivery_cost
        self.discounted_price = discount

        return discount,delivery_cost
    
    def calculateDeliveryTime(self,current_time,max_speed):
        if max_speed == 0:
            raise ZeroDivisionError("Max_speed Can't be zero")
        
        # Calculating delivery time of the package and truncate the value to 2 decimals
        delivery_time = self.truncate(self.distance/max_speed,2)

        # Adding the waited time to the delivery time of the package and round the value to 2 decimals
        self.delivery_time = round(current_time + delivery_time,2)

        return self.delivery_time

