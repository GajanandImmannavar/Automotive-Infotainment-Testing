
# class VehicleSystem:

#     def __init__(self):
#         self.system_status = "OFF"

#     def start_system(self):
#         self.system_status = "ON"

#     def stop_system(self):
#         self.system_status = "OFF"

#     def get_status(self):
#         return self.system_status



from .ecu import ECU


class VehicleSystem(ECU):

    def __init__(self):
        super().__init__("Vehicle System")
