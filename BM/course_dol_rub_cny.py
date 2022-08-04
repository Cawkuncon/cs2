import requests
from bs4 import BeautifulSoup


class CourseCnyRub:
    response = requests.get('https://fx-rate.net/CNY/RUB/').text
    soup = BeautifulSoup(response, 'lxml')
    rub = soup.find('input', {'class': 'ip_amount cal_amount_to'}).get('value')
    yuan = soup.find('input', {'class': 'ip_amount cal_amount_from'}).get('value')

    @classmethod
    def get_course(cls):
        return round(float(cls.rub) / float(cls.yuan), 2)


class CourseDolRub:
    @classmethod
    def get_course(cls):
        pass
