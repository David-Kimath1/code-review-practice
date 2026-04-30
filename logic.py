# logic.py
def calculate_status(connection):
    if connection == "active":
        return "Backend is running so good"
    return "Connection issues"

print(calculate_status("active"))