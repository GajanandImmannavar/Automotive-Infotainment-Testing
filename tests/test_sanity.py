
# Sanity Testing
# Focused testing of Bluetooth functionality


# Test 1: Verify Bluetooth connection
def test_sanity_bluetooth_connection(infotainment):

    result = infotainment.connect_bluetooth()

    assert result == "Bluetooth connected"
    assert infotainment.bluetooth_status == "CONNECTED"


# Test 2: Verify Bluetooth disconnection
def test_sanity_bluetooth_disconnection(infotainment):

    infotainment.connect_bluetooth()

    result = infotainment.disconnect_bluetooth()

    assert result == "Bluetooth disconnected"
    assert infotainment.bluetooth_status == "DISCONNECTED"


# Test 3: Verify Bluetooth does not connect when system is OFF
def test_sanity_bluetooth_when_system_off(infotainment):

    infotainment.stop_system()

    result = infotainment.connect_bluetooth()

    assert result == "System is OFF"
    assert infotainment.bluetooth_status == "DISCONNECTED"
