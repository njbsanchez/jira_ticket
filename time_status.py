from jiraone import LOGIN, PROJECT, file_reader
from jiraone.module import time_in_status
import json

config = json.load(open('config.json'))
LOGIN(**config)

key = ["WCC-9433", "WCC-9411", "WCC-9332", "WCC-9299", "WCC-9298", "WCC-9297", "WCC-9296", "WCC-9295", "WCC-9294", "WCC-9292", "WCC-9291", "WCC-9290", "WCC-9289", "WCC-9288", "WCC-9287", "WCC-9286", "WCC-9285", "WCC-9284", "WCC-9283", "WCC-9282", "WCC-9281", "WCC-9279", "WCC-9278", "WCC-9277", "WCC-9276", "WCC-9275", "WCC-9274", "WCC-9273", "WCC-9272", "WCC-9271", "WCC-9270", "WCC-9269", "WCC-9268", "WCC-9267", "WCC-9266", "WCC-9265", "WCC-9264", "WCC-9262", "WCC-9261", "WCC-9260", "WCC-9259", "WCC-9258", "WCC-9257", "WCC-9256", "WCC-9255", "WCC-9254", "WCC-9253", "WCC-9252", "WCC-9251", "WCC-9250", "WCC-9249", "WCC-9247", "WCC-9246", "WCC-9245", "WCC-9244", "WCC-9243", "WCC-9242", "WCC-9241", "WCC-9240", "WCC-9239", "WCC-9238", "WCC-9237", "WCC-9236", "WCC-9235", "WCC-9234", "WCC-9233", "WCC-9232", "WCC-9231", "WCC-9230", "WCC-9229", "WCC-9227", "WCC-9226", "WCC-9225", "WCC-9224", "WCC-9223", "WCC-9222", "WCC-9221", "WCC-9220", "WCC-9219", "WCC-9218", "WCC-9217", "WCC-9216", "WCC-9215", "WCC-9214", "WCC-9212", "WCC-9211", "WCC-9210", "WCC-9209", "WCC-9208", "WCC-9207", "WCC-9206", "WCC-9205", "WCC-9204", "WCC-9203", "WCC-9202", "WCC-9201", "WCC-9200", "WCC-9199", "WCC-9198", "WCC-9197"]

if __name__ == "__main__":     
    time_in_status(PROJECT, key, file_reader, pprint=True, is_printable=False,     
    output_format="json", report_folder="STATUSPAGE", report_file="time.csv",     
    status="In progress", login=LOGIN, output_filename="result")