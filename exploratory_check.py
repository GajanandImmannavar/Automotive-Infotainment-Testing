from src.infotainment import Infotainment

system = Infotainment()

# Step 1: Start system
system.start_system()

# Step 2: Play music
system.play_music()

print("Before shutdown:")
print("System Status:", system.get_status())
print("Music Status:", system.music_status)

# Step 3: Stop system
system.stop_system()

print("\nAfter shutdown:")
print("System Status:", system.get_status())
print("Music Status:", system.music_status)

# Step 4: Verify expected behavior
if system.music_status == "STOPPED":
    print("\nResult: PASS")
else:
    print("\nResult: FAIL - BUG002 reproduced")