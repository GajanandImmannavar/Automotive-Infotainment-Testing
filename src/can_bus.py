
class CANBus:

    def __init__(self):
        self.messages = []

    def send_message(self, can_id, sender, receiver, data):

        # Validate standard 11-bit CAN ID
        if not isinstance(can_id, int) or not 0 <= can_id <= 0x7FF:
            return "Invalid CAN ID"

        message = {
            "can_id": can_id,
            "sender": sender,
            "receiver": receiver,
            "data": data
        }

        self.messages.append(message)

        return "Message sent successfully"

    def receive_messages(self, receiver):

        received_messages = []

        for message in self.messages:
            if message["receiver"] == receiver:
                received_messages.append(message)

        return received_messages
