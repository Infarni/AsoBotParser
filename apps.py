import os
import asyncio
import csv

from scraper.aso_api import AsoAPI
from handlers.logger import LoggArch
from handlers.writer import CsvWriter
from telegram.handlers import AppFactory


async def main():
    logger = LoggArch(__name__)

    with open(os.path.join('data', 'format_apps.csv'), 'r') as file:
        csv_reader = csv.reader(file)

        apps_id = [row[0] for row in csv_reader][1:]

    apps = await AppFactory.get_all_apps(apps_id)

    table = [
        ['App Id', 'Month', 'Region', 'Units k', '%', 'Rev $k', '%', 'Link to full report']
    ]

    CsvWriter.write(os.path.join('data', 'apps.csv'), table)

    for app in apps:
        logger.info(f'Get data from {app.id}')

        link = await app.get_link()

        app_data = AsoAPI.get_app(link, app.id)
        table_rows = []
        for row in app_data:
            table_rows.append(list(row.values()))

        CsvWriter.write(os.path.join('data', 'apps.csv'), table_rows)


if __name__ == '__main__':
    asyncio.run(main())
