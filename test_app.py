import requests
import urllib.parse
import json

# The text you want to test
text = "Nairobi is in war"

# URL encode the text
text = urllib.parse.quote(text)

# The URL of the test route
test_url = f"http://localhost:5001/test?input={text}"

# Send the GET request to the test route
test_response = requests.get(test_url)

# Print the response from the test route
print(test_response.text)

# The URL of the predict route
predict_url = "http://localhost:5001/predict"

# The headers for the POST request
headers = {"Content-Type": "application/json"}

# The data for the POST request
data = {"text": text}

# Send the POST request to the predict route
predict_response = requests.post(predict_url, headers=headers, data=json.dumps(data))

# Print the response from the predict route
print(predict_response.json())