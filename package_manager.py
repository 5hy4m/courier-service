from package import Package
from vehicle import Vehicle

import math
class PackageManager(Package,Vehicle):
    def __init__(self,no_of_packages,base_delivery_cost,no_of_vehicles,max_speed,max_weight):
        try:
            self.available_vehicles = int(no_of_vehicles)
            self.max_speed = float(max_speed)
            self.max_weight = int(max_weight)
            self.base_delivery_cost = float(base_delivery_cost)
            self.no_of_packages = int(no_of_packages)
            self.current_time = 0.0
        except ValueError as e:
            raise ValueError(e)
        
        self.sorted_packages = self.getPackagesSorted() #Sort Packages with respect to it's weight

    def findTheCombination(self,array2D):
        row = self.no_of_packages
        col = self.max_weight
        combination = []
        while row > 0 and col > 0:
            current_package_weight = self.sorted_packages[row-1].weight
            # current_value = array2D[row][col]
            previous_element_value = array2D[row-1][col - int(current_package_weight)] 
            is_col_value_negative = (col - int(current_package_weight)) < 0
            # print((current_package_weight,previous_element_value,current_value))
            
            if array2D[row][col] == array2D[row-1][col]:
                if is_col_value_negative:
                    row -= 1
                    continue

                if array2D[row][col] == previous_element_value + current_package_weight:
                    # included
                    row -= 1
                    combination.append(self.sorted_packages[row])
                    # combination.append(self.sorted_packages[col - current_package_weight])
                    col = col - int(current_package_weight)
                    continue
                else:
                    row -= 1
                    continue

            else:
                # included
                row -= 1
                combination.append(self.sorted_packages[row])
                # combination.append(self.sorted_packages[col - current_package_weight])
                col = col - int(current_package_weight)
                continue

        # for c in combination:
        #     print (c.name)
        return combination

    def build2dArray(self):
        max_weight = self.max_weight

        # Creating 2d Array
        array2D = [ [ 0 for i in range(max_weight+1) ] for j in range(self.no_of_packages+1) ]
        
        # weights will be added to this list if there are more than one package included 
        combination = []

        # Iterating through 2d Array
        for row in range(self.no_of_packages+1): #Iterate through each package from 0 to nth package + 1
            for col in range(max_weight+1): #Iterate through each weight 0 to max_weight + 1

                #Checking Base Case
                if row == 0 or col == 0:
                    # assigning current cell value equal to 0
                    array2D[row][col] = 0
                    continue

                # getting current package(row) weight value from the package objects
                current_package_weight = self.sorted_packages[row-1].weight

                # getting previous package(row) weight value from the 2dArray by doing column of weight - current_package_weight
                previous_package_weight = array2D[row-1][col - current_package_weight]

                # print(current_package_weight,previous_package_weight)
                # import pdb;pdb.set_trace()
                
                if row == 3 and col == 6:
                    pass
                    # import pdb;pdb.set_trace()
                
                # Checking current package(row) weight < current column of weight
                if current_package_weight <= col:

                    # For maximizing the no of packages. Checking if there are any packages included before to get this weight.
                    if current_package_weight + previous_package_weight in combination:
                        # Assign that value to the current cell
                        array2D[row][col] = current_package_weight + previous_package_weight
                        continue
                        
                    # If previous package weight == 0 then it cannot be included!! so we append only items that are previously included
                    if previous_package_weight != 0:
                        combination.append(current_package_weight + previous_package_weight)

                    # Assigning Max value to the current cell
                    array2D[row][col] = max(current_package_weight + previous_package_weight , array2D[row-1][col])
                else:
                    # Assign the weight from previous package with the same column of weight
                    array2D[row][col] = array2D[row-1][col]
        return array2D


    def calculatePackages(self):
        # This function finds optimal package combination and calculates delivery time for each package
    
        # Iterate until all the packages are delivered
        while self.no_of_packages != 0:
            array2D = self.build2dArray()
            print('*'*100)
            for row in array2D:
                print(row)
            print('*'*100)
            # Get the Package combination that needs to be delivered
            package_combination = self.findTheCombination(array2D)
            for package in package_combination:  
                print(package.weight)

            #Deliver and calculate time taken for each package in the package combination
            self.calculateTimeTaken(package_combination)

    @staticmethod
    def truncate(n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier

    def calculateDeliveryTime(self,package):
        if self.max_speed == 0:
            raise ZeroDivisionError("Max_speed Can't be zero")
        
        # Calculating delivery time of the package and truncate the value to 2 decimals
        delivery_time = self.truncate(package.distance/self.max_speed,2)

        # Adding the waited time to the delivery time of the package and round the value to 2 decimals
        package.delivery_time = round(self.current_time + delivery_time,2)

        return package.delivery_time

    def calculateTimeTaken(self,combination):
        #Gets the correct pkg combination to be dispatched and Prints the Output 
        vehicle = self.getVehicle()

        #checking If vehicle is available 
        if vehicle.available:
            max_time = 0
            for package in combination:
                # Calculating Delivery time of each package
                package_delivery_time = self.calculateDeliveryTime(package)

                # Calculating Delivery Cost of each package
                package.calculateDeliveryCost( self.base_delivery_cost )

                if max_time < package_delivery_time:
                    max_time = package_delivery_time

            vehicle.return_time +=  max_time * 2
            vehicle.available = False

            #Removing the delivered packages
            self.sorted_packages = list(filter(lambda x: x not in combination,self.sorted_packages))
            self.no_of_packages = len(self.sorted_packages)
        else:
            # Waiting for the vehicle nearest vehicle to return
            self.current_time += vehicle.return_time - self.current_time
            vehicle.available = True