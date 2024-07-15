class SomeClass:
    _instance = None

    @staticmethod
    def get_instance():
        if SomeClass._instance is None:
            SomeClass._instance = SomeClass()
        return SomeClass._instance

    def __init__(self):
        print(f"Singleton instance ID: {id(self)}")


some_singleton_class = SomeClass.get_instance()
