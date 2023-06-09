import csv
import io
import time


import requests
import json

from bs4 import BeautifulSoup

from handlers.logger import LoggArch


class AsoAPI:
    @staticmethod
    def get_category(url: str) -> dict[str, str | list[dict[str, str | int]]]:
        logger = LoggArch(__name__)

        logger.debug(f'Get html from {url}')
        response_html = requests.get(url)

        logger.debug(f'Get json from {url}/data.json')
        response_json = requests.get(url + '/data.json')

        soup = BeautifulSoup(response_html.content, 'lxml')

        rating_name = soup.select('.headerblock > h4 > b')[0].text.split('apps')[0]
        country = soup.select('.headerblock > h4 > b')[0].text.split('\n')[-1].split(',')[0]
        date = soup.select('.headerblock > h4 > b')[0].text.split(country)[-1][2:]

        csv_url = soup.select('.floatmenu > li:nth-child(1) > a:nth-child(1)')[0]['href']

        logger.debug(f'Get csv from {url}/{csv_url}')
        csv_reader = csv.reader(io.StringIO(requests.get(f'{url}/{csv_url}').text), delimiter=';')

        csv_data = []
        for row in csv_reader:
            csv_data.append(row)

        publishers = [row[4] for row in csv_data][1:]
        developers = [row[5] for row in csv_data][1:]

        json_data = json.loads(response_json.content.decode('utf-8-sig'))

        apps_data = []
        for index, app in enumerate(json_data):
            apps_data.append(app | {'Publisher': publishers[index], 'Developer Website': developers[index]})

        data = {
            'rating_name': rating_name,
            'country': country,
            'date': date,
            'apps': apps_data
        }

        return data

    @staticmethod
    def get_app(url: str, app_id: str) -> list[dict[str, str | int]]:
        logger = LoggArch(__name__)

        time.sleep(2)

        while True:
            logger.debug(f'Get html from {url}')
            response_html = requests.get(url)

            if response_html.status_code == 404:
                logger.warning('Status code 404, reload')
                continue
            else:
                break

        while True:
            logger.debug(f'Get json from {url}/data.json')
            response_json = requests.get(url + '/data.json')

            if response_json.status_code == 404:
                logger.warning('Status code 404, reload')
                continue
            else:
                break

        json_data = json.loads(response_json.content.decode('utf-8-sig'))

        soup = BeautifulSoup(response_html.content, 'lxml')

        data = []

        id = app_id
        month = soup.select('.headerblock > h4 > b')[0].text.split(',')[-1].split('\r')[0].strip()

        for item in json_data:
            data.append(
                {
                    'App Id': id,
                    'Month': month,
                    'Region': item['region'],
                    'Units k': item['installs'],
                    '%': item['installsshare'],
                    'Rev $k': item['revenue'],
                    ' % ': item['revenueshare'],
                    'Link to full report': url
                }
            )
            logger.info(data[-1])

        return data
