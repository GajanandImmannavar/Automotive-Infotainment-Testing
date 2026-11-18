
import pandas as pd

test_cases = [
    ["TC001", "Infotainment", "Verify music playback", "System ON", "Play music", "Music started", "High"],
    ["TC002", "Infotainment", "Verify volume 50", "System ON", "Set volume 50", "Volume updated", "High"],
    ["TC003", "Infotainment", "Verify volume 0", "System ON", "Set volume 0", "Volume updated", "Medium"],
    ["TC004", "Infotainment", "Verify invalid volume", "System ON", "Set volume -10", "Invalid volume", "High"],
    ["TC005", "Infotainment", "Verify Bluetooth connection", "System ON", "Connect Bluetooth", "Bluetooth connected", "Medium"],
    ["TC006", "Instrument Cluster", "Verify speed update", "System ON", "Set speed 80", "Speed updated", "High"],
    ["TC007", "Instrument Cluster", "Verify invalid speed", "System ON", "Set speed 350", "Invalid speed", "High"],
    ["TC008", "Instrument Cluster", "Verify fuel update", "System ON", "Set fuel 8", "Fuel updated", "High"],
    ["TC009", "Instrument Cluster", "Verify low fuel warning", "System ON", "Set fuel 8", "Low fuel warning ON", "High"],
    ["TC010", "Instrument Cluster", "Verify seatbelt warning", "System ON", "Unfasten seatbelt", "Seatbelt warning ON", "High"],
]

columns = [
    "Test Case ID",
    "Module",
    "Test Scenario",
    "Precondition",
    "Test Steps",
    "Expected Result",
    "Priority"
]

df = pd.DataFrame(test_cases, columns=columns)

df["Actual Result"] = ""
df["Status"] = "Not Executed"

df.to_excel("test_cases/manual_test_cases.xlsx", index=False)

print("Manual test cases created successfully!")
