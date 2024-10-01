from IFlightStrategy import *
from ..Drone import *

class BaseDepartureStrategy(IFlightStrategy):
    """
    Стратегия вылета с базовой точки
    """
    def execute(self, commands: list):
        logging.info(f'Выбрана стратеия: "Взлет с базы"')
        for command in commands:
            command.execute()
        return commands