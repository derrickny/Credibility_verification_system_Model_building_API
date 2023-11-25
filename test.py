import requests
import json

def get_prediction(user_input):
    # Send a POST request to the Flask API
    url = "https://c90e-41-80-113-166.ngrok-free.app/predict"
    headers = {"Content-Type": "application/json"}
    data = {"text": user_input}
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

        # Try to parse the response as JSON and return it
        return response.json()

    except requests.RequestException as e:
        # Handle any request exception (e.g., connection error)
        return {"error": f"Request error: {str(e)}"}

    except json.JSONDecodeError:
        # Handle JSON decoding error
        return {"error": "Could not parse response as JSON"}

if __name__ == "__main__":
    # Ask the user for a statement
    user_input = input("Enter a statement: ")

    # Get the prediction
    prediction = get_prediction(user_input)

    # Print the prediction
    print("Prediction:", prediction)
