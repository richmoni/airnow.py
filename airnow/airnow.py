#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

import requests

__version__ = '0.1.0'

BASE_URL = 'https://www.airnowapi.org'
USER_AGENT = 'https://github.com/0isamu/airnow.py'


class AirNowAPI():
    def __init__(self, api_key):
        self.api_key = api_key
        self.format = 'application/json'

    def get_forecast_by_zip_code(self, zip_code, date=None, distance=None):
        if date is None:
            date = datetime.datetime.today().strftime('%Y-%m-%d')
        if distance is None:
            distance = 25

        # API parameters
        options = {}
        options['url'] = '/aq/forecast/zipCode/'
        options['format'] = self.format
        options['zipCode'] = zip_code
        options['date'] = date
        options['distance'] = str(distance)
        options['api_key'] = self.api_key

        # API request URL
        REQUEST_URL = options['url'] \
            + '?format=' + options['format'] \
            + '&zipCode=' + options['zipCode'] \
            + '&date=' + options['date'] \
            + '&distance=' + options['distance'] \
            + '&API_KEY=' + options['api_key']

        # Perform the AirNow API data request
        _json = _request(REQUEST_URL)
        if _json is None:
            return None
        else:
            return Forecast(_json[0])

    def get_forecast_by_lat_long(self, latitude, longitude, date=None,
                                 distance=None):
        if date is None:
            date = datetime.datetime.today().strftime('%Y-%m-%d')
        if distance is None:
            distance = 25

        # API parameters
        options = {}
        options['url'] = '/aq/forecast/latLong/'
        options['format'] = self.format
        options['latitude'] = str(latitude)
        options['longitude'] = str(longitude)
        options['date'] = date
        options['distance'] = str(distance)
        options['api_key'] = self.api_key

        # API request URL
        REQUEST_URL = options['url'] \
            + '?format=' + options['format'] \
            + '&latitude=' + options['latitude'] \
            + '&longitude=' + options['longitude'] \
            + '&date=' + options['date'] \
            + '&distance=' + options['distance'] \
            + '&API_KEY=' + options['api_key']

        # Perform the AirNow API data request
        _json = _request(REQUEST_URL)
        if _json is None:
            return None
        else:
            return Forecast(_json[0])

    def get_observation_by_zip_code(self, zip_code, date=None, distance=None):
        pass

    def get_observation_by_lat_long(self, latitude, longitude, date=None,
                                    distance=None):
        pass

    def get_observations_by_monitoring_site(self, bbox, parameters, datatype,
                                            startdate=None, enddate=None):
        pass


class Forecast():
    def __init__(self, _json):
        self._json = _json
        self.date_issue = self._json['DateIssue']
        self.date_forecast = self._json['DateForecast']
        self.reporting_area = self._json['ReportingArea']
        self.state_code = self._json['StateCode']
        self.latitude = self._json['Latitude']
        self.longitude = self._json['Longitude']
        self.parameter_name = self._json['ParameterName']
        self.aqi = self._json['AQI']
        self.category_number = self._json['Category']['Number']
        self.category_name = self._json['Category']['Name']
        self.action_day = self._json['ActionDay']
        self.discussion = self._json['Discussion']


class Observation():
    def __init__(self, _json):
        self._json = _json
        self.date_observed = self._json['DateObserved']
        self.hour_observed = self._json['HourObserved']
        self.local_time_zone = self._json['LocalTimeZone']
        self.reporting_area = self._json['ReportingArea']
        self.state_code = self._json['StateCode']
        self.latitude = self._json['Latitude']
        self.longitude = self._json['Longitude']
        self.parameter_name = self._json['ParameterName']
        self.aqi = self._json['AQI']
        self.category_number = self._json['Category']['Number']
        self.category_name = self._json['Category']['Name']


def _request(endpoint):
    headers = {'user-agent': USER_AGENT}
    r = requests.get(BASE_URL + endpoint, headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        r.raise_for_status()
        return None


###############################################################################

client = AirNowAPI('EDD59593-7B93-4B39-B78E-A6A31FE6CFB4')
response = client.get_forecast_by_zip_code('20002')
print(response.date_issue)
print(response.date_forecast)
print(response.reporting_area)
print(response.state_code)
print(response.latitude)
print(response.longitude)
print(response.parameter_name)
print(response.aqi)
print(response.category_number)
print(response.category_name)
print(response.action_day)
print(response.discussion)
