from jiraone import LOGIN, PROJECT, file_reader
from jiraone.module import time_in_status
import json

config = json.load(open('config.json'))
LOGIN(**config)
key = ["COM-12", "COM-14"]

if __name__ == "__main__":     
    time_in_status(PROJECT, key, file_reader, pprint=True, is_printable=False,     
    output_format="json", report_folder="STATUSPAGE", report_file="time.csv",     
    status="In progress", login=LOGIN, output_filename="result")