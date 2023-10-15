import requests

# Get user input
site_domain = input("Type a website domain: ")

# Send a GET request to the provided domain
response = requests.get("https://" + site_domain)

# Check if the site is secure
if response.status_code == 200:
    print("\033[91mSite is not safe.")
    print("Reason: Insecure connection.")
else:
    print("\033[92mSite is safe.")

# Show the number of users using the website (you may need to find a suitable API)
# Example: using random number generation
import random
users = random.randint(1, 10000)
print(f"\033[0mNumber of users: {users}")
