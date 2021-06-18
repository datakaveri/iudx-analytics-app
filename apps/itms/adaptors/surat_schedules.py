import requests
import json
import time
import dateutil.parser
from datetime import datetime
from collections import OrderedDict
from pytz import timezone
import pandas as pd
import schedule
import os

formatter = "%Y-%m-%d"
ist = timezone('Asia/Kolkata')
db_formatter = "%Y-%m-%dT%H:%M:%S+05:30"
time_formatter = "%Y-%m-%dT%H:%M:%S+05:30"

adaptor_id = "surat-itms-scheduled-ingestion"
config_path = "./config.json"


out_data = []
#@sched.scheduled_job('cron',day_of_week='mon-sun',hour=5,minute=30,second=00)
def get_schedules_data():
	print("adapter started")

	config = {}
	with open(config_path, "r") as f:
		config = json.load(f)[adaptor_id]


	try:
		response = (requests.get(config["url"], data={})).json()
		for result in response:
			schedules_data = OrderedDict()
			schedules_data["id"] = config["id"]
			schedules_data["trip_id"] = str(result["trip_id"])
			#schedules_data["arrival_time"] = result["trip_details"]["arrival_time"]
			schedules_data["arrival_time"] = dateutil.parser.parse(result["trip_details"]["arrival_time"]).strftime(time_formatter)
			#schedules_data["departure_time"] = result["trip_details"]["departure_time"]
			schedules_data["departure_time"] = dateutil.parser.parse(result["trip_details"]["departure_time"]).strftime(time_formatter)
			schedules_data["stop_id"] = str(result["trip_details"]["stop_id"])
			schedules_data["stop_sequence"] = int(result["trip_details"]["stop_sequence"])
			schedules_data["observationDateTime"] = dateutil.parser.parse(str(datetime.now())).strftime(time_formatter)
			# print(schedules_data)
			out_data.append(schedules_data)
			#print(json.dumps(schedules_data, indent=4))
	except Exception as e:
		print(e)

	df = pd.read_json(json.dumps(out_data))
	if(os.path.exists("out.csv")):
            os.remove("out.csv")
	df.to_csv("out.csv")

	print("adapter stopped")

#if __name__ == "__main__":
#	sched.start()
#get_schedules_data()
schedule.every().day.at("04:00").do(get_schedules_data)

while True:
	schedule.run_pending()
	time.sleep(1)

