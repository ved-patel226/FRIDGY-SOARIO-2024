from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from termcolor import cprint
from datetime import datetime
import pickle
import os

try:
    from py_tools.weather import ErrandDay
except Exception as e:
    print(f"Error importing ErrandDay: {e}")
    from .weather import ErrandDay

def load_credentials():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    return creds

def save_credentials(creds):
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)    

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly', 'https://www.googleapis.com/auth/calendar']

def google_redirect():
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    creds = flow.run_local_server(port=8080)

    cprint(f"Access token: {creds.token}", "red", attrs=["bold"])

def get_service():
    creds = load_credentials()
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=8080)
        save_credentials(creds)
    service = build('calendar', 'v3', credentials=creds)
    return service
def get_all_events():
    events = []
    start_times = []
    
    calendar_id = 'primary'
    page_token = None
    service = get_service()
    
    while True:
        events_result = service.events().list(calendarId=calendar_id, pageToken=page_token).execute()
        events = events_result.get('items', [])
        for event in events:
            if 'dateTime' in event['start']:
                start_time_str = event['start']['dateTime']
                start_time = datetime.fromisoformat(start_time_str)
            elif 'date' in event['start']:
                start_time_str = event['start']['date']
                start_time = datetime.fromisoformat(start_time_str)  # All-day events use only the date
            
            start_times.append(start_time)
            
        page_token = events_result.get('nextPageToken')
        if not page_token:
            break
        
    return start_times

def perfect_errand_day(lat="40.517310", long="-74.410946"):
    errands = ErrandDay(lat, long).get_errand_day()
    dates = []
        
    for index, row in errands.iterrows():
        dates.append(datetime.fromisoformat(str(row[0])))
    
    errand_dates = [date.date() for date in dates]
    event_dates = [event.date() for event in get_all_events()]
    
    non_matching_dates = set(errand_dates) - set(event_dates)
    
    if len(non_matching_dates) == 0:
        cprint("No non-matching dates", "red", attrs=["bold"])
        return None
    else:
        cprint(f"Non-matching errand dates: {non_matching_dates}", "green", attrs=["bold"])
        return list(non_matching_dates)      

def create_all_day_event(event_date, summary="Shopping Day - FRIDGY", description="Have fun Shopping!"):
    if isinstance(event_date, datetime):
        event_date = event_date.strftime("%Y-%m-%d")
    
    service = get_service()
    event = {
        'summary': summary,
        'description': description,
        'start': {
            'date': event_date,
            'timeZone': 'UTC',
        },
        'end': {
            'date': event_date,
            'timeZone': 'UTC',
        },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    cprint(f"Event created: {event.get('htmlLink')}", "green", attrs=["bold"])
    return event

if __name__ == "__main__":
    get_all_events()