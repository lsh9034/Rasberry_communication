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
        self.Limit_distance = 16;
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
        speed = self.car.FASTEST
        self.car.steering.center_alignment()
        self.car.accelerator.go_forward(speed)
        deltha = time.time()
        count = 0
        while(True):
            distance = self.car.distance_detector.get_distance()
           # print(distance)
            if distance< self.Limit_distance and distance != -1:
                count+=1
                if count>=3:
                    self.car.accelerator.stop()
                    deltha = time.time() - deltha
                    break
            else:
                count=0
        self.car.accelerator.go_backward(speed - 5)
        time.sleep(deltha)
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
