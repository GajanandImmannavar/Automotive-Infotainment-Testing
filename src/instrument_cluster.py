
from .vehicle_system import VehicleSystem


class InstrumentCluster(VehicleSystem):

    def __init__(self):
        super().__init__()
        self.ecu_name = "Instrument Cluster ECU"
        self.speed = 0
        self.fuel = 100
        self.engine_temperature = 90
        self.seatbelt_fastened = True
        self.door_open = False

    def update_speed(self, speed):
        if self.system_status != "ON":
            return "System is OFF"

        if 0 <= speed <= 300:
            self.speed = speed
            return "Speed updated"

        return "Invalid speed"

    def update_fuel(self, fuel):
        if self.system_status != "ON":
            return "System is OFF"

        if 0 <= fuel <= 100:
            self.fuel = fuel
            return "Fuel updated"

        return "Invalid fuel level"

    def update_temperature(self, temperature):
        if self.system_status != "ON":
            return "System is OFF"

        if 0 <= temperature <= 200:
            self.engine_temperature = temperature
            return "Temperature updated"

        return "Invalid temperature"

    def check_seatbelt(self, fastened):
        if self.system_status != "ON":
            return "System is OFF"

        self.seatbelt_fastened = fastened

        if not fastened:
            return "Seatbelt warning ON"

        return "Seatbelt warning OFF"

    def check_door(self, opened):
        if self.system_status != "ON":
            return "System is OFF"

        self.door_open = opened

        if opened:
            return "Door warning ON"

        return "Door warning OFF"

    def check_low_fuel(self):
        if self.fuel < 10:
            return "Low fuel warning ON"

        return "Low fuel warning OFF"
