import operator
import functools

from offer import Offer

class Package(Offer):
    package_instances = []

    def __init__(self,details):
        self.name = details[0]
        self.weight = float(details[1])
        self.distance = float(details[2])
        self.offer = Offer.get_object(details[3])
        self.package_instances.append(self)

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

    def summationOfTheArray(self,array):
        return functools.reduce(operator.add,array)

    def get_weights(self):
        return sorted([instance for instance in self.package_instances],key=lambda x: x.weight) 

    def calculateDeliveryCost(self,base_delivery_cost):
        delivery_cost = base_delivery_cost + (self.weight * 10) + (self.distance * 5)
        if self.checkOffer():
            discount = delivery_cost * (self.offer.discount/100)
            delivery_cost -= discount 

        print(self.name,discount,delivery_cost)
        return delivery_cost
    
    def recursive_package(self,package_weights,max_weight,combinations,current_index):
        if current_index >= len(package_weights):
            print([i.weight for i in combinations])
            print('Length Exceeded')
            return combinations

        if len(combinations) == 0 or (self.summationOfTheArray([c.weight for c in combinations]) + package_weights[current_index].weight) <= max_weight:
            combinations.append(package_weights[current_index])
            return self.recursive_package(package_weights,max_weight,combinations,current_index+1)
        else:
            print([i.weight for i in combinations])
            return combinations

    def find_best(self,package_weights,max_weight):
        combinations = []
        return self.recursive_package(package_weights,max_weight,combinations,0)

    def calculateTimeTaken(self,base_delivery_cost,no_of_vehicles,max_speed,max_weight):
        package_weights = self.get_weights()
        current_time = 0 #hrs
        total_weight = 0
        while len(package_weights) != 0:
            no_of_packages = len(package_weights)
            combinations = []
            for index,weight in enumerate(package_weights):
                for elements in combinations:
                    for ele in elements:
                        print(ele.weight,ele.name)
                    print("="*50)
                
                if len(combinations) <= 1 or (len(combinations) >= 2 and len(combinations[-2]) <= len(combinations[-1])):
                    combinations.append(self.find_best(package_weights[index:],max_weight))
                else:
                    combinations = combinations[:-1]
                    import pdb;pdb.set_trace()
                    total_weight_array = [self.summationOfTheArray([combination.weight for combination in combination_arr]) for combination_arr in combinations]
                    # selected_packages = combinations[total_weight_array.index(max(total_weight_array))]
                    max_value = max(total_weight_array)
                    index_value = total_weight_array.index(max_value)
                    selected_packages = combinations[index_value]
                    self.useVehicle(selected_packages)
                    pass

        pass


