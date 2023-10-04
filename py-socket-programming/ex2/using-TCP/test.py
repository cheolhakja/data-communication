import requests

# Define the URL you want to send the HTTP request to
url = 'https://example.com'  # Replace with your desired URL

# Define the HTTP method (GET, POST, etc.) and any additional headers
http_method = 'GET'  # Change to 'POST' or other methods if needed
headers = {'User-Agent': 'MyApp/1.0'}  # Example headers

# Define any request parameters (query parameters for GET, data for POST)
params = {'param1': 'value1', 'param2': 'value2'}  # Example parameters

# Send the HTTP request
response = requests.request(http_method, url, headers=headers, params=params)

# Get the HTTP request message in string format
request_message = response.request.headers + '\n\n' + response.request.body
print(request_message)