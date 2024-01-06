# Flight Deal Finder
The Flight Deal Notifier uses a Google Sheet to register desired locations for traveling and its average price. It uses the Tequila Kiwi API to look for deals to this desired locations and sends a SMS with the relevant info.

## Setup
In order to run the program you need to complete the following check list:

- Tequila Kiwi Flight API Account: This is necessary for the API credentials.
- Sheety API Account: Same as before, this required in order to get the credentials of the Google Sheets to be read and write.
- Twilio API Account: In order to send a SMS, you need to get a free phone from which you send the notifications.
- The following environment variables or .env file:
```
SHEETY_URL = <your_sheety_url>
SHEETY_TOKEN = <authorization_token_of_your_choice>

TEQUILA_API_KEY = <your_tequila_api_key>

TWILIO_ACCOUNT_SID = <your_twilio_account_sid>
TWILIO_AUTH_TOKEN = <your_twilio_auth_token>
TO_PHONE = <your_phone_number>
```

## How to use
Once you've set up everything, you can run the program with python main.py. The program will search for flight deals from airport of choice to all of the destinations listed in the Sheety spreadsheet. If a deal is found that is significantly cheaper than the value stored in the spreadsheet(the lowest price known), the program will send an SMS message and email notification to alert you of the deal.

## Files
* __main.py__: The main program file that searches for flight deals and sends notifications.
* __flight_search.py__: A helper module that searches the Tequila Flight API for flight deals.
* __data_manager.py__: A helper module that retrieves and updates the list of destinations and customer emails from the Sheety API.
* __notification_manager.py__: A helper module that sends SMS messages and emails using the Twilio API and SMTP protocol.
* __flight_data.py__: A class that represents flight data, used to store flight information retrieved from the Tequila Flight API.
