from offer import Offer

class Package(Offer):
    def __init__(self,details):
        self.name = details[0]
        self.weight = float(details[1])
        self.distance = float(details[2])
        self.offer = Offer.get_object(details[3])

    # @classmethod
    # def calculate_total_delivery_cost(cls):
    #     import pdb;pdb.set_trace()

    def checkOffer(self):
        if self.offer:
            if not self.distance >= self.offer.ll_distance and not self.distance <= self.offer.ul_distance:
                print('Offer code not valid due to distance limitation')
                return False
            if not self.weight >= self.offer.ll_weight and not self.weight <= self.offer.ul_weight:
                print('Offer code not valid due to weight limitation')
                return False
            return True
        else:
            print('Offer code does not exist')
            return False

    def calculateDeliveryCost(self,base_delivery_cost):
        delivery_cost = base_delivery_cost + (self.weight * 10) + (self.distance * 5)
        if self.checkOffer():
            discount = delivery_cost * (self.offer.discount/100)
            delivery_cost -= discount 

        print(self.name,discount,delivery_cost)
        return delivery_cost
    
    def calculateTimeTaken(self):
        
        pass


