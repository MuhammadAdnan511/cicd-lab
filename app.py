import os

API_KEY = "12345-SECRET-KEY"   # ❌ hardcoded secret

def login(password):
    if password == "admin123":   # ❌ weak auth
        print("Logged in")

eval("print('Dangerous')")  # ❌ code injection risk
