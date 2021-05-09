class Offer():
    def __init__(self,offer):
        self.code = offer['code']
        self.discount = offer['discount']
        self.ul_distance = offer['ul_distance']
        self.ll_distance = offer['ll_distance']
        self.ul_weight = offer['ul_weight']
        self.ll_weight = offer['ll_weight']

    