class Offer():
    offer_instances = []

    def __init__(self,offer):
        try:
            self.code = offer['code']
            self.discount = float(offer['discount'])
            self.ll_distance = float(offer['ll_distance']) # Lower limit distance
            self.ul_distance = float(offer['ul_distance']) # Upper Limit distance
            self.ll_weight = float(offer['ll_weight']) # Lower limit weight
            self.ul_weight = float(offer['ul_weight']) # Upper Limit weight
            self.offer_instances.append(self)
        except ValueError as e:
            raise ValueError(e)

    @classmethod
    def getOfferObject(cls,offer_code):
        for instance in cls.offer_instances:
            if instance.code == offer_code:
                return instance
        return None
    