
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

workbook = Workbook()
sheet = workbook.active
sheet.title = "RTM"

headers = [
    "Requirement ID",
    "Requirement Description",
    "Test Case ID",
    "Test Case Description",
    "Test Status"
]

sheet.append(headers)

requirements = [
    ["REQ001", "Infotainment system should start successfully",
     "TC001", "Verify infotainment system starts", "Pass"],

    ["REQ002", "Volume should accept values between 0 and 100",
     "TC002", "Verify valid volume values", "Pass"],

    ["REQ003", "Volume should reject values outside 0 to 100",
     "TC003", "Verify invalid volume values", "Pass"],

    ["REQ004", "Music should play when system is ON",
     "TC004", "Verify music playback", "Pass"],

    ["REQ005", "Music should stop when system shuts down",
     "TC005", "Verify music stops after shutdown", "Pass"],

    ["REQ006", "Bluetooth should connect when system is ON",
     "TC006", "Verify Bluetooth connection", "Pass"],

    ["REQ007", "Instrument cluster should update vehicle speed",
     "TC007", "Verify speed update", "Pass"],

    ["REQ008", "System should display a low fuel warning",
     "TC008", "Verify low fuel warning", "Pass"]
]

for requirement in requirements:
    sheet.append(requirement)

# Format header
for cell in sheet[1]:
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill(
        start_color="1F4E78",
        end_color="1F4E78",
        fill_type="solid"
    )
    cell.alignment = Alignment(horizontal="center")

# Adjust column widths
for column in sheet.columns:
    max_length = 0
    column_letter = column[0].column_letter

    for cell in column:
        if cell.value:
            max_length = max(max_length, len(str(cell.value)))

    sheet.column_dimensions[column_letter].width = max_length + 5

workbook.save("test_cases/RTM.xlsx")

print("RTM Excel file created successfully!")
