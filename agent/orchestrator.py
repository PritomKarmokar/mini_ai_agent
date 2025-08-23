from tools.knowledge_base import KnowledgeBase
from tools.weather_client import WeatherClient

class Orchestrator:
    def __init__(self):
        self.weather_client = WeatherClient()
        self.knowledge_base = KnowledgeBase()

    def handle(self, user_input: str) -> str:
        return self.knowledge_base.evaluate(user_input)