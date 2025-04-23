from datetime import datetime

def format_time(value):
    # assuming value is "YYYY-MM-DDTHH:MM"
    dt = datetime.strptime(value, "%Y-%m-%dT%H:%M")
    return dt.strftime("%b %d, %Y — %I:%M %p")
