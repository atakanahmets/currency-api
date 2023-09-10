import requests
from datetime import datetime, date

class CurrencyConverter:
    def __init__(self):
        self.api_key = 'APIKEY'  # API KEY 
        self.url = f'http://api.exchangeratesapi.io/v1/latest?access_key={self.api_key}'
        self.output = {}
        self.file_name = datetime.now().strftime('%d %b - %Y')

    def do_request(self):
        res = requests.get(self.url)
        if res.status_code == 200:
            self.output = res.json()

    def write_to_file(self):
        if 'rates' in self.output:
            usd_rate = self.output['rates'].get('USD')
            if usd_rate is not None:
                with open(f'{self.file_name}.txt', 'w') as file:
                    file.write(f'USD Exchange Rate: {usd_rate}\n')

    def convert_currency(self, amount, from_currency, to_currency):
        if 'rates' in self.output:
            if from_currency != 'EUR':
                amount = amount / self.output['rates'][from_currency]
            converted_amount = round(amount * self.output['rates'][to_currency], 2)
            return converted_amount
        return None

    def show_exchange_rates(self):
        if 'rates' in self.output:
            print("Exchange Rates:")
            for currency, rate in self.output['rates'].items():
                print(f"{currency}: {rate}")

    

converter = CurrencyConverter()
converter.do_request()

while True:
    print("\n1. Döviz Dönüşümü")
    print("2. Güncel Döviz Kurları")
    print("3. Çıkış")
    
    choice = input("Lütfen bir seçenek girin (1/2/3): ")
    
    if choice == '1':
        from_currency = input("Dönüşüm yapılacak döviz birimi (örn. USD): ").upper()
        to_currency = input("Dönüşüm hedef döviz birimi (örn. EUR): ").upper()
        amount = float(input("Dönüştürülecek miktarı girin: "))
        converted_amount = converter.convert_currency(amount, from_currency, to_currency)
        if converted_amount is not None:
            print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
        else:
            print("Döviz kuru bilgileri alınamadı.")
    
    elif choice == '2':
        converter.show_exchange_rates()
    
    elif choice == '3':
        print("Çıkış yapılıyor...")
        break

    else:
        print("Geçersiz seçenek. Lütfen tekrar deneyin.")
