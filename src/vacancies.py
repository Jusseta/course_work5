import requests


class ResponseError(Exception):
    def __init__(self):
        self.message = 'Проблема соединения с сервером'

    def __str__(self):
        return self.message


class HeadHunterAPI:
    """Формирование запроса на HeadHunter"""
    def __init__(self):
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.params = {'pages': 100, 'per_page': 50, 'only_with_vacancies': True}
        self.employers = [2999230,  # P&G
                          39305,  # Gazprom
                          3529,  # Sber
                          5557093,  # e-Comet
                          9206033,  # G5 Games
                          9311920,  # DNS
                          5060211,  # Astra
                          955,  # Sogaz
                          55440,  # Melon FG
                          1740]  # Yandex

    def get_response(self):
        """Получение списка вакансий от данных работодателей"""
        vacancies = []
        for employer in self.employers:
            response = requests.get(f"https://api.hh.ru/vacancies?employer_id={employer}",
                                    headers=self.header, params=self.params)
            if response.status_code != 200:
                raise ResponseError
            vacancies.append(response.json()['items'])
        return vacancies
