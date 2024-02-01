import json
import boto3

def process_booking(name, surname, date_of_trip, transport_type, destination):
    """
    Process the booking information and create a response text.
    """
    response_text = f"Booking made for: Name: {name}, Surname: {surname}, Date of Trip: {date_of_trip}, Destination: {destination}, Transport: {transport_type}"

    print("reponse text: "+response_text)

    return response_text


def lambda_handler(event, context):

    # Check if the API path matches '/bookTrip'
    if event.get('apiPath') == '/bookTrip':
        # Initialize default values
        name = surname = date_of_trip = destination = 'Unknown'

        # Extract properties from the requestBody
        properties = event.get('requestBody', {}).get('content', {}).get('application/json', {}).get('properties', [])

        # Extracting values based on the 'name' key
        for prop in properties:
            if prop['name'] == 'name':
                name = prop['value']
            elif prop['name'] == 'surname':
                surname = prop['value']
            elif prop['name'] == 'date_of_trip':
                date_of_trip = prop['value']
            elif prop['name'] == 'transport_type':
                transport_type = prop['value']
            elif prop['name'] == 'destination':
                destination = prop['value']

        # Process the booking and get the response text
        response_text = process_booking(name, surname, date_of_trip, destination)
        
        response_body = {
            'application/json':
            {
                'body': json.dumps(response_text)
            }
        }
        
        response = {
            "messageVersion": "1.0",
            "response": {
                "actionGroup": event.get('actionGroup','Unknown'),
                "apiPath": event.get('apiPath','Unknown'),
                "httpMethod": event.get('httpMethod','Unknown'),
                "httpStatusCode": 200,
                "responseBody": response_body
            }
        }

        # Returning the response
        return response
    else:
        # Handle other API paths or return a default message
        response_text = 'Invalid API path'
        
        response_body = {
            'application/json':
            {
                'body': response_text
            }
        }
        
        response = {
            "messageVersion": "1.0",
            "response": {
                "actionGroup": event.get('actionGroup','Unknown'),
                "apiPath": event.get('apiPath','Unknown'),
                "httpMethod": event.get('httpMethod','Unknown'),
                "httpStatusCode": 400,
                "responseBody": response_body
            }
        }
        
        return response