                                                  #########################################################################
# Date: 2018/10/02
# file name: 1st_assignment_main.py
# Purpose: this code has been generated for the 4 wheels drive body
# moving object to perform the project with ultra sensor
# this code is used for the student only
#########################################################################

from car import Car
import time


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 1ST_ASSIGNMENT_CODE
    # Complete the code to perform First Assignment
    # =======================================================================
    def car_startup(self):
        # Implement the assignment code here.
       # defalut = self.car.steering.turning_offset()
 #       self.car.steering.set_angle(30)
  #      time.sleep(2)
        self.car.steering.set_angle(90)
    #    time.sleep(2)
        self.car.accelerator.go_forward(50)
        deltha = time.time()
        while(True):
            distance = self.car.distance_detector.get_distance()
            print(distance)
            if distance< 15 and distance != -1:
                deltha = time.time() - deltha
                self.car.accelerator.go_backward(50)
                time.sleep(deltha) 
                break
        self.car.accelerator.stop()
        time.sleep(1)
        pass


if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
