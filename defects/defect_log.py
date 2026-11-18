
import pandas as pd

defects = [
    [
        "BUG001",
        "Infotainment",
        "Volume accepts values above 100",
        "Set volume to 150",
        "System should reject invalid volume",
        "System accepts volume 150",
        "Major",
        "Open"
    ]
]

columns = [
    "Defect ID",
    "Module",
    "Defect Description",
    "Steps to Reproduce",
    "Expected Result",
    "Actual Result",
    "Severity",
    "Status"
]

df = pd.DataFrame(defects, columns=columns)

df.to_excel("defects/defect_log.xlsx", index=False)

print("Defect report created successfully!")
