from IStrategy import *


class FlightChangeStrategy(IFlightStrategy):
    """
    Стратегия изменения маршрута.
    """
    def execute(self, commands: list):
        logging.info(f'Выбрана стратеия: "Изменение маршрута"')
        for command in commands:
            command.execute().
        return commands