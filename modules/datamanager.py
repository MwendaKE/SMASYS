from kivy.app import App

from pymongo import MongoClient
from modules.msgmanager import show_error
from datetime import datetime


NOW = datetime.now()
PREVIOUS_YEAR = NOW.year - 1

def get_database():
    DATABASE = App.get_running_app().database_name
    client = MongoClient('localhost', 27017)

    #database = client["mwesmasys_db"] # ORIGINAL DB
    #database = client["mwesmasys_test_db"] # TEST DB
    
    database = client[DATABASE] # TEST DB
    
    return database

# REST OF CODE HIDDEN
