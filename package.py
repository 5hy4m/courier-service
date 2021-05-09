from offer import Offer

class Package(Offer):
    def __init__(self,details):
        self.name = details[0]
        self.distance = details[1]
        self.offer = details[2]
        self.weight = details[3]

    @classmethod
    def calculate_total_delivery_cost(self):
        import pdb;pdb.set_trace()