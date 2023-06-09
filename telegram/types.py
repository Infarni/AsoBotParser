import time
import asyncio

from pyrogram import Client, types

from settings import ASO_ID


class Category:
    def __init__(self, client: Client, name: str, country: str, delay: float = 1):
        self.client = client
        self.name = name
        self.country = country
        self.full_name = f'{self.name}({self.country})'
        self.delay = delay

    def __str__(self):
        return f'Category: {self.full_name}'

    async def _get_last_msg(self) -> types.Message:
        async for message in self.client.get_chat_history(ASO_ID, limit=5):
            return message

    async def _until_message_text(self, text: str, into: bool = False) -> bool:
        start = time.perf_counter()
        while True:
            await asyncio.sleep(self.delay)
            msg = await self._get_last_msg()

            if time.perf_counter() - start > 30:
                raise TimeoutError

            if not msg.from_user.is_bot:
                continue

            if msg.text == '❕ There is no data in the database for the specified report parameters.':
                return False

            if not into:
                if msg.text == text:
                    return True
            else:
                if text in msg.text:
                    return True

    async def _preparation(self):
        await self.client.send_message(ASO_ID, '/Top_500_By_Category')

        await self._until_message_text('Device:')

        await self.client.send_message(ASO_ID, 'iPhone')

        await self._until_message_text('Rating type:')

        await self.client.send_message(ASO_ID, '14')

        await self._until_message_text('Category:')

        await self.client.send_message(ASO_ID, self.name)

    async def get_link(self):
        while True:
            try:
                await self._preparation()

                await self.client.send_message(ASO_ID, self.country)

                status = await self._until_message_text('#Top_500_by_Category', into=True)

                break
            except TimeoutError:
                continue

        if status:
            return (await self._get_last_msg()).text.split('\n')[-1]

        return


class SubCategory(Category):
    def __init__(
            self,
            client: Client,
            name: str,
            country: str,
            sub: str,
            delay: float = 1
    ):
        super().__init__(client, name, country, delay=delay)

        self.sub = sub
        self.full_name = f'{self.name}|{self.sub}({self.country})'

    def __str__(self):
        return f'SubCategory: {self.full_name}'

    async def _preparation(self):
        await super()._preparation()

        await self.client.send_message(ASO_ID, self.sub)


class App:
    def __init__(self, client: Client, app_id: str, delay: float = 1):
        self.client = client
        self.id = app_id
        self.delay = delay

    def __str__(self):
        return f'App: {self.id}'

    async def _get_last_msg(self) -> types.Message:
        async for message in self.client.get_chat_history(ASO_ID, limit=5):
            return message

    async def _until_message_text(self, text: str, into: bool = False) -> bool:
        start = time.perf_counter()
        while True:
            await asyncio.sleep(self.delay)
            msg = await self._get_last_msg()

            if time.perf_counter() - start > 30:
                raise TimeoutError

            if not msg.from_user.is_bot:
                continue

            if not into:
                if msg.text == text:
                    return True
            else:
                if text in msg.text:
                    return True

    async def _preparation(self):
        await self.client.send_message(ASO_ID, '/Installs_And_Revenue')

        await self._until_message_text('Send app name, link or id:')

        await self.client.send_message(ASO_ID, self.id)

        await self._until_message_text('Report type:')

        await self.client.send_message(ASO_ID, 'LastMonth')

    async def get_link(self) -> str:
        while True:
            try:
                await self._preparation()

                await self._until_message_text('‎#Installs_and_Revenue', into=True)

                break
            except TimeoutError:
                continue

        msg = await self._get_last_msg()
        link = msg.entities[-1].url

        return link