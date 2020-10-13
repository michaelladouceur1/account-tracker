import time
import os 
import json 
import requests

# URLS
AUTH_URL = 'https://api.tdameritrade.com/v1/oauth2/token'
PRICE_HISTORY_URL = 'https://api.tdameritrade.com/v1/marketdata/'
MARKET_HOURS_URL = 'https://api.tdameritrade.com/v1/marketdata/OPTION/hours'

class API:
    def __init__(self):
        self.api_key = self._get_api_key()
        self.account_id = self._get_account_id()
        self.refresh_token = self._get_refresh_token()
        self.access_token = {
            'token': '',
            'createdAt': time.time(),
            'expiresIn': -1
        }
        self.headers = {'Authorization': ''}

    def _get_api_key(self):
        return os.getenv('TD_API_KEY')

    def _get_account_id(self):
        return os.getenv('TD_BROKER_ID')

    def _get_refresh_token(self):
        return os.getenv('TD_REFRESH_TOKEN')

    def _check_access_token_age(self):
        # Return access token age
        return (time.time() - self.access_token['createdAt'])

    def _check_access_token_invalid(self):
        # Check if access token age is greater than expiration
        if self._check_access_token_age() >= self.access_token['expiresIn'] - 60:
            return True
        else:
            return False
    
    def _get_refresh_access_token_params(self):
        data = {
            'grant_type': 'refresh_token',
            'refresh_token': self.refresh_token,
            'client_id': self.api_key
        }
        return data

    def _refresh_access_token(self):
        # Refresh access token if expired
        print('Refreshing access token...')
        data = self._get_refresh_access_token_params()
        r = requests.post(AUTH_URL, data=data)
        if r.status_code != 200:
            print(r.status_code)
            raise Exception('Authentication not successful')
        print('Access token refreshed...')
        data = r.json()
        self.access_token['createdAt'] = time.time()
        self.access_token['expiresIn'] = data['expires_in']
        self.access_token['token'] = data['access_token']

    def _get_access_token(self):
        # Check if access token needs to be refreshed
        if self._check_access_token_invalid():
            self._refresh_access_token()
        return self.access_token['token']
        
    def _get_headers(self):
        access_token = self._get_access_token()
        self.headers['Authorization'] = f'Bearer {access_token}'

    def _get_price_history_params(self,period_type,period,frequency_type,frequency):
        params = {
            'apikey': self.api_key,
            'periodType': period_type,
            'period': period,
            'frequencyType': frequency_type,
            'frequency': frequency
        }
        return params

    def get_price_history(self,symbol,period_type,period,frequency_type,frequency):
        self._get_headers() 
        params = self._get_price_history_params(period_type,period,frequency_type,frequency)
        ph_url = f'{PRICE_HISTORY_URL}{symbol}/pricehistory'
        r = requests.get(ph_url, headers=self.headers, params=params)
        return r.json()

api = API()
print(api.get_price_history('TSLA','month',1,'daily',1))