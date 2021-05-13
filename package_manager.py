from offer import Offer
from package import Package
from vehicle import Vehicle

import math
class PackageManager(Package,Offer,Vehicle):
    def __init__(self,base_delivery_cost,no_of_vehicles,max_speed,max_weight):
        try:
            self.available_vehicles = int(no_of_vehicles)
            self.max_speed = float(max_speed)
            self.max_weight = float(max_weight)
            self.base_delivery_cost = float(base_delivery_cost)
            self.current_time = 0.0
            self.package_weights = self.get_weights()
        except ValueError as e:
            raise ValueError(e)

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
                    total_weight_array = [self.summationOfTheArray([combination.weight for combination in combination_arr]) for combination_arr in combinations]
                    # selected_packages = combinations[total_weight_array.index(max(total_weight_array))]
                    max_value = max(total_weight_array)
                    index_value = total_weight_array.index(max_value)
                    self.calculateTimeTaken(combinations[index_value])
                    combinations = []
                    break
        pass
    
    @staticmethod
    def truncate(n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier

    def calculateDeliveryTime(self,package):
        if self.max_speed == 0:
            raise ZeroDivisionError("Max_speed Can't be zero")
        
        return self.truncate(package.distance/self.max_speed,2)

    def calculateTimeTaken(self,combination):
        vehicle = self.getVehicle(self.current_time)
        if vehicle.available:
            # if self.current_time != 0.0:
            #     import pdb;pdb.set_trace()
            time_arr = [ self.calculateDeliveryTime(package) for package in combination ]
            max_time = max(time_arr)
            vehicle.return_time +=  max_time * 2
            vehicle.available = False

            self.package_weights = list(filter(lambda x: x not in combination,self.package_weights))
            
            for index,package in enumerate(combination):
                output_string = package.calculateDeliveryCost( self.base_delivery_cost )
                print(output_string,self.current_time + self.calculateDeliveryTime(package))
        else:
            self.current_time += vehicle.return_time - self.current_time
            print('self.current_time',self.current_time)
            vehicle.available = True
            pass