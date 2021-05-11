from offer import Offer
from package import Package
from vehicle import Vehicle

import math
class PackageManager(Package,Offer,Vehicle):
    def __init__(self,base_delivery_cost,no_of_vehicles,max_speed,max_weight):
        self.available_vehicles = int(no_of_vehicles)
        self.max_speed = float(max_speed)
        self.max_weight = float(max_weight)
        self.base_delivery_cost = base_delivery_cost
        self.current_time = 0.00
        self.package_weights = self.get_weights()

    def recursive_package(self,package_weights,max_weight,combination,current_index):
        if current_index >= len(package_weights):
            # print([package.weight for package in combination])
            # print('Length Exceeded')
            return combination

        if (len(combination) != 0 and self.summationOfTheArray([package.weight for package in combination]) + package_weights[current_index].weight) <= max_weight:
            combination.append(package_weights[current_index])

            return self.recursive_package(package_weights,max_weight,combination,current_index+1)
        else:
            # print([package.weight for package in combination])
            if len(combination) == self.package_weights:
                pass
            return combination

    def find_best(self,package_weights,max_weight):
        return self.recursive_package(package_weights,max_weight,[],0)
    
    def calculatePackages(self,base_delivery_cost,max_weight):
        current_time = 0 #hrs
        total_weight = 0
        combinations = []
        while len(self.package_weights) != 0:
            for index,weight in enumerate(self.package_weights):
                # for elements in combinations:
                #     for ele in elements:
                #         print(ele.weight,ele.name)
                #     print("="*50)
                if len(combinations) != len(self.package_weights) and (len(combinations) <= 1 or (len(combinations) >= 2 and len(combinations[-2]) <= len(combinations[-1]))):
                    combinations.append(self.find_best(self.package_weights[index:],max_weight))
                else:
                    # combinations = combinations[:-1]
                    total_weight_array = [self.summationOfTheArray([combination.weight for combination in combination_arr]) for combination_arr in combinations]
                    # selected_packages = combinations[total_weight_array.index(max(total_weight_array))]
                    max_value = max(total_weight_array)
                    index_value = total_weight_array.index(max_value)
                    self.calculateTimeTaken(combinations[index_value])
                    combinations = []
                    break
                    # self.useVehicle(selected_packages,no_of_vehicles,max_speed)
        pass
    
    def truncate(self,n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier

    def calculateTime(self,package):
        print('calculateTime')
        return self.truncate(package.distance/self.max_speed,2)

    def calculateTimeTaken(self,combination):
        vehicle = self.getVehicle()
        if vehicle.available:
            time_arr = [ self.calculateTime(package) for package in combination ]
            # print(time_arr)
            max_time = max([ self.calculateTime(package) for package in combination ])
            vehicle.return_time =  max_time * 2
            vehicle.available = False

            self.package_weights = list(filter(lambda x: x not in combination,self.package_weights))
            
            for index,package in enumerate(combination):
                output_string = package.calculateDeliveryCost( self.base_delivery_cost )
                print(output_string,self.current_time + self.calculateTime(package))
        else:
            self.current_time += vehicle.return_time
            vehicle.available = True
            pass