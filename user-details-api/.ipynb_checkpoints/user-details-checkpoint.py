import json

def get_user_details(user_id):
    """
    Return user details based on user ID.
    """
    if user_id == "1":
        person = {
            "name": "Anton",
            "surname": "Lukin"
        }
        return person
    elif user_id == "2":
        person = {
            "name": "John",
            "surname": "Doe"
        }
        return person
    else:
        return "User not found"

def lambda_handler(event, context):

    # Handle the getUserDetails API path
    if event.get('apiPath') == '/getUserDetails/{userId}':
        user_id = event.get('pathParameters', {}).get('userId', 'Unknown')
        user_details = get_user_details(user_id)

        response_body = {
            'application/json': {
                'body': json.dumps(user_details)
            }
        }

        response = {
            "messageVersion": "1.0",
            "response": {
                "actionGroup": event.get('actionGroup','Unknown'),
                "apiPath": event.get('apiPath','Unknown'),
                "httpMethod": event.get('httpMethod','Unknown'),
                "httpStatusCode": 200 if user_id != 'Unknown' else 404,
                "responseBody": response_body
            }
        }
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