class Engine:
    def start(self):
        print("Engine starts")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        print("Car is starting...")
        self.engine.start()


c = Car()
c.start_car()