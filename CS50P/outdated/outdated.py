def get_month_number(month_name):
    month_map = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12,
    }
    return month_map.get(month_name, None)

def main():
    while True:
        try:
            date_input = input("Enter a date (MM/DD/YYYY or Month Day, Year): ")

            if ',' in date_input:
                month, day_year = date_input.split(',', 1)
                month_day = month.strip().split()
                if len(month_day) == 2:
                    month_name, day = month_day
                    day = day.strip()
                    year = day_year.strip()
                    month_number = get_month_number(month_name)
                    if month_number and day.isdigit() and 1 <= int(day) <= 31:
                        formatted_date = f"{year}-{month_number:02d}-{int(day):02d}"
                        print(formatted_date)
                        break
                continue
            elif '/' in date_input:
                month, day, year = map(int, date_input.split("/"))
                if 1 <= month <= 12 and 1 <= day <= 31:
                    formatted_date = f"{year}-{month:02d}-{day:02d}"
                    print(formatted_date)
                    break
                continue
        except ValueError:
            continue

if __name__ == "__main__":
    main()
