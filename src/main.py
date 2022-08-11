import asyncio
import platform
import sys
import time
import uvicorn

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

def run():
    # asyncio.run(di_controller_container.twitch_controller.run())
    # start_time = time.perf_counter()
    # asyncio.run(di_controller_container.lamoda_controller.run())
    # print(f'HTTPX Async: {time.perf_counter() - start_time} seconds')
    uvicorn.run(
        di_container.app,
        host=di_container.config.service.host,
        port=di_container.config.service.port,
        log_level=di_container.config.service.log_level
    )
