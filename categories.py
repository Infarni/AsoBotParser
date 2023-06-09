import os
import asyncio

from scraper.aso_api import AsoAPI

from handlers.logger import LoggArch
from handlers.writer import CsvWriter

from telegram.handlers import CategoryFactory

from settings import CATEGORIES, COUNTRIES, FULL_COUNTRIES


async def main():
    logger = LoggArch(__name__)

    logger.debug('Get categories')

    categories = await CategoryFactory.get_all_categories(
        CATEGORIES,
        COUNTRIES
    )

    csv = [
        ['Rating title', 'Category', 'Country', 'Date', 'Logo Link', 'Title', 'Url', 'Sub Title', 'Rank', 'Publisher',
         'Developer Website']]
    CsvWriter.write(os.path.join('data', 'categories.csv'), csv)

    data = []
    categories_number = len(categories)
    for number, category in enumerate(categories):
        logger.debug(f'Get link from category: {category.full_name}')

        link = await category.get_link()

        if not link:
            logger.debug(f'There is no data in the database for the specified report parameters.')

        logger.info(f'Category: {category.full_name} ({number + 1}/{categories_number}) link - {link}')

        data.append({'link': link, 'Category': category.full_name, 'Country': category.country})

        if link is None:
            csv = [[
                None,
                category.full_name,
                FULL_COUNTRIES[category.country],
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None
            ]]

            CsvWriter.write(os.path.join('data', 'categories.csv'), csv)
        else:
            apps_data = AsoAPI.get_category(link)

            for app in apps_data['apps']:
                csv = [[
                    apps_data['rating_name'],
                    category.full_name,
                    apps_data['country'],
                    apps_data['date'],
                    app['logo'],
                    app['title'],
                    app['url'],
                    app['subtitle'],
                    app['rank'],
                    app['Publisher'],
                    app['Developer Website']
                ]]

                CsvWriter.write(os.path.join('data', 'categories.csv'), csv)


if __name__ == '__main__':
    asyncio.run(main())
