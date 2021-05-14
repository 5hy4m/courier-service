class Vehicle():
    vehicle_instances = []
    def __init__(self,weight,speed):
        self.available = True
        self.return_time = 0.00
        try:
            self.weight = float(weight)
            self.speed = float(speed)
        except ValueError as e:
            raise e
        self.vehicle_instances.append(self)

    @classmethod
    def getVehicle(cls):
        # Gives the Avaialable Vehicle or Vehicle which will return soon

        # print('getVehicle',[(i.return_time,i.available) for i in cls.vehicle_instances])
        return_vehicle = cls.vehicle_instances[0]
        for vehicle in cls.vehicle_instances[1:]:
            if return_vehicle.return_time > vehicle.return_time:
                return_vehicle = vehicle
        return return_vehicle