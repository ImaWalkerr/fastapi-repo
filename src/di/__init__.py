from src.di.container_controller import ContainerController
from src.di.container_dao import ContainerDAO
from src.di.container_general import ContainerGeneral
from src.di.container_parser import ContainerTwitch, ContainerParser

di_container = ContainerGeneral()
dao_container = ContainerDAO(di_container)
twitch_controller = ContainerTwitch(di_container, dao_container)
parser_controller = ContainerParser(di_container, dao_container)

di_controller_container = ContainerController(
    di_container,
    dao_container,
    twitch_controller,
    parser_controller
)
