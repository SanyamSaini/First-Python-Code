class Car:
    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("I'm going {} kph!".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass


if __name__ == '__main__':

    myCar = Car()

    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?").upper()

        if action not in "ABOS" or len(action) != 1:
            print("I don\'t know how to do that")
            continue
        if action == 'A':
            myCar.accelerate()
        elif action == 'B':
            myCar.brake()
        elif action == 'O':
            print("The car has driven {} Kilometers".format(myCar.odometer))
        elif action == 'S':
            print("The car\'s average speed was {} kph".format(myCar.average_speed()))

        myCar.step()
        myCar.say_state()
