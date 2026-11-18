
from src.can_bus import CANBus


def test_send_can_message():

    can = CANBus()

    result = can.send_message(
        0x100,
        "Engine ECU",
        "Instrument Cluster ECU",
        {"speed": 60}
    )

    assert result == "Message sent successfully"
    assert len(can.messages) == 1


def test_receive_can_message():

    can = CANBus()

    can.send_message(
        0x100,
        "Engine ECU",
        "Instrument Cluster ECU",
        {"speed": 60}
    )

    messages = can.receive_messages("Instrument Cluster ECU")

    assert len(messages) == 1
    assert messages[0]["data"]["speed"] == 60


def test_receive_message_from_wrong_ecu():

    can = CANBus()

    can.send_message(
        0x100,
        "Engine ECU",
        "Instrument Cluster ECU",
        {"speed": 60}
    )

    messages = can.receive_messages("Infotainment ECU")

    assert len(messages) == 0


def test_invalid_can_id():

    can = CANBus()

    result = can.send_message(
        -10,
        "Engine ECU",
        "Instrument Cluster ECU",
        {"speed": 60}
    )

    assert result == "Invalid CAN ID"
    assert len(can.messages) == 0


def test_maximum_valid_can_id():

    can = CANBus()

    result = can.send_message(
        0x7FF,
        "Engine ECU",
        "Instrument Cluster ECU",
        {"speed": 60}
    )

    assert result == "Message sent successfully"
