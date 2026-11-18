
from src.infotainment import Infotainment
from src.instrument_cluster import InstrumentCluster


def test_both_modules_start_together():

    infotainment = Infotainment()
    cluster = InstrumentCluster()

    infotainment.start_system()
    cluster.start_system()

    assert infotainment.get_status() == "ON"
    assert cluster.get_status() == "ON"

    assert infotainment.play_music() == "Music started"
    assert cluster.update_speed(80) == "Speed updated"


def test_both_modules_stop_together():

    infotainment = Infotainment()
    cluster = InstrumentCluster()

    infotainment.start_system()
    cluster.start_system()

    infotainment.stop_system()
    cluster.stop_system()

    assert infotainment.get_status() == "OFF"
    assert cluster.get_status() == "OFF"

    assert infotainment.play_music() == "System is OFF"
    assert cluster.update_speed(80) == "System is OFF"
