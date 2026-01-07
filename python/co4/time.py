class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        sec = self.__second + other.__second
        minute = self.__minute + other.__minute
        hour = self.__hour + other.__hour

        if sec >= 60:
            minute += sec // 60
            sec = sec % 60

        if minute >= 60:
            hour += minute // 60
            minute = minute % 60

        return Time(hour, minute, sec)

    def display(self):
        print(f"Time = {self.__hour}:{self.__minute}:{self.__second}")


# 🔹 object creation
t1 = Time(2, 45, 50)
t2 = Time(1, 20, 30)

# 🔹 operator overloading
t3 = t1 + t2

# 🔹 output
t3.display()
