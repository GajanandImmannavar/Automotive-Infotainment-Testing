
from src.ecu import ECU
from src.infotainment import Infotainment
from src.instrument_cluster import InstrumentCluster


def test_ecu_start_and_stop():

    ecu = ECU("Engine ECU")

    assert ecu.get_ecu_name() == "Engine ECU"
    assert ecu.get_status() == "OFF"

    ecu.start_system()
    assert ecu.get_status() == "ON"

    ecu.stop_system()
    assert ecu.get_status() == "OFF"


def test_infotainment_ecu_name():

    system = Infotainment()

    assert system.get_ecu_name() == "Infotainment ECU"


def test_instrument_cluster_ecu_name():

    system = InstrumentCluster()

    assert system.get_ecu_name() == "Instrument Cluster ECU"
