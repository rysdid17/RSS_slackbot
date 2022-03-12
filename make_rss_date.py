from datetime import date, datetime

def make_today():
    today_year = datetime.now().strftime('%Y')
    today_month = datetime.now().strftime('%m')
    today_day = datetime.now().strftime("%d")

    if today_month[0] == '0':
        today_month = today_month[1:]

    if today_day[0] == '0':
        today_day = today_day[1:]
    
    today = today_year + today_month + today_day
    return today