from cell_phone import CellPhone

phone = CellPhone('iPhone 4')

print(f"Contacts: {phone.contacts}")

phone.receive_message("I am message one")
phone.receive_message("I am message two")

print(f"Messages: {phone.messages}")

phone.send_text()

phone.toggle_vibrate()

if (phone.vibrate_mode):
    print("Phone is on vibrate")
else:
    print("Phone is not on vibrate")