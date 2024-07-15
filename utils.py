from models.singleton_example import some_singleton_class


class MyModel:
    def __init__(self):
        self.name = "MyModel"
        self.observer = some_singleton_class.get_instance()
