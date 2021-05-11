class Vehicle():
    vehicle_instances = []
    def __init__(self,weight,speed):
        self.weight = float(weight)
        self.speed = float(speed)
        self.available = True
        self.return_time = 0.00
        self.vehicle_instances.append(self)
    
    # def findNextReadyVehicle():
    #     return_vehicle = vehicle_instances[0] 
    #     for vehicle in vehicle_instances:
    #         if return_vehicle.return_time > vehicle.return_time:
    #             return_vehicle = vehicle
    #         return return_vehicle
        

    def getVehicle(self):
        return_vehicle = self.vehicle_instances[0] 
        for vehicle in self.vehicle_instances[1:]:
            if return_vehicle.return_time > vehicle.return_time:
                return_vehicle = vehicle
            return return_vehicle

    # @classmethod
    # def get_object(cls,offer_code):
    #     for instance in cls.instances:
    #         if instance.code == offer_code:
    #             return instance
    #     return None