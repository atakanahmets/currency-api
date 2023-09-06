import requests 
from datetime import datetime
from datetime import date

class Currency:
    def __init__(self):
        self.api_key = '51ee8245f3cdf838bb67d7578dc6854f'
        self.url = f'http://api.exchangeratesapi.io/v1/latest?access_key={self.api_key}'
        self.output = ''
        self.file_name = datetime.now().strftime('%d %b -%Y')
        

    def do_requests(self):
        res = requests.get(self.url)
        if res.status_code == 200:
            self.output = res.json()


    def write_to_file(self):
        print(self.output['rates']['USD'])

    def nowt(self):
        today = date.today()
        print(today)

c = Currency()
c.do_requests()
c.write_to_file()
c.nowt()