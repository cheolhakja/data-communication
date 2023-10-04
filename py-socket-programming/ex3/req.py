import requests
import os
import sys 

# url = "https://namu.wiki/w/%EB%A6%AC%EB%B2%84%ED%92%80"
url = sys.argv[1] 
if len(sys.argv) < 2: 
    print("Error. URL must be presented.") 
    sys.exit() 

print("URL: " + url)
protocol = url.split('//')[0] #http
url_except_protocol = url.split('//')[1] #gaia.cs.umass.edu/kurose_ross/index.php
serverName = url_except_protocol.split('/')[0] #gaia.cs.umass.edu


try:
    response = requests.get(url)
    html_content = response.text
    print(html_content)

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


pwd = os.getcwd()

file_name = "index.html"  
file_path = os.path.join(pwd, file_name)

with open(file_path, "w", encoding="utf-8") as file:
    file.write(html_content)