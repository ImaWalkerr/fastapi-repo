import httpx
import requests

from src.di.container_general import ContainerGeneral
from src.di.container_dao import ContainerDAO


class TwitchWrapper:

    def __init__(self, container_general: ContainerGeneral, container_dao: ContainerDAO):
        self.main_url = container_general.config.twitch.main_url
        self.game_url = container_general.config.twitch.game_url
        self.streams_url = container_general.config.twitch.streams_url
        self.refresh = container_general.config.twitch.refresh
        self.client_id = container_general.config.twitch.client_id
        self.client_secret = container_general.config.twitch.client_secret
        self.access_token = container_general.config.twitch.access_token
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Client-ID': self.client_id,
        }
        self.live = 'live'
        self.db = container_dao.mongo_source

    def _get_header(self):
        response = requests.post(
            f'{self.refresh}'
            f'token?client_id={self.client_id}'
            f'&client_secret={self.client_secret}'
            '&grant_type=client_credentials'
        )
        return {
            'Client-ID': self.client_id,
            'Authorization': 'Bearer {}'.format(response.json()['access_token']),
        }

    async def _get_games(self):
        data = ('fields id,'
                'name,'
                'summary,'
                'genres.name,'
                'platforms.name,'
                'release_dates.human,'
                'aggregated_rating,'
                'aggregated_rating_count,'
                'rating,'
                'rating_count,'
                'cover.url,'
                'screenshots.url;'
                'limit 500;')
        async with httpx.AsyncClient() as client:
            return await client.post(
                f'{self.game_url}',
                headers=self.headers,
                data=data
            ).json()

    async def _get_streamers(self):
        data = ('fields id,'
                'user_id,'
                'user_login,'
                'user_name,'
                'game_id,'
                'game_name,'
                'title,'
                'limit 50;')
        async with httpx.AsyncClient() as client:
            return await client.post(
                f'{self.streams_url}',
                headers=self.headers,
                data=data
            ).json()

    async def _get_streams(self):
        data = ('field id,'
                'game_id,'
                'game_name,'
                'viewer_count,'
                'started_at,'
                'language,'
                'tags_id,'
                'is_mature;'
                'limit 50;'
                + (f'where type = {self.live};' if self.live else ''))
        async with httpx.AsyncClient() as client:
            return await client.post(
                f'{self.streams_url}',
                headers=self.headers,
                data=data
            ).json()

    async def parse_twitch(self):
        # get_refresh_token = self._get_header()
        games = await self._get_games()
        streamers = await self._get_streamers()
        streams = await self._get_streams()
        await self.db.insert_games(games)
        await self.db.insert_streamers(streamers)
        # await self.db.insert_streams(streams)
