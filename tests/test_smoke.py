
# Smoke Testing
# Verify major functionalities of the automotive system


# Test 1: Verify infotainment system starts
def test_smoke_infotainment_start(infotainment):

    assert infotainment.get_status() == "ON"


# Test 2: Verify instrument cluster starts
def test_smoke_cluster_start(cluster):

    assert cluster.get_status() == "ON"


# Test 3: Verify basic infotainment functionality
def test_smoke_music_playback(infotainment):

    result = infotainment.play_music()

    assert result == "Music started"


# Test 4: Verify basic instrument cluster functionality
def test_smoke_speed_update(cluster):

    result = cluster.update_speed(80)

    assert result == "Speed updated"
    assert cluster.speed == 80
