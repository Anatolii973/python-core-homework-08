from datetime import datetime

current_datetime = datetime.now()

future_month = (current_datetime.month % 12) + 1
future_year = current_datetime.year + int(current_datetime.month / 12)
future_datetime = datetime(future_year, future_month, 1)

print(current_datetime < future_datetime)