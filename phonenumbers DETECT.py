import phonenumbers
from phonenumbers import geocoder, carrier, timezone, NumberParseException

# Ask user for number
phone_number_str = input("Enter phone number (with or without country code): ")

# Try to parse the number
try:
    if phone_number_str.startswith('+'):
        # If user entered country code
        phone_number = phonenumbers.parse(phone_number_str)
    else:
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
        2: "Fixed line or mobile",
        3: "Toll free",
        4: "Premium rate",
        5: "Shared cost",
        6: "VoIP",
        7: "Personal number",
        8: "Pager",
        9: "UAN",
        10: "Voicemail",
        99: "Unknown"
    }
    print("Number Type:", types.get(num_type, "Unknown"))
else:
    print("Invalid phone number")


'''WITH HELP OF PIP INSTALL PHONENUMBERS WE HAVE INSTALLED EXTERNAL LIB 
import phonenumbers
This line imports the main phonenumbers library, which lets Python read, analyze, and validate phone numbers.
It’s based on Google’s libphonenumber.

This imports specific tools from the phonenumbers module:

geocoder: Gets location info (like country, state, or city).

carrier: Gets the mobile operator (like Jio, Airtel, Vi).

timezone: Gets time zones related to the number’s location.
phone_number1 = phonenumbers.parse("+91 9818387668")
This parses the string phone number into a format that the library can understand.

+91 is the country code for India.

The number  -------------is a typical Indian mobile number.

parse() turns this into a structured object with country code, national number, etc.
print(geocoder.description_for_number(phone_number1, "en"))
This line uses the geocoder tool to find the location (region or state).

"en" means the result will be in English.

Example output: "Delhi" or "India" — depending on how specific the number info is.

print("Carrier:", carrier.name_for_number(phone_number1, "en"))
Uses the carrier tool to find out the mobile operator.

For example, output could be: Carrier: Airtel or Carrier: Jio.

print("Timezone(s):", timezone.time_zones_for_number(phone_number1))
This gives the time zones where the number is registered.

Indian numbers usually show: Timezone(s): ['Asia/Kolkata']'''
