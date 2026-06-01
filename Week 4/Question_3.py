bs_months = [
    "Baisakh", "Jestha", "Ashadh", "Shrawan", "Bhadra", "Ashwin",
    "Kartik",  "Mangsir", "Poush", "Magh",    "Falgun", "Chaitra"
]
 
customers = [
    {"name": "Ramesh Thapa",  "date": "1985-06-24", "cal": "AD", "need": "BS", "style": "full"},
    {"name": "Sunita Karki",  "date": "2055-09-10", "cal": "BS", "need": "AD", "style": "iso"},
    {"name": "Bikash Rai",    "date": "1998-11-30", "cal": "AD", "need": "BS", "style": "nepali"},
    {"name": "Anjali Gurung", "date": "2040-01-05", "cal": "BS", "need": "AD", "style": "full"},
]
 
def convert_date(date_str, from_cal, to_cal, style="iso"):
    year, month, day = map(int, date_str.split("-"))
 
    if from_cal == to_cal:
        converted_year = year
    elif from_cal == "AD" and to_cal == "BS":
        converted_year = year + 56
    else:
        converted_year = year - 56
 
    month_name = bs_months[month - 1]
 
    def get_suffix(d):
        if d in (1, 21, 31): return "st"
        if d in (2, 22):     return "nd"
        if d in (3, 23):     return "rd"
        return "th"
 
    if style == "iso":
        return f"{converted_year}-{month:02d}-{day:02d}"
    elif style == "full":
        suffix = get_suffix(day)
        return f"{day}{suffix} {month_name}, {converted_year} {to_cal}"
    elif style == "nepali":
        return f"{day} {month_name} {converted_year}"
 
print("\n---- Bank Date Conversion ----")
for c in customers:
    result = convert_date(c["date"], c["cal"], c["need"], c["style"])
    print(f"{c['name']:<15} | Original: {c['date']} {c['cal']} | Converted: {result}")
 
