class Competition:
    __raise_amount = 1.10

    def __init__(self, name, prize):
        self.__name = name
        self.__prize = prize

    def get_name(self):
        return self.__name

    def get_prize(self):
        return self.__prize

    def raise_prize(self):
        self.__prize = self.__prize * self.__raise_amount


class Cycling(Competition):

    def __init__(self, name, prize, country):
        Competition.__init__(self, name,
                             prize)  # Whenever we use parent class name then it is mandatory to pass self parameter

        self.__country = country

    def get_country(self):
        return self.__country


class Cycling1(Competition):

    def __init__(self, name, prize, country):
        super().__init__(name, prize)  # If we are using super() then we don't need to pass self parameter

        self.__country = country

    def get_country(self):
        return self.__country
