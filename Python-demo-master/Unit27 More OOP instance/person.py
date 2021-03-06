class Person():

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        # int:only get the integer part
        # round: (num[, x])
        self.pay = int(self.pay * (1+percent))

    def __str__(self):
        return('Person: %s, %s, %s' % (self.name, self.job, self.pay))


class Manager(Person):

    def __init__(self, name, pay, job="boss",):
        Person.__init__(self, name, pay, job)

    def giveRaise(self, percent, bonus=.10):
        # bad way
        # self.pay = int(self.pay*(1+bonus+percent))
        # better way
        Person.giveRaise(self, percent+bonus)


if __name__ == "__main__":
    allen = Person("Allen Yuan", "dev", 100)
    print(allen.name, allen.pay)
    print(allen.lastName())
    allen.giveRaise(0.1)
    print(allen.pay)

    bob=Manager("bob", 5000)
    print(bob)


