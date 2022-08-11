import asyncio
import logging
import httpx

from bs4 import BeautifulSoup
from fastapi import HTTPException
from src.di.container_general import ContainerGeneral
from src.di.container_dao import ContainerDAO


class ParseLamoda:

    def __init__(self, container_general: ContainerGeneral, container_dao: ContainerDAO):
        self.women_clothes_url = container_general.config.parser.women_url
        self.men_clothes_url = container_general.config.parser.men_url
        self.db = container_dao.mongo_source

    async def _parse_clothes(self, clothes_url, page):
        clothe_list = []
        # timeout = httpx.Timeout(10.0, connect=60.0, read=10.0, write=5.0)
        async with httpx.AsyncClient(timeout=None) as client:
            completed_url = f'{clothes_url}?page={page}'
            response = await client.get(completed_url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                all_clothe_data = soup.find_all('div', class_='x-product-card__card')

                for data in all_clothe_data:
                    clothe_name = data.find('div', class_='x-product-card-description__product-name').text
                    clothe_brand = data.find('div', class_='x-product-card-description__brand-name').text
                    clothe_price = data.find('div', class_='x-product-card-description__microdata-wrap').find(
                        'span').text

                    clothe_data = dict(
                        name=clothe_name,
                        brand=clothe_brand,
                        price=clothe_price
                    )
                    clothe_list.append(clothe_data)
            else:
                raise HTTPException(status_code=400, detail='Invalid status code')

        return clothe_list

    logging.info('Parsing completed')

    async def get_clothes_data(self):
        tasks = []
        for page in range(1, 51):
            tasks.append(self._parse_clothes(self.women_clothes_url, page))
            tasks.append(self._parse_clothes(self.men_clothes_url, page))
        await asyncio.gather(*tasks)
        await asyncio.sleep(1)

    # async def parse_clothes_to_mongo(self):
    #     l1 = await self._parse_clothes(self.women_clothes_url)
    #     l2 = await self._parse_clothes(self.men_clothes_url)
    #     await self.db.insert_clothes(l1)
    #     await self.db.insert_clothes(l2)

    logging.info('Upload completed')
