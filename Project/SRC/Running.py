import threading
import time
import sys
class Running(threading.Thread):
    def __init__(self, name="default"):
        """
        Displays a notification on the terminal that a process is running, when called shows notification
        When call join ends notification
        """
        threading.Thread.__init__(self)
        self.name = name
        self.__flag = True
        self.start() 

    def run(self):
        self.__testing_notify = ['|','/','-','\\','|','/','-','\\']
        i=0
        
        while (self.__flag):
            print(self.__testing_notify[i%(len(self.__testing_notify))],end='\r')
            i = (i+1)            
            time.sleep(0.5)


    def join(self):
        """
        Stops loop when requested
        """

        self.__flag = False



