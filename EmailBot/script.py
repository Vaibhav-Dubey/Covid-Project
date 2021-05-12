import requests , json 
import datetime
from datetime import date 
from emailSaample import sendemail


today=datetime.datetime.today()+datetime.timedelta(days=1)
today=today.strftime("%d-%m-%Y")
print(type(today))
today=str(today)
print(today)

now = datetime.datetime.now()

current_time = now.strftime("%H:%M:%S")
print(current_time)
print(type(current_time))

while(current_time>"12:54:00" and current_time< "12:56:00"):
    headers = {
        'accept': 'application/json',
        'Accept-Language': 'hi_IN',
        'User-Agent':'Mozilla/5.0'
    }

    params = (
        ('pincode', '410210'),
        ('date', today),
    )

    response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin', headers=headers, params=params)



    data = (response.json())
    if (data["sessions"][0]["available_capacity"]>50):
        sendemail()
        break
    