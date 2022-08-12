from pydantic import BaseSettings


_CONFIG_PREFIX = 'FASTAPI_SERVICE_'


class Service(BaseSettings):
    host: str
    port: int
    log_level: str

    class Config:
        env_prefix = _CONFIG_PREFIX + 'CONTAINER_'
        env_file = '.env'
        env_file_encoding = 'utf-8'


class Redis(BaseSettings):
    host: str
    post: int
    db: int

    class Config:
        env_prefix = _CONFIG_PREFIX + 'REDIS_'
        env_file = '.env'
        env_file_encoding = 'utf-8'


class MongoDB(BaseSettings):
    host: str
    port: int
    username: str
    password: str

    class Config:
        env_prefix = _CONFIG_PREFIX + 'MONGO_'
        env_file = '.env'
        env_file_encoding = 'utf-8'


class Zookeeper(BaseSettings):
    port: str
    client_port: str
    tick_time: str

    class Config:
        env_prefix = _CONFIG_PREFIX + 'ZOOKEEPER_'
        env_file = '.env'
        env_file_encoding = 'utf-8'


class Kafka(BaseSettings):
    zookeeper_connect: str
    advertised_listeners: str
    listener_security_protocol_map: str
    inter_broker_listener_name: str

    class Config:
        env_prefix = _CONFIG_PREFIX + 'KAFKA_'
        env_file = '.env'
        env_file_encoding = 'utf-8'


class KafkaUi(BaseSettings):
    clusters_0_name: str
    clusters_0_bootstrapservers: str
    clusters_0_zookeeper: str
    clusters_0_readonly: str

    class Config:
        env_prefix = _CONFIG_PREFIX + 'KAFKA_UI_'
        env_file = '.env'
        env_file_encoding = 'utf-8'


class Twitch(BaseSettings):
    main_url: str
    game_url: str
    streams_url: str
    refresh: str
    client_id: str
    client_secret: str
    access_token: str

    class Config:
        env_prefix = _CONFIG_PREFIX + 'TWITCH_'
        env_file = '.env'
        env_file_encoding = 'utf-8'


class Parser(BaseSettings):
    women_url: str
    men_url: str

    class Config:
        env_prefix = _CONFIG_PREFIX + 'PARSER_'
        env_file = '.env'
        env_file_encoding = 'utf-8'


class Config(BaseSettings):
    service: Service = Service()
    redis: Redis = Redis()
    mongodb: MongoDB = MongoDB()
    zookeeper: Zookeeper = Zookeeper()
    kafka: Kafka = Kafka()
    kafka_ui: KafkaUi = KafkaUi()
    twitch: Twitch = Twitch()
    parser: Parser = Parser()

    class Config:
        env_prefix = _CONFIG_PREFIX
        env_file = '.env'
        env_file_encoding = 'utf-8'
