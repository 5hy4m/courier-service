import operator
import functools

from offer import Offer

class Package(Offer):
    package_instances = []

    def __init__(self,details):
        try:
            self.name = details[0]
            self.weight = float(details[1])
            self.distance = float(details[2])
            self.offer = self.getOfferObject(details[3])
            self.package_instances.append(self)
        except ValueError as e:
            raise ValueError(e)

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

    @staticmethod
    def summationOfTheArray(array):
        return functools.reduce(operator.add,array)
    
    @classmethod
    def get_weights(cls):
        # We will 
        return sorted([instance for instance in cls.package_instances],key=lambda x: x.weight) 

    def calculateDeliveryCost(self,base_delivery_cost):
        delivery_cost = base_delivery_cost + (self.weight * 10) + (self.distance * 5)
        
        if self.checkOffer():
            discount = round(delivery_cost * (self.offer.discount/100),2)
            delivery_cost -= discount 
        else:
            discount = 0.0

        delivery_cost = int(delivery_cost) if delivery_cost.is_integer() else delivery_cost
        discount = int(discount) if discount.is_integer() else discount
        return f'{self.name} {discount} {delivery_cost}'

