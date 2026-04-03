import os

API_KEY = os.getenv("API_KEY")

def login(password):
    if password == os.getenv("ADMIN_PASS"):
        print("Logged in")

if API_KEY:
    print("API key loaded successfully")
