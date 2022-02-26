from jira import JIRA
from jira import JIRAError

import requests
from requests.auth import HTTPBasicAuth
import json

# import ast
# import pandas as pd

# -- functions -- #

def get_auth_info(json_file):
    """takes config.json file, returns auth dictionary of info"""
    
    f= open(json_file)
    data = json.load(f)
    user_info = {}

    for key in data:
        user_info[key] = data[key]

    f.close()
    
    return user_info

def authenticate(user_info):
    """takes user_info dictionary and authenticates through JIRA"""
   
    auth_secret = user_info['password']
    auth_key = user_info['user']
    auth_url = user_info['url']

    auth = HTTPBasicAuth(auth_key, auth_secret)
    
    return auth

def jira_auth(user_info):
    """takes user_info dictionary, returns authentication through JIRA"""
   
    auth_secret = user_info['password']
    auth_key = user_info['user']
    auth_url = user_info['url']
    
    jiraOptions = {'server': auth_url}
    jira = JIRA(options=jiraOptions, basic_auth=(
        auth_key, auth_secret))
    
    return jira
    
def get_last_one_mo(jira):
   """takes jira, returns array of issue objects from last month""" 
   for issue in jira.search_issues('project in ("Web Content & Campaigns") AND createdDate >= startofmonth(-1) AND createdDate <= endOfmonth(-1)', maxResults=1):
      print('{}: {}'.format(issue.key, issue.fields.__dict__))
   
      
if __name__ == "__main__":
       
   auth_dict = get_auth_info("config.json")
   jira = jira_auth(auth_dict)
   
   get_last_one_mo(jira)