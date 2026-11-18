
import pandas as pd

from src.infotainment import Infotainment
from src.instrument_cluster import InstrumentCluster


file_path = "test_cases/manual_test_cases.xlsx"

df = pd.read_excel(file_path, dtype=str).fillna("")

results = {}

# TC001 - Music playback
i = Infotainment()
i.start_system()
results["TC001"] = i.play_music()

# TC002 - Volume 50
i = Infotainment()
i.start_system()
results["TC002"] = i.set_volume(50)

# TC003 - Volume 0
i = Infotainment()
i.start_system()
results["TC003"] = i.set_volume(0)

# TC004 - Invalid volume
i = Infotainment()
i.start_system()
results["TC004"] = i.set_volume(-10)

# TC005 - Bluetooth connection
i = Infotainment()
i.start_system()
results["TC005"] = i.connect_bluetooth()

# TC006 - Speed update
c = InstrumentCluster()
c.start_system()
results["TC006"] = c.update_speed(80)

# TC007 - Invalid speed
c = InstrumentCluster()
c.start_system()
results["TC007"] = c.update_speed(350)

# TC008 - Fuel update
c = InstrumentCluster()
c.start_system()
results["TC008"] = c.update_fuel(8)

# TC009 - Low fuel warning
c = InstrumentCluster()
c.start_system()
c.update_fuel(8)
results["TC009"] = c.check_low_fuel()

# TC010 - Seatbelt warning
c = InstrumentCluster()
c.start_system()
results["TC010"] = c.check_seatbelt(False)


# Update Excel results
for index, row in df.iterrows():

    test_id = row["Test Case ID"]

    actual = results[test_id]

    df.at[index, "Actual Result"] = actual

    if actual == row["Expected Result"]:
        df.at[index, "Status"] = "PASS"
    else:
        df.at[index, "Status"] = "FAIL"


df.to_excel(file_path, index=False)

print("\nTEST EXECUTION SUMMARY")
print("----------------------")

print("Total Tests:", len(df))
print("Passed:", (df["Status"] == "PASS").sum())
print("Failed:", (df["Status"] == "FAIL").sum())

print("\nTest execution completed!")
