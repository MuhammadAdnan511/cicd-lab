import os

API_KEY = os.getenv("API_KEY")  # ✅ secure

def login(password):
    if password == os.getenv("ADMIN_PASS"):
        print("Logged in")
