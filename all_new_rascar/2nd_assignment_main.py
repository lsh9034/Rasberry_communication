#########################################################################
# Date: 2018/10/02
# file name: 2nd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time



class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)
        self.default_degree = 10
        self.weight = [-4,-2,0,2,4]

    def drive_parking(self):
        self.car.drive_parking()
    # =======================================================================
    # 2ND_ASSIGNMENT_CODE
    # Complete the code to perform Second Assignment
    # =======================================================================
    def car_startup(self):
        # implement the assignment code here
        while (True):
            status = self.car.line_detector.read_digital()
            degree = 90
            check = False
            for i in range(len(status)):
                if status[i] == 1 and check == False:
                    degree = self.weight[i] * self.default_degree
                    check = True
                else:
                    degree += self.default_degree
            self.car.steering.turn(degree)
        pass


if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()