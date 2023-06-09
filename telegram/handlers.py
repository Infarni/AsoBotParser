import csv

from pyrogram import Client

from settings import API_ID, API_HASH, PHONE

from .types import Category, SubCategory, App


class CategoryFactory:
    @staticmethod
    async def get_all_categories(
            categories: list,
            countries: list
    ) -> list[Category | SubCategory]:
        client = Client(PHONE, api_id=API_ID, api_hash=API_HASH, phone_number=PHONE)
        await client.start()

        result = []
        for category in categories:
            sub_categories = category['sub_categories']
            if sub_categories:
                for sub_category in sub_categories:
                    for country in countries:
                        result.append(
                            SubCategory(
                                client,
                                category['name'],
                                country,
                                sub_category['name']
                            )
                        )
            else:
                for country in countries:
                    result.append(
                        Category(
                            client,
                            category['name'],
                            country
                        )
                    )

        return result


class AppFactory:
    @staticmethod
    async def get_all_apps(apps_id: list) -> list[App]:
        client = Client(PHONE, api_id=API_ID, api_hash=API_HASH, phone_number=PHONE)
        await client.start()

        result = [App(client, app_id) for app_id in apps_id]

        return result
