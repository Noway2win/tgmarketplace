import json

import requests
from celery.schedules import crontab
from celery.task import periodic_task


@periodic_task(run_every=crontab(hour=7, minute=0))
def get_usd_price():
    response = requests.get("https://belarusbank.by/api/kursExchange?city=Минск")
    json_list = response.json()
    json_dict = json_list[0]
    usd_price = json_dict["USD_in"]
    return usd_price
