import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
import requests

class WeatherFetcher:
    def __init__(self, latitude, longitude, cache_expire=3600, retries=5, backoff_factor=0.2, debug=False):
        self.latitude = latitude
        self.longitude = longitude
        self.debug = debug
        self.cache_session = requests_cache.CachedSession('.cache', expire_after=cache_expire)
        self.retry_session = retry(self.cache_session, retries=retries, backoff_factor=backoff_factor)
        self.openmeteo = openmeteo_requests.Client(session=self.retry_session)

    def fetch_weather(self):
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "daily": "precipitation_probability_max",
        }
        responses = self.openmeteo.weather_api(url, params=params)
        return responses[0]

    def process_weather(self, response):
        daily = response.Daily()
        daily_precipitation_probability_max = daily.Variables(0).ValuesAsNumpy()

        daily_data = {"date": pd.date_range(
            start=pd.to_datetime(daily.Time(), unit="s", utc=True),
            end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=daily.Interval()),
            inclusive="left"
        )}
        daily_data["precipitation_probability_max"] = daily_precipitation_probability_max

        daily_dataframe = pd.DataFrame(data=daily_data)
        
        if self.debug:
            for index, row in daily_dataframe.iterrows():
                print(f"Date: {row['date']}, Precipitation Probability Max: {row['precipitation_probability_max']}")
        return daily_dataframe

class ErrandDay:
    def __init__(self, latitude, longitude, cache_expire=3600, retries=5, backoff_factor=0.2, debug=False):
        self.weather_fetcher = WeatherFetcher(latitude=latitude, longitude=longitude, cache_expire=cache_expire, retries=retries, backoff_factor=backoff_factor, debug=debug)
        self.weather_data = self.weather_fetcher.fetch_weather()
        self.processed_data = self.weather_fetcher.process_weather(self.weather_data)

    def get_errand_day(self):
        precipitation = self.processed_data[self.processed_data["precipitation_probability_max"] < 25]
        return precipitation

def get_lat_long(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    response = requests.get(url)
    data = response.json()

    if data['results']:
        result = data['results'][0]
        latitude = result['latitude']
        longitude = result['longitude']
        return latitude, longitude
    else:
        return None

if __name__ == "__main__":
    print(get_lat_long("Edison"))