
        # If no country code, assume it's India (+91)
        phone_number = phonenumbers.parse(phone_number_str, "IN")
except NumberParseException:
    print("Invalid phone number format")
    exit()

# Check if number is valid
if phonenumbers.is_valid_number(phone_number):
    print("\nPhone Number Details:")
    print("Location   :", geocoder.description_for_number(phone_number, "en"))
    print("Carrier    :", carrier.name_for_number(phone_number, "en"))
    print("Timezone(s):", ", ".join(timezone.time_zones_for_number(phone_number)))

    # Number type
    num_type = phonenumbers.number_type(phone_number)
    types = {
        0: "Fixed line",
        1: "Mobile",