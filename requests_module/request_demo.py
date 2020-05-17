import requests

# Download the image from the url
response = requests.get("https://imgs.xkcd.com/comics/python.png")
if response.status_code == 200:
    try:
        with open("comic.png", "wb") as file:
            # file.write(response.content)
            print("File downloaded successfully!")
    except FileNotFoundError:
        print("Exception: File not found")

# Get Request
payload = {'page': 2, 'count': 25}
response = requests.get("https://httpbin.org/get", params=payload)
if response.status_code == 200:
    print(response.url)

# Post Request
payload = {'username': 'alpha', 'password': 'mega'}
response = requests.post("https://httpbin.org/post", data=payload)
if response.status_code == 200:
    print(response.text)

# JSON Response
if response.status_code == 200:
    response_dict = response.json()
    response_dict_form = response_dict['form']
    print(f"The Username and Password is: {response_dict_form['username']} and {response_dict['form']['password']}")

# Auth
payload = {'username': 'alpha', 'password': 'mega'}
response = requests.get("https://httpbin.org/basic-auth/alpha/mega", auth=(payload['username'], payload['password']))

if response.status_code == 200:
    print(response.text)
elif response.status_code == 401:
    print("Unauthorized login")

# Timeout
response = requests.get("https://httpbin.org/delay/1", timeout=3)
print(response)

# Returns Image
response = requests.get("https://httpbin.org/image/jpeg")
if response.status_code == 200:
    with open("bin_image.jpeg", "wb") as file:
        file.write(response.content)

# Returns IP Address
response = requests.get("https://httpbin.org/ip")
if response.status_code == 200:
    print(response.text)

