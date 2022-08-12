import asyncio
import logging
import platform
import sys
import time
import uvicorn
import json
from kafka import KafkaProducer
from faker import Faker
from src.routers import lamoda_router
from src.routers.twitch_routers import games_router, streams_router, streamers_router
from src.di import di_container, di_controller_container

di_container.app.include_router(
    lamoda_router.router,
    prefix='/clothes',
    tags={'clothes'}
)

di_container.app.include_router(
    games_router.router,
    prefix='/games',
    tags={'games'}
)

di_container.app.include_router(
    streams_router.router,
    prefix='/streams',
    tags={'streams'}
)

di_container.app.include_router(
    streamers_router.router,
    prefix='/streamers',
    tags={'streamers'}
)

if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

fake = Faker()

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='producer.log',
                    filemode='w')


logger = logging.getLogger()
logger.setLevel(logging.INFO)

producer = KafkaProducer(bootstrap_servers=['kafka:29092'],
                         api_version=(0, 11, 5),
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))


def main():
    for i in range(10):
        test_stream_data = {
            'game_id': fake.random_int(min=2000, max=10000),
            'game_name': fake.name(),
            'stream_id': fake.random_int(min=2000, max=10000),
            'title': fake.text(),
            'user_id': fake.random_int(min=2000, max=10000),
            'user_login': fake.name(),
            'user_name': fake.name()
            }
        producer.send('stream-tracker', test_stream_data, key=b'string')
        producer.flush()


def run():
    main()
    logging.basicConfig(filename='logging.conf', level=logging.DEBUG)
    logging.info('Started')
    # asyncio.run(di_controller_container.twitch_controller.run())
    # start_time = time.perf_counter()
    # asyncio.run(di_controller_container.lamoda_controller.run())
    # print(f'HTTPX Async: {time.perf_counter() - start_time} seconds')
    logging.info('Finished')
    uvicorn.run(
        di_container.app,
        host=di_container.config.service.host,
        port=di_container.config.service.port,
        log_level=di_container.config.service.log_level
    )
