import csv
class Astronaut:
    """Astronaut"""
    #initialize
    def __init__(self,name, status, flighttime):
        self.__name = name
        self.__status = status
        self.__flighttime = flighttime

    #get
    @property
    def get_name(self):
        return self.__name
    
    @property
    def get_flighttime(self):
        return self.__flighttime

    @property
    def get_status(self):
        return self.__status

    #set
    def set_name(self,name):
        self.__name = name

    def set_flighttime(self, flighttime):
        self.__flighttime = flighttime

    def set_status(self, status):
        self.__status = status

    #comparisons for flight time
    def __gt__(self, other):
        print(f"Does {self.__name} have more flight time than {other.__name}?")
        return self.__flighttime > other.__flighttime

    def __ge__(self, other):
        print(f"Are the flight hours for {self.__name} greater than or equal to  {other.__name}?")
        return self.__flighttime >= other.__flighttime

    def __eq__(self, other):
        print(f"Do {self.__name} and {other.__name} have the same flight time?")
        return self.__flighttime == other.__flighttime

    def __str__(self):
        return f"{self.__name}, {self.__status}"


f = open('astronauts.csv' 'r')
astroDict = csv.DictReader(f)

astroList = []

for i in astroDict:
    astroList.append(Astronaut(i['Name'], i['Status'], i['Space Flight (hr)']))

for i in astroList:
    print(i)

print(astroList[0] > astroList[1])
print(astroList[0] >= astroList[1])
print(astroList[0] == astroList[1])

