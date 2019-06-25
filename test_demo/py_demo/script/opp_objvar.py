class Robot:

    population = 0

    def __init__(self, name):
        self.name = name
        print ("(initializing {})".format(self.name))

        Robot.population += 1

    def die(self):
        print ("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))

        else:
            print ("There are still {:d} robots working".format(Robot.population))

    def say_hi(self):
        print ("Greetings ,my masters call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        print ("We have {:d} robots.".format(cls.population))
        



droid = Robot("R1-D1")
droid.say_hi()
droid.how_many

droid2 = Robot("R2-D2")
droid2.say_hi()
droid2.how_many()

print ("Robots can do some work here")

print ("Robots have finished their work . So let's destroy them")

droid.die()

droid2.die()

Robot.how_many()

