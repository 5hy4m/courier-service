class Offer():
    instances = []

    def __init__(self,offer):
        self.code = offer['code']
        self.discount = float(offer['discount'])
        self.ul_distance = float(offer['ul_distance'])
        self.ll_distance = float(offer['ll_distance'])
        self.ul_weight = float(offer['ul_weight'])
        self.ll_weight = float(offer['ll_weight'])
        self.instances.append(self)

    @classmethod
    def get_object(cls,offer_code):
        for instance in cls.instances:
            if instance.code == offer_code:
                return instance
        return None
    