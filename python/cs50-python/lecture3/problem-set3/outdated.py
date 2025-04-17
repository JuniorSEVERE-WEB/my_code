months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()
    try:
        # Essayer le format MM/JJ/AAAA
        month, day, year = date.split("/")
        month = int(month)
        day = int(day)
        if 1 <= month <= 12 and 1 <= day <= 31:
            break
    except:
        try:
            # Essayer le format 'Month Day, Year'
            parts = date.split(" ")
            if len(parts) != 3 or not parts[1].endswith(","):
                continue
                
            old_month, old_day, year = parts
            old_day = old_day.replace(",", "")
            
            # Conversion du mois
            month = months.index(old_month.title()) + 1
            day = int(old_day)
            
            if 1 <= month <= 12 and 1 <= day <= 31:
                break
        except:
            pass

print(f"{year}-{month:02}-{day:02}")