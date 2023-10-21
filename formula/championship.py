from haydovchi import Haydovchi
from gp import Gp
from timee import Time

class Championship:
    def __init__(self) -> None:
        self.driver_list: list[Haydovchi] = []
        self.gp_list:list[Gp] = []
        self.time_list:list[Time] = []

    def setTime(self, time:Time, gp, driver):
        dri = Time(time)
        self.time_list.append(dri)
        for dr in self.gp_list:
            if dr.name == driver:
                return dri
            self.driver_list.append(driver)
        for g in self.gp_list:
            if g.name == gp:    
                pass
            else:
                self.gp_list.append(gp)    

    def defineGrandprix(self, name):
        gp = Gp(name)
        self.gp_list.append(gp)
        return gp
    
    def getGrandPrix(self, name):
        for gp in self.gp_list:
            if gp.name == name:
                return gp
        return None    
    
    def createDriver(self, name):
        driver = Haydovchi(name)
        self.driver_list.append(driver)

        print('qoshildi')
        return driver

    def getDrivers(self):
        return self.driver_list
    
    def getDriver(self, name):
        for driver in self.driver_list:
            if driver.name == name:
                return driver
        return None