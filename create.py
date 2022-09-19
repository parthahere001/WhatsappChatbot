from __future__ import print_function
import os.path
import datetime

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ['https://www.googleapis.com/auth/calendar']

def create_event(start_date, start_time, end_date, end_time,event_name):
    start_date = datetime.datetime.strptime(start_date, '%d-%b-%y').strftime('%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date, '%d-%b-%y').strftime('%Y-%m-%d')
    start_time = datetime.datetime.strptime(start_time, '%I:%M%p').strftime('%H:%M:'+'00')

