class ECU:

    def __init__(self, ecu_name):
        self.ecu_name = ecu_name
        self.system_status = "OFF"

    def start_system(self):
        self.system_status = "ON"

    def stop_system(self):
        self.system_status = "OFF"

    def get_status(self):
        return self.system_status

    def get_ecu_name(self):
        return self.ecu_name