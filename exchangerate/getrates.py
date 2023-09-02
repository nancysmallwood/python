import json
import requests
import datetime
from datetime import date

# The API base path is https://openexchangerates.org/api/
# Personal app id is e29441c6d558417ab4a3339e14ade65f
#
# Options for API calls
# https://openexchangerates.org/api/
#                                   latest.json
#                                   currencies.json
#                                   historical/2013-02-16.json
# from exchangerate.json_util import write_json_file
#

h_url = "https://openexchangerates.org/api/historical/"
app_id = "e29441c6d558417ab4a3339e14ade65f"
output_path = '.\\output\\'


def get_json_historical_rates(historical_date):
    api_url = h_url + historical_date.strftime("%Y-%m-%d") + ".json" + "?app_id=" + app_id
    response = requests.get(api_url)
    return response.json()


def write_json_file(filename, json_data):
    with open(filename, 'w') as f:
        json.dump(json_data, f, indent=4, sort_keys=True)


def run():
    historical_date = date(2022, 7, 1)
    next_date = historical_date
    for x in range(10):
        filename = output_path + next_date.strftime("%Y-%m-%d") + ".json"
        print(filename)
        rates_json = get_json_historical_rates(next_date)
        write_json_file(filename, rates_json)
        next_date = next_date + datetime.timedelta(days=1)


run()
