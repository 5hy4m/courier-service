from package import Package
from vehicle import Vehicle

import math
class PackageManager(Package,Vehicle):
    def __init__(self,base_delivery_cost,no_of_vehicles,max_speed,max_weight):
        try:
            self.available_vehicles = int(no_of_vehicles)
            self.max_speed = float(max_speed)
            self.max_weight = float(max_weight)
            self.base_delivery_cost = float(base_delivery_cost)
            self.current_time = 0.0
        except ValueError as e:
            raise ValueError(e)
        
        self.sorted_packages = self.getPackagesSorted() #Sort Packages with respect to it's weight

    def recursive_package(self,sorted_packages,combination,current_index):
        # Recursive Funtion finds possible combinations
        if current_index >= len(sorted_packages):
            # print([package.weight for package in combination])
            # print('Length Exceeded')
            return combination

        if (len(combination) != 0 and self.summationOfTheArray([package.weight for package in combination]) + sorted_packages[current_index].weight) <= self.max_weight:
            combination.append(sorted_packages[current_index])

            return self.recursive_package(sorted_packages[current_index:],combination,current_index+1)
        else:
            # print([package.weight for package in combination])
            if len(combination) == self.sorted_packages:
                pass
            return combination
    
    def find_best(self,index):
        return self.recursive_package(self.sorted_packages[index:],[],0)

    def calculatePackages(self):
        # This function finds optimal package combination and calculates delivery time for each package
        combinations = []
        while len(self.sorted_packages) != 0:
            for index,weight in enumerate(self.sorted_packages):
                print((len(combinations) , len(self.sorted_packages)))
                print([[(i.weight,i.name) for i in c] for c in combinations])
                if len(combinations) != len(self.sorted_packages) and (len(combinations) <= 1 or (len(combinations) >= 2 and len(combinations[-2]) <= len(combinations[-1]))):
                    combinations.append(self.find_best(index))
                else:
                    total_weight_array = [self.summationOfTheArray([package.weight for package in combination]) for combination in combinations]
                    max_value = max(total_weight_array)
                    index_value = total_weight_array.index(max_value)
                    self.calculateTimeTaken(combinations[index_value])
                    combinations = []
                    break
    
    @staticmethod
    def truncate(n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier

    def calculateDeliveryTime(self,package):
        #calculate delivery time of the given package
        if self.max_speed == 0:
            raise ZeroDivisionError("Max_speed Can't be zero")
        
        return self.truncate(package.distance/self.max_speed,2)

    def calculateTimeTaken(self,combination):
        #Gets the correct pkg combination to be dispatched and Prints the Output 
        vehicle = self.getVehicle()
        if vehicle.available:
            max_time = 0
            for index,package in enumerate(combination):
                package_delivery_time = self.calculateDeliveryTime(package)
                if max_time < package_delivery_time:
                    max_time = package_delivery_time

                output_string = package.calculateDeliveryCost( self.base_delivery_cost )
                # print('#'*50)
                # for i in combination:
                #     print(i.name,'weight :',i.weight,'deliverytime :',package_delivery_time,'distance :',i.distance)
                # print('#'*50)
                print(output_string,round(self.current_time + package_delivery_time,2))

            vehicle.return_time +=  max_time * 2
            vehicle.available = False

            self.sorted_packages = list(filter(lambda x: x not in combination,self.sorted_packages))
        else:
            self.current_time += vehicle.return_time - self.current_time
            # print("CurrentTime :",self.current_time)
            vehicle.available = True
            pass