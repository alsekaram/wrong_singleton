from singleton_example import some_singleton_class
from utils import MyModel


class MyBot:
    def __init__(self):
        self.name = "MyWrongBot"
        self.model = MyModel()
        self.observer = some_singleton_class.get_instance()


if __name__ == "__main__":
    bot = MyBot()
    print(f"{bot.name=}")
