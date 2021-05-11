class Offer():
    offer_instances = []

    def __init__(self,offer):
        try:
            self.code = offer['code']
            self.discount = float(offer['discount'])
            self.ul_distance = float(offer['ul_distance'])
            self.ll_distance = float(offer['ll_distance'])
            self.ul_weight = float(offer['ul_weight'])
            self.ll_weight = float(offer['ll_weight'])
            self.offer_instances.append(self)
        except ValueError as e:
            raise ValueError(e)

    @classmethod
    def get_object(cls,offer_code):
        for instance in cls.offer_instances:
            if instance.code == offer_code:
                return instance
        return None
    