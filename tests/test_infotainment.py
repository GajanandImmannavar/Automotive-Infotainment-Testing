
# from src.infotainment import Infotainment


# def test_music_playback():

#     infotainment = Infotainment()
#     infotainment.start_system()

#     result = infotainment.play_music()

#     assert result == "Music started"


# def test_valid_volume():

#     infotainment = Infotainment()
#     infotainment.start_system()

#     result = infotainment.set_volume(50)

#     assert result == "Volume updated"
#     assert infotainment.volume == 50


# def test_invalid_volume():

#     infotainment = Infotainment()
#     infotainment.start_system()

#     result = infotainment.set_volume(150)

#     assert result == "Invalid volume"
#     assert infotainment.volume == 0


# def test_bluetooth_connection():

#     infotainment = Infotainment()
#     infotainment.start_system()

#     result = infotainment.connect_bluetooth()

#     assert result == "Bluetooth connected"



# def test_music_playback(infotainment):

#     assert infotainment.play_music() == "Music started"


# def test_valid_volume(infotainment):

#     result = infotainment.set_volume(50)

#     assert result == "Volume updated"
#     assert infotainment.volume == 50


# def test_invalid_volume(infotainment):

#     result = infotainment.set_volume(150)

#     assert result == "Invalid volume"
#     assert infotainment.volume == 0


# def test_bluetooth_connection(infotainment):

#     assert infotainment.connect_bluetooth() == "Bluetooth connected"




import pytest


# Test 1: Verify music playback
def test_music_playback(infotainment):

    result = infotainment.play_music()

    assert result == "Music started"


# Test 2: Verify valid volume
def test_valid_volume(infotainment):

    result = infotainment.set_volume(50)

    assert result == "Volume updated"
    assert infotainment.volume == 50


# Test 3: Verify invalid volume
def test_invalid_volume(infotainment):

    result = infotainment.set_volume(150)

    assert result == "Invalid volume"
    assert infotainment.volume == 0


# Test 4: Verify Bluetooth connection
def test_bluetooth_connection(infotainment):

    result = infotainment.connect_bluetooth()

    assert result == "Bluetooth connected"


# Test 5: Parameterized volume testing
@pytest.mark.parametrize(
    "volume, expected",
    [
        (0, "Volume updated"),
        (50, "Volume updated"),
        (100, "Volume updated"),
        (-10, "Invalid volume"),
        (150, "Invalid volume")
    ]
)
def test_volume_with_multiple_inputs(infotainment, volume, expected):

    result = infotainment.set_volume(volume)

    assert result == expected



# Boundary Value Analysis for volume
@pytest.mark.parametrize(
    "volume, expected",
    [
        (-1, "Invalid volume"),
        (0, "Volume updated"),
        (1, "Volume updated"),
        (99, "Volume updated"),
        (100, "Volume updated"),
        (101, "Invalid volume")
    ]
)
def test_volume_boundary_values(infotainment, volume, expected):

    result = infotainment.set_volume(volume)

    assert result == expected






# Equivalence Partitioning for volume
@pytest.mark.parametrize(
    "volume, expected",
    [
        (-5, "Invalid volume"),      # Invalid partition: below 0
        (50, "Volume updated"),      # Valid partition: 0 to 100
        (120, "Invalid volume")      # Invalid partition: above 100
    ]
)
def test_volume_equivalence_partitioning(infotainment, volume, expected):

    result = infotainment.set_volume(volume)

    assert result == expected





# Positive and Negative Testing

# Test 1: Play music when system is ON
def test_play_music_when_system_on(infotainment):

    result = infotainment.play_music()

    assert result == "Music started"


# Test 2: Play music when system is OFF
def test_play_music_when_system_off(infotainment):

    infotainment.stop_system()

    result = infotainment.play_music()

    assert result == "System is OFF"


# Test 3: Set volume when system is OFF
def test_set_volume_when_system_off(infotainment):

    infotainment.stop_system()

    result = infotainment.set_volume(50)

    assert result == "System is OFF"
    assert infotainment.volume == 0


# Test 4: Connect Bluetooth when system is OFF
def test_bluetooth_when_system_off(infotainment):

    infotainment.stop_system()

    result = infotainment.connect_bluetooth()

    assert result == "System is OFF"
    assert infotainment.bluetooth_status == "DISCONNECTED"
