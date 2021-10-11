class CellPhone:
    def __init__(self, model):
        self.model = model
        self.phone_number = "000-000-000"
        self.contacts = {"Jess": "505-555-0981", "Joe": "505-555-1234"}
        self.messages = []
        self.vibrate_mode = False

    def receive_message(self, inbound_message):
        self.messages.append(inbound_message)

    def toggle_vibrate(self):
        self.vibrate_mode = not self.vibrate_mode

    def send_text(self):
        contact = input("Who would you like to send a message to: ")
        contact_number = self.contacts[contact]
        msg = input("Message: ")
        print(f"To: {contact_number}\nSent: {msg}")

