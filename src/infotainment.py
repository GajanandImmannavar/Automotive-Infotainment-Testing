
from .vehicle_system import VehicleSystem


class Infotainment(VehicleSystem):

    def __init__(self):
        super().__init__()
        self.ecu_name = "Infotainment ECU"
        self.volume = 0
        self.music_status = "STOPPED"
        self.bluetooth_status = "DISCONNECTED"

    def stop_system(self):
        self.music_status = "STOPPED"
        super().stop_system()

    def play_music(self):
        if self.system_status == "ON":
            self.music_status = "PLAYING"
            return "Music started"
        return "System is OFF"

    def pause_music(self):
        if self.system_status == "ON":
            self.music_status = "PAUSED"
            return "Music paused"
        return "System is OFF"

    def set_volume(self, volume):
        if self.system_status != "ON":
            return "System is OFF"

        if 0 <= volume <= 100:
            self.volume = volume
            return "Volume updated"


        return "Invalid volume"

    def connect_bluetooth(self):
        if self.system_status == "ON":
            self.bluetooth_status = "CONNECTED"
            return "Bluetooth connected"
        return "System is OFF"

    def disconnect_bluetooth(self):
        if self.system_status == "ON":
            self.bluetooth_status = "DISCONNECTED"
            return "Bluetooth disconnected"
        return "System is OFF"
