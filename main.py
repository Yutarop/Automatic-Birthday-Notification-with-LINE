import requests
import pandas as pd
import datetime as dt

URL = "https://notify-api.line.me/api/notify"
ACCESS_TOKEN = 'Your Access Token'
HEADERS = {'Authorization': 'Bearer ' + ACCESS_TOKEN}

# get year, month, and day
today_date = dt.date.today()
year = today_date.year
month = today_date.month
day = today_date.day

# read csv
birth_data = pd.read_csv("birthdays_list.csv")
birth_data_dict = birth_data.to_dict(orient='index')

# if today is somebody's birthday
for index in birth_data_dict:
    if birth_data_dict[index]["month"] == month and birth_data_dict[index]["day"] == day:
        # send a notification to your LINE
        message = f"Today is {birth_data_dict[index]['name']}'s birthday."
        payload = {'message': message}
        r = requests.post(URL, headers=HEADERS, params=payload,)
