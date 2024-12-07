format_24 = input("Enter time (24-hour format, hh:mm): ")
hours, minutes = map(int, format_24.split(":"))
period = "am" if hours < 12 else "pm"
hours = hours % 12 or 12 
print(f"Time in 12-hour format: {hours}:{minutes:02d}{period}")