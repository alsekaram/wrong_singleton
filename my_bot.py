from models.singleton_example import SomeClass
from utils import MyModel


class MyBot:
    def __init__(self):
        self.name = "MyBot"
        self.model = MyModel()
        self.observer = SomeClass.get_instance()


if __name__ == "__main__":
    bot = MyBot()
    print(f"{bot.name=}")
