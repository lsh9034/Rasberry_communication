#########################################################################
# Date: 2018/10/02
# file name: 3rd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)
        self.default_degree = 12 #기본적으로 꺽어야하는 기본 각도
        self.weight = [-4,-2,0,2,4] #검은 색 선의 위치에 따라 곱해야할 배수

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 3RD_ASSIGNMENT_CODE
    # Complete the code to perform Third Assignment
    # =======================================================================

    def Sort_line(self,past_degree,speed):
        temp = past_degree - 90
        angle = 90 - temp
        self.car.steering.turn(angle)
        self.car.accelerator.go_backward(speed)
        while (not self.car.line_detector.is_in_line()):
            continue
        time.sleep(0.1)
        self.car.steering.turn(past_degree)
        self.car.accelerator.go_forward(speed)

    def line_tracing(self):
        past_degree = 90  # 처음은 정면
        #check_start = True  # 만약 센서가 검은색 선위에 없이 시작했을 경우에도 작동하기 위해 만든 변수
        speed = self.car.FASTEST - 50  # 가장 빠른 속도
        self.car.accelerator.go_forward(speed)  # 전진
        while (True):
            status = self.car.line_detector.read_digital()  # 5개의 센서값 받아옴
            degree = 90
            check = False  # 왼쪽에서 맨 처음 1을 만났을 때는 체크하기 위해
            for i in range(len(status)):
                if status[i] == 1:  # 맨 처음 1을 만났을 때는 가중치를 곱해줌
                    if check == False:
                        degree += self.weight[i] * self.default_degree
                        check = True
                        #check_start = False
                    elif check == True:  # 그 다음 1을 만났을 때는 기본 각도만큼 더해줌
                        degree += self.default_degree

            if check == False:
                self.Sort_line(past_degree,speed)

            elif degree != past_degree:  # 전에 꺽은 각도와 다른 경우에만 서보모터에 각도 적용
                self.car.steering.turn(degree)
                past_degree = degree
            elif [1,1,1,1,1] == status:
                break

        self.car.accelerator.go_backward(10)  # 관성제어하기 위해 약간 후진하여 빨리 정지하게함.
        time.sleep(0.7)
        self.car.accelerator.stop()
    def car_startup(self):
        # implement the assignment code here
        self.line_tracing()
        pass


if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()