# Automotive Infotainment & Instrument Cluster Testing

## Project Overview

This project is a Python-based simulation of an automotive infotainment system and instrument cluster.

The main objective is to practice software testing, manual test case execution, defect identification and test automation using Pytest.

## Technologies Used

- Python
- OOP Concepts
- Pytest
- Pandas
- Excel
- Git and GitHub

## Project Features

**1. Infotainment System**
- Start and stop system
- Play and pause music
- Volume control
- Bluetooth connection and disconnection

**2. Instrument Cluster**
- Vehicle speed monitoring
- Fuel level monitoring
- Engine temperature monitoring
- Seatbelt and door warnings
- Low fuel warning

**3. ECU and CAN Simulation**
- Basic ECU functionality
- Simulated CAN message sending and receiving
- CAN ID validation

## Testing Activities

- Created and executed manual test cases.
- Tested valid and invalid inputs.
- Performed Boundary Value Analysis.
- Identified and fixed software defects.
- Automated test cases using Pytest.
- Performed smoke, sanity, integration and regression testing.
- Generated HTML test reports.

## Defect Identification

Two issues were identified and fixed during testing:

1. The system accepted volume values above 100.
2. Music continued playing after the infotainment system was switched OFF.

Both issues were verified after fixing.

## Project Structure

```text
Automotive_QA_Validation/
│
├── src/
│   ├── __init__.py
│   ├── ecu.py
│   ├── vehicle_system.py
│   ├── infotainment.py
│   ├── instrument_cluster.py
│   └── can_bus.py
│
├── tests/
│   ├── test_ecu.py
│   ├── test_can_bus.py
│   ├── test_infotainment.py
│   ├── test_cluster.py
│   ├── test_integration.py
│   ├── test_smoke.py
│   ├── test_sanity.py
│   ├── test_regression.py
│   └── test_bug002.py
│
├── test_cases/
│   ├── create_test_cases.py
│   ├── execute_test_cases.py
│   ├── create_rtm.py
│   ├── manual_test_cases.xlsx
│   ├── RTM.xlsx
│   └── exploratory_test_session.md
│
├── defects/
│   ├── defect_log.py
│   └── defect_log.xlsx
│
├── reports/
│   └── pytest_report.html
│
├── utilities/
│   └── test_data.py
│
├── exploratory_check.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## How to Run the Project

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project:

```bash
cd Automotive_QA_Validation
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install pytest pytest-html pandas openpyxl
```

Run automated tests:

```bash
python -m pytest -v
```

Generate an HTML report:

```bash
python -m pytest -v --html=reports/pytest_report.html --self-contained-html
```

## Learning Outcomes

- Practiced Python OOP concepts.
- Gained experience in manual testing.
- Learned test case creation and execution.
- Practiced defect identification and verification.
- Learned Pytest automation.
- Understood basic automotive ECU and CAN concepts.

## Project Scope

This project is developed for learning and software testing practice. Automotive functionalities and CAN communication are simulated using Python. No physical vehicle, ECU hardware or actual CAN bus testing was performed.