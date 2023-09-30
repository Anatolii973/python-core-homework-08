from datetime import date, timedelta, datetime
start_date = date.today()
end_date = start_date + timedelta(7)

def get_period(start_date: date, days: int): # функция периода всех дат от текущей ,
                                             # дельтой 7 дней, на выходе словарь {(число,дата):тек.год}
    result = {}
    for _ in range(days + 1):
        result[start_date.day, start_date.month] = start_date.year
        start_date += timedelta(1)
    
    return result

def get_birthdays_per_week(users: list) -> list:
    res = {"Monday" : [], "Tuesday" : [], "Wednesday" : [], "Thursday" : [], "Friday" : []}

    start_date = date(2023, 12, 29)
    period = get_period(start_date, 7)
    
    # end_date = start_date + timedelta(7)
    
    for user in users:
        bd: date = user["birthday"]
        date_bd = bd.day, bd.month
        
        if date_bd in list(period):
           date_bd_week = datetime(year=period[date_bd], month=bd.month, day=bd.day)
           
           for key in res.keys():
              if date_bd_week.strftime('%A') == key:
                 res[key] = user['name']
              else:
                #  date_bd_week.strftime('%A') == 'Saturday' or date_bd_week.strftime('%A') == 'Sunday':
                 res["Monday"].append(user['name'])


        #    print(date_bd_week.weekday()) 

        # print(user["name"], period[date_bd] )
    return res   

if __name__ == '__main__':
    users = [{"name": "Bill", "birthday": date(1990, 12, 30)},
             {"name": "Marry", "birthday": date(2000, 1, 2)},
             {"name": "John", "birthday": date(2003, 1, 5)},
             {"name": "Jack", "birthday": date(2005, 1, 1)}
             ]
    result = get_birthdays_per_week(users)

    
    print(result)
    # Виводимо результат
    
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
    get_period(start_date, 7)