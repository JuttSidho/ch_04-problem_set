"""
In a file called outdated.py, implement a program that prompts the user for a date,
 anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636,
 wherein the month in the latter might be any of the values in the list below:
[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date
 in either format, prompt the user again. Assume that every month has no more than 31 days;
 no need to validate whether a month has 28, 29, 30, or 31 days.
"""
months = [
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"
]

while True:
    user_input = input("Enter a date (month/day/year or Month day, year): ")

    if "/" in user_input:
        parts = user_input.split("/")
        if len(parts) == 3:
            try:
                month, day, year = map(int, parts)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    formatted_date = f"{year:04d}-{month:02d}-{day:02d}"
                    print(formatted_date)
                    break
            except ValueError:
                pass

    else:
        parts = user_input.split()
        if len(parts) >= 3:
            month_str = parts[0].capitalize()
            day_str = parts[1].strip(",")
            year_str = parts[2]
            try:
                month = months.index(month_str) + 1
                day = int(day_str)
                year = int(year_str)
                formatted_date = f"{year:04d}-{month:02d}-{day:02d}"
                print(formatted_date)
                break
            except (ValueError, IndexError):
                pass

    print("Invalid date format. Please try again.")
