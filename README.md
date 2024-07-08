# Web-login-brute
This tool attempts to perform a brute-force login by sending HTTP POST requests to a specified target URL (http://127.0.0.1:5000). It uses a list of usernames (admin, user, test) and passwords from a file (2023-200_most_used_passwords.txt). During each attempt, it checks if the response contains the string "Welcome back", indicating success.
