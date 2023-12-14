from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class cryptoApiPull:
    def __init__(self):
        None

    def apiRunner(self, limit):
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' 
        #Original Sandbox Environment: 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        API_KEY = "1c1d135a-1385-468b-bead-59720449dd9f"
        parameters = {
        'start':'1',
        'limit': limit, #only voiew top3 cryptocurrencies by marked cap
        'convert':'USD'
        }
        headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY,
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            print("apiRunner ran succesfully")
            return data
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)


    # def forLoop(self):
    #     data = None
    #     try: 
    #         for i in range(3):
    #             dataAsString = self.dataToStringCoverter(self.apiRunner())
    #             self.returnData(dataAsString)
    #             sleep(5)  #sover i 260 sekunder
    #         print("forLoop ran succesfully")
    #         exit() #lukke python scriptet

    #     except Exception as e:
    #         print(e)

    def returnData(self, data):
        return data


    def dataToStringConverter(self, data):
        text = json.dumps(data, indent=4)
        print("dataToStringConverter ran succesfully")
        return text
