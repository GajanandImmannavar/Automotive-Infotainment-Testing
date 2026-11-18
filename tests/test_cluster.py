
# from src.instrument_cluster import InstrumentCluster


# def test_valid_speed():

#     cluster = InstrumentCluster()
#     cluster.start_system()

#     result = cluster.update_speed(80)

#     assert result == "Speed updated"
#     assert cluster.speed == 80


# def test_invalid_speed():

#     cluster = InstrumentCluster()
#     cluster.start_system()

#     result = cluster.update_speed(350)

#     assert result == "Invalid speed"
#     assert cluster.speed == 0


# def test_valid_fuel():

#     cluster = InstrumentCluster()
#     cluster.start_system()

#     result = cluster.update_fuel(50)

#     assert result == "Fuel updated"
#     assert cluster.fuel == 50


# def test_invalid_fuel():

#     cluster = InstrumentCluster()
#     cluster.start_system()

#     result = cluster.update_fuel(150)

#     assert result == "Invalid fuel level"
#     assert cluster.fuel == 100


# def test_low_fuel_warning():

#     cluster = InstrumentCluster()
#     cluster.start_system()

#     cluster.update_fuel(8)

#     result = cluster.check_low_fuel()

#     assert result == "Low fuel warning ON"


# def test_seatbelt_warning():

#     cluster = InstrumentCluster()
#     cluster.start_system()

#     result = cluster.check_seatbelt(False)

#     assert result == "Seatbelt warning ON"


# def test_door_warning():

#     cluster = InstrumentCluster()
#     cluster.start_system()

#     result = cluster.check_door(True)

#     assert result == "Door warning ON"




# def test_valid_speed(cluster):

#     result = cluster.update_speed(80)

#     assert result == "Speed updated"
#     assert cluster.speed == 80


# def test_invalid_speed(cluster):

#     result = cluster.update_speed(350)

#     assert result == "Invalid speed"
#     assert cluster.speed == 0


# def test_valid_fuel(cluster):

#     result = cluster.update_fuel(50)

#     assert result == "Fuel updated"
#     assert cluster.fuel == 50


# def test_invalid_fuel(cluster):

#     result = cluster.update_fuel(150)

#     assert result == "Invalid fuel level"
#     assert cluster.fuel == 100


# def test_low_fuel_warning(cluster):

#     cluster.update_fuel(8)

#     result = cluster.check_low_fuel()

#     assert result == "Low fuel warning ON"


# def test_seatbelt_warning(cluster):

#     result = cluster.check_seatbelt(False)

#     assert result == "Seatbelt warning ON"


# def test_door_warning(cluster):

#     result = cluster.check_door(True)

#     assert result == "Door warning ON"




import pytest


# Test 1: Verify valid speed
def test_valid_speed(cluster):
    result = cluster.update_speed(80)

    assert result == "Speed updated"
    assert cluster.speed == 80


# Test 2: Verify invalid speed
def test_invalid_speed(cluster):
    result = cluster.update_speed(350)

    assert result == "Invalid speed"
    assert cluster.speed == 0


# Test 3: Verify valid fuel
def test_valid_fuel(cluster):
    result = cluster.update_fuel(50)

    assert result == "Fuel updated"
    assert cluster.fuel == 50


# Test 4: Verify invalid fuel
def test_invalid_fuel(cluster):
    result = cluster.update_fuel(150)

    assert result == "Invalid fuel level"
    assert cluster.fuel == 100


# Test 5: Verify low fuel warning
def test_low_fuel_warning(cluster):
    cluster.update_fuel(8)

    result = cluster.check_low_fuel()

    assert result == "Low fuel warning ON"


# Test 6: Verify seatbelt warning
def test_seatbelt_warning(cluster):
    result = cluster.check_seatbelt(False)

    assert result == "Seatbelt warning ON"


# Test 7: Verify door warning
def test_door_warning(cluster):
    result = cluster.check_door(True)

    assert result == "Door warning ON"


# Test 8: Parameterized speed testing
@pytest.mark.parametrize(
    "speed, expected",
    [
        (0, "Speed updated"),
        (80, "Speed updated"),
        (300, "Speed updated"),
        (-10, "Invalid speed"),
        (350, "Invalid speed")
    ]
)
def test_speed_with_multiple_inputs(cluster, speed, expected):
    result = cluster.update_speed(speed)

    assert result == expected


