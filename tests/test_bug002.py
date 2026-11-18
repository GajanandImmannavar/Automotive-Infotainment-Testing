
# BUG002: Music status should stop when system shuts down

def test_music_stops_when_system_shuts_down(infotainment):

    # Start music
    infotainment.play_music()

    # Stop infotainment system
    infotainment.stop_system()

    # Verify music status
    assert infotainment.music_status == "STOPPED"
