class Vehicle():
    vehicle_instances = []
    def __init__(self,weight,speed):
        self.vehicle_instances.append(self)
        try:
            self.weight = float(weight)
            self.speed = float(speed)
            self.available = True
            self.return_time = 0.00
        except ValueError as e:
            raise e        

    def getVehicle(self,current_time):
        print('getVehicle',[(i.return_time,i.available) for i in self.vehicle_instances])
        return_vehicle = self.vehicle_instances[0] 
        for vehicle in self.vehicle_instances[1:]:
            if return_vehicle.return_time > vehicle.return_time:
                return_vehicle = vehicle
            return return_vehicle