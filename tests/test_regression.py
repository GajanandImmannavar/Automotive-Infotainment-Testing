
# Regression Testing
# Verify existing functionalities after fixing BUG001
# BUG001: Volume accepted values greater than 100


# Test 1: Verify valid volume after bug fix
def test_regression_valid_volume(infotainment):

    result = infotainment.set_volume(50)

    assert result == "Volume updated"
    assert infotainment.volume == 50


# Test 2: Verify invalid volume is rejected
def test_regression_invalid_volume(infotainment):

    result = infotainment.set_volume(150)

    assert result == "Invalid volume"
    assert infotainment.volume == 0


# Test 3: Verify music playback is not affected
def test_regression_music_playback(infotainment):

    result = infotainment.play_music()

    assert result == "Music started"
    assert infotainment.music_status == "PLAYING"


# Test 4: Verify Bluetooth connection is not affected
def test_regression_bluetooth_connection(infotainment):

    result = infotainment.connect_bluetooth()

    assert result == "Bluetooth connected"
    assert infotainment.bluetooth_status == "CONNECTED"


# Test 5: Verify Bluetooth disconnection is not affected
def test_regression_bluetooth_disconnection(infotainment):

    infotainment.connect_bluetooth()

    result = infotainment.disconnect_bluetooth()

    assert result == "Bluetooth disconnected"
    assert infotainment.bluetooth_status == "DISCONNECTED"


# Test 6: Verify instrument cluster speed functionality
def test_regression_cluster_speed(cluster):

    result = cluster.update_speed(80)

    assert result == "Speed updated"
    assert cluster.speed == 80
